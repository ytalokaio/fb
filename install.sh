#!/bin/bash
echo 'qual o nome do database?'
read database
echo 'qual o password do mysql?'
read password
apt-get update
apt-get upgrade
apt-get -y remove gunicorn
apt-get -y install python3-pip libmysqlclient-dev libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password '$password''
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password '$password''
sudo apt-get -y install mysql-server-5.6
pip3 install -r requirements.txt
mkdir -p /var/www/django/static
mkdir -p /var/www/django/media
chown -c -R django /var/django/www/
cp -a /media /var/www/django/media
rm -r /etc/init/gunicorn.conf
rm -r /etc/nginx/sites-available/django
ln -s /home/django/framework-base/gunicorn.conf /etc/init/gunicorn.conf
ln -s /home/django/framework-base/django /etc/nginx/sites-available/django
echo 'create database if not exists '$database';' | mysql -u root -p$password
#python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
initctl reload-configuration
service nginx restart
service gunicorn restart
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
ls -lh /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo reboot
