%define	ver	5.1
%define	sver	14
Summary:	S.M.A.R.T. control and monitoring of ATA/SCSI harddisks
Summary(pl):	Monitorowanie i kontrola dysków u¿ywaj±æ S.M.A.R.T
Name:		smartmontools
Version:	%{ver}_%{sver}
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/smartmontools/%{name}-%{ver}-%{sver}.tar.gz
# Source0-md5:	92fcc3912bf45e20da5003b7974736d3
Source1:	%{name}.init
URL:		http://smartmontools.sourceforge.net/
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	smartctl
Obsoletes:	ucsc-smartsuite
Obsoletes:	smartsuite

%description
The smartmontools package contains two utility programs (smartctl and
smartd) to control and monitor storage systems using the
Self-Monitoring, Analysis and Reporting Technology System (S.M.A.R.T.)
built into most modern ATA and SCSI hard disks. It is derived from the
smartsuite package, and includes support for ATA/ATAPI-5 disks.

%description -l pl
Pakiet zawiera dwa programy (smartctl oraz smartd) do kontroli i
monitorowania systemów przechowywania danych za pomoc± S.M.A.R.T -
systemu wbudowanego w wiêkszo¶æ nowych dysków ATA oraz SCSI. Pakiet
pochodzi od oprogramowania smartsuite i wspiera dyski ATA/ATAPI-5.

%prep
%setup -q -n %{name}-%{ver}-%{sver}

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags} -fsigned-char -DLINUX"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT/etc/rc.d/init.d

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/smartd
install smartd smartctl $RPM_BUILD_ROOT%{_sbindir}
install smartd.8 smartctl.8 $RPM_BUILD_ROOT%{_mandir}/man8

sed -e 's#^/dev/#\#/dev/#g' smartd.conf > $RPM_BUILD_ROOT%{_sysconfdir}/smartd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add smartd
if [ -f /var/lock/subsys/smartd ]; then
        /etc/rc.d/init.d/smartd restart 1>&2
else
        echo "Run \"/etc/rc.d/init.d/smartd start\" to start smartd service."
fi

%preun
if [ "$1" = "0" ]; then
        if [ -f /var/lock/subsys/smartd ]; then
                /etc/rc.d/init.d/smartd stop 1>&2
        fi
        /sbin/chkconfig --del smartd
fi

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/smartd
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/*.conf
%{_mandir}/man8/*
