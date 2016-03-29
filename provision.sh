 #!/usr/bin/env bash

if [ -e "/etc/vagrant-provisioned" ];
then
    if [ "/vagrant/provision.sh" -ot "/etc/vagrant-provisioned" ];
    then
        echo "Vagrant provisioning already completed. Skipping..."
        exit 0
    else
        echo "Starting Vagrant provisioning process..."
    fi

else
    echo "Starting Vagrant provisioning process..."
fi

# Install core components
echo "Installing core components..."
/vagrant/sh/core.sh

# Install python
echo "Installing python..."
/vagrant/sh/python.sh

# Install postgreSQL
echo "Installing postreSQL..."
/vagrant/sh/postgresql.sh

touch /etc/vagrant-provisioned

echo "--------------------------------------------------"
echo "Your vagrant instance is running"
