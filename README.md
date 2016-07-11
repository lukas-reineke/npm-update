updates all git modules in package.json

-f or --force to force reinstall, even if not out of date.

## Setup


### Dev

```
$ pip install virtualenv
```
```
$ virtualenv venv
```
```
$ . venv/bin/activate
```
```
$ pip install -e .
```


### User

```
$ pip install .
```


### Command
run

```
$ npm-update
```

options
---
shows help
```
$ npm-update --help
```
forces update
```
$ npm-update -f
$ npm-update --force
```
updates local files
```
$ npm-update -l
$ npm-update --local
```