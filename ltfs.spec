Summary: Linear Tape File System (On GitHub)
Name: ltfs
Version: 2.4.6.0
Release: 10507
License: BSD
Group: Util
Packager: User piste2750 on GitHub

URL:     https://github.com/LinearTapeFileSystem/ltfs
Source0: https://github.com/LinearTapeFileSystem/ltfs/archive/v2.4.6.0-10507/ltfs-2.4.6.0.tar.gz

BuildRequires: automake autoconf libtool make
BuildRequires: icu libicu-devel libxml2-devel libuuid-devel fuse-devel
BuildRequires: net-snmp-devel

Requires: /sbin/ldconfig, /usr/bin/awk, /usr/bin/systemctl
Requires:  libicu libxml2 libuuid fuse
Requires:  net-snmp

Patch: ltfs-ordered_copy-explicit-python3.patch

%if %{defined suse_version}
%debug_package
%endif

%description
Reference implementation of the LTFS format Spec.

%prep
%autosetup -n ltfs-%{version}-%{release} -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

# Prepare symbolic link (backends)
%if "%{_lib}" == "lib64"
    mkdir -p $RPM_BUILD_ROOT%{_exec_prefix}/lib
    ln -s -f %{_libdir}/ltfs $RPM_BUILD_ROOT%{_exec_prefix}/lib/ltfs
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/*
%{_sysconfdir}/*
%if "%{_lib}" == "lib64"
    %{_exec_prefix}/lib/ltfs
%endif
