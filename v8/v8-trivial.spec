#  $Id$

%define _builddir ./
%define _src ./
%define _image ./imagev849/

Name:           v849
Version:        4.9.391
Release:        3%{?dist}
Vendor:         Crystal Computer Corporation
Summary:        JavaScript Engine
Group:          System Environment/Libraries
License:        BSD
URL:            http://code.google.com/p/v8
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python
BuildRequires:  chrpath
BuildRequires:  util-linux

%description
V8 is Google's open source JavaScript engine. V8 is written in C++ and is used 
in Google Chrome, the open source browser from Google. V8 implements ECMAScript 
as specified in ECMA-262, 3rd edition.

See $Id$

%install

mkdir -p $RPM_BUILD_ROOT
cp -a %{_image}/* $RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name libplatform.h -exec sed -i 's|#include "include/v8-platform.h"|#include <v8-platform.h>|' {} \;
chrpath --replace \$ORIGIN/ \
    $RPM_BUILD_ROOT/opt/crystal/lib/v8/4.9/d8 \
    $RPM_BUILD_ROOT/opt/crystal/lib/v8/4.9/libv8.so \
    $RPM_BUILD_ROOT/opt/crystal/lib/v8/4.9/libicui18n.so
%clean

rm -rf $RPM_BUILD_ROOT

%post
ldconfig /opt/crystal/lib/v8/4.9

%files
%defattr(755,root,root,755)
%dir /opt/crystal/lib/v8/4.9
/opt/crystal/lib/v8/4.9/d8
%defattr(644,root,root,755)
/opt/crystal/lib/v8/4.9/libv8.so
/opt/crystal/lib/v8/4.9/libicuuc.so
/opt/crystal/lib/v8/4.9/libicui18n.so

%defattr(755,root,root,644)
%doc LICENSE LICENSE.* OWNERS ChangeLog AUTHORS WATCHLISTS README.md

%package devel
Group:          Development/Libraries
Summary:        Development headers and libraries for v8
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers, libraries and tools for v8.

%files devel

%defattr(755,root,root,-)
%dir /usr/include/v849
%dir /usr/include/v849/libplatform

%defattr(644,root,root,-)
/usr/include/v849/v8config.h
/usr/include/v849/v8-testing.h
/usr/include/v849/v8-version.h
/usr/include/v849/v8.h
/usr/include/v849/v8-experimental.h
/usr/include/v849/v8-profiler.h
/usr/include/v849/libplatform/libplatform.h
/usr/include/v849/v8-util.h
/usr/include/v849/v8-debug.h
/usr/include/v849/v8-platform.h
/usr/include/v849/OWNERS
/opt/crystal/lib/v8/4.9/libv8_base.a
/opt/crystal/lib/v8/4.9/libv8_libbase.a
/opt/crystal/lib/v8/4.9/libv8_nosnapshot.a
/opt/crystal/lib/v8/4.9/libv8_libplatform.a
