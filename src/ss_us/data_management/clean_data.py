"""Function(s) for cleaning the data set(s)."""

import pandas as pd
import numpy as np


def clean_data(data):
    data = data[data['hhrel2']=="Householder"]
    data = data[(data['age'] >= 20) & (data['age'] <= 64)]
    data['hrs'] = data['uhours'] * data['weeks']
    data = data[data['hrs'] >= 260]
    data['rincp_wag'].replace({np.nan: 0}, inplace=True)
    data['rincp_se'].replace({np.nan: 0}, inplace=True)
    data['hh_earnings'] = data['rincp_wag'] + data['rincp_se']
    data = data[data['hh_earnings'] > 0]
    data = data[data['weeks'] != 0]

    data['col'] = data['educ'].apply(lambda x: 1 if x in ['Some college','College', 'Advanced'] else 0)

    data['hourly_wage'] = data['hh_earnings'] / data['hrs']

    data = data[['hourly_wage', 'hhwgt', 'age', 'col']]

    data['lwage'] = np.log(data['hourly_wage'])
    data['age2'] = data['age'].apply(lambda x: x**2)
    return data
print('Data cleaned')
