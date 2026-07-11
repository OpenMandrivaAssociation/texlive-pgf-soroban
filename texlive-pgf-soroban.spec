%global tl_name pgf-soroban
%global tl_revision 32269

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Create images of the soroban using TikZ/PGF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-soroban
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-soroban.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-soroban.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes it possible to create pictures of the soroban
(Japanese abacus) using PGF/TikZ

