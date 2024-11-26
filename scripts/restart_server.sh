#!/bin/bash

# Navigate to the project directory
cd /var/app/current/

# Activate virtual environment
source env/bin/activate

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate --noinput

# Restart Gunicorn
pkill gunicorn
gunicorn --bind 0.0.0.0:8080 ebdjango.wsgi:application --daemon

# Restart Nginx to apply any configuration changes
sudo systemctl restart nginx
