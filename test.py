import pytest
from dispatch_package import sort


@pytest.mark.parametrize("width, height, length, mass, expected", [
    (100, 90, 100, 10, 'STANDARD'),
    (100, 100, 100, 20, 'REGECTED'),
    (150, 90, 90, 20, 'REGECTED'),
    (100, 100, 100, 10, 'SPECIAL'),
    (150, 90, 90, 10, 'SPECIAL'),
    (90, 90, 90, 20, 'SPECIAL'),
])

def test_dispatch(width, height, length, mass, expected):
  assert sort(width, height, length, mass) == expected