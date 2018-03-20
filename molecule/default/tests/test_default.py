"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    """
    Tests that the hosts file exists
    """
    file = host.file('/etc/hosts')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_apache2_is_installed(host):
    """
    Tests that apache2 is installed
    """
    apache2 = host.package("apache2")
    assert apache2.is_installed


def test_apache2_running_and_enabled(host):
    """
    Tests that apache2 is running and enabled
    """
    apache2 = host.service("apache2")
    assert apache2.is_running
    assert apache2.is_enabled


def test_apache2_80_and_443_is_listening(host):
    """
    Tests that apache2 is listening on ports 80 and 443
    """
    apache80 = host.socket("tcp://0.0.0.0:80")
    apache443 = host.socket("tcp://0.0.0.0:443")
    assert apache80.is_listening
    assert apache443.is_listening


def test_apache_port_80_redirect_to_443(host):
    """
    Tests that apache2 gives a 301 redirect for port 80 to 443
    """
    args = "url=http://127.0.0.1 follow_redirects=none validate_certs=no"
    request = host.ansible("uri", args, check=False)
    assert request["status"] == 301


def test_apache_https_request_status_and_security(host):
    """
    Tests that apache2 gives a 200 response on https
    Tests that apache2 ServerTokens show "Apache"
    Tests strict_transport_security
    """
    args = "url=https://127.0.0.1 follow_redirects=none validate_certs=no"
    request = host.ansible("uri", args, check=False)
    assert request["status"] == 200
    assert request["server"] == "Apache"
    hsts = "max-age=63072000; includeSubDomains"
    assert request["strict_transport_security"] == hsts
