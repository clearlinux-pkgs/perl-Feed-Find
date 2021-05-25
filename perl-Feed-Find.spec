#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Feed-Find
Version  : 0.07
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/B/BT/BTROTT/Feed-Find-0.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BT/BTROTT/Feed-Find-0.07.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-feed-perl/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
Summary  : 'Syndication feed auto-discovery'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Feed-Find-license = %{version}-%{release}
Requires: perl-Feed-Find-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::ErrorHandler)
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(HTML::Parser)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(LWP)
BuildRequires : perl(Module::Install)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)

%description
NAME
Feed::Find - Syndication feed auto-discovery
SYNOPSIS
use Feed::Find;
my @feeds = Feed::Find->find('http://example.com/');

%package dev
Summary: dev components for the perl-Feed-Find package.
Group: Development
Provides: perl-Feed-Find-devel = %{version}-%{release}
Requires: perl-Feed-Find = %{version}-%{release}

%description dev
dev components for the perl-Feed-Find package.


%package license
Summary: license components for the perl-Feed-Find package.
Group: Default

%description license
license components for the perl-Feed-Find package.


%package perl
Summary: perl components for the perl-Feed-Find package.
Group: Default
Requires: perl-Feed-Find = %{version}-%{release}

%description perl
perl components for the perl-Feed-Find package.


%prep
%setup -q -n Feed-Find-0.07
cd %{_builddir}
tar xf %{_sourcedir}/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
cd %{_builddir}/Feed-Find-0.07
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Feed-Find-0.07/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Feed-Find
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Feed-Find/808cdef4c992763637fe5a5a7551c6cd5186080b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Feed::Find.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Feed-Find/808cdef4c992763637fe5a5a7551c6cd5186080b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Feed/Find.pm
