FROM base/archlinux

ENV PACMAN_OPTIONS="--noconfirm --needed"
RUN pacman $PACMAN_OPTIONS -Syu

##############################
# basic tools
##############################
RUN pacman $PACMAN_OPTIONS -S base-devel
RUN pacman $PACMAN_OPTIONS -S git unzip ntfs-3g
RUN pacman $PACMAN_OPTIONS -S man
# for mkfs.vfat
RUN pacman $PACMAN_OPTIONS -S dosfstools

# shell utilities
RUN pacman $PACMAN_OPTIONS -S mlocate tmux bash-completion ctags doxygen the_silver_searcher curl ispell cloc svn openssh
RUN pacman $PACMAN_OPTIONS -S spice

# scripts
RUN pacman $PACMAN_OPTIONS -S python python2
RUN pacman $PACMAN_OPTIONS -S python-pip ipython r ruby

##############################
# libraries
##############################
RUN pacman $PACMAN_OPTIONS -S clang llvm clang-tools-extra
RUN pacman $PACMAN_OPTIONS -S pugixml gtest rapidjson boost

RUN pacman $PACMAN_OPTIONS -S libxslt

##############################
# apps
##############################
RUN pacman $PACMAN_OPTIONS -S docker
RUN pacman $PACMAN_OPTIONS -S emacs
# the command is remove-viewer
RUN pacman $PACMAN_OPTIONS -S tigervnc
RUN pacman $PACMAN_OPTIONS -S virt-viewer
RUN pacman $PACMAN_OPTIONS -S feh tidy mplayer youtube-dl markdown

# compile utilities
RUN pacman $PACMAN_OPTIONS -S cmake ninja antlr2 gperftools valgrind
RUN pacman $PACMAN_OPTIONS -S clojure
# need to install at least a font so that the png file can be outputed
RUN pacman $PACMAN_OPTIONS -S graphviz ttf-dejavu

##############################
# xorg
##############################
RUN pacman $PACMAN_OPTIONS -S xterm xorg-server xorg-xinit rxvt-unicode xorg-xinput xorg-xdm xorg-xconsole
RUN pacman $PACMAN_OPTIONS -S lxde openbox x11vnc xfce4 xorg-xclock
# display managers
RUN pacman $PACMAN_OPTIONS -S lxdm xorg-xdm lightdm gdm xorg-twm


##############################
# AUR
##############################
# aur packages must be built using non-root
# create admin account
RUN useradd -m admin
RUN echo "admin ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/admin && chmod 0440 /etc/sudoers.d/admin
USER admin
WORKDIR /home/admin/tmp
RUN git clone https://aur.archlinux.org/cl-ppcre && cd cl-ppcre && makepkg -si --noconfirm
RUN git clone https://aur.archlinux.org/clx-git && cd clx-git && makepkg -si --noconfirm
RUN git clone https://aur.archlinux.org/stumpwm && cd stumpwm && echo "md5sums=('SKIP' 'SKIP')" >> PKGBUILD && makepkg -si --noconfirm
RUN git clone https://aur.archlinux.org/quicklisp && cd quicklisp && makepkg -si --noconfirm
# RUN git clone https://aur.archlinux.org/rtags-git && cd rtags-git && makepkg -si --noconfirm
# RUN git clone https://aur.archlinux.org/plantuml && cd plantuml && makepkg -si --noconfirm


##############################
# optional
##############################
# RUN pacman -S texlive-core texlive-most 

# vncpasswd
# vncserver

# add user
# RUN useradd -ms /bin/bash admin
# USER admin
# WORKDIR /home/admin

# CMD vncserver :1

# WORKDIR /root
# need manually perform this because it needs password
# RUN git clone https://github.com/lihebi/helium
