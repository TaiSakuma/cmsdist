### RPM external py2-numpy 1.9.2
## INITENV +PATH PYTHONPATH %i/$PYTHON_LIB_SITE_PACKAGES
Source: http://downloads.sourceforge.net/project/numpy/NumPy/%{realversion}/numpy-%{realversion}.tar.gz
Requires: python
Requires: zlib
Requires: atlas
%prep
%setup -n numpy-%{realversion}

%build
%install
case %{cmsos} in 
  osx*) SONAME=dylib ;;
  *) SONAME=so ;;
esac

export ATLAS=$ATLAS_ROOT/lib/libatlas.$SONAME
export BLAS=$ATLAS_ROOT/lib/libptf77blas.$SONAME
export LAPACK=$ATLAS_ROOT/lib/libptlapack.$SONAME

python setup.py build --fcompiler=gnu95
python setup.py install --prefix=%{i}
find %{i} -name '*.egg-info' -exec rm {} \;
