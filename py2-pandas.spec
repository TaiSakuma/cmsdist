### RPM external py2-pandas 0.16.0
## INITENV +PATH PYTHONPATH %i/$PYTHON_LIB_SITE_PACKAGES
Source: https://pypi.python.org/packages/source/p/pandas/pandas-%{realversion}.tar.gz
Requires: python
Requires: atlas
Requires: py2-numpy
Requires: py2-python-dateutil
Requires: py2-pytz
%prep
%setup -n pandas-%{realversion}

%build
%install
export ATLAS=$ATLAS_ROOT/lib/libtatlas.$SONAME
export BLAS=$ATLAS_ROOT/lib/libtatlas.$SONAME
export LAPACK=$ATLAS_ROOT/lib/libtatlas.$SONAME

mkdir -p %{i}/$PYTHON_LIB_SITE_PACKAGES
export PYTHONPATH=%{i}/$PYTHON_LIB_SITE_PACKAGES:${PYTHONPATH}
python setup.py build
python setup.py install --prefix=%{i}
rm -rf numpy-1.9.2-py2.7-linux-x86_64.egg
find %{i} -name '*.egg-info' -exec rm {} \;
