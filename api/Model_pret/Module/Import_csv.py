import os
import gdown
import shutil
import pandas as pd

def import_csv(output_folder='../Dataset/', file_name='SBAnational.csv'):
    output_path = os.path.join(output_folder, file_name)
    if not os.path.isfile(output_path):
        drive_url = 'https://drive.google.com/uc?id=1vdNaWcJgMzUnlaDVA4FuZRFYinO8UsPQ'
        gdown.download(drive_url, output_path, quiet=False)
    return output_path
