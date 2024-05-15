#!/usr/bin/env bash
# Install nginx on server
apt-get -y update > /dev/null
apt-get -y install nginx > /dev/null

#create these directories for each of our sites
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#Create a fake HTML file
touch /data/web_static/releases/test/index.html


# Update symbolic link to current release
if [ -d "/data/web_static/current" ]; then
  sudo rm -rf /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

#allow us to easily create or edit the content in this directory
sudo chown -Rh ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#restart Nginx after updating the configuration
service nginx restart
