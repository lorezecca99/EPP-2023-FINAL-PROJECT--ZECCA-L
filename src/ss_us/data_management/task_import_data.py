import pandas as pd
import pytask


from ss_us.config import SRC
from ss_us.data_management.import_data import import_dataset
#from ss_us.utilities import read_yaml


@pytask.mark.produces(SRC / "data"/"dataset_14_18.csv")
def task_import_dataset(produces):
    """Clean the data (Python version).
    This task allows to import the merged datasets from 2014 to 2018 
    concering wages and hours worked in the US """
    #data_info = read_yaml(depends_on["data_info"])
    url = 'https://www.dropbox.com/s/a0re73x92nl8ama/dataset_14_18.csv?dl=1'
    #url18='https://www.dropbox.com/s/3u4nzej8r1tsi78/dataset_18.csv?dl=1'
    dataset=import_dataset(url)
    #dataset18=import_dataset(url18)
    dataset.to_csv(produces)
    #dataset18.to_csv(produces,SRC / "data"/"dataset_18.csv")
    #return produces