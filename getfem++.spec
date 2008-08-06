Name:           getfem++
Summary:        Generic and efficient C++ library for finite element methods
Version:        3.0.3
Release:        %mkrel 2
Url:            http://home.gna.org/getfem/
License:        LGPL v2+
Group:          Development/C++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://download.gna.org/getfem/stable/getfem++-3.0.3.tar.gz

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
%configure
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%__make

%install
make DESTDIR=%buildroot install

%clean
%{__rm} -rf "%{buildroot}"


