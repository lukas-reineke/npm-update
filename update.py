# -*- coding: utf-8 -*-

import click
import os
import subprocess


@click.command()
@click.option('-f', '--force', count=True)
@click.option('-l', '--local', count=True)
def cli(force, local):
    """
        updates all git modules in package.json\n
        -f or --force to force reinstall, even if not out of date.
    """

    try:
        package = open('package.json')
        searchItem = 'git+'
        toInstall = ''
        upToDate = False

        for line in package:
            if searchItem in line:
                packageName = line.strip().split('"')

                if (force):
                    toInstall = toInstall + packageName[1] + ' '
                else:
                    split = packageName[3][4:].split(':')

                    if split[0] == 'ssh':
                        reformated = split[0] + ':' + split[1] + '/' + split[2]
                    else:
                        reformated = packageName[3][4:]

                    reformated = reformated.split('#')
                    if (len(reformated) == 1):
                        p = subprocess.Popen(
                            [
                                'git',
                                'ls-remote',
                                reformated[0],
                                'HEAD'
                            ],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )
                    else:
                        p = subprocess.Popen(
                            [
                                'git',
                                'ls-remote',
                                reformated[0],
                                reformated[1]
                            ],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )

                    output, err = p.communicate()
                    newestVersion = str(output).split("\t")[0]

                    modulePackage = open(
                        os.path.join(
                            'node_modules', packageName[1], 'package.json'
                        )
                    )
                    installedVersion = None
                    for moduleLine in modulePackage:
                        if 'resolved' in moduleLine:
                            installedVersion = moduleLine.split('#')[1].split('"')[0]

                    if (newestVersion != installedVersion):
                        toInstall = toInstall + packageName[1] + ' '
                    else:
                        upToDate = True
            if (local):
                if 'file:' in line:
                    packageName = line.strip().split('"')
                    toInstall = toInstall + packageName[1] + ' '


        if (toInstall):
            click.echo('installing:\n -- %s\n' % toInstall[:-1].replace(' ', '\n -- '))
            os.system("npm i " + toInstall)
        else:
            if (upToDate):
                click.echo('all git modules are up to date, nothing to do.')
            else:
                click.echo('no git modules in package.json')

    except:
        click.echo('no package.json found')
