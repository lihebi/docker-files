FROM debian:testing


# r-doc-info libstdc++-6-doc bash-doc
# gnome-commander
# imagemagick

RUN apt-get update -y
# build essential packages
RUN apt-get install -y\
            build-essential  pkg-config cmake ninja-build\
            cmake-curses-gui autoconf
# system packages
RUN apt-get install -y\
            cifs-utils ntfs-3g samba smbclient 
            
# shell utility packages
RUN apt-get install -y\
            tmux gawk global sudo git curl silversearcher-ag tree exuberant-ctags\
            doxygen gdb sysstat tidy subversion perl cloc\
            python3-pip python-pip swi-prolog flex bison\
            mc iw wicd\
            antlr antlr3 libantlr-dev netselect-apt\
            pylint3 antlr4

# libraries
RUN apt-get install -y\
            sqlite3 libsqlite3-dev gnulib libboost-all-dev libgtest-dev libpugixml-dev\
            libpng-dev libz-dev libpoppler-glib-dev libpoppler-private-dev\
            r-base r-base-dev z3 libz3-dev zlib1g-dev libwebkitgtk-dev\
            libarchive-dev\
            libxslt1-dev libcurl4-openssl-dev
            lua5.3 liblua5.3-dev

# desktop
# RUN apt-get install -y\
#             xorg xinit stumpwm xcursor-themes ratpoison conky dzen2 rxvt-unicode-256color\
#             xsel autocutsel xdm pavucontrol xpdf feh conkeror graphviz\
#             plantuml chromium virt-viewer virt-manager lm-sensors

# heavy app
RUN apt-get install -y\
            emacs25 llvm clang

# git configuration
RUN git config --global user.name "Hebi Li";
RUN git config --global user.email "lihebi.com@gmail.com";
RUN git config --global credential.helper cache;
RUN git config --global push.default simple;

# config repos
RUN git clone https://github.com/lihebi/dothebi ~/.hebi
RUN git clone https://github.com/lihebi/emacs.d ~/.emacs.d
RUN git clone https://github.com/lihebi/dotinfo ~/.info
RUN git clone https://github.com/lihebi/stumpwm.d ~/.stumpwm.d
RUN cd ~/.hebi && ./install.sh

# run emacs to bootstrap the packages

# no quicklisp
# no gtest compilation
# no srcml
