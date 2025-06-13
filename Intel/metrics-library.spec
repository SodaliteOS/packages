%global ver 1.0.198
%global major 1
%global minor 0
%global rel 1
%define __cmake_builddir .

Name: metrics-library
Version: %{ver}
Release: %{rel}%{?dist}
Summary: oneAPI Level Zero Ray Tracing Support

Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/metrics-library
Source0: %{url}/archive/refs/tags/%{name}-%{ver}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: git
BuildRequires: pkgconf-pkg-config
BuildRequires: libdrm-devel

%description
The oneAPI Level Zero Ray Tracing Support library implements high performance CPU
based construction algorithms for 3D acceleration structures that are
compatible with the ray tracing hardware of Intel GPUs.
This library is used by Intel(R) oneAPI Level Zero to implement part of the
RTAS builder extension.
This library should not get used directly but only through Level Zero.
.
oneAPI Level Zero Ray Tracing Support


%prep
%autosetup -n %{name}-%{name}-%{ver}

%build
%cmake .

%make_build

%install
%make_install

%files
%defattr(-,root,root)
%license LICENSE.md
%{_libdir}/libigdml.so.%{major}
%{_libdir}/libigdml.so.%{ver}
%{_includedir}/metrics_library_api_%{major}_%{minor}.h
%{_libdir}/libigdml.so
%{_libdir}/libigdml64.so
%{_libdir}/pkgconfig/libigdml.pc


%doc

%changelog
* Thu Jun 13 2025 Dazed Fairywren <smilescooper@duck.com> - 0.9.5
- Spec file init
