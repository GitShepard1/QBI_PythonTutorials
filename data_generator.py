
"""
Tutorial 1 Exercise

"""

import random
import datetime
import argparse
import sys
import os
from os.path import basename, exists, dirname

def exercise3(expt, numdays, error):

    def generate_data():
        data = []
        for x in range(1000):
            data.append(float("%0.3f"%random.random()))

        add_error = random.randint(0, 10)
        if add_error > 0:
            for e in range(1,add_error):
                error_loc = random.randint(0, len(data)-1)
                data[error_loc] = error

        return data

    base = datetime.datetime(2017, 07, 5, 13, 26, 11, 567000)
    date_list = [(base - datetime.timedelta(days=x)).strftime("%y-%m-%d") for x in range(0, numdays)]

    for grp in ['WT', 'MUTATE']:
        for d in date_list:
            filename = './Tutorials/Tutorial 1/Data/Exercise 3/{0}_data/{0}_{1}_{2}.txt'.format(expt, grp,d)
            print('Generating file {}'.format(basename(filename)))
            if not exists(dirname(filename)):
                print('Creating new directory')
                os.makedirs(basename(filename))
            outfile = open(filename, 'w')
            rand_data = generate_data()
            for item in rand_data:
                outfile.write("{}\n".format(item))
            outfile.close()

################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=sys.argv[0],
                                     description='Creates random data for exercise 3')
    parser.add_argument('--expt', action='store', help='Name of experiment', default='EXPRESSION')
    parser.add_argument('--numdays', metavar='N', type=int, action='store',
                        help='an integer indicating number of days for generating files')
    parser.add_argument('--error', metavar='N', type=int, action='store',
                        help='an integer value labelled as error in the files')

    args = parser.parse_args()
    expt = args.expt
    numdays = args.numdays
    error = args.error

    if all([arg is not None for arg in [expt, numdays, error]]):
        exercise3(expt=expt, numdays=numdays, error=error)
