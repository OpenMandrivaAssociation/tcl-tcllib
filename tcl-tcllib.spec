%define oname	tcllib

Summary:	Collection of utility modules for Tcl
Name:		tcl-%{oname}
Version:	1.18
Release:	1
License:	BSD
Group:		System/Libraries
Url:		http://www.tcl.tk/software/tcllib/
Source0:	%{oname}-%{version}.tar.bz2
Source100:	tcl-tcllib.rpmlintrc
BuildRequires:	tcl-devel
BuildArch:	noarch

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
%{_bindir}/nns
%{_bindir}/nnsd
%{_bindir}/nnslog
%{_bindir}/pt

%{tcl_sitelib}/tcllib%{version}
%{_mandir}/mann/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x --libdir=%{tcl_sitelib}
%make

%install
%makeinstall_std

