%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl.UTF-8):	%{_pearname} - zestaw testów regresyjnych
Name:		php-pear-%{_pearname}
Version:	1.3.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4b9dd2158e4035318481c93bbd59aaa5
URL:		http://pear.php.net/package/PHPUnit/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
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

%description -l pl.UTF-8
PHPUnit jest zestawem testów regresyjnych używanych przez developerów,
którzy implementują jednostki testowe w PHP. Jest bazowane na JUnit,
który można znaleźć pod adresem http://www.junit.org/.

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
