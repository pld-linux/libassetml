Summary:	Library assetml to share and reuse content like image and audio file
Name:		libassetml
Version:	1.2.1
Release:	1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/ofset/%{name}-%{version}.tar.gz
# Source0-md5:	4b10fd0fb8e00a4fb526665413479516
URL:		http://ofset.sf.net/assetml
Requires:	libxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library based on an XML file format that is used to share
and reuse content like image and audio file. Application using this
library can query files on their system that provides an assetml xml
file description.

%package  devel
Summary:	Devel Library assetml to share image and audio file between project
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
AssetML Devel Library

%package  static
Summary:	AssetML Static Library
Group:		Development/Libraries
Requires:	%{name}-%{devel} = %{version}-%{release}

%description static
AssetML Static Library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/assetml-query
%attr(755,root,root) %{_prefix}/lib/libassetml.so.*
%{_infodir}/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/libassetml*
%{_pkgconfigdir}/libassetml.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*a
