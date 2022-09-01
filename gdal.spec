#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gdal
Version  : 3.4.3
Release  : 57
URL      : http://download.osgeo.org/gdal/3.4.3/gdal-3.4.3.tar.xz
Source0  : http://download.osgeo.org/gdal/3.4.3/gdal-3.4.3.tar.xz
Summary  : Geospatial Data Abstraction Library
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC LGPL-2.0 Libpng MIT Public-Domain Qhull
Requires: gdal-bin = %{version}-%{release}
Requires: gdal-data = %{version}-%{release}
Requires: gdal-filemap = %{version}-%{release}
Requires: gdal-lib = %{version}-%{release}
Requires: gdal-license = %{version}-%{release}
BuildRequires : SFCGAL-dev
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : curl-dev
BuildRequires : expat-dev
BuildRequires : geos-dev
BuildRequires : giflib-dev
BuildRequires : hdf5-dev
BuildRequires : json-c-dev
BuildRequires : libgeotiff-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libwebp-dev
BuildRequires : ocl-icd-dev
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : pcre2-dev
BuildRequires : pkgconfig(OpenEXR)
BuildRequires : pkgconfig(libpq)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(poppler)
BuildRequires : pkgconfig(spatialite)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : proj
BuildRequires : proj-dev
BuildRequires : qhull-dev
BuildRequires : tiff-dev
BuildRequires : unixODBC-dev
BuildRequires : xerces-c-dev
BuildRequires : zstd-dev

%description
The following source files are taken from the HDF-EOS package
EHapi.c,
GDapi.c,
SWapi.c,
HDFEOSVersion.h,
HdfEosDef.h,
ease.h

%package bin
Summary: bin components for the gdal package.
Group: Binaries
Requires: gdal-data = %{version}-%{release}
Requires: gdal-license = %{version}-%{release}
Requires: gdal-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the gdal package.
Group: Default

%description filemap
filemap components for the gdal package.


%package lib
Summary: lib components for the gdal package.
Group: Libraries
Requires: gdal-data = %{version}-%{release}
Requires: gdal-license = %{version}-%{release}
Requires: gdal-filemap = %{version}-%{release}

%description lib
lib components for the gdal package.


%package license
Summary: license components for the gdal package.
Group: Default

%description license
license components for the gdal package.


