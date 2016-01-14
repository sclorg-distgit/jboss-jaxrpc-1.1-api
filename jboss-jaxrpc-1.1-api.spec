%global pkg_name jboss-jaxrpc-1.1-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.0.1
Release:          7.10%{?dist}
Summary:          Java API for XML-Based RPC (JAX-RPC) 1.1
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-jaxrpc-api_spec.git jboss-jaxrpc-1.1-api
# cd jboss-jaxrpc-1.1-api/ && git archive --format=tar --prefix=jboss-jaxrpc-1.1-api/ jboss-jaxrpc-api_1.1_spec-1.0.1.Final | xz > jboss-jaxrpc-1.1-api-1.0.1.Final.tar.xz
Source0:          %{pkg_name}-%{namedversion}.tar.xz

BuildRequires:    %{?scl_prefix}jboss-servlet-3.0-api
BuildRequires:    %{?scl_prefix}jboss-specs-parent
BuildRequires:    %{?scl_prefix_java_common}javapackages-tools
BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix}maven-compiler-plugin
BuildRequires:    %{?scl_prefix}maven-install-plugin
BuildRequires:    %{?scl_prefix}maven-jar-plugin
BuildRequires:    %{?scl_prefix}maven-javadoc-plugin
BuildRequires:    %{?scl_prefix}maven-enforcer-plugin
BuildRequires:    %{?scl_prefix}maven-dependency-plugin

Requires:         %{?scl_prefix}jboss-servlet-3.0-api

BuildArch:        noarch

%description
The JAX-RPC 1.1 API classes.

%package javadoc
Summary:          Javadocs for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n jboss-jaxrpc-1.1-api

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
mvn-rpmbuild install javadoc:aggregate
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jaxrpc-api_1.1_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{pkg_name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{pkg_name}.pom

# DEPMAP
%add_maven_depmap

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%{?scl:EOF}

%files -f .mfiles
%doc README LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-7.10
- Mass rebuild 2015-01-13

* Wed Jan 07 2015 Michal Srb <msrb@redhat.com> - 1.0.1-7.9
- Migrate to .mfiles

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-7.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-7.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-7.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-7.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-7.4
- Remove requires on java

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.0.1-7.3
- SCL-ize BR/R

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-7.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-7.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.1-7
- Mass rebuild 2013-12-27

* Fri Dec 13 2013 Ade Lee <alee@redhat.com> 1.0.1-6
- Fix spec file dist tag for rpmlint

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-5
- Remove unneeded BR: maven-plugin-cobertura

* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.1-4
- Resolves #961461 - Remove unneeded maven-checkstyle-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.20120309gita3c227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120309gita3c227
- Packaging after license cleanup upstrea

* Mon Oct 24 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-2
- Fixed apidocs issue

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Initial packaging
