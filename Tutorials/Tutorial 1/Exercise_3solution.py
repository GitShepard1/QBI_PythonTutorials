"""
@title:     Exercise 1.3
@author:    Alan Ho
@
"""

import os
import numpy as np
from os.path import join
from scipy import stats

def clean_data(file, filedir, error_phrase='ERROR'):
    f = open(join(filedir, file), 'r')
    data = []
    for line in f.readlines():
        data.append(line)

    f.close()

    data = [float(row) for row in data if row != error_phrase]

    return np.mean(data)


####### RUNNING THE SCRIPT #################
if __name__ == '__main__':

    inputdir = raw_input('Choose file directory: ')
    error_phrase = raw_input('Choose error phrase: ')
    files = os.listdir(inputdir)
    mutate_files = [f for f in files if 'MUTATE' in f]
    wt_files = [f for f in files if 'WT' in f]

    complete_data = \
        {
            'WT': [clean_data(f, filedir = inputdir, error_phrase=error_phrase) for f in wt_files],
            'MUTATE': [clean_data(f, filedir=inputdir, error_phrase=error_phrase) for f in mutate_files]
        }

    ttest_result = stats.ttest_ind(complete_data['WT'], complete_data['MUTATE'])

    print('RUNNING ANALYSIS FOR {}'.format(inputdir))
    print('Filtering out error == {}\n'.format(error_phrase))
    print('Results\n')
    print('WT:     mean {} \n'.format(np.mean(complete_data['WT'])))
    print('        SD   {} \n'.format(np.std(complete_data['WT'])))

    print('MUTATE: mean {} \n'.format(np.mean(complete_data['MUTATE'])))
    print('        SD   {} \n'.format(np.std(complete_data['MUTATE'])))

    print(ttest_result)
