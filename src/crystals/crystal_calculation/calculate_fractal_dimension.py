import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import logging

def fractal_dimension(averageArea, rseq):
    larea = np.log(averageArea)
    grad, intercept, r_value, p_val, std = stats.linregress(np.log(rseq[5:25]), larea[5:25])
    # Performs a linear regression on the middle section of the graph
    logging.info("Gradient estimate: ", grad)
    logging.info("Standard Error of line: ", std)
    CIlower = grad - 2.58 * std # 99% confidence interval
    CIhigher = grad + 2.58 * std
    CI = (CIlower, CIhigher)
    logging.info(f"Confidence interval: {CI}")
    return {"confidence_interval": CI, "gradient": grad}
