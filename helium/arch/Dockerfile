FROM base/archlinux
RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm base-devel
RUN pacman -S --noconfirm clang llvm
RUN pacman -S --noconfirm clang-tools-extra
RUN pacman -S --noconfirm pugixml gtest r rapidjson boost
RUN pacman -S --noconfirm python python2
RUN pacman -S --noconfirm docker
RUN pacman -S --noconfirm emacs

RUN pacman -S --noconfirm git cmake
# need to install at least a font so that the png file can be outputed
RUN pacman -S --noconfirm graphviz ttf-dejavu

# WORKDIR /root
# need manually perform this because it needs password
RUN git clone https://github.com/lihebi/helium /usr/src/helium
WORKDIR /usr/src/helium
RUN mkdir build
WORKDIR /usr/src/helium/build
RUN cmake .. && make -j4
WORKDIR /usr/src/helium
RUN bash setup.sh
