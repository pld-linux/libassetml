Summary:	Library assetml to share and reuse content like image and audio file
Summary(pl):	Biblioteka assetml to wspó³dzielenia zasobów typu obrazki i d¼wiêki
Name:		libassetml
Version:	1.2.1
Release:	1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/ofset/%{name}-%{version}.tar.gz
# Source0-md5:	4b10fd0fb8e00a4fb526665413479516
URL:		http://ofset.sf.net/assetml/
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library based on an XML file format that is used to share
and reuse content like image and audio file. Application using this
library can query files on their system that provides an assetml xml
file description.

%description -l pl
Ta biblioteka oparta o format plików XML s³u¿y do wspó³dzielenia i
ponownego wykorzystywania zasobów typu obrazki i pliki d¼wiêkowe.
Aplikacja u¿ywaj±ca tej biblioteki mo¿e zapytaæ o obecne w systemie
pliki z do³±czonym opisem w formacie assetml xml.

%package devel
Summary:	Header files for AssetML library
Summary(pl):	Pliki nag³ówkowe biblioteki AssetML
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for AssetML library.

%description devel -l pl
Pliki nag³ówkowe biblioteki AssetML.

%package static
Summary:	Static AssetML library
Summary(pl):	Statyczna biblioteka AssetML
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AssetML library.

%description static -l pl
Statyczna biblioteka AssetML.

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
%attr(755,root,root) %{_libdir}/libassetml.so.*.*.*
%{_infodir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libassetml*
%{_pkgconfigdir}/libassetml.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
