%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit
%define		_status		alpha
%define		_pearname	%{_class}
Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl):	%{_pearname} - zestaw testów regresyjnych
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.alpha1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}-alpha1.tgz
# Source0-md5:	4ebb22d0a183612dfa53f75da225d0b8
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHPUnit is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at http://www.junit.org/.

This class has in PEAR status: %{_status}.

%description -l pl
PHPUnit jest zestawem testów regresyjnych u¿ywanych przez developerów,
którzy implementuj± jednostki testowe w PHP. Jest bazowane na JUnit,
który mo¿na znale¼æ pod adresem http://www.junit.org/.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{version}-alpha1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Extensions/Logger,Framework,Runner,TextUI}

#install %{_pearname}-%{version}-alpha1/*.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}-alpha1/Extensions/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Extensions
install %{_pearname}-%{version}-alpha1/Extensions/Logger/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Extensions/Logger
install %{_pearname}-%{version}-alpha1/Framework/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Framework
install %{_pearname}-%{version}-alpha1/Runner/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Runner

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}-alpha1/Tests
%{php_pear_dir}/%{_class}
