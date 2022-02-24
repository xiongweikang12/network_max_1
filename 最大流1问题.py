import tkinter

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from ortools.graph import pywrapgraph
import time
import tkinter as tk
from tkinter import messagebox


def str_into_list(StringVar):#将Entry中的string isdigit 转换成列表
    content=[]
    for signal in StringVar:
        if signal.isdigit():
            content.append(int(signal))
        else:
            continue
    return content

#控件窗口定义
window=tk.Tk()
window.title('最大流问题')
window.geometry('200x200')
#变量定义
start_str=tk.StringVar
end_str=tk.StringVar
capacity_str=tk.StringVar
flow_str=tk.StringVar
#分别为四个输入框
frame_entry=tk.Frame(window)
frame_entry.pack()
start_node_entry=tk.Entry(frame_entry)
start_node_entry.pack()
end_node_entry=tk.Entry(frame_entry)
end_node_entry.pack()
capacity_entry=tk.Entry(frame_entry)
capacity_entry.pack()
flow_entry=tk.Entry(frame_entry)
flow_entry.pack()


def insert():#将填充的entry list return

    start_str=start_node_entry.get()
    list_start_node=str_into_list(start_str)
    print(list_start_node)


    end_str=end_node_entry.get()
    list_end_node=str_into_list(end_str)
    print(list_end_node)

    capacity_str=capacity_entry.get()
    list_capacity=str_into_list(capacity_str)
    print(list_capacity)


    flow_str=flow_entry.get()
    list_flow=str_into_list(flow_str)
    print(list_flow)
    return list_start_node,list_end_node,list_capacity,list_flow

def clear_entry():
    start_node_entry.delete(0,tkinter.END)
    end_node_entry.delete(0,tkinter.END)
    capacity_entry.delete(0,tkinter.END)
    flow_entry.delete(0,tkinter.END)



frame_command=tk.Frame(frame_entry)
frame_command.pack()










#TODO 什么输入方式 最好的方法 我想是通过excel的网格表 ，导入dataframe 导出
def read_excel_return():# 传入表路径，返回dataframe
    df_test_digit=pd.read_excel("test_input_digit_node.xls")
    return df_test_digit




#TODO 输入图信息，默认sart_node[0]为源点 end_node[-1]为汇点，找到截集，可视化
#例子
#test_1

#test_2
#
# list_sart_node = [0,0,1,2,2,3,3]
# list_end_node = [1,2,4,1,3,1,4]
# list_capacity= [0,1,0,2,0,1,3]
# list_flow = [2, 3, 3, 1, 2, 0, 2]
#
# list_sart_node=list_sart_node_1
# list_end_node=list_end_node_1
# list_capacity=list_capacity_1
# list_flow=list_flow_1

#test_3


