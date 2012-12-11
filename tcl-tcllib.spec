%define oname	tcllib

Name:           tcl-%{oname}
Version:        1.10
Release:        %mkrel 6
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



%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.10-6mdv2010.0
+ Revision: 445379
- rebuild

* Fri Dec 05 2008 Adam Williamson <awilliamson@mandriva.org> 1.10-5mdv2009.1
+ Revision: 310129
- move to new location per policy
- rebuild for tcl 8.6

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.10-4mdv2009.0
+ Revision: 261430
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.10-3mdv2009.0
+ Revision: 254190
- rebuild

* Wed Mar 19 2008 Adam Williamson <awilliamson@mandriva.org> 1.10-1mdv2008.1
+ Revision: 188740
- new version 1.10 (needed: 1.9 does not work at all with tcl/tk 8.5, will break other apps if it's installed)

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.9-2mdv2008.1
+ Revision: 171140
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix spacing at top of description

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.9-1mdv2008.1
+ Revision: 140918
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - fix man pages extension


* Mon Dec 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.9-1mdv2007.0
+ Revision: 98593
- Change package name

* Mon Dec 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.9-1mdv2007.1
+ Revision: 98560
- Import tcllib

