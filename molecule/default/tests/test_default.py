import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_limits_file(host):
    assert host.file("/etc/security/limits.conf").exists

    cmd = host.run("cat /etc/security/limits.conf | grep nproc | grep -v ^#")
    assert cmd.stdout == """*	hard	nproc	64000
*	soft	nproc	64000
"""

    cmd = host.run("cat /etc/security/limits.conf | grep nofile | grep -v ^#")
    assert cmd.stdout == """*	hard	nofile	64000
*	soft	nofile	64000
"""

    cmd = host.run("cat /etc/security/limits.conf | grep memlock | grep -v ^#")
    assert cmd.stdout == """*	hard	memlock	1024
*	soft	memlock	1024
"""
