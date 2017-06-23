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



# Common Packages

RUN pacman -S --noconfirm python-pip ipython r ruby

# xorg
RUN pacman -S --noconfirm xterm xorg-server xorg-xinit rxvt-unicode xorg-xinput xorg-xdm xorg-xconsole

# compile utilities
RUN pacman -S --noconfirm cmake ninja antlr2 gperftools valgrind clojure
RUN pacman -S --noconfirm ntfs-3g
# for mkfs.vfat
RUN pacman -S --noconfirm dosfstools

# shell utilities
RUN pacman -S --noconfirm mlocate tmux bash-completion ctags doxygen the_silver_searcher curl ispell cloc svn openssh
RUN pacman -S --noconfirm spice

# optional
# RUN pacman -S texlive-core texlive-most 

# libraries
RUN pacman -S --noconfirm libxslt

RUN pacman -S --noconfirm tigervnc

# app
# the command is remove-viewer
# FIXME not working
# RUN pacman -S --noconfirm virt-viewer
# RUN pacman -S --noconfirm feh tidy unzip mplayer youtube-dl markdown

# WORKDIR /root
# need manually perform this because it needs password
# RUN git clone https://github.com/lihebi/helium
