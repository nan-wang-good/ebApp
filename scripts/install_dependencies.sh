#!/bin/bash
cd /home/ec2-user/environment/ebdjango
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
