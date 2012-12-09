# revision 23085
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-ukrainian
Version:	20120124
Release:	1
Summary:	Ukrainian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ukrainian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Requires:	texlive-ukrhyph

%description
Hyphenation patterns for Ukrainian in T2A and UTF-8 encodings.
For 8-bit engines, the 'ukrhyph' package provides a number of
different pattern sets, as well as different (8-bit) encodings,
that can be chosen at format-generation time.  The UTF-8
version only provides the default pattern set.  A mechanism
similar to the one used for 8-bit patterns may be implemented
in the future.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-ukrainian
%_texmf_language_def_d/hyphen-ukrainian
%_texmf_language_lua_d/hyphen-ukrainian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-ukrainian <<EOF
\%% from hyphen-ukrainian:
ukrainian loadhyph-uk.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-ukrainian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-ukrainian <<EOF
\%% from hyphen-ukrainian:
\addlanguage{ukrainian}{loadhyph-uk.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-ukrainian
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


%changelog
* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120124-1
+ Revision: 767633
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 759944
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718685
- texlive-hyphen-ukrainian
- texlive-hyphen-ukrainian
- texlive-hyphen-ukrainian
- texlive-hyphen-ukrainian

