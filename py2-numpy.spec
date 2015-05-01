### RPM external py2-numpy 1.9.2
## INITENV +PATH PYTHONPATH %i/$PYTHON_LIB_SITE_PACKAGES
Source: http://downloads.sourceforge.net/project/numpy/NumPy/%{realversion}/numpy-%{realversion}.tar.gz

%define isdarwin %(case %{cmsos} in (osx*) echo 1 ;; (*) echo 0 ;; esac)

Requires: python
Requires: zlib
Requires: atlas
Requires: lapack
%prep
%setup -n numpy-%{realversion}

%build
%install
case %{cmsos} in 
  osx*) SONAME=dylib ;;
  *) SONAME=so ;;
esac

export LAPACK_ROOT
export LAPACK=$LAPACK_ROOT/lib/liblapack.$SONAME
export BLAS=$LAPACK_ROOT/lib/libblas.$SONAME

python setup.py build --fcompiler=gnu95
python setup.py install --prefix=%{i}
find %{i} -name '*.egg-info' -exec rm {} \;
