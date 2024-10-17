Name:		texlive-selnolig
Version:	68747
Release:	1
Summary:	Selectively disable typographic ligatures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/selnolig
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/selnolig.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/selnolig.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package suppresses typographic ligatures selectively, i.e.,
based on predefined search patterns. The search patterns focus
on ligatures deemed inappropriate because they span morpheme
boundaries. For example, the word shelfful, which is mentioned
in the TeXbook as a word for which the ff ligature might be
inappropriate, is automatically typeset as shelf\/ful rather
than as shel{ff}ul. For English and German language documents,
the package provides extensive rules for the selective
suppression of so-called "common" ligatures. These comprise the
ff, fi, fl, ffi, and ffl ligatures as well as the ft and fft
ligatures. Other f-ligatures, such as fb, fh, fj and fk, are
suppressed globally, while exceptions are made for names and
words of non-English/German origin, such as Kafka and fjord.
For English language documents, the package further provides
ligature suppression macros for a number of so-called
"discretionary" or "rare" ligatures such as ct, st, and sp. The
package requires use of a recent LuaLaTeX format (for example
TeXLive2012 or 2013, or MiKTeX2.9).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig-english-hyphex.sty
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig-english-patterns.sty
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig-german-hyphex.sty
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig-german-patterns.sty
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig.lua
%{_texmfdistdir}/tex/lualatex/selnolig/selnolig.sty
%doc %{_texmfdistdir}/doc/lualatex/selnolig/README
%doc %{_texmfdistdir}/doc/lualatex/selnolig/gpp-ft.fea
%doc %{_texmfdistdir}/doc/lualatex/selnolig/selnolig-bugreport.tex
%doc %{_texmfdistdir}/doc/lualatex/selnolig/selnolig-english-test.pdf
%doc %{_texmfdistdir}/doc/lualatex/selnolig/selnolig-english-test.tex
%doc %{_texmfdistdir}/doc/lualatex/selnolig/selnolig-english-wordlist.tex
%doc %{_texmfdistdir}/doc/lualatex/selnolig/selnolig-german-test.pdf
%doc %{_texmfdistdir}/doc/lualatex/selnolig/selnolig-german-test.tex
%doc %{_texmfdistdir}/doc/lualatex/selnolig/selnolig-german-wordlist.tex
%doc %{_texmfdistdir}/doc/lualatex/selnolig/selnolig.pdf
%doc %{_texmfdistdir}/doc/lualatex/selnolig/selnolig.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
