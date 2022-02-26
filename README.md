# rpm-ltfs
The spec file for LTFS v2.5.

At this time, this spec file is for preliminary version.

# Current version

Version 2.5.0.0-1

# Prereqsite

* Packages required for building LTFS
* rpmbuild
* spectool

# How to create rpm

1. Install rpmbuild `yum install rpmbuild`
2. Install spectool `yum install rpmdevtools`
3. Create rpmbuild directory structure if it is not existed `touch ./dummy.spec; rpmbuild ./dummy.spec`
4. copy ltfs.spec to rpmbuild/SPECS
5. cd rpmbuild
6. spectool -D -g -R ./SPECS/ltfs.spec
7. cd SPECS
8. rpmbuild -bs ltfs.spec
9. rpmbuild --rebuild ../SRPMS/ltfs-2.5.0.0-1.src.rpm

# Confimed OS

* CentOS 7: ltfs.spec
* CentOS 8: ltfs.spec
