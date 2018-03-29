# ansible-role-apache

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/joshuacherry/ansible-role-apache.svg?branch=master)](https://travis-ci.org/joshuacherry/ansible-role-apache)
![Ansible](https://img.shields.io/badge/ansible-2.4.3-green.svg)

Configures [Apache](https://httpd.apache.org/) on an Ubuntu server.

## Requirements

- Ansible >= 2.4.3

## Install

### Install from GitHub

`ansible-galaxy install git+https://github.com/joshuacherry/ansible-role-apache.git`

## Features

| OS            |
| :------------ |
| Ubuntu 16.04  |

- Manage custom apache configurations
- Enable/Disable apache modules
- Manage multiple Virtualhosts
- Enable/Disable reverse proxy
- Append unspecified apache configuration  to VirtualHost

## Versioning

[Semantic Versioning](http://semver.org/)

For the versions available, see the [tags on this repository](https://github.com/joshuacherry/ansible-role-apache/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Role variables

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

This role includes a Vagrantfile used with a Docker-based test harness for integration testing. Using Vagrant allows all contributors to test on the same platform and avoid false test failures due to untested or incompatible docker versions.

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
1. Run `vagrant up` from the same directory as the Vagrantfile in this repository.
1. SSH into the VM with: `vagrant ssh`
1. Run tests with `molecule`.

### Testing with Docker and tox

Tox will test against the configured dependencies in [tox.ini](tox.ini). This allows you to test the role against multiple version of ansible, molecule, python, and more. Once the dependencies are set, tox will run the same molecule command to test code.

```bash
cd /ansible-role-apache
tox
```

### Testing with Docker and molecule

```bash
cd /ansible-role-apache
molecule test
```

See `molecule` for more information including a full list of available commands.

### interactive debugging

You can use log into a docker image created by molecule for interactive testing with the below commands.

```bash
cd /ansible-role-apache
molecule converge
# Ubuntu
docker exec -it ubuntu /bin/bash
# CentOS
docker exec -it centos /bin/bash
```

## Example Playbook

```yaml
---
- name: Playbook for ansible-role-apache
  hosts: all

  tasks:
  - include_role:
      name: ansible-role-apache
```