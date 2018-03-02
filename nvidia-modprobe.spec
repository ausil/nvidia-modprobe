Name:           nvidia-modprobe
Version:        390.25
Release:        2%{?dist}
Summary:        Load the NVIDIA kernel module and create NVIDIA character device files

License:        MIT and GPLv2+
URL:            https://github.com/NVIDIA/nvidia-modprobe
Source0:        %{url}/archive/%{version}/nvidia-modprobe-%{version}.tar.gz
ExclusiveArch:  x86_64 i686 armv7hl

BuildRequires:  m4


%description
Load the NVIDIA kernel module and create NVIDIA character device files.


%prep
%setup -q


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
%make_build NV_VERBOSE=1 PREFIX=%{_prefix} STRIP_CMD=true NV_KEEP_UNSTRIPPED_BINARIES=1
(cd _out/Linux_*/ ; cp nvidia-modprobe.unstripped nvidia-modprobe ; cd -)


%install
%make_install NV_VERBOSE=1 PREFIX=%{_prefix} STRIP_CMD=true NV_KEEP_UNSTRIPPED_BINARIES=1

#Fix perm
chmod -x %{buildroot}%{_mandir}/man1/nvidia-modprobe.1.*


%files
%license COPYING
%attr(4755,root,root) %{_bindir}/nvidia-modprobe
%{_mandir}/man1/nvidia-modprobe.1.*


%changelog
* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 390.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 390.25-1
- Update to 390.25

* Thu Jan 11 2018 Leigh Scott <leigh123linux@googlemail.com> - 390.12-1
- Update to 390.12

* Sat Dec 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 387.34-1
- Update to 387.34

* Mon Oct 30 2017 Leigh Scott <leigh123linux@googlemail.com> - 387.22-1
- Update to 387.22

* Tue Sep 26 2017 Leigh Scott <leigh123linux@googlemail.com> - 384.90-1
- Update to 384.90

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 384.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Nicolas Chauvet <kwizart@gmail.com> - 384.47-1
- Update to 384.47

* Wed May 17 2017 Nicolas Chauvet <kwizart@gmail.com> - 381.22-1
- Update to 381.22

* Thu Jun 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 319.32-1
- Initial version
