%define upstream_name    Sys-Info-Driver-Linux
%define upstream_version 0.74

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Linux driver for Sys::Info
License:    GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SYS/%{upstream_name}-%{upstream_version}.tar.gz

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
