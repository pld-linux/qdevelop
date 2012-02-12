Summary:	IDE dedicated to QT4
Summary(pl.UTF-8):	IDE zaprojektowane z myślą o QT4
Name:		qdevelop
Version:	0.27.4
Release:	4
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://qdevelop.org/public/release/%{name}-%{version}.tar.gz
# Source0-md5:	0ea8b3b2ed15bfa275d5c03f40cb871b
URL:		http://qdevelop.org/
BuildRequires:	QtCore-devel
BuildRequires:	QtDesigner-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtUiTools-devel
BuildRequires:	QtXml-devel
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-build >= 4.3
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QDevelop is a development environment entirely dedicated to Qt4.

QDevelop is not a Kdevelop like or reduced. It's an independent IDE
dedicated to Qt and is totally independent of KDevelop. Less complete,
but faster, light and especially multi-platforms.

%description -l pl.UTF-8
QDevelop to środowisko programistyczne w całości poświęcone Qt4.

Qdevelop to nie jest program podobny do Kdevelop lub jego
pozbawiowioną funkcjonalności wersją. Jest to niezależne IDE
poświęcone Qt i całkowicie oddzielone od KDevelop. Mniej funkcjonalne,
ale szybsze, lżejsze i dostępne na wiele platform.

%prep
%setup -q -c

%build
%{__cmake} %{name}-%{version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -pD ./qdevelop $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%version/{ChangeLog.txt,copying,README*}
%attr(755,root,root) %{_bindir}/*
