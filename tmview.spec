Summary:	DVI files viewer
Summary(pl):	Przegl�darka plik�w DVI
Name:		tmview
Version:	0103
Release:	4
License:	distributable
Group:		Applications/Publishing
Source0:	ftp://ftp.gust.org.pl:/TeX/dviware/tmview/tmv%{version}.tgz
Source1:	%{name}.conf
Patch0:		%{name}-rc.patch
Patch1:		%{name}-paths_libs.patch
Patch2:		%{name}-Makefile.patch
Patch3:		%{name}-resolution.patch
%ifnarch sparc sparc64
BuildRequires:	svgalib-devel
%endif
BuildRequires:	XFree86-devel
BuildRequires:	kpathsea-devel
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
tmview je celo-obrazovkov� prohl��e� .dvi soubor� vyroben�ch syst�mem
TeX. M��ete si v�sledn� dokument prohl�dnout je�t� p�edt�m, ne� ho
nech�te vytisknout, nebo ho n�komu po�lete. Podporuje prohl��en� v
�erno-b�l�m provedenen� nebo v odst�nech �edi. M��ete si dokument
libovoln� zv�t�it (a zaplat�te za to jenom lehk�m sn��en�m rychlosti).
M��ete si nastavit zar�ky pro m��en� vzd�lenost� nebo m��ete
vyhled�vat v textu. M��ete si prohl�dnout n�kolik soubor�, nastavit si
z�lo�ky a nechat si je ulo�it do startovac�ho souboru. tmview
nepodporuje PXL soubory, ignoruje v�echny speci�ln� (special) p��kazy
a nepodporuje nahrazov�n� font�.

%description -l pl
Przegl�darka plik�w DVI. Podgl�dane pliki mog� by� wy�wietlane za
pomoc� SVGAlib, na framebuferze lub po prostu w X-ach. Program jest
szybki, umo�liwia anty-aliasing w stylu xdvi, wyszukiwanie tekst�w,
powi�kszanie, zak�adki, niekt�re z w�a�ciwo�ci hipertekstowych oraz
wy�wietlanie plik�w EPS (za pomoc� GhostScript-a). tmview nie wspiera
plik�w pxl. Ignoruje wszystkie komendy 'special' i nie ma mechanizmu
zast�powania font�w.

Ten pakiet zawiera tylko dokumentacj� i manuale. Oprogramowanie
znajduje si� w pakietach dvifb, dvisvga oraz dvilx.

%package -n dvifb
Summary:	DVI files viewer - framebuffer version
Summary(pl):	Przegl�darka plik�w DVI - wersja pod framebuffer
Group:		Applications/Publishing
Requires:	%{name} = %{version}

%description -n dvifb
DVI files viewer - framebuffer version

%description -n dvifb -l pl
Przegl�darka plik�w DVI - wersja pod framebuffer

%package -n dvisvga
Summary:	DVI files viewer - SVGAlib version
Summary(cs):	Prohl��e� soubor� DVI pro knihovnu SVGAlib
Summary(pl):	Przegl�darka plik�w DVI - wersja dla SVGAlib
Group:		Applications/Publishing
Requires:	%{name} = %{version}

%description -n dvisvga
DVI files viewer - SVGAlib version.

%description -n dvisvga -l pl
Przegl�darka plik�w DVI - wersja dla SVGAlib.

%package -n dvix11
Summary:	DVI files viewer - X11 version
Summary(pl):	Przegl�darka plik�w DVI - wersja dla X Window System
Group:		Applications/Publishing
Requires:	%{name} = %{version}

%description -n dvix11
DVI files viewer - X11 version.

%description -n dvix11 -l pl
Przegl�darka plik�w DVI - wersja dla X Window System.

%prep
%setup  -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} -f MakeFb CFLAGS="%{rpmcflags}"
%{__make} -f MakeLX CFLAGS="%{rpmcflags}"
%ifnarch sparc sparc64
%{__make} -f MakeSVGA CFLAGS="%{rpmcflags}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
	$RPM_BUILD_ROOT%{x11bindir}

install doc/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo .so %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/dvifb.1
%ifnarch sparc sparc64
echo .so %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/dvisvga.1
%endif
echo .so %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/dvilx.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tmviewrc

install dvifb.linux $RPM_BUILD_ROOT%{_bindir}/dvifb
%ifnarch sparc sparc64
install dvisvga.linux $RPM_BUILD_ROOT%{_bindir}/dvisvga
%endif
install dvilx.linux $RPM_BUILD_ROOT%{x11bindir}/dvilx

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/tmview.dvi doc/tm.ps README*
%{_sysconfdir}/%{name}/*
%{_mandir}/man1/%{name}*

%files -n dvifb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvifb
%{_mandir}/man1/dvifb*

%ifnarch sparc sparc64
%files -n dvisvga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvisvga
%{_mandir}/man1/dvisvga*
%endif

%files -n dvix11
%defattr(644,root,root,755)
%attr(755,root,root) %{x11bindir}/dvilx
%{_mandir}/man1/dvilx*
