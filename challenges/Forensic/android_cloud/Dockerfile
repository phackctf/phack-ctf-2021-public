FROM php:7.4-apache

COPY conf/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY conf/apache.conf /etc/apache2/conf-available/android-lock.conf

COPY webapp /webapp

RUN a2enconf android-lock

# Install APCu caching tool
RUN pecl install apcu && docker-php-ext-enable apcu

# Download challenge archive
RUN mkdir /webapp/dev-backups

RUN curl "https://REMOVED.s3.fr-par.scw.cloud/android-cloud/android.tar.gz" \
    --output /webapp/dev-backups/backup@03-10-2020.zip
    
RUN php --ini