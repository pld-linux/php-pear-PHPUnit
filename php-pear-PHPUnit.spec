%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit
%define		_status		alpha
%define		_pearname	%{_class}
%define		_alpha		alpha2
Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl):	%{_pearname} - zestaw testów regresyjnych
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{_alpha}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}-%{_alpha}.tgz
# Source0-md5:	dc4796a04b1a51b820d2ed057908c7cb
URL:		http://pear.php.net/package/%{_pearname}/
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
%setup -q -c -n %{name}-%{version}-%{_alpha}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Extensions/Logger,Framework,Runner,TextUI}

#install %{_pearname}-%{version}-%{_alpha}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}-%{_alpha}/Extensions/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Extensions
install %{_pearname}-%{version}-%{_alpha}/Extensions/Logger/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Extensions/Logger
install %{_pearname}-%{version}-%{_alpha}/Framework/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Framework
install %{_pearname}-%{version}-%{_alpha}/Runner/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Runner

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}-%{_alpha}/Tests
%{php_pear_dir}/%{_class}
