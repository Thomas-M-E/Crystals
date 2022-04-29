import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def fractal_dimension(averageArea, rseq):
    larea = np.log(averageArea)
    plt.scatter(np.log(rseq),larea,c='blue')
    plt.scatter(np.log(rseq[10:25]),larea[10:25],c='red')
    # plots a scatter plot of the log of the radius and the log of the average number of occupied sites within that radius
    plt.title("Log-Log plot of Occupied Sites Against Radius")
    plt.xlabel("Log(Radius)")
    plt.ylabel("Log(Number of Occupied Sites)")

    grad, intercept, r_value, p_val, std = stats.linregress(np.log(rseq[5:25]),larea[5:25])
    # Performs a linear regression on the middle section of the graph
    print("Gradient estimate: ", grad)
    print("Standard Error of line: ", std)
    CIlower = grad - 2.58 * std # 99% confidence interval
    CIhigher = grad + 2.58 * std
    confidence_interval = f"""Confidence interval: ({CIlower}, {CIhigher})"""
    print(f"Confidence interval: {confidence_interval}")
    xx = np.linspace(np.log(rseq[10]), np.log(rseq[25]))
    plt.plot(xx, grad * xx + intercept, c='black') # Plots the line of best fit back on the data
    return confidence_interval
