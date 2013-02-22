# $Revision:$, $Date:$
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	XML
%define		pnam	Entities
%include	/usr/lib/rpm/macros.perl
Summary:	XML::Entities - Decode strings with XML entities
Summary(pl.UTF-8):	XML::Entities - dekodowania łańcuchów znaków zawierających encje XML
Name:		perl-XML-Entities
Version:	1.0001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b989ba88e488fddb6ac99f6be4304220
URL:		http://search.cpan.org/dist/XML-Entities/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Based upon the HTML::Entities module by Gisle Aas

This module deals with decoding of strings with XML character
entities. The module provides two functions:

The list of entities is defined in the XML::Entities::Data module. The
list can be generated from the w3.org definition (or any other). Check
perldoc XML::Entities::Data for more details.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/download-entities.pl
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/Entities
%{_mandir}/man1/*
%{_mandir}/man3/*

%define	date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log:$
