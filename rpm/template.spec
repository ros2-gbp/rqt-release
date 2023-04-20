%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rqt-gui-py
Version:        1.3.2
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS rqt_gui_py package

License:        BSD
URL:            http://ros.org/wiki/rqt_gui_py
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-qt-gui >= 0.3.0
Requires:       ros-iron-rqt-gui >= 0.3.0
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-qt-gui >= 0.3.0
BuildRequires:  ros-iron-ros-workspace
BuildRequires:  ros-iron-rqt-gui >= 0.3.0
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-lint-auto
BuildRequires:  ros-iron-ament-lint-common
%endif

%description
rqt_gui_py enables GUI plugins to use the Python client library for ROS.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Apr 20 2023 Dharini Dutia <dharini@openrobotics.org> - 1.3.2-2
- Autogenerated by Bloom

* Tue Apr 11 2023 Dharini Dutia <dharini@openrobotics.org> - 1.3.2-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Dharini Dutia <dharini@openrobotics.org> - 1.3.1-2
- Autogenerated by Bloom

