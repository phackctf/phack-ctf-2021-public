FROM php:8.0-apache

EXPOSE 80

# Install composer for Twig
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN apt-get update \
    && apt-get install -y git zip unzip gnupg curl wget \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Configure Apache & PHP
COPY apache/php.ini /usr/local/etc/php/conf.d/app.ini
COPY apache/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY apache/apache.conf /etc/apache2/conf-available/thefaceboox.conf
# RUN a2enmod rewrite remoteip && a2enconf thefaceboox
RUN a2enconf thefaceboox

# Create chall root dir
RUN mkdir /chall

# Copy challenge source
COPY src/web /chall/web
COPY src/composer.lock src/composer.json /chall/

# Setup twig templating engine
WORKDIR /chall
RUN composer require twig/twig