Summary:	DVI files viewer
Summary(pl):	Przegl±darka plików DVI
Name:		tmview
Version:	0103
Release:	5
License:	Distributable
Group:		Applications/Publishing
Source0:	ftp://ftp.gust.org.pl:/TeX/dviware/tmview/tmv%{version}.tgz
Source1:	%{name}.conf
Patch0:		%{name}-rc.patch
Patch1:		%{name}-paths_libs.patch
Patch2:		%{name}-Makefile.patch
Patch3:		%{name}-resolution.patch
BuildRequires:	XFree86-devel
BuildRequires:	kpathsea-devel
%ifarch %{ix86} alpha
BuildRequires:	svgalib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		x11bindir	/usr/X11R6/bin

%description
DVI previewer for SVGAlib, framebuffer device or Xlib. Fast, offers
xdvi-like anti-aliasing, text-string searching, arbitrary-zooming,
bookmarks, some of the hypertex features, renders eps-figures by
running gs. tmview does not support pxl-files. tmview ignores all
'special'-commands and has no font-replacing mechanism.

This package contains only documentation and manuals. For software
look into dvifb, dvisvga and dvilx packages.

%description -l cs
tmview je celo-obrazovkový prohlí¾eè .dvi souborù vyrobených systémem
TeX. Mù¾ete si výsledný dokument prohlédnout je¹tì pøedtím, ne¾ ho
necháte vytisknout, nebo ho nìkomu po¹lete. Podporuje prohlí¾ení v
èerno-bílém provedenení nebo v odstínech ¹edi. Mù¾ete si dokument
libovolnì zvìt¹it (a zaplatíte za to jenom lehkým sní¾ením rychlosti).
Mù¾ete si nastavit zará¾ky pro mìøení vzdáleností nebo mù¾ete
vyhledávat v textu. Mù¾ete si prohlédnout nìkolik souborù, nastavit si
zálo¾ky a nechat si je ulo¾it do startovacího souboru. tmview
nepodporuje PXL soubory, ignoruje v¹echny speciální (special) pøíkazy
a nepodporuje nahrazování fontù.

%description -l pl
Przegl±darka plików DVI. Podgl±dane pliki mog± byæ wy¶wietlane za
pomoc± SVGAlib, na framebuferze lub po prostu w X-ach. Program jest
szybki, umo¿liwia anty-aliasing w stylu xdvi, wyszukiwanie tekstów,
powiêkszanie, zak³adki, niektóre z w³a¶ciwo¶ci hipertekstowych oraz
wy¶wietlanie plików EPS (za pomoc± GhostScript-a). tmview nie wspiera
plików pxl. Ignoruje wszystkie komendy 'special' i nie ma mechanizmu
zastêpowania fontów.

Ten pakiet zawiera tylko dokumentacjê i manuale. Oprogramowanie
znajduje siê w pakietach dvifb, dvisvga oraz dvilx.

%package -n dvifb
Summary:	DVI files viewer - framebuffer version
Summary(pl):	Przegl±darka plików DVI - wersja pod framebuffer
Group:		Applications/Publishing
Requires:	%{name} = %{version}

%description -n dvifb
DVI files viewer - framebuffer version

%description -n dvifb -l pl
Przegl±darka plików DVI - wersja pod framebuffer

%package -n dvisvga
Summary:	DVI files viewer - SVGAlib version
Summary(cs):	Prohlí¾eè souborù DVI pro knihovnu SVGAlib
Summary(pl):	Przegl±darka plików DVI - wersja dla SVGAlib
Group:		Applications/Publishing
Requires:	%{name} = %{version}

%description -n dvisvga
DVI files viewer - SVGAlib version.

%description -n dvisvga -l pl
Przegl±darka plików DVI - wersja dla SVGAlib.

%package -n dvix11
Summary:	DVI files viewer - X11 version
Summary(pl):	Przegl±darka plików DVI - wersja dla X Window System
Group:		Applications/Publishing
Requires:	%{name} = %{version}

%description -n dvix11
DVI files viewer - X11 version.

%description -n dvix11 -l pl
Przegl±darka plików DVI - wersja dla X Window System.

%prep
%setup  -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} -f MakeFb CFLAGS="%{rpmcflags}"
%{__make} -f MakeLX CFLAGS="%{rpmcflags}"
%ifarch %{ix86} alpha
%{__make} -f MakeSVGA CFLAGS="%{rpmcflags}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
	$RPM_BUILD_ROOT%{x11bindir}

install doc/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install dvifb.linux $RPM_BUILD_ROOT%{_bindir}/dvifb
echo .so %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/dvifb.1

install dvilx.linux $RPM_BUILD_ROOT%{x11bindir}/dvilx
echo .so %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/dvilx.1

%ifarch %{ix86} alpha
install dvisvga.linux $RPM_BUILD_ROOT%{_bindir}/dvisvga
echo .so %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/dvisvga.1
%endif

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tmviewrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/tmview.dvi doc/tm.ps README
%{_sysconfdir}/%{name}/*
%{_mandir}/man1/%{name}*

%files -n dvifb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvifb
%{_mandir}/man1/dvifb*

%ifarch %{ix86} alpha
%files -n dvisvga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvisvga
%{_mandir}/man1/dvisvga*
%endif

%files -n dvix11
%defattr(644,root,root,755)
%attr(755,root,root) %{x11bindir}/dvilx
%{_mandir}/man1/dvilx*
