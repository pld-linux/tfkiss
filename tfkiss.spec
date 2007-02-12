Summary:	TheFirmware TNC Software Emulator
Summary(pl.UTF-8):   Emulator TNC
Name:		tfkiss
Version:	1.2.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.wspse.de/packet_radio/misc/%{name}-%{version}.tar.gz
# Source0-md5:	80e9738f2b061d20011ea1d64f84b57a
Patch0:		%{name}-configure.patch
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TFKISS is based on TheFirmware by NORD><LINK.

%description -l pl.UTF-8
TFKISS jest emulatorem TNC.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure \
	--enable-hibaud \
	--enable-xpid \
	--enable-flexnet \
	--enable-axip
%{__make} \
	CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/ax25/tfkiss/examples,%{_docdir}/%{name}-%{version}}

install src/tfkiss $RPM_BUILD_ROOT%{_bindir}

install {examples/tfkiss.cfg,examples/tfkiss.ini} \
	$RPM_BUILD_ROOT%{_sysconfdir}/ax25/tfkiss

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/alas.{eng,txt} doc/copyrght.txt doc/tfkiss.doc doc/rfc1226
%doc CHANGES INSTALL README examples/tfkiss.cfg.smpl* examples/tfkiss.ini.smpl*
%attr(755,root,root) %{_bindir}/tfkiss
%dir %attr(700,root,root) %{_sysconfdir}/ax25/tfkiss
%attr(600,root,root) %{_sysconfdir}/ax25/tfkiss/*
