%define svn	1218
%define release 0.%{svn}.1

Name:		kiba-plugins
Version:	0.1
Release:	%{release}
Summary:	Various plugins for Kiba-Dock
Group:		System/X11
URL:		http://www.kiba-dock.org/
Source0:	%{name}-%{svn}.tar.xz
Patch0:		kiba-plugins-fix-str-fmt.patch
License:	GPLv2+
BuildRequires:	kiba-dock-devel = %{version}
BuildRequires:	intltool
BuildRequires:	librsvg-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	libalsa-devel
BuildRequires:	libgtop2.0-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	gnome-menus-devel
BuildRequires:	startup-notification-devel
buildrequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
Requires:	kiba-dock

%description
This package contains several plugins for Kiba-Dock. It includes
various volume controls, a clock, calendar, system information tool,
and several other plugins.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
sh autogen.sh -V
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog 
%{_libdir}/kiba-dock
%{_datadir}/kiba-dock/config_schemas/*/*.xml
%{_datadir}/kiba-dock/icons/*


%changelog
* Thu Feb 11 2010 Funda Wang <fwang@mandriva.org> 0.1-0.1218.1mdv2010.1
+ Revision: 504137
- New snapshot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Fri Aug 29 2008 Adam Williamson <awilliamson@mandriva.org> 0.1-0.862.2mdv2009.0
+ Revision: 277444
- enable some plugins which seem to be needed for kiba to run

* Sat Aug 16 2008 Adam Williamson <awilliamson@mandriva.org> 0.1-0.862.1mdv2009.0
+ Revision: 272488
- revert filelist change which is only relevant when building something that
  doesn't get built on bs
- akamaru still isn't enabled it seems...
- disable underlinking protection (breaks build and there's no shared lib here)
- enable akamaru build
- new snapshot 862

* Thu Mar 06 2008 Adam Williamson <awilliamson@mandriva.org> 0.1-0.722.1mdv2008.1
+ Revision: 180291
- buildrequires librsvg-devel
- import kiba-plugins


