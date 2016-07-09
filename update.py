# -*- coding: utf-8 -*-

import click
import os
import sys

@click.command()
def cli():
    """
        updates all git modules in package.json
    """


    try:
        package = open('package.json')
        searchItem = 'git+'
        toInstall = ''

        for line in package:
            if searchItem in line:
                packageName = line.strip().split('"')
                toInstall = toInstall + packageName[1] + ' '
        if (toInstall):
            click.echo('installing:\n -- %s\n' % toInstall[:-1].replace(' ', '\n -- '))
            os.system("npm i " + toInstall)
        else:
            click.echo('no git modules in package.json')

    except:
        click.echo('no package.json found')
