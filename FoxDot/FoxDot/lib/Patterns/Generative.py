"""
    Generative pattern classes for FoxDot.

    PLife  -- Cellular automaton pattern with chaos control

"""

from __future__ import absolute_import, division, print_function

from .Main import GeneratorPattern, Pattern

import random


class PLife(GeneratorPattern):
    ''' Returns values shaped by cellular automaton rules.
        `chaos`: 0.0 (linear/steady) to 1.0 (fully chaotic)
        `steps`: grid size / repetition length (default 16)
        `low`:   minimum output value (default 0)
        `high`:  maximum output value (default 1)
        e.g. `amplify=PLife(0.5)`         — amp values in [0.5, 1.0]
             `degree=PLife(0.7, 0, 7)`   — scale degrees 0-7
             `oct=PLife(0.3, 4, 6)`      — octave range 4-6
             `lpf=PLife(0.6, 400, 4000)` — filter sweep '''

    def __init__(self, chaos=0.0, low=0, high=1, steps=16, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)
        self.args = (chaos, low, high, steps)
        self.chaos = float(chaos)
        self.steps = steps
        self.low = low
        self.high = high
        self._use_int = isinstance(low, int) and isinstance(high, int)
        self._grid = []
        self._rule = self._chaos_to_rule(self.chaos)
        self._compute_grid(256)

    @staticmethod
    def _chaos_to_rule(chaos):
        rules = [
            (0.0,  0),    # all zeros — perfectly linear
            (0.15, 254),  # nearly all ones — steady
            (0.3,  90),   # XOR rule — moderate complexity
            (0.5,  110),  # edge of chaos — complex structures
            (0.7,  150),  # chaotic with structure
            (0.85, 30),   # highly chaotic
            (1.0,  30),   # maximum chaos
        ]
        for i in range(len(rules) - 1):
            if chaos <= rules[i + 1][0]:
                mid = (rules[i][0] + rules[i + 1][0]) / 2.0
                if chaos <= mid:
                    return rules[i][1]
                else:
                    return rules[i + 1][1]
        return 30

    def _compute_grid(self, num_rows):
        rulemap = {}
        for i in range(8):
            neighborhood = ((i >> 2) & 1, (i >> 1) & 1, i & 1)
            rulemap[neighborhood] = (self._rule >> i) & 1

        row = [0] * self.steps
        row[self.steps // 2] = 1
        self._grid = [row[:]]

        for _ in range(num_rows - 1):
            new_row = [0] * self.steps
            for j in range(self.steps):
                left = row[(j - 1) % self.steps]
                center = row[j]
                right = row[(j + 1) % self.steps]
                new_row[j] = rulemap[(left, center, right)]
            self._grid.append(new_row)
            row = new_row

    def func(self, index):
        r = index // self.steps
        c = index % self.steps
        if self.chaos <= 0.0:
            return self.high
        # Use a local neighborhood density for continuous output
        radius = 2
        needed = r + radius + 1
        if needed >= len(self._grid):
            self._compute_grid(needed + 256)
        total = 0
        count = 0
        for dr in range(-radius, radius + 1):
            ri = r + dr
            if ri < 0:
                continue
            for dc in range(-radius, radius + 1):
                ci = (c + dc) % self.steps
                total += self._grid[ri][ci]
                count += 1
        density = total / count
        # chaos controls how much of the range is used
        floor = self.low + (self.high - self.low) * (1.0 - self.chaos)
        val = floor + (self.high - floor) * density
        if self._use_int:
            return int(round(val))
        return val
