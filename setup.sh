#!/usr/bin/env bash                                                                                     

sudo apt-get install alien
sudo apt-get install python
sudo apt-get install wget
sudo apt-get install dpkg
chmod +x prepget
chmod +x prepget.1
sudo cp prepget /usr/bin
sudo cp prepget.1 /usr/share/man/man1/
