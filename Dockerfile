FROM php:8.2.10-apache
RUN docker-php-ext-install pdo pdo_mysql mysqli
RUN a2enmod rewrite

COPY html/ /var/www/html
EXPOSE 80