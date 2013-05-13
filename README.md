SecProxy
========

SecProxy tar.gz, deb, pac and rpm builder scripts. 

Building deb package manual
-------

* Untar `SecProxy.tar.gz` into some temporary directory
* Copy extracted files, without `vphsecproxy` and `vphsecagent` into `deb/debian/input` directory 
* Enter into `deb` directory and build package (`sudo ./rules`)

In the feature we can use fakeroot to avoid `sudo`


Building pacman package manual
-------

* Ensure the base-devel group is installed. Packages belonging to this group are not required to be listed as dependencies in PKGBUILD files. (pacman -S base-devel
)
* Copy `SecProxy.tar.gz` into `pac/$pkgname-$pkgver.tar.gz`
* Generate md5 sum and update `PKGBUILD` file (`makepkg -g >> PKGBUILD`)
* Generate pacman package (`makepkg`, use `makepkg -s` to install required dependencies) 

Building RPM package manual (for RHEL/CentOS 6)
-------

NOTE: Run all commands as normal user - NOT root !!!

* Prapare build environment:
	$ mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
	$ echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
* Copy 'SecProxy.tar.gz' into rpmbuild/SOURCES
* Prepare 'SecProxy-rc.tar.gz' by running in SecProxy/rpm command:
	$ tar -czvf SecProxy-rc.tar.gz rc
* Copy this 'SecProxy-rc.tar.gz' into rpmbuild/SOURCES
* Copy 'secproxy.spec' from this repo into rpmbuild/SPECS/
* Build package using: 
	$ rpmbuild -ba ~/rpmbuild/SPECS/secproxy.spec
