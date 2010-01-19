%define upstream_name    Sys-Info-Driver-Linux
%define upstream_version 0.74

Summary:	Linux driver for Sys::Info  
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
License:        GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SYS/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Sys-Info
BuildRequires:	perl-Unix-Processors
BuildRequires:	perl-Linux-Distribution
Requires:	perl-Sys-Info-Base
Requires:	perl-Linux-Distribution
Requires:	perl-Unix-Processors
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Perl module for linux driver for Sys::Info  .

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

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
