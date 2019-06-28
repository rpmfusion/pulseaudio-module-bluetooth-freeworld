Name:           pulseaudio-module-bluetooth-freeworld
Summary:        Bluetooth support for the PulseAudio sound server, supports aptX, LDAC codecs
Version:        1.1.99
Release:        2%{?dist}
License:        GPLv3
URL:            https://github.com/EHfive/pulseaudio-modules-bt/

%global pa_version   12.2
%global pa_archivename pulseaudio-%{pa_version}
%global bt_archivename pulseaudio-modules-bt-%{version}

Source0:        https://github.com/EHfive/pulseaudio-modules-bt/archive/v%{version}/%{bt_archivename}.tar.gz
Source1:        http://freedesktop.org/software/pulseaudio/releases/%{pa_archivename}.tar.xz

Provides:       pulseaudio-module-bluetooth = %{pa_version}-100
Conflicts:      pulseaudio-module-bluetooth < %{pa_version}-100

BuildRequires:  automake libtool
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pulseaudio >= %{pa_version}
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(dbus-1)

# aptX, LDAC, AAC
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  libldac-devel
BuildRequires:  pkgconfig(fdk-aac)

Requires:       pulseaudio%{_isa} >= %{pa_version}

# Optional runtime dependencies respectively for aptX, LDAC Bluetooth codecs
Recommends:     ffmpeg-libs%{_isa}
Recommends:     libldac%{_isa}
Recommends:     fdk-aac-free%{_isa}

%description
Contains Bluetooth audio (A2DP/HSP/HFP) support for the PulseAudio sound server.
Includes support for LDAC, aptX, aptX-HD and AAC codecs.

%prep
# BT source
%setup -n %{bt_archivename} -q
# PA source, unpack into 'pa' folder
%setup -D -T -a 1 -n %{bt_archivename} -q
rm -rf pa
mv %{pa_archivename} pa

%build
%cmake .
%make_build

%install
%make_install

%files
%{_libdir}/pulse-%{pa_version}/modules/libbluez*-util.so
%{_libdir}/pulse-%{pa_version}/modules/module-bluez*-device.so
%{_libdir}/pulse-%{pa_version}/modules/module-bluez*-discover.so
%{_libdir}/pulse-%{pa_version}/modules/module-bluetooth-discover.so
%{_libdir}/pulse-%{pa_version}/modules/module-bluetooth-policy.so

%changelog
* Sat Jun 29 2019 Gergely Gombos <gombosg@gmail.com> - 1.1.99-3
- Add fdk-aac-free BuildRequires

* Fri Apr 12 2019 Gergely Gombos <gombosg@gmail.com> - 1.1.99-2
- Fix sources file

* Fri Apr 12 2019 Gergely Gombos <gombosg@gmail.com> - 1.1.99-1
- 1.1.99 upgrade

* Tue Apr 2 2019 Gergely Gombos <gombosg@gmail.com> - 1.1-3
- Review comments fixup

* Mon Apr 1 2019 Gergely Gombos <gombosg@gmail.com> - 1.1-2
- Remove fdk-aac support, clean up macros

* Thu Mar 14 2019 Gergely Gombos <gombosg@gmail.com> - 1.1-1
- Switch to fdk-aac-free, rename to -freeworld

* Mon Mar 11 2019 Gergely Gombos <gombosg@gmail.com> - 1.1-2
- Clean up Requires tags, use pkgconfig where possible add _isa

* Sun Mar 10 2019 Gergely Gombos <gombosg@gmail.com> - 1.1-1
- New versioning, drop patch scheme, only build BT files

* Tue Feb 19 2019 Gergely Gombos <gombosg@gmail.com> - 12.2-1
- Add upstream patch qpaeq_python2.patch, bump % prov_ver

* Tue Feb 19 2019 Gergely Gombos <gombosg@gmail.com> - 12.2-1
- Rename to pulseaudio-module-bluetooth-nonfree, reset dist tag

* Sun Jan 27 2019 Gergely Gombos <gombosg@gmail.com> - 12.2-2
- Bump for 1.0 patch release, prepare for RPM Fusion submission

* Tue Dec 18 2018 Gergely Gombos <gombosg@gmail.com> - 12.2-1
- Version bump, only release Bluetooth module (rename)

* Mon Dec 3 2018 Gergely Gombos <gombosg@gmail.com> - 12.2-2
- pulseaudio-12.2 with extra Bluetooth codecs
