%define libdmx %mklibname dmx 1
Name: libdmx
Summary: The dmx Library
Version: 1.0.2
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libdmx-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The DMX extension provides support for communication with and control of
Xdmx server. Attributes of the Xdmx server and of the back-end screens
attached to the server can be queried and modified via this protocol.

#-----------------------------------------------------------

%package -n %{libdmx}
Summary: The dmx Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libdmx}
The DMX extension provides support for communication with and control of
Xdmx server. Attributes of the Xdmx server and of the back-end screens
attached to the server can be queried and modified via this protocol.

#-----------------------------------------------------------

%package -n %{libdmx}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libdmx} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libdmx-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{libdmx}-devel
Development files for %{name}

%files -n %{libdmx}-devel
%defattr(-,root,root)
%{_libdir}/libdmx.so
%{_libdir}/libdmx.la
%{_libdir}/pkgconfig/dmx.pc
%{_mandir}/man3/DMX*.3x.bz2


#-----------------------------------------------------------

%package -n %{libdmx}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libdmx}-devel >= %{version}
Provides: libdmx-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libdmx}-static-devel
Static development files for %{name}

%files -n %{libdmx}-static-devel
%defattr(-,root,root)
%{_libdir}/libdmx.a

#-----------------------------------------------------------

%prep
%setup -q -n libdmx-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libdmx}
%defattr(-,root,root)
%{_libdir}/libdmx.so.1
%{_libdir}/libdmx.so.1.0.0


