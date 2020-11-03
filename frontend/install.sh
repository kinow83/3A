#!/bin/bash

sudo dnf install nodejs
sudo dnf install npm
sudo npm install -g npm

echo -n "node ver: "; node -v
echo -n "npm ver: "; npm -v


sudo npm install -g @vue/cli
