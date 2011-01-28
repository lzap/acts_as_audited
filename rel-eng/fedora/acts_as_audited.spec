# Generated from acts_as_audited-1.1.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname acts_as_audited
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: ActiveRecord extension that logs all changes to your models in an audits table
Name: rubygem-%{gemname}
Version: 1.1.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/collectiveidea/acts_as_audited
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(activerecord) >= 2.1
Requires: rubygem(thoughtbot-shoulda) >= 0
Requires: rubygem(jnunemaker-matchy) >= 0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
ActiveRecord extension that logs all changes to your models in an audits table


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Jan 28 2011 Lukáš Zapletal <lzap@lzapx.brq.redhat.com> - 1.1.1-1
- Initial package
