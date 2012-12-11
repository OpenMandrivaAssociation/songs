%define name	songs
%define version	0.3
%define release %mkrel 5

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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3-5mdv2010.0
+ Revision: 433988
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-4mdv2009.0
+ Revision: 260899
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-3mdv2009.0
+ Revision: 252765
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3-1mdv2008.1
+ Revision: 135460
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import songs


* Sun Oct 09 2005 Austin Acton <austin@mandriva.org> 0.3-1mdk
- New release 0.3
- build opts

* Fri Aug 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2-2mdk
- rebuild to fix menu

* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 0.2-1mdk
- initial package
