#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 2e8dc37
#
# Source0 file verified with key 0x33EBBFC47B3DD87D (even.rouault@spatialys.com)
#
Name     : gdal
Version  : 3.10.2
Release  : 136
URL      : https://download.osgeo.org/gdal/CURRENT/gdal-3.10.2.tar.gz
Source0  : https://download.osgeo.org/gdal/CURRENT/gdal-3.10.2.tar.gz
Source1  : https://download.osgeo.org/gdal/CURRENT/gdal-3.10.2.tar.gz.sig
Source2  : 33EBBFC47B3DD87D.pkey
Summary  : Geospatial Data Abstraction Library
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT Public-Domain libpng-2.0
Requires: gdal-bin = %{version}-%{release}
Requires: gdal-data = %{version}-%{release}
Requires: gdal-lib = %{version}-%{release}
Requires: gdal-license = %{version}-%{release}
Requires: gdal-man = %{version}-%{release}
Requires: gdal-python = %{version}-%{release}
Requires: gdal-python3 = %{version}-%{release}
BuildRequires : bison-dev
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : giflib-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : gnupg
BuildRequires : hdf5-dev
BuildRequires : libgeotiff-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : openjpeg
BuildRequires : pcre-dev
BuildRequires : pcre2-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(OpenEXR)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(geos)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(poppler)
BuildRequires : pkgconfig(shapelib)
BuildRequires : pkgconfig(spatialite)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : poppler-dev
BuildRequires : proj
BuildRequires : proj-dev
BuildRequires : pypi-numpy
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : swig
BuildRequires : tiff-dev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Building on Unix with gcc and autotools
If checking out from CVS:
sh autogen.sh
Then configure, make, make install

%package bin
Summary: bin components for the gdal package.
Group: Binaries
Requires: gdal-data = %{version}-%{release}
Requires: gdal-license = %{version}-%{release}

%description bin
bin components for the gdal package.


%package data
Summary: data components for the gdal package.
Group: Data

%description data
data components for the gdal package.


%package dev
Summary: dev components for the gdal package.
Group: Development
Requires: gdal-lib = %{version}-%{release}
Requires: gdal-bin = %{version}-%{release}
Requires: gdal-data = %{version}-%{release}
Provides: gdal-devel = %{version}-%{release}
Requires: gdal = %{version}-%{release}

%description dev
dev components for the gdal package.


%package lib
Summary: lib components for the gdal package.
Group: Libraries
Requires: gdal-data = %{version}-%{release}
Requires: gdal-license = %{version}-%{release}

%description lib
lib components for the gdal package.


%package license
Summary: license components for the gdal package.
Group: Default

%description license
license components for the gdal package.


%package man
Summary: man components for the gdal package.
Group: Default

%description man
man components for the gdal package.


%package python
Summary: python components for the gdal package.
Group: Default
Requires: gdal-python3 = %{version}-%{release}

%description python
python components for the gdal package.


