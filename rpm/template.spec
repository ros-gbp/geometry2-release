%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-tf2
Version:        0.7.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tf2 package

License:        BSD
URL:            http://www.ros.org/wiki/tf2
Source0:        %{name}-%{version}.tar.gz

Requires:       console-bridge-devel
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-rostime
Requires:       ros-noetic-tf2-msgs
BuildRequires:  console-bridge-devel
BuildRequires:  ros-noetic-catkin >= 0.5.68
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-rostime
BuildRequires:  ros-noetic-tf2-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
tf2 is the second generation of the transform library, which lets the user keep
track of multiple coordinate frames over time. tf2 maintains the relationship
between coordinate frames in a tree structure buffered in time, and lets the
user transform points, vectors, etc between any two coordinate frames at any
desired point in time.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Sep 01 2020 Tully Foote <tfoote@osrfoundation.org> - 0.7.5-1
- Autogenerated by Bloom

* Tue Aug 25 2020 Tully Foote <tfoote@osrfoundation.org> - 0.7.3-1
- Autogenerated by Bloom

* Mon Jun 08 2020 Tully Foote <tfoote@osrfoundation.org> - 0.7.2-1
- Autogenerated by Bloom

* Wed May 13 2020 Tully Foote <tfoote@osrfoundation.org> - 0.7.1-1
- Autogenerated by Bloom

