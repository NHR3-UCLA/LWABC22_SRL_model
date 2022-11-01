#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:33:55 2022

@author: glavrent
"""

#load variables
import os
import sys
#arithmetic libraries
import numpy as np
from scipy import stats  as scipystats
#statistics libraries
import pandas as pd


def LavrentiadisWangAbrahamsonBozorgniaGoulet2022SurfRupLen(mag, wrup_max, sof='Strike-Slip', eps=0):
    '''
    Lavrentiadis, Wang,  Abrahamson, Bozorgnia, and Goulet (2022)
    Surface Rupture Lenght model

    Parameters
    ----------
    mag : real
        Moment Magnitude.
    wrup_max : TYPE
        Width of seismogenic zone (m).
    sof : string, optional
        Style of faulting. The valid options are: Normal, Strike-Slip, and Reverse
        The default is 'Strike-Slip'.
    eps : real, optional
        Aleatory epsilon. The default is 0.

    Returns
    -------
    srl : real
        Surface Rupture Length - for given epislon (m).
    srl_med : real
        Surface Rupture Length - median estimate (m).
    tau_srl : real
        Aleatory variability SRL.
    '''

    #Model coefficinets
    #--------------------
    #width model
    b_1 =-1.1602
    b_2 = 0.3396
    #srl model
    c_1 =-4.16733
    c_2 = 1.0
    c_3 = np.array([-0.1207, 0, -0.1207])
    tau_u = 0.2537
    #style of fauling    
    c_sof = np.array(['normal','strike-slip','reverse'])
    
    #Rupture Width Model
    #--------------------
    log_unb_wrup = b_1 + b_2*mag + 3.0
    log_wrup     = np.minimum(log_unb_wrup, np.log10(wrup_max) )

    #Surface Rupture Length Model
    #--------------------
    #scaling term
    x1 = mag - (log_wrup-3.0);

    #median surface rupture length
    c_3 = c_3[c_sof == sof.lower()]
    srl_med = 10**( c_1 + c_2*x1 + c_3 + 3.0 )

    #aleatory std
    tau_srl = tau_u / ( 1 + scipystats.logistic.cdf(2.1972*(log_unb_wrup-np.log10(wrup_max))/0.1) )

    #surface rupture length
    srl = srl_med * 10**(eps*tau_srl)

    return srl, srl_med, tau_srl
    
