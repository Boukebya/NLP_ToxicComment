# file containing functions for working with the data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Function to put the data into a dataframe
def create_dataframe(filename):
    df = pd.read_csv(filename)
    # print shape
    print("Shape of the dataframe is: " + str(df.shape))
    # print head
    print(df.head())

    return df
