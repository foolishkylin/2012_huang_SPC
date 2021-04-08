#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: nomalocaris <nomalocaris.top>
""""""
from __future__ import (absolute_import, unicode_literals)
import numpy as np
from tools import convergence_judge, plot_several_curve, generate_random_graph


# set the parm
N = 500  # num of agents
sigma = np.random.uniform(0.4, 1, N)
init_value_range = (-10, 10)
c = 10
beta = 0.5
# q in [1-sigma, 1]
q = np.random.uniform(1 - min(sigma), 1)

# cal the privacy budget
epsilon = q / (c * q + min(sigma) - 1)
# init agant vector
theta_vec = np.random.randint(init_value_range[0], init_value_range[1], N)
tot_theta_vec = theta_vec.copy()
# generate UC graph
graph, nodes, edges = generate_random_graph(N, neighbour_rate=0.2)
# init time
t = 0
t_seq = [t]

while not convergence_judge(theta_vec, eps=1e-2):
    # client send msg which added laplace noise
    eta_vec = np.random.laplace(0, c*q**t, N)
    x_vec = theta_vec + eta_vec

    # msg from client neighbour's and self's state
    y_vec = np.array([np.mean(theta_vec[graph[i]+[i]]) for i in range(N)])
    # client update itself
    theta_vec = (1 - sigma) * theta_vec + sigma * y_vec
    # record the variation of agent states
    tot_theta_vec = np.vstack((tot_theta_vec, theta_vec))

    # update t
    t += 1
    print('round: %d \t mean: %d \t' % (t, np.mean(theta_vec)))
    t_seq.append(t)


# set the num of curve which want to be plot
curve_num = 16
y = []
for i in range(curve_num):
    y.append(tot_theta_vec[:, i])
# plot the convergance curve
plot_several_curve(
    x=t_seq,
    y=y,
    line_num=curve_num,
    label_prefix='',
    title='Convergance curve(σm=%.3f, q=%.3f, ε=%.3f)' % (min(sigma), q, epsilon),
    xlabel='T',
    ylabel='θi(T)'
)
