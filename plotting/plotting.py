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

def main ():
    style.use("fivethirtyeight")
    fig = plt.figure()

    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)


    def animate(i):
        #df = pd.read_csv('C:/Users/HP/Desktop/Flux/projet/git/real time stock data.csv')
        
        folder_path = "data flink/cryto1"  # Replace with the actual path to your folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        # Sort the files by creation time
        files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
        df = pd.DataFrame()
        for file in files_sorted:
            path = "data flink/crypto1"+file
            df1 = pd.read_csv(path,sep=" ", header=None)
            df = df.append(df1)

        
        folder_path = "data flink/crypto2"  # Replace with the actual path to your folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        # Sort the files by creation time
        files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
        df2 = pd.DataFrame()
        for file in files_sorted:
            path = "data flink/crypto2"+file
            df1 = pd.read_csv(path,sep=" ", header=None)
            df2 = df2.append(df1)

        folder_path = "data flink/crypto3"  # Replace with the actual path to your folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        # Sort the files by creation time
        files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
        df3 = pd.DataFrame()
        for file in files_sorted:
            path = "data flink/crypto3"+file
            df1 = pd.read_csv(path,sep=" ", header=None)
            df3 = df3.append(df1)

        folder_path = "data flink/crypto4"  # Replace with the actual path to your folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        # Sort the files by creation time
        files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
        df4 = pd.DataFrame()
        for file in files_sorted:
            path = "data flink/crypto4"+file
            df1 = pd.read_csv(path,sep=" ", header=None)
            df4 = df4.append(df1)

        ys = df.iloc[1:, 0].values
        xs = list(range(1, len(ys)+1))
        ax1.clear()
        ax1.plot(xs,ys,color='black')
        ax1.set_title('crypto1 price',fontsize=12)
        
        ys = df2.iloc[1:, 0].values
        xs = list(range(1, len(ys)+1))

        ax2.clear()
        ax2.plot(xs,ys,color='red')
        ax2.set_title('crypto2 price',fontsize=12)


        ys = df3.iloc[1:, 0].values
        ax3.clear()
        ax3.plot(xs,ys,color='blue')
        ax3.set_title('crypto3 price',fontsize=12)

        
        ys = df4.iloc[1:, 0].values
        ax4.clear()
        ax4.plot(xs,ys,color='orange')
        ax4.set_title('crypto4 price',fontsize=12)
        
    ani = animation.FuncAnimation(fig,animate,interval=1000)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()