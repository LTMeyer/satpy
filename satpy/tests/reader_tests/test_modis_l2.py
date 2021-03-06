#!/usr/bin/python
# Copyright (c) 2019.
#
#
# Author(s):
#   Lucas Meyer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""Unit tests for MODIS L2 HDF reader."""

import os
import unittest

import numpy as np

from pyhdf.SD import SD, SDC

from satpy import available_readers, Scene

# Mock MODIS HDF4 file
SCAN_WIDTH = 406
SCAN_LEN = 270
SCALE_FACTOR = 1
TEST_DATA = {
    'Latitude': {'data': np.zeros((SCAN_WIDTH, SCAN_LEN), dtype=np.float32),
                 'type': SDC.FLOAT32,
                 'fill_value': -999,
                 'attrs': {'dim_labels': ['Cell_Along_Swath_5km:mod35', 'Cell_Across_Swath_5km:mod35']}},
    'Longitude': {'data': np.zeros((SCAN_WIDTH, SCAN_LEN), dtype=np.float32),
                  'type': SDC.FLOAT32,
                  'fill_value': -999,
                  'attrs': {'dim_labels': ['Cell_Along_Swath_5km:mod35', 'Cell_Across_Swath_5km:mod35']}},
    'Sensor_Zenith': {'data': np.zeros((SCAN_WIDTH, SCAN_LEN), dtype=np.int16),
                      'type': SDC.INT32,
                      'fill_value': -32767,
                      'attrs': {'dim_labels': ['Cell_Along_Swath_5km:mod35', 'Cell_Across_Swath_5km:mod35']}},
    'Cloud_Mask': {'data': np.zeros((6, 5*SCAN_WIDTH, 5*SCAN_LEN+4), dtype=np.int8),
                   'type': SDC.INT8,
                   'fill_value': 0,
                   'attrs': {'dim_labels': ['Byte_Segment:mod35',
                                            'Cell_Along_Swath_1km:mod35',
                                            'Cell_Across_Swath_1km:mod35']}},
    'Quality_Assurance': {'data': np.ones((5*SCAN_WIDTH, 5*SCAN_LEN+4, 10), dtype=np.int8),
                          'type': SDC.INT8,
                          'fill_value': 0,
                          'attrs': {'dim_labels': ['Cell_Along_Swath_1km:mod35',
                                                   'Cell_Across_Swath_1km:mod35',
                                                   'QA_Dimension:mod35']}}
}


def generate_file_name():
    """Generate a file name that follows MODIS 35 L2 convention in a temporary directory."""
    import tempfile
    from datetime import datetime

    creation_time = datetime.now()
    processing_time = datetime.now()
    file_name = 'MOD35_L2.A{}.{}.061.{}.hdf'.format(
        creation_time.strftime("%Y%j"),
        creation_time.strftime("%H%M"),
        processing_time.strftime("%Y%j%H%M%S")
    )

    base_dir = tempfile.mkdtemp()
    file_name = os.path.join(base_dir, file_name)
    return base_dir, file_name


def create_test_data():
    """Create a fake MODIS 35 L2 HDF4 file with headers."""
    from datetime import datetime, timedelta

    base_dir, file_name = generate_file_name()
    h = SD(file_name, SDC.WRITE | SDC.CREATE)
    # Set hdf file attributes
    beginning_date = datetime.now()
    ending_date = beginning_date + timedelta(minutes=5)
    core_metadata_header = "GROUP = INVENTORYMETADATA\nGROUPTYPE = MASTERGROUP\n\n" \
                           "GROUP = RANGEDATETIME\n\nOBJECT = RANGEBEGINNINGDATE\nNUM_VAL = 1\nVALUE = \"{}\"\n" \
                           "END_OBJECT = RANGEBEGINNINGDATE\n\nOBJECT = RANGEBEGINNINGTIME\n"\
                           "NUM_VAL = 1\nVALUE = \"{}\"\n"\
                           "END_OBJECT = RANGEBEGINNINGTIME\n\nOBJECT = RANGEENDINGDATE\nNUM_VAL = 1\nVALUE = \"{}\"\n"\
                           "END_OBJECT = RANGEENDINGDATE\n\nOBJECT = RANGEENDINGTIME\nNUM_VAL = 1\nVALUE = \"{}\"\n" \
                           "END_OBJECT = RANGEENDINGTIME\nEND_GROUP = RANGEDATETIME".format(
                               beginning_date.strftime("%Y-%m-%d"),
                               beginning_date.strftime("%H:%M:%S.%f"),
                               ending_date.strftime("%Y-%m-%d"),
                               ending_date.strftime("%H:%M:%S.%f")
                           )
    struct_metadata_header = "GROUP=SwathStructure\n"\
                             "GROUP=SWATH_1\n"\
                             "GROUP=DimensionMap\n"\
                             "OBJECT=DimensionMap_2\n"\
                             "GeoDimension=\"Cell_Along_Swath_5km\"\n"\
                             "END_OBJECT=DimensionMap_2\n"\
                             "END_GROUP=DimensionMap\n"\
                             "END_GROUP=SWATH_1\n"\
                             "END_GROUP=SwathStructure\nEND"
    archive_metadata_header = "GROUP = ARCHIVEDMETADATA\nEND_GROUP = ARCHIVEDMETADATA\nEND"
    setattr(h, 'CoreMetadata.0', core_metadata_header)
    setattr(h, 'StructMetadata.0', struct_metadata_header)
    setattr(h, 'ArchiveMetadata.0', archive_metadata_header)

    # Fill datasets
    for dataset in TEST_DATA:
        v = h.create(dataset, TEST_DATA[dataset]['type'], TEST_DATA[dataset]['data'].shape)
        v[:] = TEST_DATA[dataset]['data']
        dim_count = 0
        for dimension_name in TEST_DATA[dataset]['attrs']['dim_labels']:
            v.dim(dim_count).setname(dimension_name)
            dim_count += 1
        v.setfillvalue(TEST_DATA[dataset]['fill_value'])
        v.scale_factor = SCALE_FACTOR
    h.end()
    return base_dir, file_name


