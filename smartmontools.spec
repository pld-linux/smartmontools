Summary:	S.M.A.R.T. control and monitoring of ATA/SCSI harddisks
Summary(cs):	smartmontools - pro monitorování S.M.A.R.T. diskù a zaøízení
Summary(de):	smartmontools - zur Überwachung von S.M.A.R.T.-Platten und-Geräten
Summary(es):	smartmontools - para el seguimiento de discos y dispositivos S.M.A.R.T.
Summary(fr):	smartmontools - pour le suivi des disques et instruments S.M.A.R.T.
Summary(it):	smartmontools - per monitare dischi e dispositivi S.M.A.R.T.
Summary(pl):	Monitorowanie i kontrola dysków za pomoc± S.M.A.R.T
Summary(pt):	smartmontools - para monitorar discos e dispositivos S.M.A.R.T.
Name:		smartmontools
Version:	5.31
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/smartmontools/%{name}-%{version}.tar.gz
# Source0-md5:	820acc2f0d030adc04cae2dfac28ea85
Source1:	%{name}.init
URL:		http://smartmontools.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	smartctl
Obsoletes:	ucsc-smartsuite
Obsoletes:	smartsuite

%description
The smartmontools package contains tools to control and monitor
storage systems using the Self-Monitoring, Analysis and Reporting
Technology System (S.M.A.R.T.) built into most modern ATA and SCSI
hard disks. This is used to check the reliability of the hard drive
and to predict drive failures. The suite is derived from the
smartsuite package, and contains two utilities. The first, smartctl,
is a command line utility designed to perform simple S.M.A.R.T. tasks.
The second, smartd, is a daemon that periodically monitors S.M.A.R.T.
status and reports errors to syslog. Currently this package includes
support for ATA/ATAPI-5 disks. It's intended to incorporate as much
"vendor specific" and "reserved" information as possible about disk
drives. 

%description -l cs
smartmontools øídí a monitorují zaøízení pro ukládání dat za pou¾ití
technologie automatického monitorování, analýzy a hlá¹ení
(Self-Monitoring, Analysis and Reporting Technology System -
S.M.A.R.T.) vestavìného do pevných diskù ATA a SCSI. Pou¾ívá se ke
kontrole pou¾itelnosti pevného disku a pøedvídání havárií diskù.
Nástroje jsou odvozeny od balíèku smartsuite a obsahují dva programy.
První, smartctl, je nástroj pro provádìní jednoduchých S.M.A.R.T. úloh
na pøíkazové øádce. Druhý, smartd, je démon, který periodicky
monitoruje stav a hlásí chyby do systémového protokolu. Balíèek je
kompatibilní se specifikací ATA/ATAPI-5. Balíèek je navr¾en tak, aby
pokryl co nejvíce polo¾ek s informacemi "závislé na výrobci" a
"rezervováno".

%description -l de
Die smartmontools steuern und überwachen Speichergeräte mittels des
S.M.A.R.T.-Systems (Self-Monitoring, Analysis and Reporting
Technology, Technologie zur Selbst-Überwachung, Analyse und
Berichterstellung), das in ATA- und SCSI-Festplatten eingesetzt wird.
Sie werden benutzt, um die Zuverlässigkeit der Festplatte zu prüfen
und Plattenfehler vorherzusagen. Die Suite wurde vom smartsuite-Paket
abgeleitet und enthält zwei Dienstprogramme. Das erste, smartctl, ist
ein Kommandozeilentool, das einfache S.M.A.R.T. Aufgaben ausführt. Das
zweite, smartd, ist ein Daemon, der periodisch den S.M.A.R.T.-Status
überwacht und Fehler ins Syslog protokolliert. Das Paket ist zur
ATA/ATAPI-5 Spezifikation kompatibel. Das Paket versucht, so viele
"herstellerspezifische" und "reservierte" Information über
Plattenlaufwerke wie möglich bereitzustellen.

