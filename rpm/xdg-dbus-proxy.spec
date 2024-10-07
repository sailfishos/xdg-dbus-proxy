Name:           xdg-dbus-proxy
Version:        0.1.6
Release:        1
Summary:        Filtering proxy for D-Bus connections
License:        LGPLv2+
URL:            https://github.com/sailfishos/xdg-dbus-proxy
Source0:        %{name}-%{version}.tar.xz
Patch1:         0001-Add-D-Bus-interface-for-querying-client-process-deta.patch

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)

%description
xdg-dbus-proxy is a filtering proxy for D-Bus connections. It was
originally part of the flatpak project, but it has been broken out
as a standalone module to facilitate using it in other contexts.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Dman=disabled
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS
%{_bindir}/xdg-dbus-proxy
