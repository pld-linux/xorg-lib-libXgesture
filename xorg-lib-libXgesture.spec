Summary:	Xgesture extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia Xgesture
Name:		xorg-lib-libXgesture
Version:	0.1.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://download.tizen.org/releases/2.2.1/latest/repos/tizen-main/source/libXgesture-%{version}-3.3.src.rpm
# Source0-md5:	95e27d4041313b8a24746c5655282b39
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-gestureproto-devel >= 0.1.0
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
Obsoletes:	libXgesture
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xgesture extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia Xgesture.

%package devel
Summary:	Header files for libXgesture library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXgesture
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-gestureproto-devel >= 0.1.0
Obsoletes:	libXgesture-devel

%description devel
Xgesture extension library.

This package contains the header files needed to develop programs that
use libXgesture.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia Xgesture.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXgesture.

%package static
Summary:	Static libXgesture library
Summary(pl.UTF-8):	Biblioteka statyczna libXgesture
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXgesture-static

%description static
Xgesture extension library.

This package contains the static libXgesture library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia Xgesture.

Pakiet zawiera statyczną bibliotekę libXgesture.

%prep
%setup -q -c -T -n libXgesture-%{version}
rpm2cpio %{SOURCE0} | cpio -i libXgesture-%{version}.tar.gz
tar xf libXgesture-%{version}.tar.gz -C ..

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NOTICE
%attr(755,root,root) %{_libdir}/libXgesture.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXgesture.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXgesture.so
%{_libdir}/libXgesture.la
%{_includedir}/X11/extensions/gesture.h
%{_pkgconfigdir}/xgesture.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXgesture.a