%package python3
Summary: python3 components for the gdal package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gdal package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 33EBBFC47B3DD87D' gpg.status
%setup -q -n gdal-3.10.2
cd %{_builddir}/gdal-3.10.2
pushd ..
cp -a gdal-3.10.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742500840
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DGDAL_USE_POPPLER=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DGDAL_USE_POPPLER=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742500840
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gdal
cp %{_builddir}/gdal-%{version}/LICENSE.TXT %{buildroot}/usr/share/package-licenses/gdal/51134147a0feb5f2a47099a8b81d33f1099dfd21 || :
cp %{_builddir}/gdal-%{version}/frmts/gif/giflib/COPYING %{buildroot}/usr/share/package-licenses/gdal/f9c9a2d3495a0766b4cf20d4b90cfe714dab3dc1 || :
cp %{_builddir}/gdal-%{version}/frmts/mrf/LERCV1/LICENSE.TXT %{buildroot}/usr/share/package-licenses/gdal/3035b519169390d1aaa3a43267deaae5cdff8a9b || :
cp %{_builddir}/gdal-%{version}/frmts/pcraster/libcsf/COPYING %{buildroot}/usr/share/package-licenses/gdal/1d982db70b88f943cc7d15013c28a126339d6cbc || :
cp %{_builddir}/gdal-%{version}/frmts/png/libpng/LICENSE %{buildroot}/usr/share/package-licenses/gdal/570f5344ea5facacb5e0bbb3fe4e0674189a5f0e || :
cp %{_builddir}/gdal-%{version}/ogr/ogrsf_frmts/flatgeobuf/LICENSE %{buildroot}/usr/share/package-licenses/gdal/161732baff9a38188301a521b567a20245367c7e || :
cp %{_builddir}/gdal-%{version}/ogr/ogrsf_frmts/flatgeobuf/flatbuffers/LICENSE %{buildroot}/usr/share/package-licenses/gdal/abb8eb20f7f319cd8b292cdccce15826bac01363 || :
cp %{_builddir}/gdal-%{version}/ogr/ogrsf_frmts/geojson/libjson/COPYING %{buildroot}/usr/share/package-licenses/gdal/0cd23537e3c32497c7b87157b36f9d2eb5fca64b || :
cp %{_builddir}/gdal-%{version}/ogr/ogrsf_frmts/pmtiles/pmtiles/LICENSE %{buildroot}/usr/share/package-licenses/gdal/7a081f74aa51f66c8f5b2b7d9220b0d2c03693f1 || :
cp %{_builddir}/gdal-%{version}/port/LICENCE_minizip %{buildroot}/usr/share/package-licenses/gdal/f7f1d88d0aea6c567a2c351b08b0fe80f2582054 || :
cp %{_builddir}/gdal-%{version}/third_party/LercLib/LICENSE %{buildroot}/usr/share/package-licenses/gdal/3035b519169390d1aaa3a43267deaae5cdff8a9b || :
cp %{_builddir}/gdal-%{version}/third_party/fast_float/LICENSE-MIT %{buildroot}/usr/share/package-licenses/gdal/11e6be99fa6ad788d013a38598c7da3e5d90efbe || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/etc/bash_completion.d/gdal-bash-completion.sh
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/gdalplugins/drivers.ini

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gdal_contour
/V3/usr/bin/gdal_create
/V3/usr/bin/gdal_footprint
/V3/usr/bin/gdal_grid
/V3/usr/bin/gdal_rasterize
/V3/usr/bin/gdal_translate
/V3/usr/bin/gdal_viewshed
/V3/usr/bin/gdaladdo
/V3/usr/bin/gdalbuildvrt
/V3/usr/bin/gdaldem
/V3/usr/bin/gdalenhance
/V3/usr/bin/gdalinfo
/V3/usr/bin/gdallocationinfo
/V3/usr/bin/gdalmanage
/V3/usr/bin/gdalmdiminfo
/V3/usr/bin/gdalmdimtranslate
/V3/usr/bin/gdalsrsinfo
/V3/usr/bin/gdaltindex
/V3/usr/bin/gdaltransform
/V3/usr/bin/gdalwarp
/V3/usr/bin/gnmanalyse
/V3/usr/bin/gnmmanage
/V3/usr/bin/nearblack
/V3/usr/bin/ogr2ogr
/V3/usr/bin/ogrinfo
/V3/usr/bin/ogrlineref
/V3/usr/bin/ogrtindex
/V3/usr/bin/sozip
/usr/bin/gdal-config
/usr/bin/gdal2tiles
/usr/bin/gdal2tiles.py
/usr/bin/gdal2xyz
/usr/bin/gdal2xyz.py
/usr/bin/gdal_calc
/usr/bin/gdal_calc.py
/usr/bin/gdal_contour
/usr/bin/gdal_create
/usr/bin/gdal_edit
/usr/bin/gdal_edit.py
/usr/bin/gdal_fillnodata
/usr/bin/gdal_fillnodata.py
/usr/bin/gdal_footprint
/usr/bin/gdal_grid
/usr/bin/gdal_merge
/usr/bin/gdal_merge.py
/usr/bin/gdal_pansharpen
/usr/bin/gdal_pansharpen.py
/usr/bin/gdal_polygonize
/usr/bin/gdal_polygonize.py
/usr/bin/gdal_proximity
/usr/bin/gdal_proximity.py
/usr/bin/gdal_rasterize
/usr/bin/gdal_retile
/usr/bin/gdal_retile.py
/usr/bin/gdal_sieve
/usr/bin/gdal_sieve.py
/usr/bin/gdal_translate
/usr/bin/gdal_viewshed
/usr/bin/gdaladdo
/usr/bin/gdalattachpct
/usr/bin/gdalattachpct.py
/usr/bin/gdalbuildvrt
/usr/bin/gdalcompare
/usr/bin/gdalcompare.py
/usr/bin/gdaldem
/usr/bin/gdalenhance
/usr/bin/gdalinfo
/usr/bin/gdallocationinfo
/usr/bin/gdalmanage
/usr/bin/gdalmdiminfo
/usr/bin/gdalmdimtranslate
/usr/bin/gdalmove
/usr/bin/gdalmove.py
/usr/bin/gdalsrsinfo
/usr/bin/gdaltindex
/usr/bin/gdaltransform
/usr/bin/gdalwarp
/usr/bin/gnmanalyse
/usr/bin/gnmmanage
/usr/bin/nearblack
/usr/bin/ogr2ogr
/usr/bin/ogr_layer_algebra
/usr/bin/ogr_layer_algebra.py
/usr/bin/ogrinfo
/usr/bin/ogrlineref
/usr/bin/ogrmerge
/usr/bin/ogrmerge.py
/usr/bin/ogrtindex
/usr/bin/pct2rgb
/usr/bin/pct2rgb.py
/usr/bin/rgb2pct
/usr/bin/rgb2pct.py
/usr/bin/sozip

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/gdal-config
/usr/share/bash-completion/completions/gdal2tiles.py
/usr/share/bash-completion/completions/gdal2xyz.py
/usr/share/bash-completion/completions/gdal_calc.py
/usr/share/bash-completion/completions/gdal_contour
/usr/share/bash-completion/completions/gdal_create
/usr/share/bash-completion/completions/gdal_edit.py
/usr/share/bash-completion/completions/gdal_fillnodata.py
/usr/share/bash-completion/completions/gdal_grid
/usr/share/bash-completion/completions/gdal_merge.py
/usr/share/bash-completion/completions/gdal_polygonize.py
/usr/share/bash-completion/completions/gdal_proximity.py
/usr/share/bash-completion/completions/gdal_rasterize
/usr/share/bash-completion/completions/gdal_retile.py
/usr/share/bash-completion/completions/gdal_sieve.py
/usr/share/bash-completion/completions/gdal_translate
/usr/share/bash-completion/completions/gdal_viewshed
/usr/share/bash-completion/completions/gdaladdo
/usr/share/bash-completion/completions/gdalbuildvrt
/usr/share/bash-completion/completions/gdalchksum.py
/usr/share/bash-completion/completions/gdalcompare.py
/usr/share/bash-completion/completions/gdaldem
/usr/share/bash-completion/completions/gdalenhance
/usr/share/bash-completion/completions/gdalident.py
/usr/share/bash-completion/completions/gdalimport.py
/usr/share/bash-completion/completions/gdalinfo
/usr/share/bash-completion/completions/gdallocationinfo
/usr/share/bash-completion/completions/gdalmanage
/usr/share/bash-completion/completions/gdalmove.py
/usr/share/bash-completion/completions/gdalsrsinfo
/usr/share/bash-completion/completions/gdaltindex
/usr/share/bash-completion/completions/gdaltransform
/usr/share/bash-completion/completions/gdalwarp
/usr/share/bash-completion/completions/ogr2ogr
/usr/share/bash-completion/completions/ogrinfo
/usr/share/bash-completion/completions/ogrlineref
/usr/share/bash-completion/completions/ogrmerge.py
/usr/share/bash-completion/completions/ogrtindex
/usr/share/gdal/GDALLogoBW.svg
/usr/share/gdal/GDALLogoColor.svg
/usr/share/gdal/GDALLogoGS.svg
/usr/share/gdal/LICENSE.TXT
/usr/share/gdal/MM_m_idofic.csv
/usr/share/gdal/bag_template.xml
/usr/share/gdal/cubewerx_extra.wkt
/usr/share/gdal/default.rsc
/usr/share/gdal/ecw_cs.wkt
/usr/share/gdal/eedaconf.json
/usr/share/gdal/epsg.wkt
/usr/share/gdal/esri_StatePlane_extra.wkt
/usr/share/gdal/gdalicon.png
/usr/share/gdal/gdalinfo_output.schema.json
/usr/share/gdal/gdalmdiminfo_output.schema.json
/usr/share/gdal/gdaltileindex.xsd
/usr/share/gdal/gdalvrt.xsd
/usr/share/gdal/gfs.xsd
/usr/share/gdal/gml_registry.xml
/usr/share/gdal/gml_registry.xsd
/usr/share/gdal/grib2_center.csv
/usr/share/gdal/grib2_process.csv
/usr/share/gdal/grib2_subcenter.csv
/usr/share/gdal/grib2_table_4_2_0_0.csv
/usr/share/gdal/grib2_table_4_2_0_1.csv
/usr/share/gdal/grib2_table_4_2_0_13.csv
/usr/share/gdal/grib2_table_4_2_0_14.csv
/usr/share/gdal/grib2_table_4_2_0_15.csv
/usr/share/gdal/grib2_table_4_2_0_16.csv
/usr/share/gdal/grib2_table_4_2_0_17.csv
/usr/share/gdal/grib2_table_4_2_0_18.csv
/usr/share/gdal/grib2_table_4_2_0_19.csv
/usr/share/gdal/grib2_table_4_2_0_190.csv
/usr/share/gdal/grib2_table_4_2_0_191.csv
/usr/share/gdal/grib2_table_4_2_0_2.csv
/usr/share/gdal/grib2_table_4_2_0_20.csv
/usr/share/gdal/grib2_table_4_2_0_21.csv
/usr/share/gdal/grib2_table_4_2_0_3.csv
/usr/share/gdal/grib2_table_4_2_0_4.csv
/usr/share/gdal/grib2_table_4_2_0_5.csv
/usr/share/gdal/grib2_table_4_2_0_6.csv
/usr/share/gdal/grib2_table_4_2_0_7.csv
/usr/share/gdal/grib2_table_4_2_10_0.csv
/usr/share/gdal/grib2_table_4_2_10_1.csv
/usr/share/gdal/grib2_table_4_2_10_191.csv
/usr/share/gdal/grib2_table_4_2_10_2.csv
/usr/share/gdal/grib2_table_4_2_10_3.csv
/usr/share/gdal/grib2_table_4_2_10_4.csv
/usr/share/gdal/grib2_table_4_2_1_0.csv
/usr/share/gdal/grib2_table_4_2_1_1.csv
/usr/share/gdal/grib2_table_4_2_1_2.csv
/usr/share/gdal/grib2_table_4_2_20_0.csv
/usr/share/gdal/grib2_table_4_2_20_1.csv
/usr/share/gdal/grib2_table_4_2_20_2.csv
/usr/share/gdal/grib2_table_4_2_2_0.csv
/usr/share/gdal/grib2_table_4_2_2_3.csv
/usr/share/gdal/grib2_table_4_2_2_4.csv
/usr/share/gdal/grib2_table_4_2_2_5.csv
/usr/share/gdal/grib2_table_4_2_2_6.csv
/usr/share/gdal/grib2_table_4_2_3_0.csv
/usr/share/gdal/grib2_table_4_2_3_1.csv
/usr/share/gdal/grib2_table_4_2_3_2.csv
/usr/share/gdal/grib2_table_4_2_3_3.csv
/usr/share/gdal/grib2_table_4_2_3_4.csv
/usr/share/gdal/grib2_table_4_2_3_5.csv
/usr/share/gdal/grib2_table_4_2_3_6.csv
/usr/share/gdal/grib2_table_4_2_4_0.csv
/usr/share/gdal/grib2_table_4_2_4_1.csv
/usr/share/gdal/grib2_table_4_2_4_10.csv
/usr/share/gdal/grib2_table_4_2_4_2.csv
/usr/share/gdal/grib2_table_4_2_4_3.csv
/usr/share/gdal/grib2_table_4_2_4_4.csv
/usr/share/gdal/grib2_table_4_2_4_5.csv
/usr/share/gdal/grib2_table_4_2_4_6.csv
/usr/share/gdal/grib2_table_4_2_4_7.csv
/usr/share/gdal/grib2_table_4_2_4_8.csv
/usr/share/gdal/grib2_table_4_2_4_9.csv
/usr/share/gdal/grib2_table_4_2_local_Canada.csv
/usr/share/gdal/grib2_table_4_2_local_HPC.csv
/usr/share/gdal/grib2_table_4_2_local_MRMS.csv
/usr/share/gdal/grib2_table_4_2_local_NCEP.csv
/usr/share/gdal/grib2_table_4_2_local_NDFD.csv
/usr/share/gdal/grib2_table_4_2_local_index.csv
/usr/share/gdal/grib2_table_4_5.csv
/usr/share/gdal/grib2_table_versions.csv
/usr/share/gdal/gt_datum.csv
/usr/share/gdal/gt_ellips.csv
/usr/share/gdal/header.dxf
/usr/share/gdal/inspire_cp_BasicPropertyUnit.gfs
/usr/share/gdal/inspire_cp_CadastralBoundary.gfs
/usr/share/gdal/inspire_cp_CadastralParcel.gfs
/usr/share/gdal/inspire_cp_CadastralZoning.gfs
/usr/share/gdal/jpfgdgml_AdmArea.gfs
/usr/share/gdal/jpfgdgml_AdmBdry.gfs
/usr/share/gdal/jpfgdgml_AdmPt.gfs
/usr/share/gdal/jpfgdgml_BldA.gfs
/usr/share/gdal/jpfgdgml_BldL.gfs
/usr/share/gdal/jpfgdgml_Cntr.gfs
/usr/share/gdal/jpfgdgml_CommBdry.gfs
/usr/share/gdal/jpfgdgml_CommPt.gfs
/usr/share/gdal/jpfgdgml_Cstline.gfs
/usr/share/gdal/jpfgdgml_ElevPt.gfs
/usr/share/gdal/jpfgdgml_GCP.gfs
/usr/share/gdal/jpfgdgml_LeveeEdge.gfs
/usr/share/gdal/jpfgdgml_RailCL.gfs
/usr/share/gdal/jpfgdgml_RdASL.gfs
/usr/share/gdal/jpfgdgml_RdArea.gfs
/usr/share/gdal/jpfgdgml_RdCompt.gfs
/usr/share/gdal/jpfgdgml_RdEdg.gfs
/usr/share/gdal/jpfgdgml_RdMgtBdry.gfs
/usr/share/gdal/jpfgdgml_RdSgmtA.gfs
/usr/share/gdal/jpfgdgml_RvrMgtBdry.gfs
/usr/share/gdal/jpfgdgml_SBAPt.gfs
/usr/share/gdal/jpfgdgml_SBArea.gfs
/usr/share/gdal/jpfgdgml_SBBdry.gfs
/usr/share/gdal/jpfgdgml_WA.gfs
/usr/share/gdal/jpfgdgml_WL.gfs
/usr/share/gdal/jpfgdgml_WStrA.gfs
/usr/share/gdal/jpfgdgml_WStrL.gfs
/usr/share/gdal/nitf_spec.xml
/usr/share/gdal/nitf_spec.xsd
/usr/share/gdal/ogrinfo_output.schema.json
/usr/share/gdal/ogrvrt.xsd
/usr/share/gdal/osmconf.ini
/usr/share/gdal/ozi_datum.csv
/usr/share/gdal/ozi_ellips.csv
/usr/share/gdal/pci_datum.txt
/usr/share/gdal/pci_ellips.txt
/usr/share/gdal/pdfcomposition.xsd
/usr/share/gdal/pds4_template.xml
/usr/share/gdal/plscenesconf.json
/usr/share/gdal/ruian_vf_ob_v1.gfs
/usr/share/gdal/ruian_vf_st_uvoh_v1.gfs
/usr/share/gdal/ruian_vf_st_v1.gfs
/usr/share/gdal/ruian_vf_v1.gfs
/usr/share/gdal/s57agencies.csv
/usr/share/gdal/s57attributes.csv
/usr/share/gdal/s57expectedinput.csv
/usr/share/gdal/s57objectclasses.csv
/usr/share/gdal/seed_2d.dgn
/usr/share/gdal/seed_3d.dgn
/usr/share/gdal/stateplane.csv
/usr/share/gdal/template_tiles.mapml
/usr/share/gdal/tms_LINZAntarticaMapTileGrid.json
/usr/share/gdal/tms_MapML_APSTILE.json
/usr/share/gdal/tms_MapML_CBMTILE.json
/usr/share/gdal/tms_NZTM2000.json
/usr/share/gdal/trailer.dxf
/usr/share/gdal/vdv452.xml
/usr/share/gdal/vdv452.xsd
/usr/share/gdal/vicar.json

