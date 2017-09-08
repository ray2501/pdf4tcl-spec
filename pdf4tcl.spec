#
# spec file for package pdf4tcl
#

Name:           pdf4tcl
BuildRequires:  tcl >= 8.6
Version:        0.9.1
Release:        0
Summary:        A library for generating PDF documents from Tcl
Url:            https://sourceforge.net/projects/pdf4tcl
License:        TCL
Group:          Development/Libraries/Tcl
BuildArch:      noarch
Requires:       tcl >= 8.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://sourceforge.net/projects/pdf4tcl/files/pdf4tcl091.tar.gz

%description
Pdf4Tcl is a library for generating PDF documents from Tcl.

%prep
%setup -q -n %{name}091

%build

%install
dir=%buildroot%tcl_noarchdir/%name%version
mkdir -m755 -p $dir
chmod a-x *.tcl
cp -a *.tcl bitmaps $dir
chmod a-x licence.terms

%files
%defattr(-,root,root)
%doc pdf4tcl.html licence.terms
%tcl_noarchdir

%changelog

