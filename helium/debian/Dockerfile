FROM debian:jessie

RUN apt-get update -y
RUN apt-get install -y apt-utils
RUN apt-get install -y build-essential  pkg-config cmake autoconf
RUN apt-get install -y git doxygen cloc
RUN apt-get install -y sqlite3 libsqlite3-dev libboost-all-dev libgtest-dev
RUN apt-get install -y libpugixml-dev
RUN apt-get install -y emacs
RUN apt-get install -y wget
RUN apt-get install -y libtinfo-dev libz-dev
RUN apt-get install -y subversion
RUN apt-get install -y locate

# download srcml
RUN wget http://131.123.42.38/lmcrs/beta/srcML-Ubuntu14.04-64.deb -O /tmp/srcml.deb
RUN dpkg -i /tmp/srcml.deb
# clone rapidjson
RUN git clone https://github.com/miloyip/rapidjson /tmp/rapidjson
RUN cp -r /tmp/rapidjson/include/rapidjson /usr/include

# compile llvm
RUN svn co http://llvm.org/svn/llvm-project/llvm/trunk /tmp/llvm
RUN svn co http://llvm.org/svn/llvm-project/cfe/trunk /tmp/llvm/tools/clang
RUN svn co http://llvm.org/svn/llvm-project/clang-tools-extra/trunk /tmp/llvm/tools/clang/tools/extra
RUN svn co http://llvm.org/svn/llvm-project/compiler-rt/trunk /tmp/llvm/projects/compiler-rt
WORKDIR /tmp/llvm-build
RUN cmake /tmp/llvm -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_RTTI=ON
# compile it manually because it cost a hour
# RUN make install

WORKDIR /tmp/gtest-build
RUN cmake /usr/src/gtest && make && cp libgtest*.a /usr/local/lib

# clone helium
# need to run manually because needs password
# RUN git clone https://github.com/lihebi/helium ~
# RUN cd ~/helium/lib/ctags* && make && make-install
# RUN ldconfig
# RUN mkdir ~/helium/build && cd ~/helium/build && cmake .. && make -j4

# set up helium
# RUN bash ~/helium/setup.sh
# RUN bash ~/helium/setup-shell.sh

RUN apt-get update -y
RUN apt-get install -y build-essential  pkg-config cmake autoconf
RUN apt-get install -y git doxygen cloc
RUN apt-get install -y sqlite3 libsqlite3-dev libboost-all-dev libgtest-dev
RUN apt-get install -y libpugixml-dev
RUN apt-get install -y emacs
RUN apt-get install -y wget
RUN apt-get install -y libtinfo-dev libz-dev
RUN apt-get install -y subversion

# the llvm and clang in repo is 3.8 and 3.9, we need 4.0
# also the clang config file in the official repo has setup issue
# download the binary from llvm release
# RUN apt-get install -y llvm clang libclang-dev

# RUN cd /tmp && wget http://releases.llvm.org/4.0.0/clang+llvm-4.0.0-x86_64-linux-gnu-debian8.tar.xz

# rapidjson in debian is 0.12, we should use 1.0
# use the github version and copy the header files
# RUN apt-get install rapidjson-dev

# RUN git clone https://github.com/miloyip/rapidjson

# required to run srcml
RUN apt-get install -y locate
RUN apt-get install -y libcrypto++-dev

# compiling srcml because the binary provided uses libcrypto-1.0.0
# specifically, but now debian ship with 1.0.2 ..
RUN apt-get install -y libarchive-dev libxml2-dev
RUN apt-get install -y libcurl4-openssl-dev libxslt-dev
RUN apt-get install -y antlr libantlr-dev libssl-dev

# manual steps
# - compile llvm
# - rapidjson
# - compile gtest
# - clone helium, build ctags
# - install srcml
