# revision 15878
# category Package
# catalog-ctan /macros/generic/misc/patch.doc
# catalog-date 2008-06-02 13:47:56 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-patch
Version:	20080602
Release:	1
Summary:	Patch loaded packages, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/misc/patch.doc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patch.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The package defines macros that allow patching of existing
commands, specifying those parts of the existing macro to be
replaced, along with the replacements. Thus it provides more
sophisticated manipulation than a package like patchcmd, which
only permits modification by adding commands at the beginning
or end of an existing definition. The package is distributed in
a relative of LaTeX doc format: it will run unmodified, though
it benefits from docstrip treatment.

#-----------------------------------------------------------------------
%files
#- source
%doc %{_texmfdistdir}/source/generic/patch/patch.doc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar source %{buildroot}%{_texmfdistdir}
