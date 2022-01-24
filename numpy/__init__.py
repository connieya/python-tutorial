import pandas as pd
import numpy as np
import os
import shutil
from tqdm import tqdm
from glob import glob
import librosa
# import seaborn as sns
import warnings
# from matplotlib import pyplot as plt


warnings.filterwarnings("ignore")

path = 'C:/workspace/audio'


file = glob(path)
print(file)