# list_sart_node = [0,0,1,1,1,2,2,2,3,3,3,3,4,4,5,6,6,7,7,7,7,7,8,9,10]
# list_end_node = [1,2,3,4,6,3,4,7,4,5,6,8,5,10,6,8,9,4,5,6,9,10,11,11,11]
# list_capacity = [30,16,7,5,18,8,2,6,22,3,9,4,24,4,7,2,7,24,7,13,12,15,6,19,19]
# list_flow = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def show_content():
    list_sart_node, list_end_node, list_capacity, list_flow = insert()
    while True:
        if len(list_sart_node)==len(list_end_node)==len(list_capacity)==len(list_flow) and len(list_sart_node)>0:
        #及当entry框内所有的都非空 并且其长度都相等insect成立 break ，否则messagebox提醒，清除entry框，重新输入
            break
        else:
            messagebox.showerror(title='error warning', message='entry is empty or '
                                 'the lenght of these lists is no equid'
                                ' check out carafully again and rewrite pleas')
            quit()





    if 1==2:
        pass
    else:

        max_flow = pywrapgraph.SimpleMaxFlow()
        for i in range(0,len(list_sart_node)):
        # if choice.lower()=='y':

            max_flow.AddArcWithCapacity( list_sart_node[i],list_end_node[i] ,list_capacity[i] )  # tail,head,capacities
            #由于，算法默认其输入三个参数sart_node ,end_node,capacity,其正向为capacity与flow的差
        if list_flow:
            for j_1 in range(0,len(list_sart_node)):
            # if choice.lower() == 'y':
                max_flow.AddArcWithCapacity(list_end_node[j_1], list_sart_node[j_1] , list_flow[j_1])
            #如果不是全零流量，则将end_node作为sart_node,sart_node作为end_node,flow为capacity的全零流
        if max_flow.Solve(list_sart_node[0], list_end_node[-1]) == max_flow.OPTIMAL:

            print('')
            print(' Arc  Flow/Capacity ')
            for e in range(max_flow.NumArcs()):  # 网络边数
                print('%1s -> %1s    %3s / %3s ' % (max_flow.Tail(e), max_flow.Head(e), max_flow.Flow(e), max_flow.Capacity(e)))
            # print('souer side min-cut:', max_flow.GetSourceSideMinCut())
            # print('sink side min-cut:', max_flow.GetSinkSideMinCut())
        else:
            print('there was an issue with the max flow input')

        all_capacity=list(np.array(list_capacity)+np.array(list_flow))
        print(all_capacity)
        G=nx.DiGraph()

        list_empty=[]
        for j_2 in range(len(list_sart_node)):
            container_tuple=(list_sart_node[j_2],list_end_node[j_2],all_capacity[j_2])
            list_empty.append(container_tuple)

        G.add_weighted_edges_from(list_empty)
        pos_node=nx.spring_layout(G)
        label_1=nx.get_edge_attributes(G,'weight')

        label_2={}

        j_3=range(len(label_1.values()))
        j_3=list(j_3)
        list_empty_label=[]
        for j_4 in range(len(list_sart_node)):
            container_label_tuple=(list(label_1.keys())[j_4],list(label_1.values())[j_4],list_flow[j_4])
            list_empty_label.append(container_label_tuple)

        for a_1,a_2,a_3 in list_empty_label:
            label_2[a_1]=str(a_2)+'——'+str(a_3)

        nx.draw_networkx_nodes(G,pos_node,node_color='b')
        nx.draw_networkx_edges(G,pos_node,edge_color='b',alpha=0.6)
        nx.draw_networkx_labels(G,pos_node)
        nx.draw_networkx_edge_labels(G,pos_node,label_2)

        # print(G[max_flow.GetSourceSideMinCut()[0]])
        max_capacity=0
        for j_5 in max_flow.GetSourceSideMinCut():#MinCut 的 node 集合
            G_1=nx.Graph()
            max_flow_digit=G[j_5] #相邻点 dict(dict)
            container_list_MinCut=[]
            sigl_capacity=0
            for j_6 in range(len(list(max_flow_digit.keys()))):
                container_tuple_MinCut=(j_5,list(max_flow_digit.keys())[j_6]) #转化为tuple 用于可视化的数据接受
                # if list(max_flow_digit.keys())[j_6] in G[j_5]:
                container_list_MinCut.append(container_tuple_MinCut) #list(tuple)
                G_1.add_edges_from(container_list_MinCut)


                pos_MinCut_node_dict = {}
                pos_MinCut_node=list(max_flow_digit.keys())
                pos_MinCut_node.insert(0,j_5) #截集点的set，用于设置点的坐标

                if list(max_flow_digit.keys())[j_6]  in list(max_flow.GetSourceSideMinCut()):
                    #对于在截集的内的元素来说其相对于一个整体，其计数capacity时忽略
                    pass
                else:
                    sigl_capacity+=list(max_flow_digit.values())[j_6]['weight'] #单点的和,除相对与自己不在set中的点的capacity的和
            print(sigl_capacity)

            max_capacity+=sigl_capacity
        #多点和（单点和的和）

            for get_tick in pos_MinCut_node:
                pos_MinCut_node_dict[get_tick] = pos_node[get_tick]
            nx.draw_networkx_nodes(G_1, pos_MinCut_node_dict,node_color='r')
            nx.draw_networkx_edges(G_1,pos_MinCut_node_dict,edge_color='r')

        print('Mincut为:',max_flow.GetSourceSideMinCut())
        print('该网络的最大流为:',max_capacity)

        plt.show()

button_show = tk.Button(frame_command, text='启动', command=show_content)#算法程序按钮
button_show.pack()
button_quit = tk.Button(frame_command, text='退出', command=quit)
button_quit.pack()
button_clear=tk.Button(frame_command,text='清空',command=clear_entry)
button_clear.pack()

if __name__ == '__main__':
    window.mainloop()




#TODO 头痛碎觉ZZZZZZZZZZZZZ
#TODO 2021/11/14
#TODO 肝完作业，回去碎觉
#TODO 复习完两章数据分析，看一章节数据分析 2021/11/20
#TODO 2022/2/21




