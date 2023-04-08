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

        file = [f for f in os.listdir(os.path.join(folder_path, "TSLA")) if os.path.isfile(os.path.join(os.path.join(folder_path, "TSLA"), f))][0]
        df1 = pd.read_csv(os.path.join(folder_path, "TSLA", file), header = None)
        df1[1] = df1[1].apply(lambda s: float(s[:-1]))

        file = [f for f in os.listdir(os.path.join(folder_path, "AAPL")) if os.path.isfile(os.path.join(os.path.join(folder_path, "AAPL"), f))][0]
        df2 = pd.read_csv(os.path.join(folder_path, "AAPL", file), header = None)
        df2[1] = df2[1].apply(lambda s: float(s[:-1]))

        file = [f for f in os.listdir(os.path.join(folder_path, "GOOG")) if os.path.isfile(os.path.join(os.path.join(folder_path, "GOOG"), f))][0]
        df3 = pd.read_csv(os.path.join(folder_path, "GOOG", file), header = None)
        df3[1] = df3[1].apply(lambda s: float(s[:-1]))

        file = [f for f in os.listdir(os.path.join(folder_path, "NFLX")) if os.path.isfile(os.path.join(os.path.join(folder_path, "NFLX"), f))][0]
        df4 = pd.read_csv(os.path.join(folder_path, "NFLX", file), header = None)
        df4[1] = df4[1].apply(lambda s: float(s[:-1]))

        ys = df1.iloc[:, 1].values
        xs = list(range(1, len(ys)+1))
        ax1.clear()
        ax1.plot(xs,ys,color='blue')
        ax1.set_title('Tesla price',fontsize=12)
        
        ys = df2.iloc[:, 1].values
        xs = list(range(1, len(ys)+1))
        ax2.clear()
        ax2.plot(xs,ys,color='black')
        ax2.set_title('Apple price',fontsize=12)


        ys = df3.iloc[1:, 1].values
        xs = list(range(1, len(ys)+1))
        ax3.clear()
        ax3.plot(xs,ys,color='orange')
        ax3.set_title('Google price',fontsize=12)

        
        ys = df4.iloc[1:, 1].values
        xs = list(range(1, len(ys)+1))
        ax4.clear()
        ax4.plot(xs,ys,color='red')
        ax4.set_title('Netflix price',fontsize=12)
        
    ani = animation.FuncAnimation(fig,animate,interval=1000)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()