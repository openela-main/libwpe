Name:           libwpe
Version:        1.10.0
Release:        4%{?dist}
Summary:        General-purpose library for the WPE-flavored port of WebKit
License:        BSD
URL:            https://github.com/WebPlatformForEmbedded/%{name}
Source0:        https://github.com/WebPlatformForEmbedded/libwpe/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(xkbcommon)

Provides: wpebackend = %{version}-%{release}
Obsoletes: wpebackend < 0.2.0-2

%description
General-purpose library developed for the WPE-flavored port of WebKit

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%autosetup -p1 -n libwpe-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS
%{_libdir}/libwpe-1.0.so.1.*
%{_libdir}/libwpe-1.0.so.1

%files devel
%{_includedir}/wpe-1.0/
%{_libdir}/libwpe-1.0.so
%{_libdir}/pkgconfig/wpe-1.0.pc

%changelog
* Tue Oct 25 2022 Michael Catanzaro <mcatanzaro@redhat.com> - 1.10.0-4
- RHEL 8 import
  Resolves: #2135479