%files dev
%defattr(-,root,root,-)
/usr/include/cpl_atomic_ops.h
/usr/include/cpl_auto_close.h
/usr/include/cpl_compressor.h
/usr/include/cpl_config.h
/usr/include/cpl_config_extras.h
/usr/include/cpl_conv.h
/usr/include/cpl_csv.h
/usr/include/cpl_error.h
/usr/include/cpl_hash_set.h
/usr/include/cpl_http.h
/usr/include/cpl_json.h
/usr/include/cpl_list.h
/usr/include/cpl_minixml.h
/usr/include/cpl_multiproc.h
/usr/include/cpl_port.h
/usr/include/cpl_progress.h
/usr/include/cpl_quad_tree.h
/usr/include/cpl_spawn.h
/usr/include/cpl_string.h
/usr/include/cpl_time.h
/usr/include/cpl_virtualmem.h
/usr/include/cpl_vsi.h
/usr/include/cpl_vsi_error.h
/usr/include/cpl_vsi_virtual.h
/usr/include/cplkeywordparser.h
/usr/include/gdal.h
/usr/include/gdal_alg.h
/usr/include/gdal_alg_priv.h
/usr/include/gdal_csv.h
/usr/include/gdal_frmts.h
/usr/include/gdal_mdreader.h
/usr/include/gdal_pam.h
/usr/include/gdal_priv.h
/usr/include/gdal_proxy.h
/usr/include/gdal_rat.h
/usr/include/gdal_simplesurf.h
/usr/include/gdal_utils.h
/usr/include/gdal_version.h
/usr/include/gdal_vrt.h
/usr/include/gdalcachedpixelaccessor.h
/usr/include/gdalgeorefpamdataset.h
/usr/include/gdalgrid.h
/usr/include/gdalgrid_priv.h
/usr/include/gdaljp2abstractdataset.h
/usr/include/gdaljp2metadata.h
/usr/include/gdalpansharpen.h
/usr/include/gdalsubdatasetinfo.h
/usr/include/gdalwarper.h
/usr/include/gnm.h
/usr/include/gnm_api.h
/usr/include/gnmgraph.h
/usr/include/memdataset.h
/usr/include/ogr_api.h
/usr/include/ogr_core.h
/usr/include/ogr_feature.h
/usr/include/ogr_featurestyle.h
/usr/include/ogr_geocoding.h
/usr/include/ogr_geomcoordinateprecision.h
/usr/include/ogr_geometry.h
/usr/include/ogr_p.h
/usr/include/ogr_recordbatch.h
/usr/include/ogr_spatialref.h
/usr/include/ogr_srs_api.h
/usr/include/ogr_swq.h
/usr/include/ogrsf_frmts.h
/usr/include/rawdataset.h
/usr/include/vrtdataset.h
/usr/lib64/cmake/gdal/GDAL-targets-relwithdebinfo.cmake
/usr/lib64/cmake/gdal/GDAL-targets.cmake
/usr/lib64/cmake/gdal/GDALConfig.cmake
/usr/lib64/cmake/gdal/GDALConfigVersion.cmake
/usr/lib64/libgdal.so
/usr/lib64/pkgconfig/gdal.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgdal.so.36.3.10.2
/usr/lib64/libgdal.so.36
/usr/lib64/libgdal.so.36.3.10.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gdal/0cd23537e3c32497c7b87157b36f9d2eb5fca64b
/usr/share/package-licenses/gdal/11e6be99fa6ad788d013a38598c7da3e5d90efbe
/usr/share/package-licenses/gdal/161732baff9a38188301a521b567a20245367c7e
/usr/share/package-licenses/gdal/1d982db70b88f943cc7d15013c28a126339d6cbc
/usr/share/package-licenses/gdal/3035b519169390d1aaa3a43267deaae5cdff8a9b
/usr/share/package-licenses/gdal/51134147a0feb5f2a47099a8b81d33f1099dfd21
/usr/share/package-licenses/gdal/570f5344ea5facacb5e0bbb3fe4e0674189a5f0e
/usr/share/package-licenses/gdal/7a081f74aa51f66c8f5b2b7d9220b0d2c03693f1
/usr/share/package-licenses/gdal/abb8eb20f7f319cd8b292cdccce15826bac01363
/usr/share/package-licenses/gdal/f7f1d88d0aea6c567a2c351b08b0fe80f2582054
/usr/share/package-licenses/gdal/f9c9a2d3495a0766b4cf20d4b90cfe714dab3dc1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gdal-config.1
/usr/share/man/man1/gdal2tiles.1
/usr/share/man/man1/gdal_calc.1
/usr/share/man/man1/gdal_contour.1
/usr/share/man/man1/gdal_create.1
/usr/share/man/man1/gdal_edit.1
/usr/share/man/man1/gdal_fillnodata.1
/usr/share/man/man1/gdal_footprint.1
/usr/share/man/man1/gdal_grid.1
/usr/share/man/man1/gdal_merge.1
/usr/share/man/man1/gdal_pansharpen.1
/usr/share/man/man1/gdal_polygonize.1
/usr/share/man/man1/gdal_proximity.1
/usr/share/man/man1/gdal_rasterize.1
/usr/share/man/man1/gdal_retile.1
/usr/share/man/man1/gdal_sieve.1
/usr/share/man/man1/gdal_translate.1
/usr/share/man/man1/gdal_viewshed.1
/usr/share/man/man1/gdaladdo.1
/usr/share/man/man1/gdalbuildvrt.1
/usr/share/man/man1/gdalcompare.1
/usr/share/man/man1/gdaldem.1
/usr/share/man/man1/gdalinfo.1
/usr/share/man/man1/gdallocationinfo.1
/usr/share/man/man1/gdalmanage.1
/usr/share/man/man1/gdalmdiminfo.1
/usr/share/man/man1/gdalmdimtranslate.1
/usr/share/man/man1/gdalmove.1
/usr/share/man/man1/gdalsrsinfo.1
/usr/share/man/man1/gdaltindex.1
/usr/share/man/man1/gdaltransform.1
/usr/share/man/man1/gdalwarp.1
/usr/share/man/man1/gnmanalyse.1
/usr/share/man/man1/gnmmanage.1
/usr/share/man/man1/nearblack.1
/usr/share/man/man1/ogr2ogr.1
/usr/share/man/man1/ogr_layer_algebra.1
/usr/share/man/man1/ogrinfo.1
/usr/share/man/man1/ogrlineref.1
/usr/share/man/man1/ogrmerge.1
/usr/share/man/man1/ogrtindex.1
/usr/share/man/man1/pct2rgb.1
/usr/share/man/man1/rgb2pct.1
/usr/share/man/man1/sozip.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
