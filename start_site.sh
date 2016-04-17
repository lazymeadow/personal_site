#!/bin/bash

sudo pip install -r install/pip-install-requirements
nohup python main_site.py > main.out &
nohup python art_blog.py > art.out &

