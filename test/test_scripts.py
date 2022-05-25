import os
import unittest
import shutil
import pandas as pd

from mock import patch


class TestScripts(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_env={'DATA_PATH':'tmp_data', 'DESTINATION_NAME': 'tmp_destination'}
        return super().setUp()

    def test_unpack_downloaded_data(self):
        with patch.dict(os.environ, self.mock_env):
            from scripts.unpack_downloaded_data import unpack_downloaded_data
            
            data_path=self.mock_env['DATA_PATH']
            repo_with_files=data_path+'/timestamp1'
            destination_path= data_path+'/'+ self.mock_env['DESTINATION_NAME']

            create_tmp_data(data_path,repo_with_files, destination_path)
            unpack_downloaded_data(['timestamp1'])

            files_in_dest_repo = [f for f in os.listdir(destination_path) if '.csv' in f]
            self.assertEqual(len(files_in_dest_repo), 1)
            self.assertEqual(files_in_dest_repo[0], 'tmp1_timestamp1.csv')

            repos_in_data = [f.split('.csv')[0] for f in os.listdir(data_path) if '.csv' in f]
            self.assertTrue('timestamp1' not in repos_in_data)

            destroy_tmp_data(data_path)

def create_tmp_data(data_path,repo_with_files, destination_path):
    # Create data repo
    os.mkdir(data_path)

    # Create repo with .csv
    os.mkdir(repo_with_files)        
    df = pd.DataFrame(columns=['A','B'])
    df.to_csv(path_or_buf=repo_with_files+'/tmp1.csv', index=False)

    # Create destination repo
    os.mkdir(destination_path)

def destroy_tmp_data(data_path):
    shutil.rmtree(data_path)