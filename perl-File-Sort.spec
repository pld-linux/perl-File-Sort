%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Sort
Summary:	File::Sort perl module
Summary(pl):	Modu³ perla File::Sort
Name:		perl-File-Sort
Version:	1.01
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Sort sorts text files by lines (or records).

%description -l pl
File::Sort sortuje pliki tekstowe wed³ug linii (lub rekordów).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README eg
%{perl_vendorlib}/File/Sort.pm
%{_mandir}/man3/*
