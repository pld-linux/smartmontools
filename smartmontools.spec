Summary:	S.M.A.R.T. control and monitoring of ATA/SCSI harddisks
Summary(pl):	Monitorowanie i kontrola dysk�w za pomoc� S.M.A.R.T
Name:		smartmontools
Version:	5.19
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/smartmontools/%{name}-%{version}.tar.gz
# Source0-md5:	c2c7687ac928ce43338c7dae5205e18b
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
monitorowania system�w przechowywania danych za pomoc� S.M.A.R.T -
systemu wbudowanego w wi�kszo�� nowych dysk�w ATA oraz SCSI. Pakiet
pochodzi od oprogramowania smartsuite i wspiera dyski ATA/ATAPI-5.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fsigned-char -DLINUX"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/smartd

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
%{_mandir}/man5/*
%{_mandir}/man8/*
