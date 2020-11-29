# % global snap       20190806
# % global gitcommit  99aa1fe3d0b90a9ad5682d8cb3092e6e10f6d5cb
# % global shortcommit % (c=% {gitcommit}; echo ${c:0:5})

%undefine __cmake_in_source_build

Name:           pulseaudio-module-bluetooth-freeworld
Summary:        Bluetooth support for the PulseAudio sound server, supports aptX, LDAC codecs
Version:        1.4
Release:        5%{?snap:.%{snap}git%{shortcommit}}%{?dist}
License:        GPLv3
URL:            https://github.com/EHfive/pulseaudio-modules-bt/

# see https://src.fedoraproject.org/rpms/pulseaudio for versions
%global pa_major   14.0
%global pa_version   14.0

%global pa_archivename pulseaudio-%{pa_version}

%if 0%{?snap}
%global bt_archivename pulseaudio-modules-bt-%{gitcommit}
%else
%global bt_archivename pulseaudio-modules-bt-%{version}
%endif

%if 0%{?snap}
Source0:        %{url}/archive/%{gitcommit}/%{bt_archivename}.tar.gz
%else
Source0:        %{url}/archive/v%{version}/%{bt_archivename}.tar.gz
%endif
Source1:        http://freedesktop.org/software/pulseaudio/releases/%{pa_archivename}.tar.xz

Provides:       pulseaudio-module-bluetooth = %{pa_version}-100
Conflicts:      pulseaudio-module-bluetooth < %{pa_version}-100

BuildRequires:  automake libtool
BuildRequires:  gcc-c++
BuildRequires:  cmake3
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
Requires:       fdk-aac-free%{_isa}

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
%cmake3
%cmake3_build

%install
%cmake3_install

%files
%{_libdir}/pulse-%{pa_major}/modules/libbluez*-util.so
%{_libdir}/pulse-%{pa_major}/modules/module-bluez*-device.so
%{_libdir}/pulse-%{pa_major}/modules/module-bluez*-discover.so
%{_libdir}/pulse-%{pa_major}/modules/module-bluetooth-discover.so
%{_libdir}/pulse-%{pa_major}/modules/module-bluetooth-policy.so

%changelog
* Sun Nov 29 2020 Gergely Gombos <gombosg@disroot.org> - 1.4-5
- pulseaudio 14.0 for F32-F33-F34

* Tue Nov 24 2020 Gergely Gombos <gombosg@disroot.org> - 1.4-4
- pulseaudio 14.0 for F34+, F31 EOL, fix F32 version

* Thu Oct 08 2020 Gergely Gombos <gombosg@disroot.org> - 1.4-3
- pulseaudio 13.99.2 for F33+, F30 EOL

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Gergely Gombos <gombosg@disroot.org> - 1.4-1
- 1.4 release

* Thu Mar 19 2020 Gergely Gombos <gombosg@disroot.org> - 1.3-4
- Bump Pulseaudio dependency version in F31 to 13.99.1

* Mon Mar 02 2020 Gergely Gombos <gombosg@disroot.org> - 1.3-3
- Bump Pulseaudio dependency version in F32

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 05 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3-1
- 1.3 release

* Wed Aug 7 2019 Gergely Gombos <gombosg@disroot.org> - 1.2-1
- 1.2 release

* Tue Aug 6 2019 Gergely Gombos <gombosg@disroot.org> - 1.1.99-7.20190806git99aa1f
- Upgrade to Pulseaudio 12.99.1 for rawhide

* Sun Jun 30 2019 Gergely Gombos <gombosg@disroot.org> - 1.1.99-6.20190630git2fde9
- Correct Source0 field

* Sun Jun 30 2019 Gergely Gombos <gombosg@disroot.org> - 1.1.99-5.20190630git2fde9
- Compile with fixes from master commit 2fde9b7 until upstream releases

* Sat Jun 29 2019 Gergely Gombos <gombosg@gmail.com> - 1.1.99-4
- Add fdk-aac-free as hard dependency (it's not dlopened)

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
