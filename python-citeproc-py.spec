%global modname citeproc-py

Name:           python-%{modname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Yet another Python CSL Processor

License:        BSD
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://pypi.python.org/packages/source/c/citeproc-py/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
BuildRequires:  python-lxml
Requires:       python-lxml

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-lxml
Requires:       python3-lxml

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
rm -rf *.egg-info

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

pushd %{buildroot}%{_bindir}
  mv csl_unsorted python3-csl_unsorted
  sed -i -e '1s|^.*$|#!/usr/bin/env %{__python3}|' python3-csl_unsorted
  for i in csl_unsorted csl_unsorted-3 csl_unsorted-%{python3_version}
  do
    ln -s python3-csl_unsorted $i
  done

  cp python3-csl_unsorted python2-csl_unsorted
  sed -i -e '1s|^.*$|#!/usr/bin/env %{__python2}|' python2-csl_unsorted
  for i in csl_unsorted-2 csl_unsorted-%{python2_version}
  do
    ln -s python2-csl_unsorted $i
  done
popd

%files -n python2-%{modname}
%license LICENSE
%doc README.rst examples
%{_bindir}/python2-csl_unsorted
%{_bindir}/csl_unsorted-2
%{_bindir}/csl_unsorted-%{python2_version}
%{python2_sitelib}/citeproc/
%{python2_sitelib}/citeproc_py*.egg-info/

%files -n python3-%{modname}
%license LICENSE
%doc README.rst examples
%{_bindir}/csl_unsorted
%{_bindir}/python3-csl_unsorted
%{_bindir}/csl_unsorted-3
%{_bindir}/csl_unsorted-%{python3_version}
%{python3_sitelib}/citeproc/
%{python3_sitelib}/citeproc_py*.egg-info/

%changelog
* Wed Nov 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Initial package
