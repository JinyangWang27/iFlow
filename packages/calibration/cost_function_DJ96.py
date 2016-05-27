"""
cost_function_DJ96

Date: 22-Apr-16
Authors: Y.M. Dijkstra
"""
import numpy as np


def cost_function_DJ96(x, zeta_obs, zeta_mod,):
    """
    Parameters:
        x (array(N+2)) - coordinate array of the observation points + the domain boundary points
        zeta_obs (array(N)) - complex amplitude of the observed water level in one frequency
        zeta_mod (array(N)) - complex amplitude of the modelled water level in one frequency at the same locations as the observations

    Returns:
        cost functions as defined by Jones and Davies 1996 + weighing of distance between observation points
    """

    dzeta = np.abs(zeta_mod)-np.abs(zeta_obs)
    dphi = np.angle(zeta_mod)-np.angle(zeta_obs)
    weights = x[2:]-x[:-2]
    weights = weights/sum(weights)

    return np.sum(weights*(np.sqrt( (dzeta)**2.+2.*np.abs(zeta_mod)*np.abs(zeta_obs)*(1.-np.cos(dphi)) )))/len(weights)