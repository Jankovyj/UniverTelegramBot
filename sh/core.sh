#!/bin/bash

apt-get update
# Install build tools
apt-get install -y git build-essential
# Install Pillow external libraries
apt-get install -y libtiff4-dev libjpeg8-dev zlib1g-dev \
        libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev \
        tk8.5-dev python-tk libffi-dev libxml2-dev libtool
