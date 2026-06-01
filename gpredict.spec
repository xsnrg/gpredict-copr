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

# Ensure icon is installed in standard location
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 data/gpredict-icon.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gpredict.png || true
install -m 644 pixmaps/gpredict.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gpredict.png 2>/dev/null || true

# Update desktop file
desktop-file-edit --set-icon=gpredict %{buildroot}%{_datadir}/applications/gpredict.desktop || true

%check
# No tests

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/gpredict
%{_datadir}/gpredict/
%{_datadir}/applications/gpredict.desktop
%{_datadir}/icons/hicolor/*/apps/gpredict.png
%{_mandir}/man1/gpredict.1*

%changelog
* Mon Jun 01 2026 Jim Howard <xsnrg@users.noreply.github.com> - 2.5.1-1
- Update to 2.5.1 + robust icon handling
