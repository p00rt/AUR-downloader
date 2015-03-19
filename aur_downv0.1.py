import os

os.system("rmdir /tmp/.AUR_DOWN")
os.system("mkdir /tmp/.AUR_DOWN")
in_pkgs = raw_input( "Type AUR packages names separated by commas without spaces (eg. eggs,milk,cheese): " )
med_pkgs = in_pkgs.split(',')
pkgs = []
for i in med_pkgs:
    pkgs.append(i)


def pkgs_install():
    for i in pkgs:
        os.system( "cd /tmp/.AUR_DOWN && wget https://aur.archlinux.org/packages/" + i[0] + i[1] + '/' + i +'/' + i +".tar.gz" )
        os.system("cd /tmp/.AUR_DOWN && tar xvf " + i +".tar.gz" )
        os.system("cd /tmp/.AUR_DOWN/"+i +" && makepkg -si")

pkgs_install()
os.system("rm -r /.tmp/AUR_DOWN")

