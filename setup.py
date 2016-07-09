from setuptools import setup

setup(
    name='updatenpm',
    version='0.1',
    py_modules=['update'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        update=update:cli
    ''',
)