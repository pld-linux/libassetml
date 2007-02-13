# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library assetml to share and reuse content like image and audio file
Summary(pl.UTF-8):	Biblioteka assetml to współdzielenia zasobów typu obrazki i dźwięki
Name:		libassetml
Version:	1.2.1
Release:	2
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/ofset/%{name}-%{version}.tar.gz
# Source0-md5:	4b10fd0fb8e00a4fb526665413479516
Patch0:		%{name}-info.patch
URL:		http://ofset.sf.net/assetml/
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	tetex
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library based on an XML file format that is used to share
and reuse content like image and audio file. Application using this
library can query files on their system that provides an assetml xml
file description.

%description -l pl.UTF-8
Ta biblioteka oparta o format plików XML służy do współdzielenia i
ponownego wykorzystywania zasobów typu obrazki i pliki dźwiękowe.
Aplikacja używająca tej biblioteki może zapytać o obecne w systemie
pliki z dołączonym opisem w formacie assetml xml.

%package devel
Summary:	Header files for AssetML library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AssetML
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0.0
Requires:	libxml2-devel

%description devel
Header files for AssetML library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AssetML.

%package static
Summary:	Static AssetML library
Summary(pl.UTF-8):	Statyczna biblioteka AssetML
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AssetML library.

%description static -l pl.UTF-8
Statyczna biblioteka AssetML.

%prep
%setup -q
%patch0 -p1

%build
cp /usr/share/automake/config.sub .
%configure \
	--enable-static \
	%{!?with_static_libs:--disable-static}
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

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/assetml-query
%attr(755,root,root) %{_libdir}/libassetml.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libassetml*
%{_pkgconfigdir}/libassetml.pc
%{_infodir}/*.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
