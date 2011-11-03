# revision 23085
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-ukrainian
Version:	20111103
Release:	1
Summary:	Ukrainian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ukrainian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Requires:	texlive-ukrhyph
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-hyphen-base

%description
Hyphenation patterns for Ukrainian in T2A and UTF-8 encodings.
For 8-bit engines, the 'ukrhyph' package provides a number of
different pattern sets, as well as different (8-bit) encodings,
that can be chosen at format-generation time.  The UTF-8
version only provides the default pattern set.  A mechanism
similar to the one used for 8-bit patterns may be implemented
in the future.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre

%post
    %_texmf_language_dat_post
    %_texmf_language_def_post
    %_texmf_language_lua_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_post
	%_texmf_language_def_post
	%_texmf_language_lua_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-ukrainian
%_texmf_language_def_d/hyphen-ukrainian
%_texmf_language_lua_d/hyphen-ukrainian
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-ukrainian <<EOF
%% from hyphen-ukrainian:
ukrainian loadhyph-uk.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-ukrainian <<EOF
%% from hyphen-ukrainian:
\addlanguage{ukrainian}{loadhyph-uk.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-ukrainian <<EOF
-- from hyphen-ukrainian:
	['ukrainian'] = {
		loader = 'loadhyph-uk.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-uk.pat.txt',
		hyphenation = '',
	},
EOF
