import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
ax = 0


def show():
    plt.show()


def draw_MOEAD_Pareto(moead,name):
    Pareto_F_Data = moead.EP_X_FV
    Pop_F_Data = moead.Pop_FV

    Len = len(Pareto_F_Data[0])
    if Len == 2:
        r_x = Pareto_F_Data[0][:]
        r_y = Pareto_F_Data[0][:]
        for pp in Pop_F_Data:
            plt.scatter(pp[0], pp[1], c='black', s=5)
        for p in Pareto_F_Data:
            if p[0] < r_x[0]:
                r_x[0] = p[0]
            if p[0] > r_x[1]:
                r_x[1] = p[0]
            if p[1] < r_y[0]:
                r_y[0] = p[0]
            if p[1] > r_y[1]:
                r_y[1] = p[1]
            plt.scatter(p[0], p[1], c='red', s=10)

        plt.xlabel('Function 1', fontsize=15)
        plt.ylabel('Function 2', fontsize=15)
        plt.title(name)
        plt.xlim(r_x[0] - 0.1, r_x[1] + 0.1)
        plt.ylim(r_y[0] - 0.1, r_y[1] + 0.1)
    if Len == 3:
        global ax, fig
        if ax == 0:
            ax = Axes3D(fig)
        ax.set_xlabel('Function 1')
        ax.set_ylabel('Function 2')
        ax.set_zlabel('Function 3')
        for pp in Pop_F_Data:
            ax.scatter(pp[0], pp[1], pp[2], c='black', s=5)
        for p in Pareto_F_Data:
            ax.scatter(p[0], p[1], p[2], c='red', s=10)
        # ax.set_xlim([0,2])
        # ax.set_ylim([0,2])
        # ax.set_zlim([0,2])
def draw_W(moead):
    Start_Pts = moead.Z
    path = moead.csv_file_path + '/' + moead.name + '.csv'
    data = np.loadtxt(path)
    if data.shape[1] == 3:
        global ax, fig
        if ax == 0:
            ax = Axes3D(fig)
        x, y, z = data[:, 0], data[:, 1], data[:, 2]
        # ax.set_xlabel('X')
        # ax.set_ylabel('Y')
        # ax.set_zlabel('Z')
        VecStart_x = Start_Pts[0]
        VecStart_y = Start_Pts[1]
        VecStart_z = Start_Pts[2]

        VecEnd_x = data[:, 0]
        VecEnd_y = data[:, 1]
        VecEnd_z = data[:, 2]
        ax.scatter(x, y, z, marker='.', s=50, label='', color='r')
        for i in range(VecEnd_x.shape[0]):
            ax.plot([VecStart_x, VecEnd_x[i]], [VecStart_y, VecEnd_y[i]], zs=[VecStart_z, VecEnd_z[i]])
    if data.shape[1] == 2:
        x, y = data[:, 0], data[:, 1]
        # plt.xlabel('X')
        # plt.xlabel('Y')
        VecStart_x = Start_Pts[0]
        VecStart_y = Start_Pts[1]
        VecEnd_x = data[:, 0]
        VecEnd_y = data[:, 1]
        # plt.scatter(x, y, marker='.', s=50, label='', color='r')
        for i in range(VecEnd_y.shape[0]):
            plt.plot([VecStart_x, VecEnd_x[i]], [VecStart_y, VecEnd_y[i]])