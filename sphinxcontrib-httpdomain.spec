#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-httpdomain
Version  : 1.7.0
Release  : 38
URL      : https://files.pythonhosted.org/packages/b4/8d/8dbb8b6745d7a59084cf1b28837b32c9717c1b4a97333d5b25e25fa9813b/sphinxcontrib-httpdomain-1.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b4/8d/8dbb8b6745d7a59084cf1b28837b32c9717c1b4a97333d5b25e25fa9813b/sphinxcontrib-httpdomain-1.7.0.tar.gz
Summary  : Sphinx domain for documenting HTTP APIs
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-httpdomain-license = %{version}-%{release}
Requires: sphinxcontrib-httpdomain-python = %{version}-%{release}
Requires: sphinxcontrib-httpdomain-python3 = %{version}-%{release}
Requires: Sphinx
Requires: six
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
============================

%package license
Summary: license components for the sphinxcontrib-httpdomain package.
Group: Default

%description license
license components for the sphinxcontrib-httpdomain package.


%package python
Summary: python components for the sphinxcontrib-httpdomain package.
Group: Default
Requires: sphinxcontrib-httpdomain-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-httpdomain package.


%package python3
Summary: python3 components for the sphinxcontrib-httpdomain package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_httpdomain)
Requires: pypi(six)
Requires: pypi(sphinx)

%description python3
python3 components for the sphinxcontrib-httpdomain package.


%prep
%setup -q -n sphinxcontrib-httpdomain-1.7.0
cd %{_builddir}/sphinxcontrib-httpdomain-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583697267
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-httpdomain
cp %{_builddir}/sphinxcontrib-httpdomain-1.7.0/LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-httpdomain/2e3d96196666de3d8582c67fcdc7804f28e1fe0c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-httpdomain/2e3d96196666de3d8582c67fcdc7804f28e1fe0c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
