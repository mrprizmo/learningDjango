sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade django
sudo pip3 install --upgrade gunicorn
sudo ln -sf /home/box/web/etc/django_conf.py /etc/init.d/gunicorn.d/django_conf.py
sudo /etc/init.d/gunicorn restart
sudo gunicorn --bind 0.0.0.0:8080 ask.wsgi:application