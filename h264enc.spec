Name:		h264enc
Version:	9.4.1
Release:	2
Summary:	An interactive menu-driven frontend for mencoder
Group:		Sound
License:	GPLv2
URL:		http://h264enc.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/h264enc/h264enc/%{name}-%{version}.tar.gz
Requires:	mencoder
BuildArch:	noarch


%description
h264enc is an advanced and powerful interactive menu-driven shell
script written for the GNU/Linux operating system which can help you
to encode a DVD, a video file, a directory with video files or a (S)VCD
to the H.264/MPEG-4 Part 10/AVC video format using the MEncoder encoder
from the MPlayer project and the libx264 library. It supports muxing
the final encode from AVI to Matroska, from AVI to OGM, from AVI to TS
and from AVI to the MP4 container.


%prep
%setup -q
sed -i -e "s|^PREFIX=.*$||" \
  -e "s|^DOCDIR=.*$|DOCDIR=./installed-docs|" \
  -e 's|^MANDIR=.*$|MANDIR=$PREFIX/share/man/man1|' \
  ./install

sed -i -e "s|\r$||" matrices/eqm_avc_hr_matrix
sed -i -e "s|/usr/local|%{_prefix}|" doc/README.matrices

%build
echo "i'm a script"

%install
PREFIX="$RPM_BUILD_ROOT%{_prefix}" ./install
rm ./installed-docs/uninstall

%files
%doc ./installed-docs/*
%{_bindir}/h264enc
%{_mandir}/man1/h264enc.1*


%changelog
* Fri Nov 18 2011 Alexander Khrukin <akhrukin@mandriva.org> 9.4.1-1
+ Revision: 731594
- imported package h264enc

