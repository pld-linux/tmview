#
# Conditional build:
%bcond_without	svga		# without SVGAlib support
#
Summary:	DVI files viewer
Summary(pl.UTF-8):	Przeglądarka plików DVI
Name:		tmview
Version:	0103
Release:	11
License:	distributable
Group:		Applications/Publishing
Source0:	ftp://ftp.gust.org.pl/TeX/dviware/tmview/tmv%{version}.tgz
# Source0-md5:	c1d43526a3bc32a684017ffd9f8040be
Source1:	%{name}.conf
Patch0:		%{name}-rc.patch
Patch1:		%{name}-paths_libs.patch
Patch2:		%{name}-Makefile.patch
Patch3:		%{name}-resolution.patch
Patch4:		%{name}-gcc3.patch
Patch5:		%{name}-home_etc.patch
BuildRequires:	XFree86-devel
BuildRequires:	kpathsea-devel
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVI previewer for SVGAlib, framebuffer device or Xlib. Fast, offers
xdvi-like anti-aliasing, text-string searching, arbitrary-zooming,
bookmarks, some of the hypertex features, renders eps-figures by
running gs. tmview does not support pxl-files. tmview ignores all
'special'-commands and has no font-replacing mechanism.

This package contains only documentation and manuals. For software
look into dvifb, dvisvga and dvilx packages.

%description -l cs.UTF-8
tmview je celo-obrazovkový prohlížeč .dvi souborů vyrobených systémem
TeX. Můžete si výsledný dokument prohlédnout ještě předtím, než ho
necháte vytisknout, nebo ho někomu pošlete. Podporuje prohlížení v
černo-bílém provedenení nebo v odstínech šedi. Můžete si dokument
libovolně zvětšit (a zaplatíte za to jenom lehkým snížením rychlosti).
Můžete si nastavit zarážky pro měření vzdáleností nebo můžete
vyhledávat v textu. Můžete si prohlédnout několik souborů, nastavit si
záložky a nechat si je uložit do startovacího souboru. tmview
nepodporuje PXL soubory, ignoruje všechny speciální (special) příkazy
a nepodporuje nahrazování fontů.

%description -l pl.UTF-8
Przeglądarka plików DVI. Podglądane pliki mogą być wyświetlane za
pomocą SVGAlib, na framebuferze lub po prostu w X-ach. Program jest
szybki, umożliwia anty-aliasing w stylu xdvi, wyszukiwanie tekstów,
powiększanie, zakładki, niektóre z właściwości hipertekstowych oraz
wyświetlanie plików EPS (za pomocą GhostScript-a). tmview nie wspiera
plików pxl. Ignoruje wszystkie komendy 'special' i nie ma mechanizmu
zastępowania fontów.

Ten pakiet zawiera tylko dokumentację i manuale. Oprogramowanie
znajduje się w pakietach dvifb, dvisvga oraz dvilx.

%package -n dvifb
Summary:	DVI files viewer - framebuffer version
Summary(pl.UTF-8):	Przeglądarka plików DVI - wersja pod framebuffer
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description -n dvifb
DVI files viewer - framebuffer version

%description -n dvifb -l pl.UTF-8
Przeglądarka plików DVI - wersja pod framebuffer

%package -n dvisvga
Summary:	DVI files viewer - SVGAlib version
Summary(cs.UTF-8):	Prohlížeč souborů DVI pro knihovnu SVGAlib
Summary(pl.UTF-8):	Przeglądarka plików DVI - wersja dla SVGAlib
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description -n dvisvga
DVI files viewer - SVGAlib version.

%description -n dvisvga -l pl.UTF-8
Przeglądarka plików DVI - wersja dla SVGAlib.

%package -n dvix11
Summary:	DVI files viewer - X11 version
Summary(pl.UTF-8):	Przeglądarka plików DVI - wersja dla X Window System
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description -n dvix11
DVI files viewer - X11 version.

%description -n dvix11 -l pl.UTF-8
Przeglądarka plików DVI - wersja dla X Window System.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__make} -f MakeFb \
	CFLAGS="%{rpmcflags} -DHAVE_PROTOTYPES"

%{__make} -f MakeLX \
	CFLAGS="%{rpmcflags} -DHAVE_PROTOTYPES" \
	LIBS="-L/usr/X11R6/%{_lib} -lX11 -lkpathsea -lm"

%if %{with svga}
%{__make} -f MakeSVGA \
	CFLAGS="%{rpmcflags} -DHAVE_PROTOTYPES"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}

install doc/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install dvifb.linux $RPM_BUILD_ROOT%{_bindir}/dvifb
echo .so %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/dvifb.1

install dvilx.linux $RPM_BUILD_ROOT%{_bindir}/dvilx
echo .so %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/dvilx.1

%if %{with svga}
install dvisvga.linux $RPM_BUILD_ROOT%{_bindir}/dvisvga
echo .so %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/dvisvga.1
%endif

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tmviewrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/tmview.dvi doc/tm.ps README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
%{_mandir}/man1/%{name}*

%files -n dvifb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvifb
%{_mandir}/man1/dvifb*

%if %{with svga}
%files -n dvisvga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvisvga
%{_mandir}/man1/dvisvga*
%endif

%files -n dvix11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvilx
%{_mandir}/man1/dvilx*
