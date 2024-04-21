"""Utility file for calculating column cost."""

from .utils import column_dimensions_calculations


def column_cost(feed_flow, xf, xd):
    """Takes the feed flow rate, feed mole fraction and the
    desired distillate mole fraction to calculate the column cost"""

    length = column_dimensions_calculations(feed_flow, xf, xd)[0]
    diameter = column_dimensions_calculations(feed_flow, xf, xd)[1]
    area = column_dimensions_calculations(feed_flow, xf, xd)[2]
    Co_shell = 17640
    alpha_shell = 0.802
    cost_shell = Co_shell * ((length**alpha_shell) + (diameter**alpha_shell))
    Co_heatex = 7296
    alpha_heatex = 0.65
    cost_heatex = Co_heatex * (area**alpha_heatex)
    capital_cost = cost_shell + cost_heatex
    print(f"The capital cost is ${capital_cost:1.2f}")
