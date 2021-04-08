#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: nomalocaris <nomalocaris.top>
""""""
from __future__ import (absolute_import, unicode_literals)
import numpy as np
import matplotlib.pyplot as plt


def convergence_judge(vec, eps=1e-3):
    """judge if the agents is converged
    """
    for i in range(len(vec)):
        for j in range(len(vec)):
            if i != j:
                if abs(vec[i] - vec[j]) > eps:
                    return False
    return True


def plot_several_curve(x, y, line_num, label_prefix, title, xlabel, ylabel, save_path=''):
    """plot a graph which have several curve
    """
    assert len(y) >= line_num, 'The num of y is less than the num of line'
    for i in range(line_num):
        if label_prefix != '':
            plt.plot(x, y[i], label=label_prefix+'%d' % (i+1))
        else:
            plt.plot(x, y[i])

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if label_prefix != '':
        plt.legend()

    if save_path != '':
        plt.savefig('./test2.jpg')
    plt.show()


def generate_edge(graph):
    """draw the edge of graph
    """
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges


def generate_random_graph(n, neighbour_rate=1):
    """Generate random graph with number of n

    neighbour_rate: the rate of upper-limit of neighbour
    """
    node_list = []
    graph = {}
    for node in range(n):  # create nodes
        node_list.append(node)

    for node in node_list:
        graph[node] = []  # init dict graph

    for node in node_list:  # create connected undirected graph
        number = np.random.randint(1, int(n * neighbour_rate))  # get the num of neighbour
        for i in range(number):
            index = np.random.randint(0, n - 1)  # get the random neighbour
            node_append = node_list[index]
            if node_append not in graph[node] and node != node_append:
                graph[node].append(node_append)
                graph[node_append].append(node)

    return graph, node_list, generate_edge(graph)


