Name:		vph-secproxy
Version:	1.0
Release:	1%{?dist}
Summary:	Security Proxy for VPH Share applications

Group:		Applications/Internet
License:	GPL
URL:		http://vphshare.org
# Main sources
Source0:	SecProxy.tar.gz 
# ...just rc.d scripts
Source1:	SecProxy-rc.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	java, iptables

%description
Security Proxy for VPH Share applications allowing secure access to the Atomic Service Instances.

%prep
%setup -q -n SecProxy 
%setup -q -T -D -n SecProxy -a 1

%build
# Nothing to do ... tar.gz contains binary java packages

%install
rm -rf %{buildroot}

# Nonstandard procedure...
mkdir -p %{buildroot}%{_sysconfdir}/vph-secproxy/templates # etc
mkdir -p %{buildroot}%{_datadir}/vph-secproxy # usr/share
mkdir -p %{buildroot}%{_initrddir} # etc/rc.d/init.d
mkdir -p %{buildroot}%{_localstatedir}/log/vph-secproxy # var
mkdir -p %{buildroot}%{_localstatedir}/run/vph-secproxy

cp rc/* %{buildroot}%{_initrddir}
cp *.properties %{buildroot}%{_sysconfdir}/vph-secproxy
cp *.jks %{buildroot}%{_datadir}/vph-secproxy
cp *.pem %{buildroot}%{_sysconfdir}/vph-secproxy
cp templates/* %{buildroot}%{_sysconfdir}/vph-secproxy/templates
cp lib/* %{buildroot}%{_datadir}/vph-secproxy

%clean
rm -rf %{buildroot}

%pre
useradd -M -U -d /tmp/ -s /bin/bash secproxy

%post
/sbin/chkconfig --add vphsecproxy
/sbin/chkconfig vphsecproxy on
/sbin/service vphsecproxy start
/sbin/chkconfig --add vphsecagent
/sbin/chkconfig vphsecagent on
/sbin/service vphsecagent start

%preun
/sbin/service vphsecproxy stop
/sbin/chkconfig --del vphsecproxy
/sbin/service vphsecagent stop
/sbin/chkconfig --del vphsecagent

%postun
userdel secproxy

%files
%defattr(-,root,root,-)
%dir %attr(-,secproxy,secproxy) %{_localstatedir}/log/vph-secproxy
%dir %attr(-,secproxy,secproxy) %{_localstatedir}/run/vph-secproxy
%config %{_sysconfdir}/vph-secproxy/*
%config %attr(755,-,-) %{_initrddir}/*
%{_datadir}/vph-secproxy/*


%changelog

