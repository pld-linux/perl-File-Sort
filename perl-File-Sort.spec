%include	/usr/lib/rpm/macros.perl
Summary:	File-Sort perl module
Summary(pl):	Modu³ perla File-Sort
Name:		perl-File-Sort
Version:	0.90
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Sort-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
File-Sort sorts text files by lines (or records). 

%description -l pl
File-Sort sortuje pliki tekstowe wed³ug linii (lub rekordów).

%prep
%setup -q -n File-Sort-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/File/Sort
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz eg

%{perl_sitelib}/File/Sort.pm
%{perl_sitearch}/auto/File/Sort

%{_mandir}/man3/*
