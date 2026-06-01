Name:           gpredict
Version:        2.5.1
Release:        1%{?dist}
Summary:        Real-time satellite tracking and orbit prediction program

License:        GPL-2.0-or-later
URL:            https://github.com/csete/gpredict
Source0:        https://github.com/csete/gpredict/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  hamlib-devel

%description
Gpredict is a real-time satellite tracking and orbit prediction application.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/gpredict
%{_datadir}/gpredict/
%{_datadir}/applications/gpredict.desktop
%{_datadir}/pixmaps/gpredict/
%{_datadir}/icons/hicolor/*/apps/gpredict.png
%{_datadir}/icons/hicolor/*/apps/gpredict.svg
%{_datadir}/metainfo/dk.oz9aec.Gpredict.metainfo.xml
%{_mandir}/man1/gpredict.1*

%changelog
* Mon Jun 01 2026 Jim Howard <xsnrg@users.noreply.github.com> - 2.5.1-1
- Update to 2.5.1 with broad packaging for icons, pixmaps, locales and metainfo
