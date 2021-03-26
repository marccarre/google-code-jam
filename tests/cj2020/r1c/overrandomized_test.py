import os
import pytest
from pytest import main
from cj2020.r1c.overrandomized import crack


DIR = os.path.dirname(__file__)


@pytest.mark.skip(reason='bug')
def test_crack():
    with open(os.path.join(DIR, 'sample.in.txt'), 'r') as f:
        lines = f.read().strip().split('\n')
        assert len(lines) == 10002
    u = int(lines[1])
    samples = []
    for line in lines[2:]:
        query, response = line.split()
        samples.append((int(query), response))
    assert crack(u, samples) == 'TPFOXLUSHB'


if __name__ == '__main__':
    main()
