Name:		texlive-pgf-soroban
Version:	32269
Release:	2
Summary:	Create images of the soroban using TikZ/PGF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-soroban
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-soroban.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-soroban.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
