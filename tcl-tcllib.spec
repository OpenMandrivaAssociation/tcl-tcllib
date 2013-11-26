%define oname	tcllib

Summary:	Collection of utility modules for Tcl
Name:		tcl-%{oname}
Version:	1.10
Release:	7
License:	BSD
Group:		System/Libraries
Url:		http://www.tcl.tk/software/tcllib/
Source0:	%{oname}-%{version}.tar.bz2
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
%defattr(-,root,root,0755)
%{_bindir}/page
%{_bindir}/tcldocstrip
%{_bindir}/dtplite
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

# File conflict with tk package
rm -f %{buildroot}%{_mandir}/mann/geometry.n*

