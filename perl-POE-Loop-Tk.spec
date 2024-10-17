%define upstream_name    POE-Loop-Tk
%define upstream_version 1.305

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	A POE/Tk bridge for ActiveState's Tk
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/POE-Loop-Tk-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Test::Loops)
BuildRequires:	perl(Tk)
BuildRequires:	x11-server-xvfb

BuildArch:	noarch

%description
POE::Loop::Tk implements the interface documented in the POE::Loop manpage.
Therefore it has no documentation of its own. Please see the POE::Loop
manpage for more details.

POE::Loop::Tk is one of two versions of the Tk event loop bridge. The
other, the POE::Loop::TkActiveState manpage accommodates behavior
differences in ActiveState's build of Tk. Both versions share common code
in the POE::Loop::TkCommon manpage. POE::Loop::Tk dynamically selects the
appropriate bridge code based on the runtime enviroment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes | perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# makefile.pl ignores input if not inside a tty :-(
rm run_network_tests
# this test requires interactivity
rm t/poe_loop_tk/wheel_run.t
xvfb-run %make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.304.0-1mdv2011.0
+ Revision: 552564
- update to 1.304

* Mon Aug 31 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.302.0-1mdv2010.0
+ Revision: 422751
- import perl-POE-Loop-Tk


* Mon Aug 31 2009 cpan2dist 1.302-1mdv
- initial mdv release, generated with cpan2dist

