"""Unit test for the smart_import module"""

import pytest
from floodsystem.smart_import import dynamic_import, smart_import


def test_dynamic_import():
    import numpy as np
    dynamic_numpy = dynamic_import('numpy')
    assert dynamic_numpy.sin(0) == 0
    assert dynamic_numpy.pi == np.pi
    assert dynamic_numpy.tan(dynamic_numpy.pi / 4) == np.tan(np.pi / 4)


def test_smart_import():
    import numpy as np
    smart_numpy = smart_import('numpy')
    assert smart_numpy.sin(0) == 0
    assert smart_numpy.pi == np.pi
    assert smart_numpy.tan(smart_numpy.pi / 4) == np.tan(np.pi / 4)
