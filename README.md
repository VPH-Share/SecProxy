SecProxy
========

SecProxy tar.gz, deb and pac builder scripts. 

Building deb package manual
-------

* Untar SecProxy.tar.gz into some temporary directory
* Copy extracted files, without `vphsecproxy` and `vphsecagent` into `deb/debian/input` directory 
* Enter into `deb` directory and build package (`sudo ./rules`)

In the feature we can use fakeroot to avoid `sudo`


