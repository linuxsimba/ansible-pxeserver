# -*- mode: ruby -*-
# vi: set ft=ruby :

## When running `vagrant up` run it with the `--no-parallel` option.
## This ensures that the fuel_master comes up first


Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Disable the synced_folder feature
  config.vm.synced_folder '.', '/vagrant', :disabled => true

  config.vm.define :pxeserver do |node|
    node.vm.provider :libvirt do |domain|
      domain.memory = 1024
      domain.cpus = 1
    end

    node.vm.box = 'ubuntu1604'
    node.vm.hostname = "pxeserver"
    node.vm.network :private_network,
      :ip => '10.1.1.1',
      :prefix => '24',
      :libvirt__forward_mode => 'veryisolated',
      :libvirt__network_name => 'pxetest_net',
      :libvirt__dhcp_enabled => false

    node.vm.provision :ansible do  |ansible|
      ansible.playbook = "pxeserver.yml"
      ansible.tags = 'nat_masq'
      ansible.verbose = 'vvvv'
    end
  end

  config.vm.define :pxevm do |node|
    node.vm.provider :libvirt do |domain|
      domain.memory = 512
      domain.cpus = 1
      domain.storage :file, :size => '10G', :type => 'qcow2'
      domain.boot 'hd'
      domain.boot 'network'
      domain.management_network_name = 'pxetest_net'
      domain.management_network_mac = '521122334455'
      domain.management_network_mode = 'veryisolated'
    end

  end

end
