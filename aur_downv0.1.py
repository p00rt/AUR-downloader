#!/usr/bin/python
import os
from sys import argv

os.mkidr("/tmp/.AUR_DOWN")
pkgs = argv; del pkgs[0]

def pkgs_install():
    for i in pkgs:
        os.system( "cd /tmp/.AUR_DOWN && wget https://aur.archlinux.org/packages/" + i[0] + i[1] + '/' + i +'/' + i +".tar.gz" )
        os.system("cd /tmp/.AUR_DOWN && tar xvf " + i +".tar.gz" )
        os.system("cd /tmp/.AUR_DOWN/"+i +" && makepkg -si")

pkgs_install()
os.system("rm -r /tmp/.AUR_DOWN")

