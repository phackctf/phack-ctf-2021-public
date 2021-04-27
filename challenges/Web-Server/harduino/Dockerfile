# We need php < 7 in order to use /e preg modifier
FROM php:5.4-apache

EXPOSE 80

# Install composer for Twig
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN apt-get update \
    && apt-get install -y git zip unzip gnupg curl wget \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Configure Apache & PHP
COPY apache/php.ini /usr/local/etc/php/conf.d/app.ini
COPY apache/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY apache/apache.conf /etc/apache2/conf-available/harduino.conf

# Enable conf / webapp
RUN a2enconf harduino
RUN a2ensite 000-default.conf

# Copy challenge source
COPY src /chall

# Copy flag
COPY static/flag.txt /flag.txt

# Setup twig template engine
WORKDIR /chall/workspace/apps/arduino
RUN composer require twig/twig