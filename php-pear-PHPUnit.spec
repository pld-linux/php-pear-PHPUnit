%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit
%define		_pearname	%{_class}
Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl):	%{_pearname} - zestaw test�w regresyjnych
Name:		php-pear-%{_pearname}
Version:	0.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	6e771e368d51913258a8efa175a6e437
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHPUnit is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at http://www.junit.org/.

%description -l pl
PHPUnit jest zestawem test�w regresyjnych u�ywanych przez developer�w,
kt�rzy implementuj� jednostki testowe w PHP. Jest bazowane na JUnit,
kt�ry mo�na znale�� pod adresem http://www.junit.org/.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/{%{_class},GUI}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}/GUI/*.php $RPM_BUILD_ROOT%{php_pear_dir}//GUI
install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/GUI/README
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/GUI
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/GUI/*.php
%{php_pear_dir}/*.php
