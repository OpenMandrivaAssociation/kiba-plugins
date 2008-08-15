%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1

%define svn	862
%define release %mkrel 0.%{svn}.1

Name:		kiba-plugins
Version:	0.1
Release:	%{release}
Summary:	Various plugins for Kiba-Dock
Group:		System/X11
URL:		http://www.kiba-dock.org/
Source0:	%{name}-%{svn}.tar.lzma
License:	GPLv2+
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	kiba-dock-devel = %{version}
BuildRequires:	intltool
BuildRequires:	librsvg-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libalsa-devel
BuildRequires:	libgtop2.0-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	startup-notification-devel
Requires:	kiba-dock

%description
This package contains several plugins for Kiba-Dock. It includes
various volume controls, a clock, calendar, system information tool,
and several other plugins.

%prep
%setup -q -n %{name}

%build
sh autogen.sh -V
%configure2_5x --disable-trash --disable-gmenu --disable-stack
# These use GnomeVFS so useless until ported to gvfs
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog 
%{_libdir}/kiba-dock
%{_datadir}/kiba-dock/config_schemas/*/*.xml
%{_datadir}/kiba-dock/icons/*

