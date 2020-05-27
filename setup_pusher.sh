#!/bin/bash
echo -e '
██████ ██  ██ ██████ ██  ██ ██████ ██████
██  ██ ██  ██ ██     ██  ██ ██     ██  ██
██████ ██  ██ ██████ ██████ ██████ ██████
██     ██  ██     ██ ██  ██ ██     ██ ██
██     ██████ ██████ ██  ██ ██████ ██  ██

v1.1
'

# Sets up the hipposcraper
sudo mv * ../
sudo mv ../read_scraper.py ../scrapers/


# Sets up the pusher
#+ configure alias


echo "Setting up shortcuts:"

if ! grep -q tasker ~/.bashrc || \
   ! grep -q _pusher ~/.bashrc
then
    echo -e "\n# Pusher aliases" >> ~/.bashrc
fi

if ! grep -q tasker.py ~/.bashrc
then
    tasker_alias="alias tasker='python2 $(pwd)/../tasker.py'"
    echo "$tasker_alias" >> ~/.bashrc
    echo "  -> $tasker_alias"
else
    echo "  -> tasker already defined"

fi

if ! grep -q pusher.py ~/.bashrc
then
    pusher_alias="alias pusher='python3 $(pwd)/../pusher.py'"
    echo "$pusher_alias" >> ~/.bashrc
    echo "  -> $pusher_alias"
else
    echo "  -> pusher already defined"

fi

sudo rm -r ../pusher/

echo "Reloading .bashrc:"
source ~/.bashrc
sudo rm -r ../setup_pusher.sh


echo "All set!"