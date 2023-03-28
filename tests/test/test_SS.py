import numpy as np


from ss_us.config import BLD

import pytest

def test_interest_rate_SS():
    r_SS=np.loadtxt(BLD/ "python" /"results"/ "r0_0.txt")
    r_NOSS=np.loadtxt(BLD/ "python" /"results"/ "r0_1.txt")
    assert r_NOSS < r_SS #interest rate should be lower in the steady state without social security since K/L goes up
def test_wages_SS():
    w_SS=np.loadtxt(BLD/ "python" /"results"/ "w0_0.txt")
    w_NOSS=np.loadtxt(BLD/ "python" /"results"/ "w0_1.txt")
    assert w_NOSS > w_SS #wages should be higher in the steady state without social security since K/L goes up
def test_capital_SS():
    J=66 
    kgen=np.load(BLD/ "python" /"results"/ "kgen0.npy")
    kgen_first_gen=kgen[0]
    assert kgen_first_gen==0 #capital for new-born agents/generations is 0
    for i in range(1,J):
        assert kgen[i]>=0 #agents cannot borrow (no negative savings)