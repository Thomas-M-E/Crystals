import logging

import matplotlib.pyplot as plt
import numpy as np


def plot_crystal(rseq, average_area, grad, std, intercept, CI):
    larea = np.log(average_area)
    plt.scatter(np.log(rseq), larea, c='blue')
    plt.scatter(np.log(rseq[10:25]), larea[10:25], c='red')
    # plots a scatter plot of the log of the radius
    # and the log of the average number of occupied sites within that radius
    plt.title("Log-Log plot of Occupied Sites Against Radius")
    plt.xlabel("Log(Radius)")
    plt.ylabel("Log(Number of Occupied Sites)")
    # Performs a linear regression on the middle section of the graph
    ci_lower = grad - 2.58 * std
    ci_higher = grad + 2.58 * std
    confidence_interval = (ci_lower, ci_higher)
    logging.info(f"Confidence interval: {confidence_interval}")

    xx = np.linspace(np.log(rseq[10]), np.log(rseq[25]))
    plt.plot(xx, grad * xx + intercept, c='black')
