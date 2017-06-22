FROM ubuntu:17.04

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
