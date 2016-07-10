from setuptools import setup

setup(
    name='npm-update',
    version='0.1',
    py_modules=['update'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        npm-update=update:cli
    ''',
)