%prep
%setup -q -n gdal-3.4.3
cd %{_builddir}/gdal-3.4.3
pushd ..
cp -a gdal-3.4.3 buildavx2
popd

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
export SOURCE_DATE_EPOCH=1656111745
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
%configure --disable-static --with-libtiff=yes \
--with-png=yes \
--with-spatialite=yes \
--with-sqlite3=yes \
--with-poppler=yes \
--enable-lto \
--with-gif=/usr \
--with-libjson-c=/usr \
--with-libtool=yes
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
sed -i 's/-flto"$/-flto=auto"/' ./configure.ac
# Also patch the generated configure script, in case we stop patching
# configure.ac, m4 files, etc.
sed -i 's/-flto"$/-flto=auto"/' ./configure
## build_prepend end
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --with-libtiff=yes \
--with-png=yes \
--with-spatialite=yes \
--with-sqlite3=yes \
--with-poppler=yes \
--enable-lto \
--with-gif=/usr \
--with-libjson-c=/usr \
--with-libtool=yes
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1656111745
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gdal
cp %{_builddir}/gdal-3.4.3/LICENSE.TXT %{buildroot}/usr/share/package-licenses/gdal/3c5056c99522acf3d9e2c2a2f61fdeeffced4174
cp %{_builddir}/gdal-3.4.3/alg/internal_libqhull/COPYING.txt %{buildroot}/usr/share/package-licenses/gdal/baf1d15dcf66b1e1dfee80eb405aa73105842017
cp %{_builddir}/gdal-3.4.3/doc/source/gdal_rtd/LICENSE %{buildroot}/usr/share/package-licenses/gdal/8ce271d47d282a4da574b385a8aff7a0d735188e
cp %{_builddir}/gdal-3.4.3/doc/source/license.rst %{buildroot}/usr/share/package-licenses/gdal/0f9d62383e84298877fe5f5d41f6a944f7ef8563
cp %{_builddir}/gdal-3.4.3/frmts/gif/giflib/COPYING %{buildroot}/usr/share/package-licenses/gdal/f9c9a2d3495a0766b4cf20d4b90cfe714dab3dc1
cp %{_builddir}/gdal-3.4.3/frmts/mrf/LERCV1/LICENSE.TXT %{buildroot}/usr/share/package-licenses/gdal/3035b519169390d1aaa3a43267deaae5cdff8a9b
cp %{_builddir}/gdal-3.4.3/frmts/pcraster/libcsf/COPYING %{buildroot}/usr/share/package-licenses/gdal/1d982db70b88f943cc7d15013c28a126339d6cbc
cp %{_builddir}/gdal-3.4.3/frmts/png/libpng/LICENSE %{buildroot}/usr/share/package-licenses/gdal/fc3951ba26fe1914759f605696a1d23e3b41766f
cp %{_builddir}/gdal-3.4.3/ogr/ogrsf_frmts/flatgeobuf/LICENSE %{buildroot}/usr/share/package-licenses/gdal/161732baff9a38188301a521b567a20245367c7e
cp %{_builddir}/gdal-3.4.3/ogr/ogrsf_frmts/flatgeobuf/flatbuffers/LICENSE %{buildroot}/usr/share/package-licenses/gdal/abb8eb20f7f319cd8b292cdccce15826bac01363
cp %{_builddir}/gdal-3.4.3/ogr/ogrsf_frmts/geojson/libjson/COPYING %{buildroot}/usr/share/package-licenses/gdal/0cd23537e3c32497c7b87157b36f9d2eb5fca64b
cp %{_builddir}/gdal-3.4.3/ogr/ogrsf_frmts/shape/COPYING %{buildroot}/usr/share/package-licenses/gdal/df97bdf33b01f9ed42a799dd3ed7a1599dd0cb9d
cp %{_builddir}/gdal-3.4.3/port/LICENCE_minizip %{buildroot}/usr/share/package-licenses/gdal/f7f1d88d0aea6c567a2c351b08b0fe80f2582054
cp %{_builddir}/gdal-3.4.3/third_party/LercLib/LICENSE %{buildroot}/usr/share/package-licenses/gdal/3035b519169390d1aaa3a43267deaae5cdff8a9b
cp %{_builddir}/gdal-3.4.3/third_party/LercLib/NOTICE %{buildroot}/usr/share/package-licenses/gdal/4e8e03579f57bab9de5401be3fb96344f0823ead
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/etc/bash_completion.d/gdal-bash-completion.sh
## install_append content
#install -D %{buildroot}/usr/etc/bash_completion.d/gdal-bash-completion.sh %{buildroot}/usr/share/bash-completion/completions/gdal-bash-completion.sh
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gdal-config
/usr/bin/gdal_contour
/usr/bin/gdal_create
/usr/bin/gdal_grid
/usr/bin/gdal_rasterize
/usr/bin/gdal_translate
/usr/bin/gdal_viewshed
/usr/bin/gdaladdo
/usr/bin/gdalbuildvrt
/usr/bin/gdaldem
/usr/bin/gdalenhance
/usr/bin/gdalinfo
/usr/bin/gdallocationinfo
/usr/bin/gdalmanage
/usr/bin/gdalmdiminfo
/usr/bin/gdalmdimtranslate
/usr/bin/gdalsrsinfo
/usr/bin/gdaltindex
/usr/bin/gdaltransform
/usr/bin/gdalwarp
/usr/bin/gnmanalyse
/usr/bin/gnmmanage
/usr/bin/nearblack
/usr/bin/ogr2ogr
/usr/bin/ogrinfo
/usr/bin/ogrlineref
/usr/bin/ogrtindex
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/gdal/GDALLogoBW.svg
/usr/share/gdal/GDALLogoColor.svg
/usr/share/gdal/GDALLogoGS.svg
/usr/share/gdal/LICENSE.TXT
/usr/share/gdal/bag_template.xml
/usr/share/gdal/cubewerx_extra.wkt
/usr/share/gdal/default.rsc
/usr/share/gdal/ecw_cs.wkt
/usr/share/gdal/eedaconf.json
/usr/share/gdal/epsg.wkt
/usr/share/gdal/esri_StatePlane_extra.wkt
/usr/share/gdal/gdalicon.png
/usr/share/gdal/gdalmdiminfo_output.schema.json
/usr/share/gdal/gdalvrt.xsd
/usr/share/gdal/gml_registry.xml
/usr/share/gdal/gmlasconf.xml
/usr/share/gdal/gmlasconf.xsd
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
/usr/share/gdal/netcdf_config.xsd
/usr/share/gdal/nitf_spec.xml
/usr/share/gdal/nitf_spec.xsd
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
/usr/include/cpl_minizip_ioapi.h
/usr/include/cpl_minizip_unzip.h
/usr/include/cpl_minizip_zip.h
/usr/include/cpl_multiproc.h
/usr/include/cpl_odbc.h
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
/usr/include/gdalgeorefpamdataset.h
/usr/include/gdalgrid.h
/usr/include/gdalgrid_priv.h
/usr/include/gdaljp2abstractdataset.h
/usr/include/gdaljp2metadata.h
/usr/include/gdalpansharpen.h
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
/usr/include/ogr_geometry.h
/usr/include/ogr_p.h
/usr/include/ogr_spatialref.h
/usr/include/ogr_srs_api.h
/usr/include/ogr_swq.h
/usr/include/ogrsf_frmts.h
/usr/include/rawdataset.h
/usr/include/vrtdataset.h
/usr/lib64/libgdal.so
/usr/lib64/pkgconfig/gdal.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-gdal

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libgdal.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libgdal.so.30
/usr/lib64/glibc-hwcaps/x86-64-v3/libgdal.so.30.0.3
/usr/lib64/libgdal.so.30
/usr/lib64/libgdal.so.30.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gdal/0cd23537e3c32497c7b87157b36f9d2eb5fca64b
/usr/share/package-licenses/gdal/0f9d62383e84298877fe5f5d41f6a944f7ef8563
/usr/share/package-licenses/gdal/161732baff9a38188301a521b567a20245367c7e
/usr/share/package-licenses/gdal/1d982db70b88f943cc7d15013c28a126339d6cbc
/usr/share/package-licenses/gdal/3035b519169390d1aaa3a43267deaae5cdff8a9b
/usr/share/package-licenses/gdal/3c5056c99522acf3d9e2c2a2f61fdeeffced4174
/usr/share/package-licenses/gdal/4e8e03579f57bab9de5401be3fb96344f0823ead
/usr/share/package-licenses/gdal/8ce271d47d282a4da574b385a8aff7a0d735188e
/usr/share/package-licenses/gdal/abb8eb20f7f319cd8b292cdccce15826bac01363
/usr/share/package-licenses/gdal/baf1d15dcf66b1e1dfee80eb405aa73105842017
/usr/share/package-licenses/gdal/df97bdf33b01f9ed42a799dd3ed7a1599dd0cb9d
/usr/share/package-licenses/gdal/f7f1d88d0aea6c567a2c351b08b0fe80f2582054
/usr/share/package-licenses/gdal/f9c9a2d3495a0766b4cf20d4b90cfe714dab3dc1
/usr/share/package-licenses/gdal/fc3951ba26fe1914759f605696a1d23e3b41766f
