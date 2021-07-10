from enforce_typing import enforce_types

import pytest
import sys

from engine.SimStrategy import *

@enforce_types
def testBasic():
    ss = SimStrategy()
    assert ss.max_ticks > 0

@enforce_types
def testAnnualMktsGrowthRate():
    ss = SimStrategy()
    assert hasattr(ss, 'growth_rate_if_0_sales')
    assert hasattr(ss, 'max_growth_rate')
    assert hasattr(ss, 'tau')

    ss.growth_rate_if_0_sales = -0.25
    ss.max_growth_rate = 0.5
    ss.tau = 0.075

    assert ss.annualMktsGrowthRate(0.0) == -0.25
    assert ss.annualMktsGrowthRate(0.0+1*ss.tau) == (-0.25 + 0.75/2.0)
    assert ss.annualMktsGrowthRate(0.0+2*ss.tau) == \
        (-0.25 + 0.75/2.0 + 0.75/4.0)
    assert ss.annualMktsGrowthRate(1e6) == 0.5

@enforce_types
def testSetMaxTicks():
    ss = SimStrategy()
    ss.setMaxTicks(14)
    assert ss.max_ticks == 14

@enforce_types
def testStr():
    ss = SimStrategy()
    assert "SimStrategy" in str(ss)
