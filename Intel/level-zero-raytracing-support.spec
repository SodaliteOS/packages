%global ver 1.1.0
%global rel 1
%define __cmake_builddir build

Name: level-zero-raytracing-support
Version: %{ver}
Release: %{rel}%{?dist}
Summary: oneAPI Level Zero Ray Tracing Support

Group: System Environment/Libraries
License: Apache2
URL: https://github.com/intel/level-zero-raytracing-support
Source0: %{url}/archive/refs/tags/v%{ver}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: git
BuildRequires: pkgconf-pkg-config

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
%autosetup -p1 -n %{name}-%{ver}

%build
%cmake -B build \
-G Ninja \
-D CMAKE_INSTALL_PREFIX=/usr \
-D CMAKE_BUILD_TYPE=Release .

%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root)
%config(noreplace)
%license LICENSE.txt
%license third-party-programs*
%{_libdir}/libze_intel_gpu_raytracing.so


%doc

%changelog
* Thu Mar 6 2025 Sven Woop <sven.woop@intel.com> - 1.1.0
- Added support for PTL RTAS layout.
* Thu Jun 8 2023 Pavel Androniychuk <pavel.androniychuk@intel.com> - 1.0.0
- Spec file init
