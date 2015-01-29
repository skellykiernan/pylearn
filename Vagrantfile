# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"
# Define name and version
NAME = "pylearning"
VERSION = "0.1.0"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box_check_update = false
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = NAME

  config.vm.provision "shell", path: "provision.sh"
  
  # set up default sync folder to show only a sub-directories
  config.vm.synced_folder "./", "/vagrant", disabled: true
  config.vm.synced_folder "./excerises", "/vagrant/excerises"
  
  config.vm.provider "virtualbox" do |vbox|
    vbox.name = NAME + "_" + VERSION 
    vbox.gui = true
    vbox.cpus = 2
    vbox.memory = 2048
  end
end
