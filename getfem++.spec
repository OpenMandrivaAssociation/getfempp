Name:           getfem++
Summary:        Generic and efficient C++ library for finite element methods
Version:        3.1
Release:        %mkrel 1
Url:            http://home.gna.org/getfem/
License:        LGPLv2+
Group:          Development/C++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:	blas-devel
Source0:	http://download.gna.org/getfem/stable/%name-%version.tar.gz

%description
The Getfem++ project focuses on the development of a generic and efficient 
C++ library for finite element methods. The goal is to provide a library 
allowing the computation of any elementary matrix (even for mixed finite 
element methods) on the largest class of methods and elements, and for 
arbitrary dimension (i.e. not only 2D and 3D problems).

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/getfem-config                    
%{_prefix}/getfem_toolbox
%{_includedir}/gmm
%{_includedir}/getfem
%{_includedir}/getfem_boost
%{_libdir}/libgetfem.a
%{_libdir}/libgetfem.la

#--------------------------------------------------------------------

%prep
%setup -q

%build
export CFLAGS="%optflags -fno-strict-aliasing"
%configure2_5x --enable-boost
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
%{__rm} -rf "%{buildroot}"
