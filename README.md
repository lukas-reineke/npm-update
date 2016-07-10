updates all git modules in package.json

-f or --force to force reinstall, even if not out of date.

## Setup
==========


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
$ update
```

options
---
shows help
```
$ update --help
```
forces update
```
$ update -f
$ update --force
```