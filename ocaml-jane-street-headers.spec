#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Jane Street header files
Summary(pl.UTF-8):	Pliki nagłówkowe Jane Street
Name:		ocaml-jane-street-headers
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/jane-street-headers/tags
Source0:	https://github.com/janestreet/jane-street-headers/archive/v%{version}/jane-street-headers-%{version}.tar.gz
# Source0-md5:	e9c5476e0748d0f4476ad534a51fc677
URL:		https://github.com/janestreet/jane-street-headers
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-dune >= 2.0.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
C header files shared between the various Jane Street packages.

This package contains files needed to run bytecode executables using
jane-street-headers library.

%description -l pl.UTF-8
Pliki nagłówkowe C współdzielone między różnymi pakietami Jane Street.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki jane-street-headers.

%package devel
Summary:	Jane Street header files - development part
Summary(pl.UTF-8):	Pliki nagłówkowe Jane Street - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
jane-street-headers library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki jane-street-headers.

%prep
%setup -q -n jane-street-headers-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/jane-street-headers/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/jane-street-headers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.org
%dir %{_libdir}/ocaml/jane-street-headers
%{_libdir}/ocaml/jane-street-headers/META
%{_libdir}/ocaml/jane-street-headers/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/jane-street-headers/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/jane-street-headers/*.cmi
%{_libdir}/ocaml/jane-street-headers/*.cmt
%{_libdir}/ocaml/jane-street-headers/*.h
%if %{with ocaml_opt}
%{_libdir}/ocaml/jane-street-headers/jane_street_headers.a
%{_libdir}/ocaml/jane-street-headers/*.cmx
%{_libdir}/ocaml/jane-street-headers/*.cmxa
%endif
%{_libdir}/ocaml/jane-street-headers/dune-package
%{_libdir}/ocaml/jane-street-headers/opam
