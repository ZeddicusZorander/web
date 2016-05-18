#!/bin/bash
mv etc/ ~/
sudo ln -sf ~/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf ~/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
gunicorn -c /etc/gunicorn.d/hello.py hello:app
