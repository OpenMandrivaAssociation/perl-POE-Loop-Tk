%define upstream_name    POE-Loop-Tk
%define upstream_version 1.304

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    A POE/Tk bridge for ActiveState's Tk
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(POE)
BuildRequires: perl(POE::Test::Loops)
BuildRequires: perl(Tk)
BuildRequires: x11-server-xvfb

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
%{make}

%check
# makefile.pl ignores input if not inside a tty :-(
rm run_network_tests
# this test requires interactivity
rm t/poe_loop_tk/wheel_run.t
xvfb-run %make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/man3/*
%perl_vendorlib/*


