#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sys
%define		pnam	Hostname-Long
Summary:	Sys::Hostname::Long - try every conceivable way to get full hostname
Summary(pl.UTF-8):	Sys::Hostname::Long - uzyskiwanie pełnej nazwy hosta
Name:		perl-Sys-Hostname-Long
Version:	1.4
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a5b3c23754cbcff10e283d16c42ec3d3
URL:		http://search.cpan.org/dist/Sys-Hostname-Long/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::Hostname::Long - Try every conceivable way to get full hostname.

%description -l pl.UTF-8
Sys::Hostname::Long próbuje wszelkich możliwych sposobów żeby uzyskać
pełną nazwę hosta.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Sys/Hostname
%{perl_vendorlib}/Sys/Hostname/Long.pm
%{_mandir}/man3/*
