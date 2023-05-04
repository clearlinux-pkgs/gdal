#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gdal
Version  : 3.6.1
Release  : 80
URL      : https://download.osgeo.org/gdal/3.6.1/gdal-3.6.1.tar.xz
Source0  : https://download.osgeo.org/gdal/3.6.1/gdal-3.6.1.tar.xz
Summary  : Geospatial Data Abstraction Library
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC LGPL-2.0 Libpng MIT Public-Domain
BuildRequires : bison-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : gdal-dev
BuildRequires : giflib-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : hdf5-dev
BuildRequires : libgeotiff-dev
BuildRequires : libpng-dev
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : openjpeg
BuildRequires : pkg-config
BuildRequires : pkgconfig(OpenEXR)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(freexl)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libkml)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(podofo)
BuildRequires : pkgconfig(poppler)
BuildRequires : pkgconfig(rasterlite2)
BuildRequires : pkgconfig(shapelib)
BuildRequires : pkgconfig(spatialite)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : proj
BuildRequires : proj-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : swig
BuildRequires : tiff-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The following source files are taken from the HDF-EOS package
EHapi.c,
GDapi.c,
SWapi.c,
HDFEOSVersion.h,
HdfEosDef.h,
ease.h

%prep
%setup -q -n gdal-3.6.1
cd %{_builddir}/gdal-3.6.1

%build
## build_prepend content
sed -i 's/-flto"$/-flto=auto"/' ./configure.ac
# Also patch the generated configure script, in case we stop patching
# configure.ac, m4 files, etc.
sed -i 's/-flto"$/-flto=auto"/' ./configure
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672867679
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
sed -i 's/-flto"$/-flto=auto"/' ./configure.ac
# Also patch the generated configure script, in case we stop patching
# configure.ac, m4 files, etc.
sed -i 's/-flto"$/-flto=auto"/' ./configure
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1672867679
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gdal
cp %{_builddir}/gdal-%{version}/LICENSE.TXT %{buildroot}/usr/share/package-licenses/gdal/51134147a0feb5f2a47099a8b81d33f1099dfd21 || :
cp %{_builddir}/gdal-%{version}/frmts/gif/giflib/COPYING %{buildroot}/usr/share/package-licenses/gdal/f9c9a2d3495a0766b4cf20d4b90cfe714dab3dc1 || :
cp %{_builddir}/gdal-%{version}/frmts/mrf/LERCV1/LICENSE.TXT %{buildroot}/usr/share/package-licenses/gdal/3035b519169390d1aaa3a43267deaae5cdff8a9b || :
cp %{_builddir}/gdal-%{version}/frmts/pcraster/libcsf/COPYING %{buildroot}/usr/share/package-licenses/gdal/1d982db70b88f943cc7d15013c28a126339d6cbc || :
cp %{_builddir}/gdal-%{version}/frmts/png/libpng/LICENSE %{buildroot}/usr/share/package-licenses/gdal/fc3951ba26fe1914759f605696a1d23e3b41766f || :
cp %{_builddir}/gdal-%{version}/ogr/ogrsf_frmts/flatgeobuf/LICENSE %{buildroot}/usr/share/package-licenses/gdal/161732baff9a38188301a521b567a20245367c7e || :
cp %{_builddir}/gdal-%{version}/ogr/ogrsf_frmts/flatgeobuf/flatbuffers/LICENSE %{buildroot}/usr/share/package-licenses/gdal/abb8eb20f7f319cd8b292cdccce15826bac01363 || :
cp %{_builddir}/gdal-%{version}/ogr/ogrsf_frmts/geojson/libjson/COPYING %{buildroot}/usr/share/package-licenses/gdal/0cd23537e3c32497c7b87157b36f9d2eb5fca64b || :
cp %{_builddir}/gdal-%{version}/ogr/ogrsf_frmts/shape/COPYING %{buildroot}/usr/share/package-licenses/gdal/df97bdf33b01f9ed42a799dd3ed7a1599dd0cb9d || :
cp %{_builddir}/gdal-%{version}/port/LICENCE_minizip %{buildroot}/usr/share/package-licenses/gdal/f7f1d88d0aea6c567a2c351b08b0fe80f2582054 || :
cp %{_builddir}/gdal-%{version}/third_party/LercLib/LICENSE %{buildroot}/usr/share/package-licenses/gdal/3035b519169390d1aaa3a43267deaae5cdff8a9b || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/etc/bash_completion.d/gdal-bash-completion.sh
## install_append content
#install -D %{buildroot}/usr/etc/bash_completion.d/gdal-bash-completion.sh %{buildroot}/usr/share/bash-completion/completions/gdal-bash-completion.sh
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
