Summary:	Rael's Binary Grabber
Summary(pl):	¦ci±gacz binariów Raela
Name:		bgrab
Version:	1.3.6
Release:	2
License:	Free
Group:		Networking/News
Source0:	http://www.student.dtu.dk/~c960941/bgrab/%{name}-%{version}.tgz
Patch0:		%{name}-noreplace.patch
Patch1:		%{name}-regex.h.patch
URL:		http://www.student.dtu.dk/~c960941/bgrab/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this program is to automate the downloading of binary
attachments from UseNet Newsgroups. Given a group name, this program
will connect to a news server, read all messages in that group and
extract any binary attachments included in any of those messages
(including multipart attachments). This program does not require any
keyboard interaction and could be fairly easily scheduled to run from
crond.

%description -l pl
Celem tego programu jest automatyczne ¶ci±ganie binarnych za³±czników
z grup usenetowych. Po podaniu nazwy grupy program ³±czy siê z
serwerem news, czyta wszystkie wiadomo¶ci z grupy i wyci±ga z nich
wszelkie binarne za³±czniki (tak¿e wieloczê¶ciowe). Program ten nie
wymaga interakcji i mo¿e byæ w prosty sposób u¿ywany z crona.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod 755 configure

%build
CPPFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -I%{_includedir}/ncurses"
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -I%{_includedir}/ncurses"
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%configure

%{__make} CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions  -I%{_includedir}/ncurses"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bgrab $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README*
%attr(755,root,root) %{_bindir}/*
