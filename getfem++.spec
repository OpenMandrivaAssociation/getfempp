# Debug package is empty
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Name:		getfem++
Summary:	Generic and efficient C++ library for finite element methods
Version:	4.2
Release:	2
Url:		http://home.gna.org/getfem/
License:	LGPLv2+
Group:		Development/C++
Source0:	http://download.gna.org/getfem/stable/getfem-%{version}.tar.gz
Patch0:		getfem-4.2-sfmt.patch
BuildRequires:	blas-devel
BuildRequires:	boost-static-devel
BuildRequires:	pkgconfig(muparser)

%description
The Getfem++ project focuses on the development of a generic and efficient
C++ library for finite element methods. The goal is to provide a library
allowing the computation of any elementary matrix (even for mixed finite
element methods) on the largest class of methods and elements, and for
arbitrary dimension (i.e. not only 2D and 3D problems).

%files
%doc README COPYING
%{_bindir}/getfem-config
%{_prefix}/getfem_toolbox
%{_includedir}/gmm
%{_includedir}/getfem
%{_includedir}/getfem_boost
%{_libdir}/libgetfem.a

#--------------------------------------------------------------------

%prep
%setup -qn getfem-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure2_5x \
	--enable-boost \
	--enable-muparser \
	--disable-python
%make

%install
%makeinstall_std

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 4.0.0-3mdv2011.0
+ Revision: 664823
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 4.0.0-2mdv2011.0
+ Revision: 605447
- rebuild

* Sat Feb 13 2010 Funda Wang <fwang@mandriva.org> 4.0.0-1mdv2010.1
+ Revision: 505336
- New version 4.0.0

* Wed Apr 08 2009 Funda Wang <fwang@mandriva.org> 3.1-1mdv2009.1
+ Revision: 365112
- BR boost
- New version 3.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Fri Apr 18 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.0.3-1mdv2009.0
+ Revision: 195695
- import getfem++


