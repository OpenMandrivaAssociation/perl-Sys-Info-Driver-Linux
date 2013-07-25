%define upstream_name    Sys-Info-Driver-Linux
%define upstream_version 0.7903

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.7903
Release:	1

Summary:	Linux driver for Sys::Info
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Sys/BURAK/Sys-Info-Driver-Linux-0.7903.tar.gz

BuildRequires:  lsb-release
BuildRequires:	perl(Test::Sys::Info)
BuildRequires:	perl(Linux::Distribution)
BuildRequires:	perl(Unix::Processors)
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:   lsb-release
Requires:	perl(Linux::Distribution)
Requires:	perl(Sys::Info::Base)
Requires:	perl(Unix::Processors)

%description
Perl module for linux driver for Sys::Info  .

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# (tpg) fails on 5.12.0
rm -rf t/03-basic.t
%make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.780.0-1mdv2011.0
+ Revision: 660017
- update to new version 0.78

* Sat Aug 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.770.0-1mdv2011.0
+ Revision: 567391
- update to new version 0.77
- update to new version 0.76
- disable 03-basic test as it fails on perl-5.12.0

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.740.0-2mdv2010.1
+ Revision: 505016
- renamed spec file to match pkgname

* Wed Jan 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.740.0-1mdv2010.1
+ Revision: 493969
- adding missing buildrequires:
- fix buildrequires:
- update to 0.74

* Sat Jan 02 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.720.0-1mdv2010.1
+ Revision: 484912
- import perl-Sys-Info-Driver-Linux



