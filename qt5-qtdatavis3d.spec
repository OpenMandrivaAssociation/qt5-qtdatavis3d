%define major 5
%define libname %mklibname qt5datavis3d %{major}
%define devname %mklibname qt5datavis3d -d
%define beta beta

Name:	qt5-qtdatavis3d
Version: 5.10.0
%if "%{beta}" != "%{nil}"
Source0: http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/qtdatavis3d-everywhere-src-%{version}-%{beta}.tar.xz
Release: 0.%{beta}.1
%else
Source0: http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/qtdatavis3d-opensource-src-%{version}.tar.xz
Release: 1
%endif
Summary: Qt 3D data visualization library
URL: https://github.com/qtproject/qtnetworkauth
License: LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-with-Qt-Company-Qt-exception-1.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Widgets)

%description
Qt 3D data visualization library

%package -n %{libname}
Summary: Qt library for 3D data visualization
Group: System/Libraries

%description -n %{libname}
Qt library for 3D data visualization

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package examples
Summary: Example code for the %{name} library
Group: Development/C
Requires: %{devname} = %{EVRD}
BuildRequires: pkgconfig(Qt5Widgets)

%description examples
Example code for the %{name} library

%prep
%if "%{beta}" != "%{nil}"
%setup -qn qtdatavis3d-everywhere-src-%{version}-%{beta}
%else
%setup -qn qtdatavis3d-opensource-src-%{version}
%endif
%qmake_qt5 *.pro

%build
%make

%install
make install install_docs INSTALL_ROOT="%{buildroot}"
find "%{buildroot}" -type f -name '*.prl' -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d' {} \;

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/qml/QtDataVisualization

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/Qt5DataVisualization
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/*.prl

%files examples
%{_libdir}/qt5/examples/datavisualization
