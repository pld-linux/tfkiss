Summary:	TheFirmware TNC Software Emulator
Summary(pl):	Emulator TNC
Name:		tfkiss
Version:	1.2.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	ftp://ftp.wspse.de/packet_radio/misc/%{name}-%{version}.tar.gz
Patch0:		http://zolw.eu.org/~djrzulf/PLD/patch/%{name}-configure.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	autoconf

%description
TFKISS is based on TheFirmware by NORD><LINK.

%description -l pl
TFKISS jest emulatorem TNC.

%prep
%setup -q
%patch0 -p0

%build
autoconf
%configure2_13 \
	--enable-hibaud \
	--enable-xpid \
	--enable-flexnet \
	--enable-axip		
%{__make} CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/ax25/tfkiss/examples,%{_docdir}/%{name}-%{version}}

install src/tfkiss		$RPM_BUILD_ROOT%{_bindir}

install {examples/tfkiss.cfg,examples/tfkiss.ini} 	    $RPM_BUILD_ROOT%{_sysconfdir}/ax25/tfkiss

gzip -9nf doc/alas.eng doc/alas.txt doc/copyrght.txt doc/tfkiss.doc doc/rfc1226 \
	CHANGES INSTALL README examples/tfkiss.{cfg,ini}.smpl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/alas.eng* doc/alas.txt* doc/copyrght.txt* doc/tfkiss.doc* doc/rfc1226*
%doc CHANGES* INSTALL* README* examples/tfkiss.cfg.smpl* examples/tfkiss.ini.smpl*
%attr(755,root,root)%{_bindir}/tfkiss
%dir %attr(700,root,root) %{_sysconfdir}/ax25/tfkiss
%attr(600,root,root)%{_sysconfdir}/ax25/tfkiss/*
