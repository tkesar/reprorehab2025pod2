# We will be reading 'Gait in Parkinson's Disease' data
# Jeffrey Hausdorff, PhD shared in PhysioNet
# physionet.org/content/gaitpdb/1.0.0/

# For this practice, we will only be reading one file:
# GaCo01_01.txt

# Metadata on the data format is provided in format.txt

# Each line contains 19 columns:

# Column      1: Time (in seconds)
# Columns   2-9: Vertical ground reaction force (VGRF, in N) on each of 8
#                sensors located under the left foot
# Columns 10-17: VGRF on each of the 8 sensors located under the right foot
# Column     18: Total force under the left foot
# Column     19: Total force under the right foot.

# %% Task 1. Read 'GaCo01_01.txt' using `pd.read_csv()`
import pandas as pd
# String - in which folder the txt file is saved?
folder_path = '/home/jinseok/Downloads'
# Use `sep='\t'`. Also, there's no header in the txt file.
# Make sure you don't use the first row as the header.
data = pd.read_csv('/'.join((folder_path, 'GaCo01_01.txt')),
                   sep='\t', header=None)

# %% Task 1-1. Provide the column names
names = ['Time',
         ''.join(('VGRF_L', range(1, 9))),
         ''.join(('VGRF_R', range(1, 9))),
         'TOTAL_L', 'TOTAL_R']
data.columns(names)
