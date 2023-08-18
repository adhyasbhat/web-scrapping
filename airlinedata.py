import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('igoner')

connection = sqlit3.connect('travel.sqlite')
cursor = connection.cursor()