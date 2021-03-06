## Version 0.14.1 (2019/04/12)

### Issues Closed

* [Issue 716](https://github.com/pytroll/satpy/issues/716) - Reading the EUMETSAT compact viirs format returns wrong platform name (J01 instead of NOAA-20) ([PR 717](https://github.com/pytroll/satpy/pull/717))
* [Issue 710](https://github.com/pytroll/satpy/issues/710) - Question (maybe a bug): Why does RBG array exported with scn.save_dataset contain values greater than 255 ?

In this release 2 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 721](https://github.com/pytroll/satpy/pull/721) - Consistent platform id attribute across NAT + HRIT SEVIRI readers
* [PR 719](https://github.com/pytroll/satpy/pull/719) - Fix VIIRS 'night_fog' RGB composite recipe to use M12 instead of M14
* [PR 718](https://github.com/pytroll/satpy/pull/718) - Fix 'seviri_l1b_hrit' reader's area creation for pyproj 2.0+
* [PR 717](https://github.com/pytroll/satpy/pull/717) - Fix 'viirs_compact' and 'viirs_l1b' readers to return WMO/Oscar platform name ([716](https://github.com/pytroll/satpy/issues/716))
* [PR 715](https://github.com/pytroll/satpy/pull/715) - Fix hurricane florence demo download to only include M1 files
* [PR 712](https://github.com/pytroll/satpy/pull/712) - Fix 'mitiff' writer not clipping enhanced data before scaling to 8 bit values
* [PR 709](https://github.com/pytroll/satpy/pull/709) - Fix datetime64 use in 'seviri_l1b_hrit' reader for numpy < 1.15
* [PR 708](https://github.com/pytroll/satpy/pull/708) - Fix 'seviri_0deg' and 'seviri_iodc' builtin areas (areas.yaml) not matching reader areas

#### Documentation changes

* [PR 713](https://github.com/pytroll/satpy/pull/713) - Add links to source from API documentation

In this release 9 pull requests were closed.


## Version 0.14.0 (2019/04/09)

### Issues Closed

* [Issue 698](https://github.com/pytroll/satpy/issues/698) - Read WKT geotiff
* [Issue 692](https://github.com/pytroll/satpy/issues/692) - sdr_viirs_l1b reader fails in 0.13, recent master, Works with version 0.12.0 ([PR 693](https://github.com/pytroll/satpy/pull/693))
* [Issue 683](https://github.com/pytroll/satpy/issues/683) - Question: Change image size when saving with satpy.save_dataset ([PR 691](https://github.com/pytroll/satpy/pull/691))
* [Issue 681](https://github.com/pytroll/satpy/issues/681) - incorrect data offset in HSD files ([PR 689](https://github.com/pytroll/satpy/pull/689))
* [Issue 666](https://github.com/pytroll/satpy/issues/666) - Add drawing of lat lon graticules when saving dataset ([PR 668](https://github.com/pytroll/satpy/pull/668))
* [Issue 646](https://github.com/pytroll/satpy/issues/646) - Add 'demo' subpackage for accessing example data ([PR 686](https://github.com/pytroll/satpy/pull/686))
* [Issue 528](https://github.com/pytroll/satpy/issues/528) - Support dask version of PySpectral ([PR 529](https://github.com/pytroll/satpy/pull/529))
* [Issue 511](https://github.com/pytroll/satpy/issues/511) - Add/update documentation about composites and compositors ([PR 705](https://github.com/pytroll/satpy/pull/705))

In this release 8 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 700](https://github.com/pytroll/satpy/pull/700) - Mask out invalid values in the precipitation probability product
* [PR 693](https://github.com/pytroll/satpy/pull/693) - Fix VIIRS SDR reading of visible channels at nighttime ([692](https://github.com/pytroll/satpy/issues/692))
* [PR 689](https://github.com/pytroll/satpy/pull/689) - Fix Himawari HSD reader's incorrect header information ([681](https://github.com/pytroll/satpy/issues/681))
* [PR 688](https://github.com/pytroll/satpy/pull/688) - Fix offset correction in seviri_l1b_hrit
* [PR 685](https://github.com/pytroll/satpy/pull/685) - Fix bug in Scene.resample causing AssertionError
* [PR 677](https://github.com/pytroll/satpy/pull/677) - Fix MultiScene save_animation when distributed isn't installed
* [PR 675](https://github.com/pytroll/satpy/pull/675) - Do not pass `filter_parameters` to the filehandler creation

#### Features added

* [PR 691](https://github.com/pytroll/satpy/pull/691) - Add Scene.aggregate method (python 3 only) ([683](https://github.com/pytroll/satpy/issues/683))
* [PR 686](https://github.com/pytroll/satpy/pull/686) - Add demo subpackage to simplify test data download ([646](https://github.com/pytroll/satpy/issues/646))
* [PR 676](https://github.com/pytroll/satpy/pull/676) - Feature add nightfog modis
* [PR 674](https://github.com/pytroll/satpy/pull/674) - Use platform ID to choose the right reader for AVHRR GAC data
* [PR 671](https://github.com/pytroll/satpy/pull/671) - Add satellite position to dataset attributes (seviri_l1b_hrit)
* [PR 669](https://github.com/pytroll/satpy/pull/669) - Add ocean-color for viirs and modis
* [PR 668](https://github.com/pytroll/satpy/pull/668) - Add grid/graticules to add_overlay function. ([666](https://github.com/pytroll/satpy/issues/666))
* [PR 665](https://github.com/pytroll/satpy/pull/665) - Add reader for VIIRS Active Fires
* [PR 645](https://github.com/pytroll/satpy/pull/645) - Reader for the SAR OCN L2 wind product in SAFE format.
* [PR 565](https://github.com/pytroll/satpy/pull/565) - Add reader for FY-3 VIRR (virr_l1b)
* [PR 529](https://github.com/pytroll/satpy/pull/529) - Add dask support to NIRReflectance modifier ([528](https://github.com/pytroll/satpy/issues/528))

#### Documentation changes

* [PR 707](https://github.com/pytroll/satpy/pull/707) - Add ABI Meso demo data case and clean up documentation
* [PR 705](https://github.com/pytroll/satpy/pull/705) - Document composites ([511](https://github.com/pytroll/satpy/issues/511))
* [PR 701](https://github.com/pytroll/satpy/pull/701) - Clarify release instructions
* [PR 699](https://github.com/pytroll/satpy/pull/699) - Rename SatPy to Satpy throughout documentation
* [PR 673](https://github.com/pytroll/satpy/pull/673) - Add information about GDAL_CACHEMAX to FAQ

In this release 23 pull requests were closed.


## Version 0.13.0 (2019/03/18)

### Issues Closed

* [Issue 641](https://github.com/pytroll/satpy/issues/641) - After pip upgrade to satpy 0.12 and pyproj 2.0.1 got pyproj.exceptions.CRSError
* [Issue 626](https://github.com/pytroll/satpy/issues/626) - Issue loading MODIS Aqua data ([PR 648](https://github.com/pytroll/satpy/pull/648))
* [Issue 620](https://github.com/pytroll/satpy/issues/620) - Add FAQ about controlling number of threads for pykdtree and blas ([PR 621](https://github.com/pytroll/satpy/pull/621))
* [Issue 521](https://github.com/pytroll/satpy/issues/521) - Interactively set the Calibration Mode when creating the Scene Object ([PR 543](https://github.com/pytroll/satpy/pull/543))

In this release 4 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 664](https://github.com/pytroll/satpy/pull/664) - Fix Scene.crop with RGBs and multidimensional data
* [PR 662](https://github.com/pytroll/satpy/pull/662) - Fix masked resampling when dataset dtype is integer
* [PR 661](https://github.com/pytroll/satpy/pull/661) - Fix CTTH composite not to mark invalid data as cloud-free
* [PR 660](https://github.com/pytroll/satpy/pull/660) - Fix seviri_l1b_hrit prologue/epilogue readers
* [PR 655](https://github.com/pytroll/satpy/pull/655) - Fix yaml load to be compatible with pyyaml 5.1
* [PR 652](https://github.com/pytroll/satpy/pull/652) - Fix resampling of ancillary variables when also first class datasets
* [PR 648](https://github.com/pytroll/satpy/pull/648) - Add wrapped line support for metadata in modis_l1b reader ([626](https://github.com/pytroll/satpy/issues/626))
* [PR 644](https://github.com/pytroll/satpy/pull/644) - Fix the modis overview not to sun normalize the IR channel
* [PR 633](https://github.com/pytroll/satpy/pull/633) - Fix VIIRS HNCC composite passing xarray objects to dask
* [PR 632](https://github.com/pytroll/satpy/pull/632) - Fixing start and end times when missing in the CF writer

#### Features added

* [PR 647](https://github.com/pytroll/satpy/pull/647) - Switch python-hdf4 dependencies to pyhdf
* [PR 643](https://github.com/pytroll/satpy/pull/643) - In cira_strech clip values less or equal to 0 to avoid nans and -inf.
* [PR 642](https://github.com/pytroll/satpy/pull/642) - Bugfix pps2018 cpp products
* [PR 638](https://github.com/pytroll/satpy/pull/638) - Add processing-mode and disposition-mode to the avhrr-l1b-eps file name
* [PR 636](https://github.com/pytroll/satpy/pull/636) - Facilitate selection of calibration coefficients in seviri_l1b_hrit
* [PR 635](https://github.com/pytroll/satpy/pull/635) - Add local caching of slicing for data reduction
* [PR 627](https://github.com/pytroll/satpy/pull/627) - Add DNB satellite angles (DNB_SENZ, DNB_SENA) to VIIRS SDR reader
* [PR 557](https://github.com/pytroll/satpy/pull/557) - Improve the SAR-C reading and Ice composite
* [PR 543](https://github.com/pytroll/satpy/pull/543) - Calibration mode can now be passed via a keyword argument ([521](https://github.com/pytroll/satpy/issues/521))
* [PR 538](https://github.com/pytroll/satpy/pull/538) - Support CLASS packed viirs files in viirs_sdr reader

#### Documentation changes

* [PR 659](https://github.com/pytroll/satpy/pull/659) - DOC: Refer to PyTroll coding guidelines
* [PR 653](https://github.com/pytroll/satpy/pull/653) - DOC: Fix small typos in documentation
* [PR 651](https://github.com/pytroll/satpy/pull/651) - Rename changelog for releases before 0.9.0
* [PR 621](https://github.com/pytroll/satpy/pull/621) - Add FAQ items on number of workers and threads ([620](https://github.com/pytroll/satpy/issues/620))

In this release 24 pull requests were closed.


## Version 0.12.0 (2019/02/15)

### Issues Closed

* [Issue 601](https://github.com/pytroll/satpy/issues/601) - MultiScene 'save_animation' fails if "datasets=" isn't provided ([PR 602](https://github.com/pytroll/satpy/pull/602))
* [Issue 310](https://github.com/pytroll/satpy/issues/310) - Create MultiScene from list of files ([PR 576](https://github.com/pytroll/satpy/pull/576))

In this release 2 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 616](https://github.com/pytroll/satpy/pull/616) - Fix geotiff writer being unimportable if gdal isn't installed
* [PR 615](https://github.com/pytroll/satpy/pull/615) - Fix confusing error in abi_l1b reader when file fails to open
* [PR 607](https://github.com/pytroll/satpy/pull/607) - Fix VIIRS 'histogram_dnb' compositor not returning new data
* [PR 605](https://github.com/pytroll/satpy/pull/605) - Fix enhancements using dask delayed on internal functions
* [PR 602](https://github.com/pytroll/satpy/pull/602) - Fix MultiScene save_animation not using dataset IDs correctly ([601](https://github.com/pytroll/satpy/issues/601), [601](https://github.com/pytroll/satpy/issues/601))
* [PR 600](https://github.com/pytroll/satpy/pull/600) - Fix resample reduce_data bug introduced in #582

#### Features added

* [PR 614](https://github.com/pytroll/satpy/pull/614) - Support for reduced resolution OLCI data
* [PR 613](https://github.com/pytroll/satpy/pull/613) - Add 'crop' and 'save_datasets' to MultiScene
* [PR 609](https://github.com/pytroll/satpy/pull/609) - Add ability to use dask distributed when generating animation videos
* [PR 582](https://github.com/pytroll/satpy/pull/582) - Add 'reduce_data' keyword argument to disable cropping before resampling
* [PR 576](https://github.com/pytroll/satpy/pull/576) - Add group_files and from_files utility functions for creating Scenes from multiple files ([310](https://github.com/pytroll/satpy/issues/310))
* [PR 567](https://github.com/pytroll/satpy/pull/567) - Add utility functions for generating GeoViews plots ([541](https://github.com/pytroll/satpy/issues/541))

In this release 12 pull requests were closed.


## Version 0.11.2 (2019/01/28)

### Issues Closed

* [Issue 584](https://github.com/pytroll/satpy/issues/584) - DayNightCompositor does not work with eg overview_sun as the day part ([PR 593](https://github.com/pytroll/satpy/pull/593))
* [Issue 577](https://github.com/pytroll/satpy/issues/577) - Creation of composites using `sunz_corrected` modifier fails with VIIRS SDR data
* [Issue 569](https://github.com/pytroll/satpy/issues/569) - Can not show or save ABI true color image (RuntimeWarning: invalid value encountered in log)
* [Issue 531](https://github.com/pytroll/satpy/issues/531) - Mask space pixels in AHI HSD reader ([PR 592](https://github.com/pytroll/satpy/pull/592))
* [Issue 106](https://github.com/pytroll/satpy/issues/106) - Warnings

In this release 5 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 594](https://github.com/pytroll/satpy/pull/594) - Fix VIIRS L1B reader not using standard 'y' and 'x' dimension names
* [PR 593](https://github.com/pytroll/satpy/pull/593) - Fix sunz_corrected modifier adding unnecessary x and y coordinates ([587](https://github.com/pytroll/satpy/issues/587), [584](https://github.com/pytroll/satpy/issues/584))
* [PR 592](https://github.com/pytroll/satpy/pull/592) - Fix masking of AHI HSD space pixels ([531](https://github.com/pytroll/satpy/issues/531))
* [PR 589](https://github.com/pytroll/satpy/pull/589) - Fix dask not importing sharedict automatically in dask 1.1+
* [PR 588](https://github.com/pytroll/satpy/pull/588) - Fix start_time type in seviri_l1b_nc reader
* [PR 585](https://github.com/pytroll/satpy/pull/585) - Fix geotiff writer not using fill_value from writer YAML config
* [PR 572](https://github.com/pytroll/satpy/pull/572) - Fix VIIRS SDR masking and distracting colors in composites
* [PR 570](https://github.com/pytroll/satpy/pull/570) - Fix CF epoch for xarray compat
* [PR 563](https://github.com/pytroll/satpy/pull/563) - Fix StopIteration and python 3.7 compatibility issue in MultiScene
* [PR 554](https://github.com/pytroll/satpy/pull/554) - Fix AreaDefinition usage to work with newer versions of pyresample

#### Features added

* [PR 561](https://github.com/pytroll/satpy/pull/561) - Add AHI HRIT B07 files for high resolution night data

#### Documentation changes

* [PR 590](https://github.com/pytroll/satpy/pull/590) - Add FAQ page to docs
* [PR 575](https://github.com/pytroll/satpy/pull/575) - Add page for data download resources
* [PR 574](https://github.com/pytroll/satpy/pull/574) - Add code of conduct

In this release 14 pull requests were closed.


## Version 0.11.1 (2018/12/27)

### Pull Requests Merged

#### Bugs fixed

* [PR 560](https://github.com/pytroll/satpy/pull/560) - Fix available_composite_ids including inline comp dependencies

In this release 1 pull request was closed.


## Version 0.11.0 (2018/12/21)

### Issues Closed

* [Issue 555](https://github.com/pytroll/satpy/issues/555) - GOES-16 geolocation seems off when saving as TIFF
* [Issue 552](https://github.com/pytroll/satpy/issues/552) - GOES Composites failling ([PR 553](https://github.com/pytroll/satpy/pull/553))
* [Issue 534](https://github.com/pytroll/satpy/issues/534) - Support GOES-15 in netcdf format from Eumetcast (`nc_goes` reader) ([PR 530](https://github.com/pytroll/satpy/pull/530))
* [Issue 527](https://github.com/pytroll/satpy/issues/527) - [SEP] Reader naming conventions ([PR 546](https://github.com/pytroll/satpy/pull/546))
* [Issue 518](https://github.com/pytroll/satpy/issues/518) - Make bilinear interpolation dask/xarray friendly ([PR 519](https://github.com/pytroll/satpy/pull/519))
* [Issue 467](https://github.com/pytroll/satpy/issues/467) - Flake8-ify all of satpy ([PR 515](https://github.com/pytroll/satpy/pull/515))
* [Issue 459](https://github.com/pytroll/satpy/issues/459) - How to colorize images
* [Issue 449](https://github.com/pytroll/satpy/issues/449) - Adding coastlines to single channel not working ([PR 551](https://github.com/pytroll/satpy/pull/551))
* [Issue 337](https://github.com/pytroll/satpy/issues/337) - Plot true color by using VIIRS SDR
* [Issue 333](https://github.com/pytroll/satpy/issues/333) - `available_readers` to detail unavailable items
* [Issue 263](https://github.com/pytroll/satpy/issues/263) - How to get the available dataset names from the reader
* [Issue 147](https://github.com/pytroll/satpy/issues/147) - SEVIRI HRIT reading: More userfriendly warning when no EPI/PRO files are present ([PR 452](https://github.com/pytroll/satpy/pull/452))

In this release 12 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 556](https://github.com/pytroll/satpy/pull/556) - Fix turning off enhancements in writers for float data
* [PR 553](https://github.com/pytroll/satpy/pull/553) - Fix DifferenceCompositor and other compositors when areas are incompatible ([552](https://github.com/pytroll/satpy/issues/552), [552](https://github.com/pytroll/satpy/issues/552))
* [PR 550](https://github.com/pytroll/satpy/pull/550) - Fix AHI HRIT file patterns so area's ID is correct
* [PR 548](https://github.com/pytroll/satpy/pull/548) - Fix ratio sharpening compositors when the ratio is negative
* [PR 547](https://github.com/pytroll/satpy/pull/547) - Fix EWA resampling for new versions of pyresample
* [PR 542](https://github.com/pytroll/satpy/pull/542) - Fix palette application for pps 2018 products
* [PR 508](https://github.com/pytroll/satpy/pull/508) - Fix the cf_writer to accept single-valued time coordinate variable

#### Features added

* [PR 558](https://github.com/pytroll/satpy/pull/558) - Make counts available in ahi_hsd
* [PR 551](https://github.com/pytroll/satpy/pull/551) - Fix image overlays for single band data (requires trollimage 1.6+) ([449](https://github.com/pytroll/satpy/issues/449))
* [PR 549](https://github.com/pytroll/satpy/pull/549) - Fix nwcpps ct palette from v2018 to be backwards compatible
* [PR 546](https://github.com/pytroll/satpy/pull/546) - Rename readers to meet new reader naming scheme ([527](https://github.com/pytroll/satpy/issues/527))
* [PR 545](https://github.com/pytroll/satpy/pull/545) - Add configurable parameters to solar zenith correctors
* [PR 530](https://github.com/pytroll/satpy/pull/530) - Add reader for Goes15 netcdf Eumetsat format ([534](https://github.com/pytroll/satpy/issues/534))
* [PR 519](https://github.com/pytroll/satpy/pull/519) - Add xarray/dask bilinear resampling ([518](https://github.com/pytroll/satpy/issues/518))
* [PR 507](https://github.com/pytroll/satpy/pull/507) - Change default enhancement for reflectance data to gamma 1.5
* [PR 452](https://github.com/pytroll/satpy/pull/452) - Improve handling of missing file requirements in readers ([147](https://github.com/pytroll/satpy/issues/147))

#### Documentation changes

* [PR 533](https://github.com/pytroll/satpy/pull/533) - Fix copy/paste error in readers table for viirs_l1b
* [PR 515](https://github.com/pytroll/satpy/pull/515) - Fix all flake8 errors in satpy package code ([467](https://github.com/pytroll/satpy/issues/467))

#### Backwards incompatible changes

* [PR 546](https://github.com/pytroll/satpy/pull/546) - Rename readers to meet new reader naming scheme ([527](https://github.com/pytroll/satpy/issues/527))
* [PR 507](https://github.com/pytroll/satpy/pull/507) - Change default enhancement for reflectance data to gamma 1.5

In this release 20 pull requests were closed.


## Version 0.10.0 (2018/11/23)

### Issues Closed

* [Issue 491](https://github.com/pytroll/satpy/issues/491) - Area definition of incomplete SEVIRI images
* [Issue 487](https://github.com/pytroll/satpy/issues/487) - Resampling a User Defined Scene
* [Issue 465](https://github.com/pytroll/satpy/issues/465) - Native resampler fails with 3D DataArrays ([PR 468](https://github.com/pytroll/satpy/pull/468))
* [Issue 464](https://github.com/pytroll/satpy/issues/464) - Drawing coastlines/borders with save_datasets ([PR 469](https://github.com/pytroll/satpy/pull/469))
* [Issue 453](https://github.com/pytroll/satpy/issues/453) - Review subclasses of BaseFileHander ([PR 455](https://github.com/pytroll/satpy/pull/455))
* [Issue 450](https://github.com/pytroll/satpy/issues/450) - Allow readers to accept pathlib.Path instances ([PR 451](https://github.com/pytroll/satpy/pull/451))
* [Issue 445](https://github.com/pytroll/satpy/issues/445) - Readthedocs builds are failing
* [Issue 439](https://github.com/pytroll/satpy/issues/439) - KeyError when creating true_color for ABI 
* [Issue 417](https://github.com/pytroll/satpy/issues/417) - Add custom string formatter for lower/upper support
* [Issue 414](https://github.com/pytroll/satpy/issues/414) - Inconsistent units of geostationary radiances ([PR 490](https://github.com/pytroll/satpy/pull/490))
* [Issue 405](https://github.com/pytroll/satpy/issues/405) - Angle interpolation for MODIS data missing ([PR 430](https://github.com/pytroll/satpy/pull/430))
* [Issue 397](https://github.com/pytroll/satpy/issues/397) - Add README to setup.py description ([PR 443](https://github.com/pytroll/satpy/pull/443))
* [Issue 369](https://github.com/pytroll/satpy/issues/369) - Mitiff writer is broken ([PR 480](https://github.com/pytroll/satpy/pull/480))

In this release 13 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 510](https://github.com/pytroll/satpy/pull/510) - Make sure a discrete data type is preserved through resampling
* [PR 506](https://github.com/pytroll/satpy/pull/506) - Remove dependency on nc_nwcsaf_msg
* [PR 504](https://github.com/pytroll/satpy/pull/504) - Change unnecessary warning messages to debug
* [PR 496](https://github.com/pytroll/satpy/pull/496) - Add more descriptive names to AHI readers AreaDefinition names
* [PR 492](https://github.com/pytroll/satpy/pull/492) - Fix thinned modis reading in 'hdfeos_l1b' reader
* [PR 480](https://github.com/pytroll/satpy/pull/480) - Fix 'mitiff' writer to use 'base_dir' properly ([369](https://github.com/pytroll/satpy/issues/369))
* [PR 476](https://github.com/pytroll/satpy/pull/476) - Fix handling of navigation in a grib file with lons greater than 180
* [PR 473](https://github.com/pytroll/satpy/pull/473) - Change combine_metadata to average any 'time' fields
* [PR 471](https://github.com/pytroll/satpy/pull/471) - Fix offset between VIS+IR and HRV navigation for hrit seviri
* [PR 469](https://github.com/pytroll/satpy/pull/469) - Fix attributes not being preserved when adding overlays or decorations ([464](https://github.com/pytroll/satpy/issues/464))
* [PR 468](https://github.com/pytroll/satpy/pull/468) - Fix native resampling when RGBs are resampled ([465](https://github.com/pytroll/satpy/issues/465))
* [PR 458](https://github.com/pytroll/satpy/pull/458) - Fix the slstr reader for consistency and tir view
* [PR 456](https://github.com/pytroll/satpy/pull/456) - Fix SCMI writer not writing fill values properly
* [PR 448](https://github.com/pytroll/satpy/pull/448) - Fix saving a dataset with a prerequisites attrs to netcdf
* [PR 447](https://github.com/pytroll/satpy/pull/447) - Fix masking in DayNightCompositor when composites have partial missing data
* [PR 446](https://github.com/pytroll/satpy/pull/446) - Fix nc_nwcsaf_msg reader's handling of projection units

#### Features added

* [PR 503](https://github.com/pytroll/satpy/pull/503) - Add two luminance sharpening compositors
* [PR 498](https://github.com/pytroll/satpy/pull/498) - Make it possible to configure in-line composites
* [PR 488](https://github.com/pytroll/satpy/pull/488) - Add the check_satpy function to find missing dependencies
* [PR 481](https://github.com/pytroll/satpy/pull/481) - Refactor SCMI writer to be dask friendly
* [PR 478](https://github.com/pytroll/satpy/pull/478) - Allow writers to create output directories if they don't exist
* [PR 477](https://github.com/pytroll/satpy/pull/477) - Add additional metadata to ABI L1B DataArrays
* [PR 474](https://github.com/pytroll/satpy/pull/474) - Improve handling of dependency loading when reader has multiple matches
* [PR 463](https://github.com/pytroll/satpy/pull/463) - MSG Level1.5 NetCDF Reader (code and yaml file) for VIS/IR Channels
* [PR 455](https://github.com/pytroll/satpy/pull/455) - Ensure file handlers all use filenames as strings ([453](https://github.com/pytroll/satpy/issues/453))
* [PR 451](https://github.com/pytroll/satpy/pull/451) - Allow readers to accept pathlib.Path instances as filenames. ([450](https://github.com/pytroll/satpy/issues/450))
* [PR 442](https://github.com/pytroll/satpy/pull/442) - Replace areas.def with areas.yaml
* [PR 441](https://github.com/pytroll/satpy/pull/441) - Fix metop reader
* [PR 438](https://github.com/pytroll/satpy/pull/438) - Feature new olcil2 datasets
* [PR 436](https://github.com/pytroll/satpy/pull/436) - Allow on-the-fly decompression of xRIT files in xRIT readers
* [PR 430](https://github.com/pytroll/satpy/pull/430) - Implement fast modis lon/lat and angles interpolation ([405](https://github.com/pytroll/satpy/issues/405))

#### Documentation changes

* [PR 501](https://github.com/pytroll/satpy/pull/501) - Add DOI role and reference to Zinke DNB method
* [PR 489](https://github.com/pytroll/satpy/pull/489) - Add a first version on how to write a custom reader
* [PR 444](https://github.com/pytroll/satpy/pull/444) - Fix the readers table in the sphinx docs so it wraps text
* [PR 443](https://github.com/pytroll/satpy/pull/443) - Add long_description to setup.py ([397](https://github.com/pytroll/satpy/issues/397))
* [PR 440](https://github.com/pytroll/satpy/pull/440) - Fix CI badges in README

#### Backwards incompatible changes

* [PR 485](https://github.com/pytroll/satpy/pull/485) - Deprecate 'enhancement_config' keyword argument in favor of 'enhance'

In this release 37 pull requests were closed.


## Version 0.9.4 (2018/09/29)

### Pull Requests Merged

#### Bugs fixed

* [PR 433](https://github.com/pytroll/satpy/pull/433) - Fix native_msg readers standard_names to match other satpy readers
* [PR 432](https://github.com/pytroll/satpy/pull/432) - Fix reader config loading so it raises exception for bad reader name
* [PR 428](https://github.com/pytroll/satpy/pull/428) - Fix start_time and end_time being lists in native_msg reader
* [PR 426](https://github.com/pytroll/satpy/pull/426) - Fix hrit_jma reader not having satellite lon/lat/alt info
* [PR 423](https://github.com/pytroll/satpy/pull/423) - Fixed that save_dataset does not propagate fill_value
* [PR 421](https://github.com/pytroll/satpy/pull/421) - Fix masking and simplify avhrr_aapp_l1b reader
* [PR 413](https://github.com/pytroll/satpy/pull/413) - Fix calculating solar zenith angle in eps_l1b reader
* [PR 412](https://github.com/pytroll/satpy/pull/412) - Fix platform_name and sensor not being added by avhrr eps l1b reader

#### Features added

* [PR 415](https://github.com/pytroll/satpy/pull/415) - Add hrit_jma file patterns that don't include segments

In this release 9 pull requests were closed.


## Version 0.9.3 (2018/09/10)

### Issues Closed

* [Issue 336](https://github.com/pytroll/satpy/issues/336) - Scene crop does not compare all dataset areas ([PR 406](https://github.com/pytroll/satpy/pull/406))

In this release 1 issue was closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 409](https://github.com/pytroll/satpy/pull/409) - Fix viirs_sdr reading of aggregated files
* [PR 406](https://github.com/pytroll/satpy/pull/406) - Fix Scene crop so new areas are consistent with resolution ([336](https://github.com/pytroll/satpy/issues/336))

In this release 2 pull requests were closed.


## Version 0.9.2 (2018/08/23)

### Pull Requests Merged

#### Bugs fixed

* [PR 402](https://github.com/pytroll/satpy/pull/402) - Fix 'platform_name' metadata in ACSPO and CLAVR-x readers
* [PR 401](https://github.com/pytroll/satpy/pull/401) - Wrap solar and satellite angles in xarray in AVHRR AAPP reader

In this release 2 pull requests were closed.


## Version 0.9.1 (2018/08/19)

### Issues Closed

* [Issue 388](https://github.com/pytroll/satpy/issues/388) - SCMI Writer raises exception with lettered grids ([PR 389](https://github.com/pytroll/satpy/pull/389))
* [Issue 385](https://github.com/pytroll/satpy/issues/385) - No platform_name and sensor in dataset metadata for avhrr_aapp_l1b reader ([PR 386](https://github.com/pytroll/satpy/pull/386))
* [Issue 379](https://github.com/pytroll/satpy/issues/379) - Data is not masked when loading calibrated GOES HRIT data ([PR 380](https://github.com/pytroll/satpy/pull/380))
* [Issue 377](https://github.com/pytroll/satpy/issues/377) - Unmasked data when using DayNightCompositor ([PR 378](https://github.com/pytroll/satpy/pull/378))
* [Issue 372](https://github.com/pytroll/satpy/issues/372) - "find_files_and_readers" doesn't work on Windows ([PR 373](https://github.com/pytroll/satpy/pull/373))
* [Issue 364](https://github.com/pytroll/satpy/issues/364) - Unable to load individual channels from VIIRS_SDR data.
* [Issue 350](https://github.com/pytroll/satpy/issues/350) - Creating a Scene object with NOAA-15/18 data
* [Issue 347](https://github.com/pytroll/satpy/issues/347) - No image is shown in Jupyter notebook via scene.show()
* [Issue 345](https://github.com/pytroll/satpy/issues/345) - Future warning - xarray ([PR 352](https://github.com/pytroll/satpy/pull/352))

In this release 9 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 395](https://github.com/pytroll/satpy/pull/395) - Fix DayNightCompositor not checking inputs areas
* [PR 391](https://github.com/pytroll/satpy/pull/391) - Fix native resampler using SwathDefinition as an AreaDefinition
* [PR 387](https://github.com/pytroll/satpy/pull/387) - Fix enhancement config loading when yaml file is empty
* [PR 386](https://github.com/pytroll/satpy/pull/386) - Add platform_name and sensor in avhrr_aapp_l1b reader ([385](https://github.com/pytroll/satpy/issues/385))
* [PR 381](https://github.com/pytroll/satpy/pull/381) - Fix keyword arguments not being properly passed to writers
* [PR 362](https://github.com/pytroll/satpy/pull/362) - Replace np.ma.mean by np.nanmean for pixel aggregation
* [PR 361](https://github.com/pytroll/satpy/pull/361) - Remove Rayleigh correction from abi natural composite
* [PR 360](https://github.com/pytroll/satpy/pull/360) - Fix lookup table enhancement for multi-band datasets
* [PR 339](https://github.com/pytroll/satpy/pull/339) - fixed meteosat native georeferencing

#### Documentation changes

* [PR 359](https://github.com/pytroll/satpy/pull/359) - Add examples from pytroll-examples to documentation

In this release 10 pull requests were closed.


## Version 0.9.0 (2018/07/02)

### Issues Closed

* [Issue 344](https://github.com/pytroll/satpy/issues/344) - find_files_and_reader does not seem to care about start_time! ([PR 349](https://github.com/pytroll/satpy/pull/349))
* [Issue 338](https://github.com/pytroll/satpy/issues/338) - Creating a Scene object with Terra MODIS data
* [Issue 332](https://github.com/pytroll/satpy/issues/332) - Non-requested datasets are saved when composites fail to generate ([PR 342](https://github.com/pytroll/satpy/pull/342))

In this release 3 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 355](https://github.com/pytroll/satpy/pull/355) - Fix ABI L1B reader losing file variable attributes
* [PR 353](https://github.com/pytroll/satpy/pull/353) - Fix multiscene memory issues by adding an optional batch_size
* [PR 351](https://github.com/pytroll/satpy/pull/351) - Fix AMSR-2 L1B reader loading bytes incorrectly
* [PR 349](https://github.com/pytroll/satpy/pull/349) - Fix datetime-based file selection when filename only has a start time ([344](https://github.com/pytroll/satpy/issues/344))
* [PR 348](https://github.com/pytroll/satpy/pull/348) - Fix freezing of areas before resampling even as strings
* [PR 343](https://github.com/pytroll/satpy/pull/343) - Fix shape assertion after resampling
* [PR 342](https://github.com/pytroll/satpy/pull/342) - Fix Scene save_datasets to only save datasets from the wishlist ([332](https://github.com/pytroll/satpy/issues/332))
* [PR 341](https://github.com/pytroll/satpy/pull/341) - Fix ancillary variable loading when anc var is already loaded
* [PR 340](https://github.com/pytroll/satpy/pull/340) - Cut radiances array depending on number of scans

In this release 9 pull requests were closed.


## Version 0.9.0b0 (2018/06/26)

### Issues Closed

* [Issue 328](https://github.com/pytroll/satpy/issues/328) - hrit reader bugs ([PR 329](https://github.com/pytroll/satpy/pull/329))
* [Issue 323](https://github.com/pytroll/satpy/issues/323) - "Manual" application of corrections
* [Issue 320](https://github.com/pytroll/satpy/issues/320) - Overview of code layout
* [Issue 279](https://github.com/pytroll/satpy/issues/279) - Add 'level' to DatasetID ([PR 283](https://github.com/pytroll/satpy/pull/283))
* [Issue 272](https://github.com/pytroll/satpy/issues/272) - How to save region of interest from Band 3 Himawari Data as png image ([PR 276](https://github.com/pytroll/satpy/pull/276))
* [Issue 267](https://github.com/pytroll/satpy/issues/267) - Missing dependency causes strange error during unit tests ([PR 273](https://github.com/pytroll/satpy/pull/273))
* [Issue 244](https://github.com/pytroll/satpy/issues/244) - Fix NUCAPS reader for NUCAPS EDR v2 files ([PR 326](https://github.com/pytroll/satpy/pull/326))
* [Issue 236](https://github.com/pytroll/satpy/issues/236) - scene.resample(cache_dir=) fails with TypeError: Unicode-objects must be encoded before hashing
* [Issue 233](https://github.com/pytroll/satpy/issues/233) - IOError: Unable to read attribute (no appropriate function for conversion path)
* [Issue 211](https://github.com/pytroll/satpy/issues/211) - Fix OLCI and other readers' file patterns to work on Windows
* [Issue 207](https://github.com/pytroll/satpy/issues/207) - Method not fully documented in terms of possible key word arguments
* [Issue 199](https://github.com/pytroll/satpy/issues/199) - Reading Modis file produce a double image
* [Issue 168](https://github.com/pytroll/satpy/issues/168) - Cannot read MODIS data
* [Issue 167](https://github.com/pytroll/satpy/issues/167) - KeyError 'v' using Scene(base_dir=, reader=) ([PR 325](https://github.com/pytroll/satpy/pull/325))
* [Issue 165](https://github.com/pytroll/satpy/issues/165) - HRIT GOES reader is broken ([PR 303](https://github.com/pytroll/satpy/pull/303))
* [Issue 160](https://github.com/pytroll/satpy/issues/160) - Inconsistent naming of optional datasets in composite configs and compositors
* [Issue 157](https://github.com/pytroll/satpy/issues/157) - Add animation example ([PR 322](https://github.com/pytroll/satpy/pull/322))
* [Issue 156](https://github.com/pytroll/satpy/issues/156) - Add cartopy example
* [Issue 146](https://github.com/pytroll/satpy/issues/146) - Add default null log handler
* [Issue 123](https://github.com/pytroll/satpy/issues/123) - NetCDF writer doesn't work ([PR 307](https://github.com/pytroll/satpy/pull/307))
* [Issue 114](https://github.com/pytroll/satpy/issues/114) - Print a list of available sensors/readers
* [Issue 82](https://github.com/pytroll/satpy/issues/82) - Separate file discovery from Scene init
* [Issue 61](https://github.com/pytroll/satpy/issues/61) - Creating composites post-load
* [Issue 10](https://github.com/pytroll/satpy/issues/10) - Optimize CREFL for memory

In this release 24 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 331](https://github.com/pytroll/satpy/pull/331) - Adapt slstr reader to xarray&dask
* [PR 329](https://github.com/pytroll/satpy/pull/329) - issue#328: fixed bugs loading JMA HRIT files ([328](https://github.com/pytroll/satpy/issues/328))
* [PR 326](https://github.com/pytroll/satpy/pull/326) - Fix nucaps reader for NUCAPS EDR v2 files ([244](https://github.com/pytroll/satpy/issues/244), [244](https://github.com/pytroll/satpy/issues/244))
* [PR 325](https://github.com/pytroll/satpy/pull/325) - Fix exception when Scene is given reader and base_dir ([167](https://github.com/pytroll/satpy/issues/167))
* [PR 319](https://github.com/pytroll/satpy/pull/319) - Fix msi reader delayed
* [PR 318](https://github.com/pytroll/satpy/pull/318) - Fix nir reflectance to use XArray
* [PR 312](https://github.com/pytroll/satpy/pull/312) - Allow custom regions in ahi-hsd file patterns
* [PR 311](https://github.com/pytroll/satpy/pull/311) - Allow valid_range to be a tuple for cloud product colorization
* [PR 303](https://github.com/pytroll/satpy/pull/303) - Fix hrit goes to support python 3 ([165](https://github.com/pytroll/satpy/issues/165))
* [PR 288](https://github.com/pytroll/satpy/pull/288) - Fix hrit-goes reader
* [PR 192](https://github.com/pytroll/satpy/pull/192) - Clip day and night composites after enhancement

#### Features added

* [PR 315](https://github.com/pytroll/satpy/pull/315) - Add slicing to Scene
* [PR 314](https://github.com/pytroll/satpy/pull/314) - Feature mitiff writer
* [PR 307](https://github.com/pytroll/satpy/pull/307) - Fix projections in cf writer ([123](https://github.com/pytroll/satpy/issues/123))
* [PR 305](https://github.com/pytroll/satpy/pull/305) - Add support for geolocation and angles to msi reader
* [PR 302](https://github.com/pytroll/satpy/pull/302) - Workaround the LinearNDInterpolator thread-safety issue for Sentinel 1 SAR geolocation
* [PR 301](https://github.com/pytroll/satpy/pull/301) - Factorize header definitions between hrit_msg and native_msg. Fix a bug in header definition.
* [PR 298](https://github.com/pytroll/satpy/pull/298) - Implement sentinel 2 MSI reader
* [PR 294](https://github.com/pytroll/satpy/pull/294) - Add the ocean color product to olci
* [PR 153](https://github.com/pytroll/satpy/pull/153) - [WIP] Improve compatibility of cf_writer with CF-conventions

In this release 20 pull requests were closed.


## Version 0.9.0a2 (2018/05/14)

### Issues Closed

* [Issue 286](https://github.com/pytroll/satpy/issues/286) - Proposal: search automatically for local config-files/readers
* [Issue 278](https://github.com/pytroll/satpy/issues/278) - msg native reader fails on full disk image
* [Issue 277](https://github.com/pytroll/satpy/issues/277) - msg_native reader fails when order number has a hyphen in it ([PR 282](https://github.com/pytroll/satpy/pull/282))
* [Issue 270](https://github.com/pytroll/satpy/issues/270) - How to find the value at certain latitude and longtitude
* [Issue 269](https://github.com/pytroll/satpy/issues/269) - How to intepret the parameter values in  AreaDefinition
* [Issue 268](https://github.com/pytroll/satpy/issues/268) - How to find the appropriate values of parameters in Scene.resample() function using Himawari Data
* [Issue 241](https://github.com/pytroll/satpy/issues/241) - reader native_msg using `np.str`
* [Issue 218](https://github.com/pytroll/satpy/issues/218) - Resampling to EPSG:4326 produces unexpected results
* [Issue 189](https://github.com/pytroll/satpy/issues/189) - Error when reading MSG native format
* [Issue 62](https://github.com/pytroll/satpy/issues/62) - msg_native example
* [Issue 33](https://github.com/pytroll/satpy/issues/33) - Load metadata without loading data

In this release 11 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 290](https://github.com/pytroll/satpy/pull/290) - Fix unicode-named data loading
* [PR 285](https://github.com/pytroll/satpy/pull/285) - Fix native_msg calibration bug
* [PR 282](https://github.com/pytroll/satpy/pull/282) - Fix native_msg reader for ROI input and multi-part order file patterns ([277](https://github.com/pytroll/satpy/issues/277))
* [PR 280](https://github.com/pytroll/satpy/pull/280) - Fix CLAVR-x reader to work with xarray
* [PR 274](https://github.com/pytroll/satpy/pull/274) - Convert ahi hsd reader to dask and xarray
* [PR 265](https://github.com/pytroll/satpy/pull/265) - Bugfix msg native reader
* [PR 262](https://github.com/pytroll/satpy/pull/262) - Fix dependency tree to find the best dependency when multiple matches occur
* [PR 260](https://github.com/pytroll/satpy/pull/260) - Fix ABI L1B reader masking data improperly

#### Features added

* [PR 293](https://github.com/pytroll/satpy/pull/293) - Switch to netcdf4 as engine for nc nwcsaf reading
* [PR 292](https://github.com/pytroll/satpy/pull/292) - Use pyresample's boundary classes
* [PR 291](https://github.com/pytroll/satpy/pull/291) - Allow datasets without areas to be concatenated
* [PR 289](https://github.com/pytroll/satpy/pull/289) - Fix so UMARF files (with extention .nat) are found as well
* [PR 287](https://github.com/pytroll/satpy/pull/287) - Add production configuration for NWCSAF RDT, ASII products by Marco Sassi
* [PR 283](https://github.com/pytroll/satpy/pull/283) - Add GRIB Reader ([279](https://github.com/pytroll/satpy/issues/279))
* [PR 281](https://github.com/pytroll/satpy/pull/281) - Port the maia reader to dask/xarray
* [PR 276](https://github.com/pytroll/satpy/pull/276) - Support reducing data for geos areas ([272](https://github.com/pytroll/satpy/issues/272))
* [PR 273](https://github.com/pytroll/satpy/pull/273) - Msg readers cleanup ([267](https://github.com/pytroll/satpy/issues/267))
* [PR 271](https://github.com/pytroll/satpy/pull/271) - Add appveyor and use ci-helpers for CI environments
* [PR 264](https://github.com/pytroll/satpy/pull/264) - Add caching at the scene level, and handle saving/loading from disk
* [PR 262](https://github.com/pytroll/satpy/pull/262) - Fix dependency tree to find the best dependency when multiple matches occur

In this release 20 pull requests were closed.


## Version 0.9.0a1 (2018/04/22)

### Issues Closed

* [Issue 227](https://github.com/pytroll/satpy/issues/227) - Issue Reading MSG4
* [Issue 225](https://github.com/pytroll/satpy/issues/225) - Save Datasets using SCMI ([PR 228](https://github.com/pytroll/satpy/pull/228))
* [Issue 215](https://github.com/pytroll/satpy/issues/215) - Change `Scene.compute` to something else ([PR 220](https://github.com/pytroll/satpy/pull/220))
* [Issue 208](https://github.com/pytroll/satpy/issues/208) - Strange behaviour when trying to load data to a scene object after having worked with it ([PR 214](https://github.com/pytroll/satpy/pull/214))
* [Issue 200](https://github.com/pytroll/satpy/issues/200) - Different mask handling when saving to PNG or GeoTIFF ([PR 201](https://github.com/pytroll/satpy/pull/201))
* [Issue 176](https://github.com/pytroll/satpy/issues/176) - Loading viirs natural_color composite fails ([PR 177](https://github.com/pytroll/satpy/pull/177))

In this release 6 issues were closed.

### Pull Requests Merged

#### Bugs fixed

* [PR 259](https://github.com/pytroll/satpy/pull/259) - Fix writer and refactor so bad writer name raises logical exception
* [PR 257](https://github.com/pytroll/satpy/pull/257) - Fix geotiff and png writers to save to a temporary directory
* [PR 256](https://github.com/pytroll/satpy/pull/256) - Add 'python_requires' to setup.py to specify python support
* [PR 253](https://github.com/pytroll/satpy/pull/253) - Fix ABI L1B reader to use 64-bit scaling factors for X/Y variables
* [PR 250](https://github.com/pytroll/satpy/pull/250) - Fix floating point geotiff saving in dask geotiff writer
* [PR 249](https://github.com/pytroll/satpy/pull/249) - Fix float geotiff saving on 0.8
* [PR 248](https://github.com/pytroll/satpy/pull/248) - Fix unloading composite deps when one of them has incompatible areas
* [PR 243](https://github.com/pytroll/satpy/pull/243) - Remove ABI composite reducerX modifiers

#### Features added

* [PR 252](https://github.com/pytroll/satpy/pull/252) - Use rasterio to save geotiffs when available
* [PR 239](https://github.com/pytroll/satpy/pull/239) - Add CSPP Geo (geocat) AHI reading support

In this release 10 pull requests were closed.


## Version 0.9.0a0 (2018-03-20)

#### Bugs fixed

* [Issue 179](https://github.com/pytroll/satpy/issues/179) - Cannot read AVHRR in AAPP format
* [PR 234](https://github.com/pytroll/satpy/pull/234) - Bugfix sar reader
* [PR 231](https://github.com/pytroll/satpy/pull/231) - Bugfix palette based compositor concatenation
* [PR 230](https://github.com/pytroll/satpy/pull/230) - Fix dask angle calculations of rayleigh corrector
* [PR 229](https://github.com/pytroll/satpy/pull/229) - Fix bug in dep tree when modifier deps are modified wavelengths
* [PR 228](https://github.com/pytroll/satpy/pull/228) - Fix 'platform' being used instead of 'platform_name'
* [PR 224](https://github.com/pytroll/satpy/pull/224) - Add helper method for checking areas in compositors
* [PR 222](https://github.com/pytroll/satpy/pull/222) - Fix resampler caching by source area
* [PR 221](https://github.com/pytroll/satpy/pull/221) - Fix Scene loading and resampling when generate=False
* [PR 220](https://github.com/pytroll/satpy/pull/220) - Rename Scene's `compute` to `generate_composites`
* [PR 219](https://github.com/pytroll/satpy/pull/219) - Fixed native_msg calibration problem and added env var to change the …
* [PR 214](https://github.com/pytroll/satpy/pull/214) - Fix Scene not being copied properly during resampling
* [PR 210](https://github.com/pytroll/satpy/pull/210) - Bugfix check if lons and lats should be masked before resampling
* [PR 206](https://github.com/pytroll/satpy/pull/206) - Fix optional dependencies not being passed to modifiers with opts only
* [PR 187](https://github.com/pytroll/satpy/pull/187) - Fix reader configs having mismatched names between filename and config
* [PR 185](https://github.com/pytroll/satpy/pull/185) - Bugfix nwcsaf_pps reader for file discoverability
* [PR 177](https://github.com/pytroll/satpy/pull/177) - Bugfix viirs loading - picked from (xarray)develop branch
* [PR 163](https://github.com/pytroll/satpy/pull/163) - Bugfix float geotiff

#### Features added

* [PR 232](https://github.com/pytroll/satpy/pull/232) - Add ABI L1B system tests
* [PR 226](https://github.com/pytroll/satpy/pull/226) - EARS NWCSAF products reading
* [PR 217](https://github.com/pytroll/satpy/pull/217) - Add xarray/dask support to DayNightCompositor
* [PR 216](https://github.com/pytroll/satpy/pull/216) - Fix dataset writing so computations are shared between tasks
* [PR 213](https://github.com/pytroll/satpy/pull/213) - [WIP] Reuse same resampler for similar datasets
* [PR 212](https://github.com/pytroll/satpy/pull/212) - Improve modis reader to support dask
* [PR 209](https://github.com/pytroll/satpy/pull/209) - Fix enhancements to work with xarray
* [PR 205](https://github.com/pytroll/satpy/pull/205) - Fix ABI 'natural' and 'true_color' composites to work with xarray
* [PR 204](https://github.com/pytroll/satpy/pull/204) - Add 'native' resampler
* [PR 203](https://github.com/pytroll/satpy/pull/203) - [WIP] Feature trollimage xarray
* [PR 195](https://github.com/pytroll/satpy/pull/195) - Add ABI-specific configs for Airmass composite
* [PR 186](https://github.com/pytroll/satpy/pull/186) - Add missing nodata tiff tag
* [PR 180](https://github.com/pytroll/satpy/pull/180) - Replace BW and RGBCompositor with a more generic one

#### Documentation changes

* [PR 155](https://github.com/pytroll/satpy/pull/155) - Add contributing and developers guide documentation

In this release 1 issue and 31 pull requests were closed.
