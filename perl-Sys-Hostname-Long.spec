#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sys
%define		pnam	Hostname-Long
Summary:	Sys::Hostname::Long - try every conceivable way to get full hostname
Summary(pl):	Sys::Hostname::Long - uzyskiwanie pe³nej nazwy hosta
Name:		perl-Sys-Hostname-Long
Version:	1.2
Release:	3
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae0fb8b0ed821ae2fc8e8009b8732978
BuildRequires:	perl-devel >= 1:5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-112.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::Hostname::Long - Try every conceivable way to get full hostname.

%description -l pl
Sys::Hostname::Long próbuje wszelkich mo¿liwych sposobów ¿eby uzyskaæ
pe³n± nazwê hosta.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=site
%{__make} \
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
%dir %{perl_sitelib}/Sys/Hostname
%{perl_sitelib}/Sys/Hostname/Long.pm
%{_mandir}/man3/*
