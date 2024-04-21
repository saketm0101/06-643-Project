"""Utility file for calculating column dimensions."""

from .main import mccabe_thiele_calculations
import numpy as np


def column_dimensions_calculations(feed_flow, xf, xd):

    F = feed_flow
    xb = 0.1
    D = mccabe_thiele_calculations(feed_flow, xf, xd)[1]
    B = mccabe_thiele_calculations(feed_flow, xf, xd)[2]
    reflux = 2
    bo1 = (reflux) * ((xf - xd) / (xb - xf))

    # Calculation of heat duty
    M1 = 300  # Assuming mol. wt=200
    latent_heat_vapour = 600000  # Units - kJ/kmol
    qr = (
        bo1 * (B / M1) * latent_heat_vapour
    )  # Units - kJ/hr, converting our flow rate to molar flow rate (B/Molar mass)
    qrmw = qr / 3600000  # Converting from kJ/hr to MW

    # Calculation of area
    lmtdr = 13.9  # Units - K
    Ur = 0.000852  # Units - MW/(K*m^2)
    area_reboiler = qrmw * 1000 / (Ur * lmtdr)  # Units - m^2

    M2 = 300  # Assuming mol. wt=100
    latent_heat_liquid = 600000  # Units-kJ/kmol
    qc = (
        reflux * (D / M2) * latent_heat_liquid
    )  # Units- kJ/hr, converting our flow rate to molar flow rate (D/M)
    qcmw = qc / 3600000  # Converting from kJ/hr to MW

    lmtdc = 34.8  # Units - K
    Uc = 0.000568  # Units - MW/(K*m^2)
    area_condensor = qcmw * 1000 / (Uc * lmtdc)  # Units - m^2

    area = area_condensor + area_reboiler

    vapor_flow_rate = (reflux + 1) * D
    vapor_mass_flow_rate = (vapor_flow_rate * 300) / M2
    lt = 0.5
    density_vapour = 2.05
    density_liquid = 753
    k = -0.171 * (lt**2) + (0.27 * lt) - 0.047

    # Maximum allowable velocity
    max_vapor_velocity = k * (
        ((density_liquid - density_vapour) / density_vapour) ** 0.5
    )

    diameter = np.sqrt(
        (4 * vapor_mass_flow_rate) / (np.pi * density_vapour * max_vapor_velocity)
    )
    length = 2.3 * mccabe_thiele_calculations(feed_flow, xf, xd)[0]

    return [length, diameter, area]


def column_dimensions(feed_flow, xf, xd):
    """Takes the feed flow rate, feed mole fraction and the
    desired distillate mole fraction to calculate the column dimensions"""

    a = column_dimensions_calculations(feed_flow, xf, xd)
    print("Column dimensions are:")
    return print(
        f"Length of column = {a[0]:1.3f} m\nDiameter of column = {a[1]:1.3f} m"
    )
