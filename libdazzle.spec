#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	Experimental new features for GTK+ and GLib
Summary(pl.UTF-8):	Nowe, eksperymentalne funkcje dla GTK+ i GLiba
Name:		libdazzle
Version:	3.42.0
Release:	1
License:	GPL v3+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libdazzle/3.42/%{name}-%{version}.tar.xz
# Source0-md5:	8604b1c55a1da934ec1bff72f7e30b8e
Patch0:		%{name}-doc.patch
URL:		https://gitlab.gnome.org/GNOME/libdazzle
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel >= 3.24.0
%{?with_apidocs:BuildRequires:	gtk-doc}
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	glib2-devel >= 1:2.56.0
Requires:	gtk+3 >= 3.24.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdazzle is a collection of fancy features for GLib and GTK+ that
aren't quite ready or generic enough for use inside those libraries.
This is often a proving ground for new widget prototypes. Applications
such as Builder tend to drive development of this project.

%description -l pl.UTF-8
libdazzle to zbiór fantazyjnych funkcji dla GLiba i GTK+, które
jeszcze nie są gotowe lub wystarczająco ogólne, aby znalazły się
wewnątrz tych bibliotek. Zwykle jest to miejsce do sprawdzania
prototypów nowych widgetów. Rozwój tego projektu prowadzą zwykle
aplikacje takie jak Builder.

%package devel
Summary:	Header files for libdazzle library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdazzle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.56.0
Requires:	gtk+3-devel >= 3.24.0

%description devel
Header files for libdazzle library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdazzle.

%package -n vala-libdazzle
Summary:	libdazzle API for Vala language
Summary(pl.UTF-8):	API libdazzle dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-libdazzle
libdazzle API for Vala language.

%description -n vala-libdazzle -l pl.UTF-8
API libdazzle dla języka Vala.

%package apidocs
Summary:	API documentation for libdazzle library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libdazzle
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libdazzle library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libdazzle.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	%{?with_apidocs:-Denable_gtk_doc=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING.md NEWS README.md
%attr(755,root,root) %{_bindir}/dazzle-list-counters
%attr(755,root,root) %{_libdir}/libdazzle-1.0.so.0
%{_libdir}/girepository-1.0/Dazzle-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdazzle-1.0.so
%{_includedir}/libdazzle-1.0
%{_pkgconfigdir}/libdazzle-1.0.pc
%{_datadir}/gir-1.0/Dazzle-1.0.gir

%files -n vala-libdazzle
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libdazzle-1.0.deps
%{_datadir}/vala/vapi/libdazzle-1.0.vapi

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libdazzle
%endif
