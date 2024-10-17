%define real_name Class-XPath

Summary:	Class-XPath module for perl 
Name:		perl-%{real_name}
Version:	1.4
Release:	8
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module adds XPath-style matching to your object trees. This means
that you can find nodes using an XPath-esque query with "match()" from
anywhere in the tree. Also, the "xpath()" method returns a unqique path
to a given node which can be used as an identifier.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/XPath.pm
%{_mandir}/*/*




%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.4-6mdv2011.0
+ Revision: 680831
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4-5mdv2011.0
+ Revision: 430335
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.4-4mdv2009.0
+ Revision: 241188
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-2mdv2008.0
+ Revision: 86182
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdk
- initial Mandriva package

