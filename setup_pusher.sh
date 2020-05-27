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
mv * ../
mv read_scraper.py ../scrapers/


# Sets up the pusher
#+ configure alias


echo "Setting up shortcuts:"

if ! grep -q tasker ~/.bashrc || \
   ! grep -q pusher ~/.bashrc
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

if ! grep -q tasker.py ~/.bashrc
then
    pusher_alias="alias _pusher='python3 $(pwd)/../pusher.py'"
    echo "$pusher_alias" >> ~/.bashrc
    echo "  -> $pusher_alias"
else
    echo "  -> pusher already defined"

fi

echo "Reloading .bashrc:"
source ~/.bashrc

echo "All set!"