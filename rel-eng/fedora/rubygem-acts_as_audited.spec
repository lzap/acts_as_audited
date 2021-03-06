%{!?ruby_sitelib: %global ruby_sitelib %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"] ')}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"] ')}
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname acts_as_audited
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: ActiveRecord extension that logs all changes to your models in an audits table
Name: rubygem-%{gemname}
Version: 1.1.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/collectiveidea/acts_as_audited
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem

# This spec needs RHEL5 compatibility
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

Requires: ruby(abi) = 1.8
Requires: rubygems
Requires: rubygem(activerecord) >= 2.1

BuildRequires: rubygem(shoulda) >= 2.11.3
BuildRequires: rubygem(jnunemaker-matchy) >= 0.4.0
BuildRequires: rubygems

Provides: rubygem(%{gemname}) = %{version}


%description
ActiveRecord extension that logs all changes to your models in an audits table


# This spec needs RHEL5 compatibility
%clean
rm -rf %{buildroot}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

# there are some .gitignore files being distributed
find %{buildroot}/ -name .gitignore -print0 | xargs -0 /bin/rm -f


%files
%defattr(-, root, root, -)
%{geminstdir}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Jan 28 2011 Lukas Zapletal <lzap+rpm@redhat.com> - 1.1.1-1
- Initial package
