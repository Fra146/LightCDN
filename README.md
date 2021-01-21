If you want to support me, please use this bitcoin address <3
`bc1qgrg0afnx7va6em9cuw5u5qgwkg73ax7fnrnddp`

# LightCDN
This is LightCDN a lightweight CDN (Content Delivery System) made in Python with Flask and Flask-autoindex.
## Installation
First, you need python, this software is made in Python3.8 so use 3.8 or higher.
#### In Debian:

    sudo apt install python3
    sudo apt install python3-pip
 #### In Windows:
 Download Python3 from the website, and install pip3

### Then, you need dependencies
#### In Debian:
    pip3 install pyyaml flask flask_autoindex
#### In Windows:
    pip install pyyaml flask flask_autoindex
## Starting
For testing you can simply run the software
#### In Windows:

    python cdn.py
#### In Debian:

    python3 cdn.py

But, if you want to use it in deployment you need a wsgi server, i can only say to you that the app name is cdn and that the app name is app
For Gunicorn:

    gunicorn cdn:app
