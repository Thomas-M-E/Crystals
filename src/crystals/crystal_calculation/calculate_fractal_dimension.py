import logging

import numpy as np
from TYPING import Dict
from scipy import stats


def fractal_dimension(average_area, radii) -> Dict[str, float]:
    larea = np.log(average_area)
    grad, intercept, r_value, p_val, std = stats.linregress(np.log(radii[5:25]), larea[5:25])
    # Performs a linear regression on the middle section of the graph
    logging.info("Gradient estimate: ", grad)
    logging.info("Standard Error of line: ", std)
    ci_lower = grad - 2.58 * std  # 99% confidence interval
    ci_higher = grad + 2.58 * std
    confidence_interval = (ci_lower, ci_higher)
    logging.info(f"Confidence interval: {confidence_interval}")
    return {"confidence_interval": confidence_interval, "gradient": grad}
