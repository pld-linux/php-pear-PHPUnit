%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl):	%{_pearname} - zestaw testów regresyjnych
Name:		php-pear-%{_pearname}
Version:	1.3.1
Release:	1.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	58530b4c9632a9f8a54f17240153821d
URL:		http://pear.php.net/package/PHPUnit/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(PHP/Compat.*)'

%description
PHPUnit is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at http://www.junit.org/.

In PEAR status of this package is: %{_status}.

%description -l pl
PHPUnit jest zestawem testów regresyjnych u¿ywanych przez developerów,
którzy implementuj± jednostki testowe w PHP. Jest bazowane na JUnit,
który mo¿na znale¼æ pod adresem http://www.junit.org/.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}.php
%{php_pear_dir}/%{_class}
