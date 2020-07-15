import csv
from six.moves import cPickle as pickle
import numpy as np

def main(path_pickle,path_csv):

    x = []
    
    f = open(path_pickle,'rb')
    x = pickle.load(f)
    
    i = open(path_csv,'w')
    writer = csv.writer(i)
    for line in x: writer.writerow(line)
