FROM debian:jessie
RUN apt-get -y update
RUN apt-get install -y wget libarchive-dev libcurl4-openssl-dev
RUN wget http://131.123.42.38/lmcrs/beta/srcML-Ubuntu14.04-64.deb -O srcml.deb
RUN dpkg -i srcml.deb
