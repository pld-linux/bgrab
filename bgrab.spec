Summary:	Rael's Binary Grabber
Name:		bgrab
Version:	1.3.6
Release:	1
Copyright:	Free
Group:		Networking/News
Group(pl):	Sieciowe/News
URL:		http://www.student.dtu.dk/~c960941/bgrab/
Source0:	%{name}-%{version}.tgz
Patch0:		bgrab-noreplace.patch
Patch1:		bgrab-regex.h.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this program is to automate the downloading of binary
attachments from UseNet Newsgroups.  Given a group name, this program
will connect to a news server, read all messages in that group and 
extract any binary attachments included in any of those messages
(including multipart attachments).  This program does not require any
keyboard interaction and could be fairly easily scheduled to run from
crond.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod 755 configure

%build
CPPFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -I/usr/include/ncurses"
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -I/usr/include/ncurses"
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
LDFLAGS="-s"
export CFLAGS CXXFLAGS CPPFLAGS LDFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bgrab $RPM_BUILD_ROOT%{_bindir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf COPYING README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {COPYING,README*}.gz

%attr(755,root,root) %{_bindir}/*
