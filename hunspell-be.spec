Name: hunspell-be
Summary: Belarusian hunspell dictionaries
Version: 1.1
Release: 7%{?dist}
Source: http://extensions.services.openoffice.org/files/2412/1/dict-be-official.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/project/dict-be-official
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+ and LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Belarusian hunspell dictionaries.

%package -n hyphen-be
Requires: hyphen
Summary: Belarusian hyphenation rules
Group: Applications/Text

%description -n hyphen-be
Belarusian hyphenation rules.

%prep
%setup -q -c -n hunspell-be

%build
sed -i -e "s/microsoft-cp1251/CP1251/g" be-official.aff hyph_be_BY.dic
tail -n +3 hyph_be_BY.dic| head -n 3 > README_hyph_be_BY

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p be-official.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/be_BY.aff
cp -p be-official.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/be_BY.dic
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_be_BY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_be_BY.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/myspell/*

%files -n hyphen-be
%defattr(-,root,root,-)
%doc README_hyph_be_BY
%{_datadir}/hyphen/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1-7
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 23 2010 Caolán McNamara <caolanm@redhat.com> - 1.1-2
- add README_hyph_be_BY to subpackage

* Wed Sep 23 2009 Caolán McNamara <caolanm@redhat.com> - 1.1-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.0.0-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 28 2008 Caolán McNamara <caolanm@redhat.com> - 0.1-1
- initial version
