#!/bin/bash
##############################################################################
# Configurable used in the provisioning
##############################################################################
# Versions and info for Packages and Tools
PYCHARM_VERSION='4.0.4'
PYCHARM_DOWNLOAD_URL='http://download-cf.jetbrains.com/python'
PYCHARM_PKG_NAME=pycharm-community-${PYCHARM_VERSION}

##############################################################################
# Common Functions
##############################################################################
# used to check if a package for ubuntu already installed before installing 
function check_install_pkg {
    dpkg -s $1 &> /dev/null || {
        echo "---- Installing $1"
        apt-get -y install $1
    }
}

##############################################################################
# Install packages to setup Ubuntu
##############################################################################
apt-get -y update
# install lightweight desktop only if xorg package not installed
# using xorg to indicate the presence of desktop
dpkg -s xorg &> /dev/null || {
    apt-get -y install --no-install-recommends ubuntu-desktop
}

# prefered terminal
check_install_pkg gnome-terminal

##############################################################################
# Install packages related to virtualbox
# (main to impover the screen resolution !!!)
##############################################################################
declare -a virtualbox_pkgs=('virtualbox-guest-dkms' 'virtualbox-guest-utils'
                            'virtualbox-guest-x11')

for pkg in "${virtualbox_pkgs[@]}"
do
   check_install_pkg $pkg
done

##############################################################################
# python tools
##############################################################################
check_install_pkg python3-dev

##############################################################################
# install development tools
##############################################################################

# java needed for pycharm
check_install_pkg openjdk-7-jre

# download and unpack PyCharm
# NOTE: will still need to run the pycharm.sh script in unpacked pycharm bin
# directory, when configuring ensure that command line is placed in  
if [[ -d tools/pycharm ]]; then
    echo '++++ Have already downloaded PyCharm'
else
    echo "---- Download and unpack ${PYCHARM_PKG_NAME}"
    mkdir -p tools/pycharm
    cd tools/pycharm
    # downloads the tar.gz linux install file
    wget ${PYCHARM_DOWNLOAD_URL}/${PYCHARM_PKG_NAME}.tar.gz
    tar xzvf ${PYCHARM_PKG_NAME}.tar.gz
    rm ${PYCHARM_PKG_NAME}.tar.gz
    cd ..
fi
