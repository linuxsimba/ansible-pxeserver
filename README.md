# Testing PXE Setups


Created a simple playbook and role for testing PXE booting Ubuntu.

## Requirements

* Linux Based Server/Laptop with KVM enabled
* [Vagrant-libvirt](https://linuxsimba.com/vagrant-libvirt-install)
* 4 GB RAM
* 30 GB Disk Free
* Reasonable fast internet connection to download the [Vagrant box](https://app.vagrantup.com/yk0/boxes/ubuntu-xenial)

## Creating PXE booted VM

Install the pxeserver first before starting the pxevm.

```
vagrant up pxeserver pxevm --no-parallel
```

## Logging into PXE Booted VM

SSH into the pxeserver. Sudo to root, then ssh to ``ssh root@10.1.1.10`` to access the VM.
Root password on the PXE VM is not enabled.

```
vagrant_hypervisor:$ vagrant ssh pxeserver

vagrant@pxeserver:~$ sudo su -

root@pxeserver:~# ssh root@10.1.1.10

root@pxetestvm:~#
```


## License
MIT

## TODO
At some point would like to expand it to configure Centos/Red Hat Linux as well.
