#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: nomalocaris <nomalocaris.top>
""""""
from __future__ import (absolute_import, unicode_literals)
import numpy as np
from tools import plot_several_curve, convergence_judge

# set the parm
N = 500  # num of agents
sigma = 0.5
init_value_range = (-10, 10)
c = 10
beta = 0.5
# q in [1-sigma, 1]
q = np.random.uniform(1 - sigma, 1)

# cal the privacy budget
epsilon = q / (c * q + sigma - 1)
# init agant vector
theta_vec = np.random.randint(init_value_range[0], init_value_range[1], N)
tot_theta_vec = theta_vec.copy()
# init time
t = 0
t_seq = [t]


while not convergence_judge(theta_vec):
    # client send msg which added laplace noise
    eta_vec = np.random.laplace(0, c*q**t, N)
    x_vec = theta_vec + eta_vec
    print(eta_vec)
    # server cal and update itself
    y_vec = np.mean(x_vec)
    # client update itself
    theta_vec = (1 - sigma) * theta_vec + sigma * y_vec
    # record the variation of agent states
    tot_theta_vec = np.vstack((tot_theta_vec, theta_vec))

    # update t
    t += 1
    t_seq.append(t)


# set the num of curve which want to be plot
curve_num = 8
y = []
for i in range(curve_num):
    y.append(tot_theta_vec[:, i])
# plot the convergance curve
plot_several_curve(
    x=t_seq,
    y=y,
    line_num=curve_num,
    label_prefix='θ',
    title='Convergance curve(σ=%.3f, q=%.3f, ε=%.3f)' % (sigma, q, epsilon),
    xlabel='T',
    ylabel='θi(T)'
)
