%define oname	tcllib

Summary:	Collection of utility modules for Tcl
Name:		tcl-%{oname}
Version:	2.0
Release:	1
License:	BSD
Group:		System/Libraries
Url:		https://www.tcl.tk/software/tcllib/
Source0:	https://core.tcl-lang.org/%{oname}/uv/%{oname}-%{version}.tar.xz
Source100:	tcl-tcllib.rpmlintrc
BuildRequires:	tcl-devel
BuildArch:	noarch

Requires:       tcl(abi) = %{tcl_version}

%description
Tcllib is a collection of utility modules for Tcl. These modules
provide a wide variety of functionality, from implementations of
standard data structures to implementations of common networking
protocols. The intent is to collect commonly used function into
a single library, which users can rely on to be available and
stable.

%files
%{_bindir}/page
%{_bindir}/tcldocstrip
%{_bindir}/dtplite
%{_bindir}/mkdoc
%{_bindir}/nns
%{_bindir}/nnsd
%{_bindir}/nnslog
%{_bindir}/pt

%{tcl_sitelib}/tcllib%{version}
%{_mandir}/mann/*

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%configure --libdir=%{tcl_sitelib}
%make_build doc

%install
%make_install

