FROM debian:jessie
RUN apt-get -y update
RUN apt-get install -y wget emacs
RUN apt-get install -y mailman apache2 postfix
RUN cp /etc/mailman/apache.conf /etc/apache2/sites-available/mailman.conf
