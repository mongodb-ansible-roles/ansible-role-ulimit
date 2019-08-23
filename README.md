Ansible role for ulimit
==================================

Sets ulimits for account

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-ulimit/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles/ansible-role-ulimit)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| ulimit\_nofile\_hard | Hard limit on number of open files | string | "64000" | no |
| ulimit\_nofile\_soft | Soft limit on number of open files | string | "64000" | no |
| ulimit\_nproc\_hard | Hard limit on number of processes | string | "64000" | no |
| ulimit\_nproc\_soft | Soft limit on number of processes | string | "64000" | no |
| ulimit\_memlock\_hard | Hard limit on memory lock | string | "1024" | no |
| ulimit\_memlock\_soft | Soft limit on memory lock | string | "1024" | no |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-ulimit
```

Development
-----------

Testing this role locally requires the CircleCI [Local CLI](https://circleci.com/docs/2.0/local-cli/).

To install the CLI for macOS and Linux, invoke the following command:

    $ curl -fLSs https://circle.ci/cli | DESTDIR=/usr/local/bin bash

After installing the CLI, invoke the following command to run the Molecule tests:

    $ make test

License
-------

[Apache License](LICENSE)
