"""
    Generative pattern classes for FoxDot.

    PLife  -- Cellular automaton pattern with chaos control

"""

from __future__ import absolute_import, division, print_function

from .Main import GeneratorPattern, Pattern

import random


class PLife(GeneratorPattern):
    """Cellular automaton pattern with chaos control.

    Goes from completely linear (chaos=0) to chaotic (chaos=1).
    Optional `steps` sets the grid/repetition length.

        >>> amplify=PLife(0.0)        # linear, normal
        >>> amplify=PLife(1.0)        # fully chaotic
        >>> amplify=PLife(0.5, 4)     # medium chaos, 4-step grid

    """
    def __init__(self, chaos=0.0, steps=16, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)
        self.args = (chaos, steps)
        self.chaos = float(chaos)
        self.steps = steps
        self._grid = []
        self._rule = self._chaos_to_rule(self.chaos)
        self._compute_grid(256)

    @staticmethod
    def _chaos_to_rule(chaos):
        """Map chaos 0-1 to cellular automaton rules.
        0.0 = rule 0 (all dead, linear)
        ~0.3 = rule 90 (moderate complexity)
        ~0.5 = rule 110 (complex/edge of chaos)
        1.0 = rule 30 (maximum chaos)
        """
        rules = [
            (0.0,  0),    # all zeros — perfectly linear
            (0.15, 254),  # nearly all ones — steady
            (0.3,  90),   # XOR rule — moderate complexity
            (0.5,  110),  # edge of chaos — complex structures
            (0.7,  150),  # chaotic with structure
            (0.85, 30),   # highly chaotic
            (1.0,  30),   # maximum chaos
        ]
        # Find nearest rule
        for i in range(len(rules) - 1):
            if chaos <= rules[i + 1][0]:
                # Linear interpolation bias toward closest
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
        if r >= len(self._grid):
            self._compute_grid(r + 256)
        # Scale output by chaos amount so low chaos = low amplitude variation
        raw = self._grid[r][c]
        if self.chaos <= 0.0:
            return 1.0  # perfectly linear = always 1
        return raw * self.chaos + (1.0 - self.chaos)
