import numpy as np
import pandas as pd
import os, psutil,time
from LoadMatrix import load_matrix
from LoadMatrix2 import load_matrix2

matrix=load_matrix()
print(matrix)

process = psutil.Process(os.getpid())
print('Used memory: ',process.memory_info().rss,' byte')  # in bytes


