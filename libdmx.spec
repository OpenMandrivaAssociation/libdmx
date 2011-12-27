%define major		1
%define libname 	%mklibname dmx %{major}
%define develname	%mklibname dmx -d

Name: libdmx
Summary: DMX library (part of X.org)
Version: 1.1.1
Release: 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libdmx-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.1.1
BuildRequires: x11-proto-devel >= 7.5
BuildRequires: x11-util-macros >= 1.0.1

%description
The DMX extension provides support for communication with and control of
Xdmx server. Attributes of the Xdmx server and of the back-end screens
attached to the server can be queried and modified via this protocol.

%package -n %{libname}
Summary: The dmx Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The DMX extension provides support for communication with and control of
Xdmx server. Attributes of the Xdmx server and of the back-end screens
attached to the server can be queried and modified via this protocol.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.5
Obsoletes: %{_lib}dmx1-devel
Obsoletes: %{_lib}dmx-static-devel

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
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdmx.so.%{major}*

%files -n %{develname}
%{_libdir}/libdmx.so
%{_libdir}/pkgconfig/dmx.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/DMX*.3*

