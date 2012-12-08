%define major		1
%define libname 	%mklibname dmx %{major}
%define develname	%mklibname dmx -d

Name:		libdmx
Summary:	DMX library (part of X.org)
Version:	1.1.2
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libdmx-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	x11-proto-devel >= 7.5
BuildRequires:	x11-util-macros >= 1.0.1

%description
The DMX extension provides support for communication with and control of
Xdmx server. Attributes of the Xdmx server and of the back-end screens
attached to the server can be queried and modified via this protocol.

%package -n %{libname}
Summary:	The dmx Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
The DMX extension provides support for communication with and control of
Xdmx server. Attributes of the Xdmx server and of the back-end screens
attached to the server can be queried and modified via this protocol.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	libxorg-x11-devel < 7.0
Conflicts:	x11-proto-devel < 7.5
Obsoletes:	%{_lib}dmx1-devel < 1.1.2
Obsoletes:	%{_lib}dmx-static-devel < 1.1.2

%description -n %{develname}
Development files for %{name}

%prep
%setup -q

%build
%configure2_5x	\
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdmx.so.%{major}*

%files -n %{develname}
%{_libdir}/libdmx.so
%{_libdir}/pkgconfig/dmx.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/DMX*.3*

%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.2-1
+ Revision: 783811
- version update 1.1.2

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-3
+ Revision: 745604
- rebuild
- disabled static build
- removed .la files
- employed major macro
- cleaned up spec

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2
+ Revision: 660236
- mass rebuild

* Fri Oct 29 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 590020
- new release

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 463688
- New version: 1.1.0

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-6mdv2010.0
+ Revision: 425529
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-5mdv2009.0
+ Revision: 222534
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.
    - Update BuildRequires and resubmit package.

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2008.1
+ Revision: 150550
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Jul 21 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-3mdv2008.0
+ Revision: 54145
- rebuild for 2008
- new devel policy

