#!/bin/bash
echo -e '\e[34m
┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐
│██████ ██  ██ ██████ ██  ██ ██████ ██████│
│██  ██ ██  ██ ██     ██  ██ ██     ██  ██│
│██████ ██  ██ ██████ ██████ ██████ ██████│
│██     ██  ██     ██ ██  ██ ██     ██ ██ │
│██     ██████ ██████ ██  ██ ██████ ██  ██│
\e[93m│                                     v1.1│
│      Thank you for install pusher.    🐍│
└┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┘

     \e[34m>>> \e[0m\e[4mSetting up hipposcreaper.\e[0m \e[34m<<<\e[0m'

# Sets up the hipposcraper
sudo mv * ../
sudo mv ../read_scraper.py ../scrapers/
cd ..

echo -e "\e[34m☑\e[0m hipposcraper configured"
# Sets up the pusher
#+ configure alias

echo -e '
       \e[34m>>> \e[0m\e[4mSetting up shortcuts.\e[0m \e[34m<<<\e[0m'


if ! grep -q tasker ~/.bashrc || \
   ! grep -q pusher ~/.bashrc
then
    echo -e "\n# Pusher aliases" >> ~/.bashrc
fi

if ! grep -q tasker.py ~/.bashrc
then
    tasker_alias="alias tasker='python2 $(pwd)/tasker.py'"
    echo "$tasker_alias" >> ~/.bashrc
    echo -e "\e[34m☑\e[0m $tasker_alias"
else
    echo -e "\e[34m☑\e[0m tasker already defined"

fi

if ! grep -q pusher.py ~/.bashrc
then
    pusher_alias="alias pusher='python3 $(pwd)/pusher.py'"
    echo "$pusher_alias" >> ~/.bashrc
    echo -e "\e[34m☑\e[0m $pusher_alias"
else
    echo -e "\e[34m☑\e[0m pusher already defined"

fi

sudo rm -r pusher/

echo -e '
         \e[34m>>> \e[0m\e[4mReloading .bashrc\e[0m \e[34m<<<\e[0m
'


source ~/.bashrc
sudo rm -r setup_pusher.sh

echo -e "\e[34m☑\e[0m the bash was reloaded"

echo -e '

\e[93mAuthor: \e[37mSantiago Agudelo Gaviria
\e[93mGitHub: \e[37mhttps://github.com/RedLyon1200

\e[93mCollaborator: \e[37mMarlon Aurelio García Morales
\e[93mGitHub: \e[37mhttps://github.com/clasesucatmarlon\n'