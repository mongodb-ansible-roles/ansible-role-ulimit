Ansible role for ulimit
==================================

Sets ulimits for account

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-ulimit/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-ulimit/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-ulimit/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-ulimit/actions?query=workflow%3A%22Release%22)

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

License
-------

[Apache License](LICENSE)
