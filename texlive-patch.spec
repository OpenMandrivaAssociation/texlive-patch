%global tl_name patch
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Patch loaded packages, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/misc/patch.doc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/patch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/patch.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines macros that allow patching of existing commands,
specifying those parts of the existing macro to be replaced, along with
the replacements. Thus it provides more sophisticated manipulation than
a package like patchcmd, which only permits modification by adding
commands at the beginning or end of an existing definition. The package
is distributed in a relative of LaTeX doc format: it will run
unmodified, though it benefits from docstrip treatment.

