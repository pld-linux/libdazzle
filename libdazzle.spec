Summary:	Experimental new features for GTK+ and GLib
Name:		libdazzle
Version:	3.30.2
Release:	1
License:	GPL v3
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libdazzle/3.30/%{name}-%{version}.tar.xz
# Source0-md5:	24e2e1b914a34f5b8868a9507d1f3c4c
BuildRequires:	glib2-devel >= 2.56.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	meson >= 0.40.1
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.727
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	glib2-devel >= 2.56.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdazzle is a collection of fancy features for GLib and Gtk+ that
aren't quite ready or generic enough for use inside those libraries.
This is often a proving ground for new widget prototypes. Applications
such as Builder tend to drive development of this project.

%package devel
Summary:	Header files for libdazzle library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdazzle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.56.0

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-libdazzle
libdazzle API for Vala language.

%description -n vala-libdazzle -l pl.UTF-8
API libdazzle dla języka Vala.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
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
