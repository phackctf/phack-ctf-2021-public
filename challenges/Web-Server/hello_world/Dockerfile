FROM php:8.0-apache

EXPOSE 80

# Configure Apache & PHP
COPY apache/php.ini /usr/local/etc/php/conf.d/app.ini
COPY apache/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY apache/apache.conf /etc/apache2/conf-available/hello-world.conf

RUN a2enconf hello-world

# Copy challenge source
COPY src /chall