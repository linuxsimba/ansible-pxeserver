#!/usr/bin/python

import unittest


def find_iface_via_ip(data, _ip):
    """
    Find Iface details from ansible_facts
    Arg:  _ip: IP address to match
    Returns: Attributes of found interface or None.

    """
    _ansible_facts = data.get('ansible_facts')
    iface_list = _ansible_facts.get('ansible_interfaces')

    for _ifacename in iface_list:
        iface_key = "ansible_%s" % _ifacename
        if _ansible_facts.get(iface_key).get('ipv4').get('address') == _ip:
            return _ansible_facts.get(iface_key)
    return None


class FilterModule(object):
    """ Ansible custom filter plugin """

    def filters(self):
        return {
            'iface_details': find_iface_via_ip
        }


class TestAddIP(unittest.TestCase):
    """
    test case for this filter plugin. to execute
    run ``python iface_details``
    """
    def test_add_ip(self):
        data = {
            'ansible_facts': {
                'ansible_interfaces':  [
                    'lo',
                    'eth1',
                    'eth2'
                ],
                'ansible_lo': {
                    'device': 'lo',
                    'ipv4': {
                        'address': '127.0.0.1'
                    }
                },
                'ansible_eth1': {
                    'device': 'eth1',
                    'ipv4': {
                        'address': '10.1.1.1'
                    }
                },
                'ansible_eth2': {
                    'device': 'eth2',
                    'ipv4': {
                        'address': '10.2.1.1'
                    }
                }
            }
        }
        self.assertEqual(find_iface_via_ip(data, '10.1.1.1'),
                         {'device': 'eth1', 'ipv4': {'address': '10.1.1.1'}})

if __name__ == '__main__':
    unittest.main()
