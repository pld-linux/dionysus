Summary:	GNU Dionysus - scientific constants and engineers parameters
Summary(pl.UTF-8):	GNU Dionysus - pakiet stałych naukowych i parametrów inżynierskich
Name:		dionysus
Version:	1.4.0
Release:	1
License:	GPL v3+
Group:		Applications/Science
Source0:	http://ftp.gnu.org/gnu/dionysus/%{name}-%{version}.tar.xz
# Source0-md5:	cb6fd06fcb5ea2c794a0b82d03986096
URL:		http://www.gnu.org/software/dionysus/
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dionysus is a local machine search engine for universal constants and
parameters of scientific and engineering relevance.

%description -l pl.UTF-8
Dionysus to lokalna wyszukiwarka uniwersalnych stałych i parametrów,
mających zastosowanie naukowe lub inżynierskie.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env tclsh,/usr/bin/tclsh,' src/Tcl_src/dionysus

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/dionysus
cp -p databases/*.ddb $RPM_BUILD_ROOT%{_datadir}/dionysus

%{__mv} $RPM_BUILD_ROOT%{_infodir}/dionysus{,.info}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/dionysus
%{_datadir}/dionysus
%{_infodir}/dionysus.info*
