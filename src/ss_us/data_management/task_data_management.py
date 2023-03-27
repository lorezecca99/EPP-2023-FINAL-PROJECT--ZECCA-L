"""Tasks for managing the data."""

import pandas as pd
import pytask

from ss_us.config import BLD, SRC
from ss_us.data_management.clean_data import clean_data
from ss_us.utilities import read_yaml


@pytask.mark.depends_on(
    {
        "scripts": ["clean_data.py"],
        "data_info": SRC / "data_management" / "data_info.yaml",
        "data": SRC / "data"/ "dataset.csv"
    },
)
@pytask.mark.produces(BLD / "python" / "data"/"cleaned_data.csv")
def task_clean_data_python(depends_on,produces):
    """Clean the data (Python version)."""
    #data_info = read_yaml(depends_on["data_info"])
    data = pd.read_csv(depends_on["data"])
    data = clean_data(data)
    data.to_csv(produces)


#"data_info": SRC / "data_management" / "data_info.yaml"