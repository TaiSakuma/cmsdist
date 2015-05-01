### RPM external atlas 3.10.2
# NB: http://www.netlib.org/atlas/atlas-comm/msg00280.html
#     http://cvs.pld-linux.org/cgi-bin/cvsweb/SPECS/atlas.spec
Source: http://sourceforge.net/projects/math-atlas/files/Stable/%{realversion}/atlas%{realversion}.tar.bz2

%prep
%setup -n ATLAS

%build
curl -L -O http://www.netlib.org/lapack/lapack-3.3.1.tgz
mkdir BUILD
cd BUILD
../configure -b 64 --prefix=%{i} --with-netlib-lapack-tarfile=../lapack-3.3.1.tgz
make build
make check
make ptcheck
make time

%install
cd BUILD
make install
