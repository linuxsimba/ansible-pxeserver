# Testing PXE Setups


Created a simple playbook and role for testing PXE booting Ubuntu.

## Requirements

* Linux Based Server/Laptop with KVM enabled
* [Vagrant-libvirt](https://linuxsimba.com/vagrant-libvirt-install)
* 4 GB RAM
* 30 GB Disk Free
* Reasonable fast internet connection to download the [Vagrant box](https://app.vagrantup.com/yk0/boxes/ubuntu-xenial)

## Execution

Install the pxeserver first before starting the pxevm.

```
vagrant up pxeserver pxevm --no-parallel
```


## License
MIT

## TODO
At some point would like to expand it to configure Centos/Red Hat Linux as well.
