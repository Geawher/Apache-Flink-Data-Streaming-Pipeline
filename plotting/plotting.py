# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:44:51 2023

@author: HP
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
import os

style.use("fivethirtyeight")
fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)


def animate(i):
    #df = pd.read_csv('C:/Users/HP/Desktop/Flux/projet/git/real time stock data.csv')
    

    folder_path = "data flink"  # Replace with the actual path to your folder

    # Get all the files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Sort the files by creation time
    files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    df = pd.DataFrame()
    # Print the sorted file names
    for file in files_sorted:
        path = "data flink/"+file
        df1 = pd.read_csv(path,sep=" ", header=None)
        df = df.append(df1)


    ys = df.iloc[1:, 2].values
    xs = list(range(1, len(ys)+1))
    ax1.clear()
    ax1.plot(xs,ys,color='black')
    ax1.set_title('AAPL price',fontsize=12)
    
    ys = df.iloc[1:, 3].values
    ax2.clear()
    ax2.plot(xs,ys,color='red')
    ax2.set_title('NFLX price',fontsize=12)


    ys = df.iloc[1:, 4].values
    ax3.clear()
    ax3.plot(xs,ys,color='blue')
    ax3.set_title('Goog price',fontsize=12)

    
    ys = df.iloc[1:, 5].values
    ax4.clear()
    ax4.plot(xs,ys,color='orange')
    ax4.set_title('Amzn price',fontsize=12)
    
ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.tight_layout()
plt.show()