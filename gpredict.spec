Name:           gpredict
Version:        2.5.1
Release:        1%{?dist}
Summary:        Real-time satellite tracking and orbit prediction program

License:        GPL-2.0-only
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
BuildRequires:  glib2-devel
BuildRequires:  shared-mime-info

%description
Gpredict is a real-time satellite tracking and orbit prediction application.

Requires:       gtk3 hamlib libcurl

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# Install icon to hicolor theme for desktop integration
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pixmaps/logos/gpredict_icon_color.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gpredict.png

%post
/sbin/ldconfig
if [ -x /usr/bin/update-desktop-database ] && [ -x /usr/bin/gtk-update-icon-cache ]; then
    /usr/bin/update-desktop-database -q 2>/dev/null || :
    /usr/bin/gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :
fi

%postun
/sbin/ldconfig
if [ -x /usr/bin/update-desktop-database ] && [ -x /usr/bin/gtk-update-icon-cache ]; then
    /usr/bin/update-desktop-database -q 2>/dev/null || :
    /usr/bin/gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :
fi

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/gpredict
%{_datadir}/gpredict/
%{_datadir}/applications/gpredict.desktop
%{_datadir}/pixmaps/gpredict/
%{_datadir}/icons/hicolor/*/apps/gpredict.png
%{_datadir}/metainfo/dk.oz9aec.Gpredict.metainfo.xml
%{_datadir}/locale/*/LC_MESSAGES/gpredict.mo
%{_mandir}/man1/gpredict.1*

%changelog
* Mon Jun 01 2026 Jim Howard <xsnrg@users.noreply.github.com> - 2.5.1-1
- Update to 2.5.1 + include locale files
