# revision 15878
# category Package
# catalog-ctan /graphics/pgf/contrib/pgf-soroban
# catalog-date 2008-08-23 00:06:02 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pgf-soroban
Version:	1.0
Release:	1
Summary:	Create images of the soroban using TikZ/PGF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-soroban
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-soroban.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-soroban.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package makes it possible to create pictures of the soroban
(Japanese abacus) using PGF/TikZ.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgf-soroban/pgf-soroban.sty
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/Changes
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/README
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/pgf-soroban-doc.bib
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/pgf-soroban-doc.pdf
%doc %{_texmfdistdir}/doc/latex/pgf-soroban/pgf-soroban-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
