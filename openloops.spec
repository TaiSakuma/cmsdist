### RPM external openloops 1.0.1
%define tag d888f2705fbcd315d8cf5f290f73a524464698ed
%define branch cms/v%{realversion}
%define github_user cms-externals
Source: git+https://github.com/%github_user/root.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}-%{tag}.tgz

BuildRequires: python

%define keep_archives true

%prep
%setup -n %{n}-%{realversion}

%build
cat << \EOF >> openloops.cfg
[OpenLoops]
fortran_compiler = gfortran
gfortran_f90_flags = -ffixed-line-length-0 -ffree-line-length-0 -Os
loop_optimisation = -Os
generic_optimisation = -Os
born_optimisation = -Os
EOF

./scons auto=all/

%install
mkdir %i/{lib,proclib}
cp lib/*.so %i/lib
cp proclib/*.so %i/proclib
cp proclib/*.info %i/proclib
