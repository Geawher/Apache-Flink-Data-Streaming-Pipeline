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
        folder_path = "C:\\Users\\nizar\\OneDrive\\Bureau\\output\\"  # Replace with the actual path to your folder
        
        folder_path_tsla= folder_path+"TSLA"

        files = [f for f in os.listdir(folder_path_tsla) if os.path.isfile(os.path.join(folder_path_tsla, f))]
        # Sort the files by creation time
        files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path_tsla, x)))
        df = pd.DataFrame()
        for file in files_sorted:
            path = folder_path_tsla+"\\"+file
            df1 = pd.read_csv(path, header=None)
        df1[1] = df1[1].apply(lambda s: float(s[:-1]))


        
        folder_path_aapl= folder_path+"AAPL"
        files = [f for f in os.listdir(folder_path_aapl) if os.path.isfile(os.path.join(folder_path_aapl, f))]
        # Sort the files by creation time
        files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path_aapl, x)))
        df2 = pd.DataFrame()
        for file in files_sorted:
            path = folder_path_aapl+"\\"+file
            df1 = pd.read_csv(path, header=None)
            df2 = df2.append(df1)

        df2[1] = df2[1].apply(lambda s: float(s[:-1]))

        folder_path_goog= folder_path+"GOOG"
        files = [f for f in os.listdir(folder_path_goog) if os.path.isfile(os.path.join(folder_path_goog, f))]
        # Sort the files by creation time
        files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path_goog, x)))
        df3 = pd.DataFrame()
        for file in files_sorted:
            path = folder_path+"\\"+file
            df1 = pd.read_csv(path, header=None)
            df3 = df3.append(df1)

        df3[1] = df3[1].apply(lambda s: float(s[:-1]))

        folder_path_nflx= folder_path+"NFLX"
        files = [f for f in os.listdir(folder_path_nflx) if os.path.isfile(os.path.join(folder_path_nflx, f))]
        # Sort the files by creation time
        files_sorted = sorted(files, key=lambda x: os.path.getctime(os.path.join(folder_path_nflx, x)))
        df4 = pd.DataFrame()
        for file in files_sorted:
            path = folder_path+"\\"+file
            df1 = pd.read_csv(path, header=None)
            df4 = df4.append(df1)
        
        df4[1] = df4[1].apply(lambda s: float(s[:-1]))

        ys = df.iloc[1:, 1].values
        xs = list(range(1, len(ys)+1))
        ax1.clear()
        ax1.plot(xs,ys,color='blue')
        ax1.set_title('Tesla price',fontsize=12)
        
        ys = df2.iloc[1:, 1].values
        xs = list(range(1, len(ys)+1))

        ax2.clear()
        ax2.plot(xs,ys,color='black')
        ax2.set_title('Apple price',fontsize=12)


        ys = df3.iloc[1:, 1].values
        ax3.clear()
        ax3.plot(xs,ys,color='orange')
        ax3.set_title('Google price',fontsize=12)

        
        ys = df4.iloc[1:, 1].values
        ax4.clear()
        ax4.plot(xs,ys,color='red')
        ax4.set_title('Netflix price',fontsize=12)
        
    ani = animation.FuncAnimation(fig,animate,interval=1000)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()