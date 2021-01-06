%define _unpackaged_files_terminate_build 0 

Name: green-recorder
Summary: A simple yet functional desktop recorder for Linux systems. Supports both Xorg server and Wayland (GNOME).
URL: https://github.com/foss-project/green-recorder
Version: 3.2.8
Release: 1%{?dist}
Source: https://github.com/dvershinin/green-recorder/archive/%{version}.tar.gz
License: GPLv3
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: gettext
Requires: python3
Requires: python3-pydbus
Requires: ffmpeg
Requires: gawk
Requires: libappindicator-gtk3
Requires: python3-urllib3
Recommends: python3-configparser
Requires: pulseaudio
Requires: ImageMagick
Requires: xdg-utils

%description
A simple desktop recorder for Linux systems. Supports both Xorg server and Wayland (GNOME).

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%find_lang %{name}
 
%files -f %{name}.lang
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog

* Wed Jan 06 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.2.8-1
- Updated to 3.2.8

* Thu Jul 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.2.3-1
- Updated to 3.2.3

* Sun Jun 30 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.2.2-1
- Updated to 3.2.2

* Fri Feb 15 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.2.1-1
- Updated to 3.2.1

* Thu Nov 02 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.1-1
- Updated to 3.1

* Thu Aug 17 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 3.0.4-2
- Upstream
- Added url sources

* Tue Aug 8 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.4
- Fixed small issues evreywhere.
- Removed Wayland pipeline editing option.
- Reworked UI.
- Updated translation template.
- Fixed applet on MATE.

* Mon Aug 7 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.3
- Fixed small issues.

* Sun Aug 6 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.2
- Fixed #46.

* Sun Aug 6 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.1.1
- A small fix for UI warning.

* Sun Aug 6 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.1
- A small fix for UI warning.

* Sun Aug 6 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0
- GIF format support is now available!
- Added ability to choose the audio input source.
- Preferences window was added to allow setting default values. You can now also edit the default Wayland pipeline.
- Reorganized the code and made it much clearer and simpler.
- Reorganized the graphical user interface.
- Added play button to easily enable playing the recorded video.
- Fixed a bug in recording video only or audio only on Wayland.
- Created a better ffmpeg detection on Xorg.
- Introduced a better detection method for the running display server, adding possibility to support other servers in the future with no problem.
- Various fixes and edits everywhere.

* Tue Jun 6 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.2
- Added localization support.
- Added Arabic language.
- Changed window opacity to 1.00

* Thu Apr 27 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.1.5
- Fix bug #25.

* Thu Apr 27 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.1.4
- Some various fixes.

* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.1-1
- Fix Spec file (mhsabbagh@outlook.com)
- Version 2.0 (mhsabbagh@outlook.com)

* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com>
- Fix Spec file (mhsabbagh@outlook.com)
- Version 2.0 (mhsabbagh@outlook.com)

* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.0-1
- Added Wayland Support (GNOME Session).
- Added ability to select a specific window.
- Added ability to select a specific area.
- Added ability to show/hide mouse cursor.
- Added ability to follow mouse cursor.
- Added ability run a command after finishing recording.
- Indicator now checking for ffmpeg before running.
- Fixed some issues about multi-recordings.
- Update green-recorder (gort818@gmail.com)
- Update finding the video folder (gort818@gmail.com)
- Update green-recorder (gort818@gmail.com)
- Fix hidden icon from status bar in Wayland session (moceap@hotmail.com)

* Tue Feb 14 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 1.1.2-1
- new package built with tito

* Tue Feb 14 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 1.1.2
- Version 1.1.2. 

