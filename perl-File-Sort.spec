#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Sort
Summary:	File::Sort - sort a file or merge sort multiple files
Summary(pl):	File::Sort - sortowanie pliku lub po³±czenie wyniku sortowania wielu plików
Name:		perl-File-Sort
Version:	1.01
Release:	2
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1feb4128bba2edde68ada7838e55863a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The File::Sort Perl module sorts text files by lines (or records). 
Comparisons are based on one or more sort keys extracted from each
line of input, and are performed lexicographically. By default, if
keys are not given, sort regards each input line as a single field. 
The sort is a merge sort.

%description -l pl
Modu³ Perla File::Sort sortuje pliki tekstowe wed³ug wierszy (lub
rekordów). Porównania dokonywane s± w oparciu o jeden lub wiêcej
kluczy sortowania pobieranych z ka¿dego wiersza danych wej¶ciowych i
uk³adane leksykograficznie. Domy¶lnie, je¶li nie podano klucza,
sortowanie dotyczy ca³ych wierszy danych wej¶ciowych jako pojedynczych
pól. Wyniki sortowania s± ³±czone. 

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README eg
%{perl_vendorlib}/File/Sort.pm
%{_mandir}/man3/*
