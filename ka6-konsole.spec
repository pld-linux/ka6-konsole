#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.12.0
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		konsole
Summary:	KDE Terminal Emulator
Name:		ka6-%{kaname}
Version:	24.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	6225279fc64e12c8f0adc02b558ea200
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6PrintSupport-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	kf6-extra-cmake-modules >= %{kf5ver}
BuildRequires:	kf6-kbookmarks-devel >= %{kf5ver}
BuildRequires:	kf6-kconfig-devel >= %{kf5ver}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kf5ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf5ver}
BuildRequires:	kf6-kcrash-devel >= %{kf5ver}
BuildRequires:	kf6-kdbusaddons-devel >= %{kf5ver}
BuildRequires:	kf6-kdoctools-devel >= %{kf5ver}
BuildRequires:	kf6-kglobalaccel-devel >= %{kf5ver}
BuildRequires:	kf6-kguiaddons-devel >= %{kf5ver}
BuildRequires:	kf6-ki18n-devel >= %{kf5ver}
BuildRequires:	kf6-kiconthemes-devel >= %{kf5ver}
BuildRequires:	kf6-kio-devel >= %{kf5ver}
BuildRequires:	kf6-knewstuff-devel >= %{kf5ver}
BuildRequires:	kf6-knotifications-devel >= %{kf5ver}
BuildRequires:	kf6-knotifyconfig-devel >= %{kf5ver}
BuildRequires:	kf6-kparts-devel >= %{kf5ver}
BuildRequires:	kf6-kpty-devel >= %{kf5ver}
BuildRequires:	kf6-kservice-devel >= %{kf5ver}
BuildRequires:	kf6-ktextwidgets-devel >= %{kf5ver}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kf5ver}
BuildRequires:	kf6-kwindowsystem-devel >= %{kf5ver}
BuildRequires:	kf6-kxmlgui-devel >= %{kf5ver}
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	Qt6Core >= %{qtver}
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6PrintSupport >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
Requires:	kf6-kbookmarks >= %{kf5ver}
Requires:	kf6-kconfig >= %{kf5ver}
Requires:	kf6-kconfigwidgets >= %{kf5ver}
Requires:	kf6-kcoreaddons >= %{kf5ver}
Requires:	kf6-kcrash >= %{kf5ver}
Requires:	kf6-kdbusaddons >= %{kf5ver}
Requires:	kf6-kglobalaccel >= %{kf5ver}
Requires:	kf6-kguiaddons >= %{kf5ver}
Requires:	kf6-ki18n >= %{kf5ver}
Requires:	kf6-kiconthemes >= %{kf5ver}
Requires:	kf6-kio >= %{kf5ver}
Requires:	kf6-knewstuff >= %{kf5ver}
Requires:	kf6-knotifications >= %{kf5ver}
Requires:	kf6-knotifyconfig >= %{kf5ver}
Requires:	kf6-kparts >= %{kf5ver}
Requires:	kf6-kpty >= %{kf5ver}
Requires:	kf6-kservice >= %{kf5ver}
Requires:	kf6-ktextwidgets >= %{kf5ver}
Requires:	kf6-kwidgetsaddons >= %{kf5ver}
Requires:	kf6-kwindowsystem >= %{kf5ver}
Requires:	kf6-kxmlgui >= %{kf5ver}
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konsole is a terminal emulator.

Features

• Tabs • Multiple profiles • Silence and Activity monitoring •
Bookmark support • Searching • Saving output

%description -l pl.UTF-8
Konsole jest emulatorem terminala.

Cechy

• Karty • Wiele profili • Monitoring ciszy i aktywności • Zakładki •
Szukanie • Zapisywanie danych wyjściowych

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,zh_CN}

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsole
%attr(755,root,root) %{_bindir}/konsoleprofile
%attr(755,root,root) %{_libdir}/kconf_update_bin/konsole_globalaccel
%attr(755,root,root) %{_libdir}/kconf_update_bin/konsole_show_menubar
%attr(755,root,root) %{_libdir}/libkonsoleapp.so.*.*
%attr(755,root,root) %{_libdir}/libkonsoleprivate.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/konsolepart.so
%dir %{_libdir}/qt6/plugins/konsoleplugins
%attr(755,root,root) %{_libdir}/qt6/plugins/konsoleplugins/konsole_quickcommandsplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konsoleplugins/konsole_sshmanagerplugin.so
%{_desktopdir}/org.kde.konsole.desktop
%{_datadir}/kconf_update/konsole.upd
%{_datadir}/kconf_update/konsole_add_hamburgermenu_to_toolbar.sh
%{_datadir}/kglobalaccel/org.kde.konsole.desktop
%{_datadir}/kio/servicemenus/konsolerun.desktop
%{_datadir}/knotifications6/konsole.notifyrc
%{_datadir}/metainfo/org.kde.konsole.appdata.xml
%{_datadir}/qlogging-categories6/konsole.categories
%{zsh_compdir}/_konsole
