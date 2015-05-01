### RPM external atlas 3.10.2
# NB: http://www.netlib.org/atlas/atlas-comm/msg00280.html
#     http://cvs.pld-linux.org/cgi-bin/cvsweb/SPECS/atlas.spec
Source: http://sourceforge.net/projects/math-atlas/files/Stable/%v/atlas%v.tar.bz2
Requires: lapack

%prep
%setup -n ATLAS

%build
pwd
make build

%install
