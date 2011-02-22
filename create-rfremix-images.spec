Summary:	Scripts to build RFRemix install media and live CD/DVD
Name:		create-rfremix-images
Version:	0.3
Release:	1

Group:		Development/Tools
License:	GPLv2
URL:		http://russianfedora.ru
Source0:	https://github.com/Tigro/Tarballs/raw/master/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Requires:	mock-configs-rfremix
Requires:	livecd-tools
Requires:	rfremix-kickstarts
Requires:	fedora-kickstarts


%description
This package contains scripts for creating various images of
RFRemix and Fedora.

create-install-images create installation DVD/CD images of
RFRemix/Fedora

create-live create live CD/DVD images of current RFRemix


%prep
%setup -q


%build
#Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
install -dD $RPM_BUILD_ROOT%{_bindir}/
install -dD $RPM_BUILD_ROOT%{_sbindir}/
install -m 755 create-install* $RPM_BUILD_ROOT%{_bindir}/
install -m 755 create-live $RPM_BUILD_ROOT%{_sbindir}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README ChangeLog README COPYING
%{_bindir}/create-*
%{_sbindir}/create-*


%changelog
* Tue Oct 25 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.3-1
- do not build MeeGo and Games lives at build "all"

* Mon Oct 25 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2-1
- fix names for MeeGo and LiveDVD-Games

* Mon Oct 25 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.1-2
- install create-live to /usr/sbin

* Thu Oct 21 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.1-1
- initial build
