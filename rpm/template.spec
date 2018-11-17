Name:           ros-indigo-tf2-ros
Version:        0.5.20
Release:        0%{?dist}
Summary:        ROS tf2_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf2_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-msgs
Requires:       ros-indigo-tf2-py
Requires:       ros-indigo-xmlrpcpp
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-filters >= 1.11.1
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rosgraph
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-msgs
BuildRequires:  ros-indigo-tf2-py
BuildRequires:  ros-indigo-xmlrpcpp

%description
This package contains the ROS bindings for the tf2 library, for both Python and
C++.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Nov 16 2018 Tully Foote <tfoote@osrfoundation.org> - 0.5.20-0
- Autogenerated by Bloom

* Tue Nov 06 2018 Tully Foote <tfoote@osrfoundation.org> - 0.5.19-0
- Autogenerated by Bloom

* Wed Jul 11 2018 Tully Foote <tfoote@osrfoundation.org> - 0.5.18-0
- Autogenerated by Bloom

* Fri Jan 05 2018 Tully Foote <tfoote@osrfoundation.org> - 0.5.17-0
- Autogenerated by Bloom

* Sat Jul 15 2017 Tully Foote <tfoote@osrfoundation.org> - 0.5.16-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Tully Foote <tfoote@osrfoundation.org> - 0.5.15-0
- Autogenerated by Bloom

* Mon Jan 16 2017 Tully Foote <tfoote@osrfoundation.org> - 0.5.14-0
- Autogenerated by Bloom

* Fri Mar 04 2016 Tully Foote <tfoote@osrfoundation.org> - 0.5.13-0
- Autogenerated by Bloom

* Wed Aug 05 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.12-0
- Autogenerated by Bloom

* Wed Apr 22 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.11-0
- Autogenerated by Bloom

* Tue Apr 21 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.10-0
- Autogenerated by Bloom

* Wed Mar 25 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.9-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.8-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Tully Foote <tfoote@osrfoundation.org> - 0.5.7-0
- Autogenerated by Bloom

