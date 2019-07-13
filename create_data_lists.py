from utils import create_data_lists
from config import pascal_abspath
import os
if __name__ == '__main__':
    create_data_lists(voc07_path= os.path.join(pascal_abspath, 'VOC2007'),
                      voc12_path= os.path.join(pascal_abspath, 'VOC2012'),
                      output_folder='./')
