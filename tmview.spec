Summary:	DVI files viewer
Summary(pl):	Przegl�darka plik�w DVI
Name:		tmview
Version:	0103
Release:	2
License:	distributable
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikov�n�
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
Source0:	ftp://ftp.gust.org.pl:/TeX/dviware/tmview/tmv%{version}.tgz
Source1:	%{name}.conf
Patch0:		%{name}-rc.patch
Patch1:		%{name}-paths_libs.patch
Patch2:		%{name}-Makefile.patch
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
running gs.

This package contains only documentation and manuals. For software
look into dvifb, dvisvga and dvilx packages.

%description -l pl
Przegl�darka plik�w DVI. Podgl�dane pliki mog� by� wy�wietlane za
pomoc� SVGAlib, na framebuferze lub po prostu w X-ach. Program jest
szybki, umo�liwia anty-aliasing w stylu xdvi, wyszukiwanie tekst�w,
powi�kszanie, zak�adki, niekt�re z w�a�ciwo�ci hipertekstowych oraz
wy�wietlanie plik�w EPS (za pomoc� GhostScript-a).

Ten pakiet zawiera tylko dokumentacj� i manuale. Oprogramowanie
znajduje si� w pakietach dvifb, dvisvga oraz dvilx.

%package -n dvifb
Summary:	DVI files viewer - framebuffer version
Summary(pl):	Przegl�darka plik�w DVI - wersja pod framebuffer
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikov�n�
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
Requires:	%{name} = %{version}

%description -n dvifb
DVI files viewer - framebuffer version

%description -n dvifb -l pl
Przegl�darka plik�w DVI - wersja pod framebuffer

%package -n dvisvga
Summary:	DVI files viewer - SVGAlib version
Summary(pl):	Przegl�darka plik�w DVI - wersja dla SVGAlib
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikov�n�
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
Requires:	%{name} = %{version}

%description -n dvisvga
DVI files viewer - SVGAlib version.

%description -n dvisvga -l pl
Przegl�darka plik�w DVI - wersja dla SVGAlib.

%package -n dvix11
Summary:	DVI files viewer - X11 version
Summary(pl):	Przegl�darka plik�w DVI - wersja dla X Window System
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikov�n�
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
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
echo .so %{name}.1.gz > $RPM_BUILD_ROOT%{_mandir}/man1/dvifb.1
%ifnarch sparc sparc64
echo .so %{name}.1.gz > $RPM_BUILD_ROOT%{_mandir}/man1/dvisvga.1
%endif
echo .so %{name}.1.gz > $RPM_BUILD_ROOT%{_mandir}/man1/dvilx.1

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