%description -l es
smartmontools controla y hace el seguimiento de dispositivos de
almacenamiento usando el Self-Monitoring, Analysis and Reporting
Technology System (S.M.A.R.T.) incorporado en discos duros ATA y SCSI.
Es usado para asegurar la fiabilidad de discos duros y predecir
averias. El conjunto de programas proviene del conjunto smartsuite y
contiene dos utilidades. La primera, smartctl, es una utilidad
command-line hecha para hacer operaciones S.M.A.R.T. sencillas. La
segunda, smartd, es un programa que periodicamente chequea el estatus
smart e informa de errores a syslog. Estos programas son compatibles
con el sistema ATA/ATAPI-5. Este conjunto de programas tiene el
proposito de incorporar la mayor cantidad posible de informacion
reservada y especifica de discos duros.

%description -l fr
smartmontools contrôle et fait le suivi de périphériques de stockage
utilisant le système Self-Monitoring, Analysis and Reporting
Technology (S.M.A.R.T) intégré dans les disques durs ATA et SCSI. Ce
système est utilisé pour vérifier la fiabilité du disque dur et
prédire les défaillances du lecteur. La suite logicielle dérive du
paquet smartsuite et contient deux utilitaires. Le premier, smartctl,
fonctionne en ligne de commande et permet de réaliser des tâches
S.M.A.R.T. simples. Le second, smartd, est un démon qui fait
périodiquement le suivi du statut smart et transmet les erreurs au
syslog. Ce paquet est compatible avec la spécification ATA/ATAPI-5.
Ce paquet tente d'incorporer le plus d'informations possible sur les
disques durs qu'elles soient spécifiques au constructeur ("vendor
specific") ou réservées ("reserved").

%description -l it
smartmontools controlla e monitora dischi che usano il
"Self-Monitoring, Analysis and Reporting Technology System"
(S.M.A.R.T.), in hard drive ATA e SCSI. Esso è usato per controllare
l'affidabilità dei drive e predire i guasti. La suite è derivata dal
package smartsuite e contiene due utility. La prima, smartctl, è una
utility a linea di comando progettata per eseguire semplici task
S.M.A.R.T.. La seconda, smartd, è un daemon che periodicamente
monitora lo stato di smart e riporta errori al syslog. Il package è
compatibile con le specifiche ATA/ATAPI-5. Il package vuole
incorporare tutte le possibili informazioni riservate e "vendor
specific" sui dischi.

%description -l pl
Pakiet smartmontools zawiera narzêdzia do sterowania i monitorowania
systemami przechowywania danych za pomoc± S.M.A.R.T (Self-Monitoring,
Analysis and Reporting Technology) - systemu wbudowanego w wiêkszo¶æ
nowych dysków ATA oraz SCSI. Ma to na celu sprawdzanie wiarygodno¶ci
twardego dysku i przewidywanie jego awarii. Pakiet pochodzi od
oprogramowania smartsuite i zawiera dwa narzêdzia. Pierwsze, smartctl,
to program dzia³aj±cy z linii poleceñ stworzony do wykonywania
prostych zadañ S.M.A.R.T.. Drugie, smartd, to demon okresowo
monitoruj±cy stan S.M.A.R.T. i raportuj±cy b³êdy poprzez sysloga.
Aktualnie pakiet wspiera dyski ATA/ATAPI-5. Pakiet ma na celu
w³±czenie obs³ugi jak najwiêkszej ilo¶ci informacji specyficznych dla
producenta oraz "zarezerwowanych".

%description -l pt
smartmontools controla e monitora dispositivos de armazenamento
utilizando o recurso Self-Monitoring, Analysis and Reporting
Technology System (S.M.A.R.T.) integrado nos discos rígidos ATA e
SCSI, cuja finalidade é verificar a confiabilidade do disco rígido e
prever falhas da unidade. A suite é derivada do pacote smartsuite, e
contém dois utilitários. O primeiro, smartctl, é um utilitário de
linha de comando projetado para executar tarefas simples de S.M.A.R.T.
O segundo, smartd, é um daemon que monitora periodicamente estados do
smart e reporta erros para o syslog. O pacote é compatível com a
especificação ATA/ATAPI-5. O pacote pretende incorporar o maior número
possível de informações "específicas do fabricante" e "reservadas"
sobre unidades de disco.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

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
