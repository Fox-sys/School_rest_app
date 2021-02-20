# School app made for school №45
technological stack:

1) python 3.8.3
2) Django 3.1.6
3) Django Rest Framework 3.12.2
4) PostgreSQL 12
5) Docker and Docker-compose
6) nginx

# Start up project
On linux:

1) git clone https://github.com/Fox-sys/School_rest_app.git
2) cd School_rest_app/
3) sudo docker-compose -f docker-compose.prod.yml up --build -d
4) sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
5) sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic
6) sudo docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

# Patch note
Version: 1.2.0

1) Permissions for diary service
2) some fixes
3) homework views and serializers were refactored