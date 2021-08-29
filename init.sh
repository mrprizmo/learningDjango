sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/hello.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8080 hello:app
sudo curl -vv 'http://127.0.0.1/hello/?a=1&a=2&b=3'
sudo curl -vv 'http://127.0.0.1:8080/?a=1&a=2&b=3'
