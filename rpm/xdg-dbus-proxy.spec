Name:           xdg-dbus-proxy
Version:        0.1.2
Release:        1
Summary:        Filtering proxy for D-Bus connections
License:        LGPLv2.1+
URL:            https://github.com/flatpak/xdg-dbus-proxy
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)

%description
xdg-dbus-proxy is a filtering proxy for D-Bus connections. It was
originally part of the flatpak project, but it has been broken out
as a standalone module to facilitate using it in other contexts.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%autogen --disable-static --enable-man=no
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS
%{_bindir}/xdg-dbus-proxy

