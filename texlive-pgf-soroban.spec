# revision 15878
# category Package
# catalog-ctan /graphics/pgf/contrib/pgf-soroban
# catalog-date 2008-08-23 00:06:02 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pgf-soroban
Version:	1.0
Release:	2
Summary:	Create images of the soroban using TikZ/PGF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-soroban
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-soroban.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-soroban.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes it possible to create pictures of the soroban
(Japanese abacus) using PGF/TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgf-soroban/pgf-soroban.sty
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/Changes
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/README
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/pgf-soroban-doc.bib
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/pgf-soroban-doc.pdf
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/pgf-soroban-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754860
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719245
- texlive-pgf-soroban
- texlive-pgf-soroban
- texlive-pgf-soroban
- texlive-pgf-soroban

