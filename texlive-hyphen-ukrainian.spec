%global tl_name hyphen-ukrainian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Ukrainian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-ukrainian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ukrainian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(ukrhyph)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Ukrainian in T2A and UTF-8 encodings. For 8-bit
engines, the 'ukrhyph' package provides a number of different pattern
sets, as well as different (8-bit) encodings, that can be chosen at
format-generation time. The UTF-8 version only provides the default
pattern set. A mechanism similar to the one used for 8-bit patterns may
be implemented in the future.

