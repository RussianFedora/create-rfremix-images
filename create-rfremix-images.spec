Summary:	Scripts to build RFRemix install media and live CD/DVD
Name:		create-rfremix-images
Version:	0.6
Release:	1.R

Group:		Development/Tools
License:	GPLv2
URL:		http://russianfedora.ru
Source0:	http://download.rfremix.ru/storage/create-rfremix-images/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Requires:	mock-configs-rfremix
Requires:	livecd-tools >= 16
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

* Tue Oct 25 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.3-1
- do not build MeeGo and Games lives at build "all"

* Mon Oct 25 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2-1
- fix names for MeeGo and LiveDVD-Games

* Mon Oct 25 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.1-2
- install create-live to /usr/sbin

* Thu Oct 21 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.1-1
- initial build
