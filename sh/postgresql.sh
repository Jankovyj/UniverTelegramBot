#!/bin/bash

apt-get update
# Install postgreSQL packages
apt-get install -y postgresql-server-dev-all postgresql postgresql-contrib

# Create vagrant user for postgresql
sudo -u postgres createuser -s vagrant
