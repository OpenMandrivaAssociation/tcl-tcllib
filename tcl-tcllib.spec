%define oname	tcllib

Name:           tcl-%{oname}
Version:        1.10
Release:        %mkrel 5
Summary:        Collection of utility modules for Tcl
License:        BSD
Group:          Networking/WWW
Source:         %{oname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-root
URL:            http://www.tcl.tk/software/tcllib/
Obsoletes:      tcllib
BuildRequires:  tcl-devel
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

