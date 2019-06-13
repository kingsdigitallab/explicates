# Explicates

[![Build Status](https://travis-ci.com/harryjmoss/explicates.svg?branch=master)](https://travis-ci.com/harryjmoss/explicates)
[![Coverage Status](https://coveralls.io/repos/github/harryjmoss/explicates/badge.svg?branch=master)](https://coveralls.io/repos/github/harryjmoss/explicates/badge.svg?branch=master)

A fork of [Explicates - A PostgreSQL-backed Web Annotation server](https://github.com/alexandermendes/explicates) by Alexander Mendes- forked at [v0.3.0](https://github.com/alexandermendes/explicates/commit/bc504498ef330fab46f2334f96631457d520ec90)

[**Read the documentation**](https://harryjmoss.github.io/explicates/)


## Setup

A virtual machine setup is provided for local development.

Download and install
[Vagrant](https://www.vagrantup.com/) >= 4.2.10 and
[VirtualBox](https://www.virtualbox.org/) >= 1.2.1,
then run:

```bash
# setup vm
vagrant up

# enter vm
vagrant ssh

# run
python run.py
```

The server should now be available at http://127.0.0.1:3000.

## Configuration

See [settings.py.tmpl](settings.py.tmpl) for all available configuration
settings. To change any settings make a copy of the template:

```bash
cp settings.py.tmpl settings.py
```

## Testing

Explicates is tested against [Python 2.7 and 3.4](https://travis-ci.com/harryjmoss/explicates):

```bash
# python 2
nosetests test/

# python 3
python3 -m "nose"
```
