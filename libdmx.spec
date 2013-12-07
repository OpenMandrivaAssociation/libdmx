%define major 1
%define libname %mklibname dmx %{major}
%define devname %mklibname dmx -d

Name:		libdmx
Summary:	DMX library (part of X.org)
Version:	1.1.3
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libdmx-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
The DMX extension provides support for communication with and control of
Xdmx server. Attributes of the Xdmx server and of the back-end screens
attached to the server can be queried and modified via this protocol.

%package -n %{libname}
Summary:	The dmx Library
Group:		Development/X11
Provides:	%{name} = %{version}

%description -n %{libname}
The DMX extension provides support for communication with and control of
Xdmx server. Attributes of the Xdmx server and of the back-end screens
attached to the server can be queried and modified via this protocol.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}dmx-static-devel < 1.1.2

%description -n %{devname}
Development files for %{name}.

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

%files -n %{devname}
%{_libdir}/libdmx.so
%{_libdir}/pkgconfig/dmx.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/DMX*.3*

