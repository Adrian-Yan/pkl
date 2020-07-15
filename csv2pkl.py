import csv
from six.moves import cPickle as pickle
import numpy as np

def main(path_csv, path_pickle):

    x = []
    f = open(path_csv,'r')
    reader = csv.reader(f)
    for line in reader: x.append(line)

    i = open(path_pickle,'w')
    pickle.dump(x, i, pickle.HIGHEST_PROTOCOL)