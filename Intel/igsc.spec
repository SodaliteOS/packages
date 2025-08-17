%global ver 0.9.6
%global major 0
%global rel 1
%define __cmake_builddir builddir
%define __ninja_common_opts -v -C builddir

Name: igsc
Version: %{ver}
Release: %{rel}%{?dist}
Summary: Graphics System Controller Firmware Update Library

Group: System Environment/Libraries
License: Apache2
URL: https://github.com/intel/igsc
Source0: %{url}/archive/refs/tags/V%{ver}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: git
BuildRequires: pkgconf-pkg-config
BuildRequires: systemd-devel

%description
Intel Graphics System Firmware Update Library (IGSC FUL) is a pure C low level
library that exposes a required API to perform a firmware update of an Intel
discrete graphics device. It uses a cross platform library metee in order to
access the GSC (mei) device. GSC device is an extension of the Intel discrete
graphics device (dGFX).

Graphics System Controller Firmware Update Library


%prep
%autosetup -n %{name}-%{ver}

%build
%cmake -G Ninja -S . -B builddir

%ninja_build

%install
%ninja_install

%files
%defattr(-,root,root)
%license LICENSE.txt
%{_libdir}/libigsc.so.%{ver}.0
%{_libdir}/libigsc.so.%{major}
%{_libdir}/libigsc.so
%{_includedir}/igsc_lib.h
%{_libdir}/cmake/igsc/igscTargets.cmake
%{_libdir}/cmake/igsc/igscTargets-noconfig.cmake
%{_libdir}/cmake/igsc/igscConfig.cmake
%{_libdir}/cmake/igsc/igscConfigVersion.cmake
%{_bindir}/igsc

%doc

%changelog
* Thu Aug 17 2025 Dazed Fairywren <smilescooper@duck.com> - 0.9.6
- Update package version
* Thu Jun 13 2025 Dazed Fairywren <smilescooper@duck.com> - 0.9.5
- Spec file init
