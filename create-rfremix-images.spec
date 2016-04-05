Summary:	Scripts to build RFRemix install media and live CD/DVD
Name:		create-rfremix-images
Version:	0.7.1
Release:	1%{?dist}

Group:		Development/Tools
License:	GPLv2
URL:		http://russianfedora.pro
Source0:	%{name}-%{version}.tar.xz

BuildArch:	noarch
Requires:	mock-configs-rfremix

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
install -dD $RPM_BUILD_ROOT%{_bindir}/
install -dD $RPM_BUILD_ROOT%{_sbindir}/
install -m 755 create-install* $RPM_BUILD_ROOT%{_bindir}/


%files
%doc README ChangeLog README COPYING
%{_bindir}/create-*


%changelog
* Tue Apr  5 2015 Arkady L. Shane <ashejn@yandex-team.ru> - 0.7.1-1.R
- added support of 24 version
- fix cation

* Tue Oct 27 2015 Arkady L. Shane <ashejn@yandex-team.ru> - 0.7.0-1.R
- drop create-live script
- added build Server and Workstation variants

* Thu Nov  7 2013 Arkady L. Shane <ashejn@yandex-team.ru> - 0.6.2-1.R
- update supported distribution version
- update isFinal distribution version
- switch SELinux to permissive mode during building live images
- update livecd-creator parameters

* Thu Nov  3 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.6.1-1.R
- 16 isFinal

* Mon Sep 26 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.6-1.R
- support RFRemix/Fedora 16
- requires new livecd-tools

* Sat May 21 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.5-1
- do not use --nosplitmedia for rawhide
- copy kickstarts only if directory empty (create-live)
- run MAKEDEV lo in pungi section
- added --vcs-configs option to pull configs from git, not from package
- added new pungi parameter (--isfinal) detection
- added --local option for using localhost instead official mirrors
- do not build LiveDVD by -a option

* Mon Feb 28 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.4-1
- adapt to using Fedora 15 with new pungi

* Mon Oct 25 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.3-1
- do not build MeeGo and Games lives at build "all"

* Mon Oct 25 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2-1
- fix names for MeeGo and LiveDVD-Games

* Mon Oct 25 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.1-2
- install create-live to /usr/sbin

* Thu Oct 21 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.1-1
- initial build
