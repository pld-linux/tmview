Summary:	A dvi viewer for SVGAlib
Name:		tmview
Version:	0103
Release:	1
URL:		ftp://sunsite.unc.edu/pub/Linux/apps/tex/dvi/
Source0:	tmv%{version}.tgz
Patch0:		%{name}-paths_libs.patch
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikování
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Summary(cs):	Prohlí¾eè souborù DVI pro knihovnu SVGAlib
Summary(pl):	Przegl±darka plików dvi dla SVGAlib
Requires: svgalib >= 1.9.2
BuildRequires: kpathsea-devel

%description
tmview is a screen-previewer for .dvi-files compiled by TeX. It let's
you see what your printed output will look like. You can choose
between a black-and-white representation and greyscaling. You can
choose an arbitrary zoomfactor (at some cost of performance). You can
set marks to measure distances. You can search for textstrings. You
may visit lots of DVIfiles, set bookmarks and get them saved to a
startup-file. tmview does not support pxl-files. tmview ignores all
'special'-commands and has no font-replacing mechanism.

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
Tmview jest przegl±dark± plików .dvi skompilowanych przez TeXa. tmview
pozwala Ci zobaczyæ jak bêdzie wygl±da³ wydruk z .dvi. Mo¿esz wybraæ
wy¶wietlanie w trybie czarno-bia³ym jak i odcieniami szaro¶ci. Mo¿esz
wybraæ wspó³czynnik powiêkszenia. Mo¿esz zaznaczañ punkty i mierzyæ
dystans miêdzy nimi. Mo¿esz przegl±daæ du¿e ilo¶ci plików .dvi,
zapisywaæ zak³adki (bookmarks) w pliku. tmview nie wspiera plików pxl.
tmview ignoruje wszystkie 'specjalne' komendy i nie ma mechanizmu
zastêpowania fontów.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -f MakeSVGA OPTFLAGS="$RPM_OPT_FLAGS"
%{__make} -f MakeLX OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -s dvisvga.linux $RPM_BUILD_ROOT%{_bindir}/dvisvga
install -s dvilx.linux $RPM_BUILD_ROOT%{_bindir}/dvilx
install doc/tmview.1 $RPM_BUILD_ROOT%{_mandir}/man1
ln -s dvisvga $RPM_BUILD_ROOT%{_bindir}/tmview
ln -s tmview.1 $RPM_BUILD_ROOT%{_mandir}/man1/dvilx.1
ln -s tmview.1 $RPM_BUILD_ROOT%{_mandir}/man1/dvisvga.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES IAFA-PACKAGE README doc/tmview.dvi doc/tmview.tex

%attr(755,root,root) %{_bindir}/dvisvga
%attr(755,root,root) %{_bindir}/dvilx
%attr(755,root,root) %{_bindir}/tmview
%attr(644,root, man) %{_mandir}/man1/*
