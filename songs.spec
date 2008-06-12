%define name	songs
%define version	0.3
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	A little tool used to record and mix audio files
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://sed.free.fr/songs/
License:	Public Domain
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig gtk2-devel

%description
Features of Songs
    * Unlimited number of tracks
    * Supports WAV files (mono/stereo, only 44.1 KHz, 16 bits)
    * Supports raw float files (mono/stereo)
    * Several effects
    * Not too much memory used
    * GTK2 interface

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=Songs
Comment=Multitrack wave editor
Categories=Audio;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc BUGS DESIGN NOISE TODO* README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

