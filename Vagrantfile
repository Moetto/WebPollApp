Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/vivid64"
  config.vm.provision :shell, path: "vagrantbootstrap.sh"
  config.vm.synced_folder ".", "/home/ilmo/"
  #, type: "rsync", rsync__auto: true, rsync__exclude: "python/"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.ssh.insert_key = true
end
