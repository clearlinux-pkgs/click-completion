#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : click-completion
Version  : 0.5.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/93/18/74e2542defdda23b021b12b835b7abbd0fc55896aa8d77af280ad65aa406/click-completion-0.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/18/74e2542defdda23b021b12b835b7abbd0fc55896aa8d77af280ad65aa406/click-completion-0.5.2.tar.gz
Summary  : Fish, Bash, Zsh and PowerShell completion for Click
Group    : Development/Tools
License  : MIT
Requires: click-completion-license = %{version}-%{release}
Requires: click-completion-python = %{version}-%{release}
Requires: click-completion-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(shellingham)
BuildRequires : pypi(six)

%description
# click-completion
Enhanced completion for Click
Add automatic completion support for [fish], [Zsh], [Bash] and
[PowerShell] to [Click].

%package license
Summary: license components for the click-completion package.
Group: Default

%description license
license components for the click-completion package.


%package python
Summary: python components for the click-completion package.
Group: Default
Requires: click-completion-python3 = %{version}-%{release}

%description python
python components for the click-completion package.


%package python3
Summary: python3 components for the click-completion package.
Group: Default
Requires: python3-core
Provides: pypi(click_completion)
Requires: pypi(click)
Requires: pypi(jinja2)
Requires: pypi(shellingham)
Requires: pypi(six)

%description python3
python3 components for the click-completion package.


%prep
%setup -q -n click-completion-0.5.2
cd %{_builddir}/click-completion-0.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637345318
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/click-completion
cp %{_builddir}/click-completion-0.5.2/LICENSE %{buildroot}/usr/share/package-licenses/click-completion/463ed380f2135bea2c767f93143ce38d8100cfac
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/click-completion/463ed380f2135bea2c767f93143ce38d8100cfac

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
