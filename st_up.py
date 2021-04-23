print('Load some basic libraries and base DS stack. Initialize parameters for viewing. Can be seen by calling print(_IMPORTS)')

_IMPORTS = """import datetime as dt
from collections import defaultdict, Counter, namedtuple
import json
import os
import pickle
import warnings

from IPython.display import HTML, display, set_matplotlib_formats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sqlalchemy import create_engine
from tqdm.auto import tqdm

# INITIALIZING
# warnings
warnings.filterwarnings('ignore')
# pictures
sns.set()
plt.style.use('seaborn-bright')
plt.rcParams['figure.figsize'] = 10, 6
# pandas
pd.set_option('display.max_columns', 150)
pd.set_option('display.max_rows', 100)
tqdm.pandas()

# Autoreload
get_ipython().magic(u"%reload_ext autoreload")
get_ipython().magic(u"%autoreload 2")"""

exec(_IMPORTS)