%include	/usr/lib/rpm/macros.perl
Summary:	File-Sort perl module
Summary(pl):	Modu³ perla File-Sort
Name:		perl-File-Sort
Version:	1.00
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Sort-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-Sort sorts text files by lines (or records).

%description -l pl
File-Sort sortuje pliki tekstowe wed³ug linii (lub rekordów).

%prep
%setup -q -n File-Sort-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz eg
%{perl_sitelib}/File/Sort.pm
%{_mandir}/man3/*
