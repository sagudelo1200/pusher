#!/bin/bash
# Sets up the pusher and hipposcraper:
#+  Configures aliases in .bashrc
#+  Sets inputted user information in auth.json

echo -e "Thanks for downloading Pusher!\nTo get started, let's set up some hipposcraper stuff on your computer\n"
echo "  -> Checking if auth_data.json exists..."
if [ ! -f auth_data.json ]
then
    echo "  -> auth_data.json does not exist, creating it..."
    echo "{\"intra_user_key\": \"YOUR_HOLBERTON_INTRANET_USERNAME\", \"intra_pass_key\": \"YOUR_HOLBERTON_INTRANET_PASSWORD\", \"author_name\": \"YOUR_NAME\", \"github_username\": \"YOUR_GITHUB_USERNAME\", \"github_profile_link\": \"YOUR_GITHUB_PROFILE_LINK\"}" > auth_data.json
else
    echo "  -> auth_data.json exists, proceeding..."
fi
echo -n "  -> Holberton Intranet email: "
read -r email
echo -n "  -> Holberton Intranet password: "
read -r password
echo -n "  -> Full name (for author section of README's): "
read -r name
echo -n "  -> Github username: "
read -r github_username
echo -n "  -> Github profile link: "
read -r github_link

# & escaper
PASSWORD=$(sed 's/[\*\.&]/\\&/g' <<<"$password")

if grep -q YOUR_HOLBERTON_INTRANET_USERNAME auth_data.json
then
    sed -i "s/YOUR_HOLBERTON_INTRANET_USERNAME/$email/g" auth_data.json
fi

if grep -q YOUR_HOLBERTON_INTRANET_PASSWORD auth_data.json
then
    sed -i "s/YOUR_HOLBERTON_INTRANET_PASSWORD/$PASSWORD/g" auth_data.json
fi

if grep -q YOUR_NAME auth_data.json
then
    sed -i "s/YOUR_NAME/$name/g" auth_data.json
fi

if grep -q YOUR_GITHUB_USERNAME auth_data.json
then
    sed -i "s/YOUR_GITHUB_USERNAME/$github_username/g" auth_data.json
fi

if grep -q YOUR_GITHUB_PROFILE_LINK auth_data.json
then
    sed -i "s,YOUR_GITHUB_PROFILE_LINK,$github_link,g" auth_data.json
fi

if grep -q ENTER_FULL_PATHNAME_TO_DIRECTORY_HERE hipposcrape.sh
then
    sed -i "s/ENTER_FULL_PATHNAME_TO_DIRECTORY_HERE/$(pwd)/g" hipposcrape.sh
fi

echo "Setting aliases:"

if ! grep -q tasker ~/.bashrc || \
   ! grep -q pusher ~/.bashrc
then
    echo -e "\n# Pusher aliases" >> ~/.bashrc
fi

if ! grep -q tasker.py ~/.bashrc
then
    tasker_alias="alias tasker='python2 $(pwd)/tasker.py'"
    echo "$tasker_alias" >> ~/.bashrc
    echo "  -> $tasker_alias"
else
    echo "  -> tasker already defined"

fi

if ! grep -q tasker.py ~/.bashrc
then
    pusher_alias="alias pusher='python3 $(pwd)/pusher.py'"
    echo "$pusher_alias" >> ~/.bashrc
    echo "  -> $pusher_alias"
else
    echo "  -> pusher already defined"

fi

echo "Reloading .bashrc:"
source ~/.bashrc

echo "All set!"