class TestModisL2(unittest.TestCase):
    """Test MODIS L2 reader."""

    def setUp(self):
        """Create fake HDF4 MODIS file."""
        self.base_dir, self.file_name = create_test_data()

    def tearDown(self):
        """Remove the temporary directory created for the test."""
        try:
            import shutil
            shutil.rmtree(self.base_dir, ignore_errors=True)
        except OSError:
            pass

    def test_available_reader(self):
        """Test that MODIS L2 reader is available."""
        self.assertIn('modis_l2', available_readers())

    def test_scene_available_datasets(self):
        """Test that datasets are available."""
        scene = Scene(reader='modis_l2', filenames=[self.file_name])
        available_datasets = scene.all_dataset_names()
        self.assertTrue(len(available_datasets) > 0)
        self.assertIn('cloud_mask', available_datasets)
        self.assertIn('latitude', available_datasets)
        self.assertIn('longitude', available_datasets)

    def test_load_longitude_latitude(self):
        """Test that longitude and latitude datasets are loaded correctly."""
        from satpy import DatasetID
        scene = Scene(reader='modis_l2', filenames=[self.file_name])
        for dataset_name in ['longitude', 'latitude']:
            # Default resolution should be the interpolated 1km
            scene.load([dataset_name])
            longitude_1km_id = DatasetID(name=dataset_name, resolution=1000)
            longitude_1km = scene[longitude_1km_id]
            self.assertEqual(longitude_1km.shape, (5*SCAN_WIDTH, 5*SCAN_LEN+4))
            # Specify original 5km scale
            longitude_5km = scene.load([dataset_name], resolution=5000)
            longitude_5km_id = DatasetID(name=dataset_name, resolution=5000)
            longitude_5km = scene[longitude_5km_id]
            self.assertEqual(longitude_5km.shape, TEST_DATA[dataset_name.capitalize()]['data'].shape)

    def test_load_quality_assurance(self):
        from satpy import DatasetID
        scene = Scene(reader='modis_l2', filenames=[self.file_name])
        dataset_name = 'quality_assurance'
        scene.load([dataset_name])
        quality_assurance_id = DatasetID(name=dataset_name, resolution=1000)
        self.assertIn(quality_assurance_id, scene.datasets)
        quality_assurance = scene[quality_assurance_id]
        self.assertEqual(quality_assurance.shape, (5*SCAN_WIDTH, 5*SCAN_LEN+4))

    def test_load_1000m_cloud_mask_dataset(self):
        from satpy import DatasetID
        scene = Scene(reader='modis_l2', filenames=[self.file_name])
        dataset_name = 'cloud_mask'
        scene.load([dataset_name], resolution=1000)
        cloud_mask_id = DatasetID(name=dataset_name, resolution=1000)
        self.assertIn(cloud_mask_id, scene.datasets)
        cloud_mask = scene[cloud_mask_id]
        self.assertEqual(cloud_mask.shape, (5*SCAN_WIDTH, 5*SCAN_LEN+4))

    def test_load_250m_cloud_mask_dataset(self):
        from satpy import DatasetID
        scene = Scene(reader='modis_l2', filenames=[self.file_name])
        dataset_name = 'cloud_mask'
        scene.load([dataset_name], resolution=250)
        cloud_mask_id = DatasetID(name=dataset_name, resolution=250)
        self.assertIn(cloud_mask_id, scene.datasets)
        cloud_mask = scene[cloud_mask_id]
        self.assertEqual(cloud_mask.shape, (4*5*SCAN_WIDTH, 4*(5*SCAN_LEN+4)))


def suite():
    """The test suite for test_modis_l2."""
    loader = unittest.TestLoader()
    mysuite = unittest.TestSuite()
    mysuite.addTest(loader.loadTestsFromTestCase(TestModisL2))
    return mysuite


if __name__ == '__main__':
    unittest.main()
