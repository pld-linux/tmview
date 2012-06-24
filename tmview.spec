Summary:	A dvi viewer for SVGAlib
Name:		tmview
Version:	0103
Release:	1
URL:		ftp://sunsite.unc.edu/pub/Linux/apps/tex/dvi/
Source0:	tmv%{version}.tgz
Patch0:		%{name}-paths_libs.patch
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikov�n�
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Summary(cs):	Prohl�e� soubor� DVI pro knihovnu SVGAlib
Summary(pl):	Przegl�darka plik�w dvi dla SVGAlib
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
tmview je celo-obrazovkov� prohl�e� .dvi soubor� vyroben�ch syst�mem
TeX. M��ete si v�sledn� dokument prohl�dnout je�t� p�edt�m, ne� ho
nech�te vytisknout, nebo ho n�komu po�lete. Podporuje prohl�en� v
�erno-b�l�m provedenen� nebo v odst�nech �edi. M��ete si dokument
libovoln� zv�t�it (a zaplat�te za to jenom lehk�m sn�en�m rychlosti).
M��ete si nastavit zar�ky pro m��en� vzd�lenost� nebo m��ete
vyhled�vat v textu. M��ete si prohl�dnout n�kolik soubor�, nastavit si
z�lo�ky a nechat si je ulo�it do startovac�ho souboru. tmview
nepodporuje PXL soubory, ignoruje v�echny speci�ln� (special) p��kazy
a nepodporuje nahrazov�n� font�.

%description -l pl
Tmview jest przegl�dark� plik�w .dvi skompilowanych przez TeXa. tmview
pozwala Ci zobaczy� jak b�dzie wygl�da� wydruk z .dvi. Mo�esz wybra�
wy�wietlanie w trybie czarno-bia�ym jak i odcieniami szaro�ci. Mo�esz
wybra� wsp�czynnik powi�kszenia. Mo�esz zaznacza� punkty i mierzy�
dystans mi�dzy nimi. Mo�esz przegl�da� du�e ilo�ci plik�w .dvi,
zapisywa� zak�adki (bookmarks) w pliku. tmview nie wspiera plik�w pxl.
tmview ignoruje wszystkie 'specjalne' komendy i nie ma mechanizmu
zast�powania font�w.

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
