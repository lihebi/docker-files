# note: srcml only works with jessie! not even testing,
# because the libcrypto version
# i cannot compile it on testing either because boost version i think

FROM debian:jessie
RUN apt-get -y update
RUN apt-get install -y apt-utils
RUN apt-get install -y wget libarchive-dev libcurl4-openssl-dev
RUN wget http://131.123.42.38/lmcrs/beta/srcML-Ubuntu14.04-64.deb -O srcml.deb
RUN dpkg -i srcml.deb

RUN apt-get install -y python3
RUN apt-get install -y git
COPY ./server.py /usr/local/bin/

# sending a file to this port will invoke srcml
# a result file will be send back
EXPOSE 5678

# CMD python3 /usr/local/bin/server.py
CMD python3 /usr/local/bin/server.py

# run this container by
# docker run -p 5678:5678 -d srcml-server
