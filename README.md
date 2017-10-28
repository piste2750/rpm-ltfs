# rpm-ltfs
Spec files for LTFS

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
8. rpmbuild -ta ltfs.spec

# Confimed OS

* CentOS 7: ltfs.spec