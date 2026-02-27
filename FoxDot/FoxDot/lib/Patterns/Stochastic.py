"""
Stochastic.py
-------------
Probability and stochastic generator patterns for FoxDot.

PGauss   -- Gaussian (normal) distribution values
PBrown   -- Brownian motion (constrained random walk)
PLogistic -- Logistic map (deterministic chaos)
PSkip    -- Probability gate (pass or default)
PSwitch  -- Weighted random pattern switching

"""

from __future__ import absolute_import, division, print_function

from .Main import GeneratorPattern, Pattern, asStream
from .Generators import RandomGenerator


class PGauss(RandomGenerator):
    """Gaussian (normal) distribution values.

    Returns random values from a normal distribution centered on `mean`
    with standard deviation `sigma`. Useful for humanized timing, pitch
    variation, and natural-sounding randomness.

        >>> p = PGauss(mean=4, sigma=2)
        >>> p[:8]

    """
    def __init__(self, mean=0, sigma=1, **kwargs):
        RandomGenerator.__init__(self, **kwargs)
        self.args = (mean, sigma)
        self.kwargs = kwargs
        self.mean = mean
        self.sigma = sigma
        self.init_random(**kwargs)

    def func(self, index):
        return self.gauss(self.mean, self.sigma)


class PBrown(RandomGenerator):
    """Brownian motion (constrained random walk).

    Performs a random walk with gaussian step size, clamped to [lo, hi].
    Each step adds a gaussian offset (mean=0, sigma=step) to the previous value.

        >>> p = PBrown(lo=0, hi=1, step=0.1)
        >>> p[:16]

    """
    def __init__(self, lo=0, hi=1, step=0.1, **kwargs):
        RandomGenerator.__init__(self, **kwargs)
        self.args = (lo, hi, step)
        self.kwargs = kwargs
        self.lo = float(lo)
        self.hi = float(hi)
        self.step = float(step)
        self.last_value = (self.lo + self.hi) / 2.0
        self.init_random(**kwargs)

    def func(self, index):
        self.last_value += self.gauss(0, self.step)
        if self.last_value > self.hi:
            self.last_value = self.hi
        elif self.last_value < self.lo:
            self.last_value = self.lo
        return self.last_value


class PLogistic(GeneratorPattern):
    """Logistic map (deterministic chaotic sequence).

    Generates values from the logistic equation: x = r * x * (1 - x).
    With r near 3.9-4.0, produces chaotic (but deterministic) sequences.
    Output is mapped via: value * scale + offset.

        >>> p = PLogistic(r=3.99, scale=7)
        >>> p[:8]

    """
    def __init__(self, r=3.9, x0=0.5, scale=1, offset=0, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)
        self.args = (r, x0, scale, offset)
        self.r = float(r)
        self.x = float(x0)
        self.scale = scale
        self.offset = offset

    def func(self, index):
        self.x = self.r * self.x * (1.0 - self.x)
        return self.x * self.scale + self.offset


class PSkip(RandomGenerator):
    """Probability gate.

    Passes values from source pattern with probability `prob`,
    otherwise returns `default`. Useful for creating sparse variations
    of existing patterns.

        >>> p = PSkip([1, 0.5, 0.25], prob=0.7, default=2)
        >>> p[:8]

    """
    def __init__(self, pattern, prob=0.5, default=0, **kwargs):
        RandomGenerator.__init__(self, **kwargs)
        self.args = (pattern, prob, default)
        self.kwargs = kwargs
        self.source = asStream(pattern)
        self.prob = prob
        self.default = default
        self.init_random(**kwargs)

    def func(self, index):
        if self.random.random() < self.prob:
            return self.source[index]
        return self.default


class PSwitch(RandomGenerator):
    """Weighted random pattern switching.

    Each step, randomly selects one of the source patterns based on weights
    and returns that pattern's value at the current index.

        >>> p = PSwitch([P[0,2,4], P[0,3,5]], weights=[3, 1])
        >>> p[:8]

    """
    def __init__(self, patterns, weights=None, **kwargs):
        RandomGenerator.__init__(self, **kwargs)
        self.args = (patterns, weights)
        self.kwargs = kwargs
        self.patterns = [asStream(p) for p in patterns]
        self.weights = weights if weights is not None else [1] * len(self.patterns)
        self.init_random(**kwargs)

    def func(self, index):
        chosen = self.choices(self.patterns, weights=self.weights, k=1)[0]
        return chosen[index]
