"""
    Generative pattern classes for FoxDot.

    PMarkov2  -- Higher-order Markov chain (order-N n-gram transitions)
    PLife     -- 1D elementary cellular automaton (Rule 30, 90, 110, etc.)
    PLSystem  -- L-system string rewriting mapped to values
    PEvolve   -- Genetic algorithm pattern evolution

"""

from __future__ import absolute_import, division, print_function

from .Main import GeneratorPattern, Pattern
from .Generators import RandomGenerator

import random


class PMarkov2(RandomGenerator):
    """Higher-order Markov chain generator.

    Analyzes input sequence and builds N-gram transition table.
    Falls back to progressively shorter context windows, then random from source.

        >>> p = PMarkov2([0, 2, 4, 5, 7, 0, 2, 4], order=2)
        >>> p[:8]

    """
    def __init__(self, data, order=2, **kwargs):
        RandomGenerator.__init__(self, **kwargs)
        self.args = (data, order)
        self.kwargs = kwargs
        self.source = list(data)
        self.order = order
        self.history = []
        self._transitions = {}
        self._build_table()
        self.init_random(**kwargs)

    def _build_table(self):
        src = self.source
        for n in range(1, self.order + 1):
            for i in range(len(src) - n):
                key = tuple(src[i:i + n])
                nxt = src[i + n]
                if key not in self._transitions:
                    self._transitions[key] = []
                self._transitions[key].append(nxt)

    def func(self, index):
        for n in range(self.order, 0, -1):
            if len(self.history) >= n:
                key = tuple(self.history[-n:])
                if key in self._transitions:
                    value = self.choice(self._transitions[key])
                    self.history.append(value)
                    return value
        value = self.choice(self.source)
        self.history.append(value)
        return value


class PLife(GeneratorPattern):
    """1D elementary cellular automaton pattern.

    Pre-computes a grid from Rule N (e.g. Rule 30, 90, 110).
    Returns 0/1 values -- useful for rhythms, gates, binary patterns.

        >>> p = PLife(rule=30, size=16, row=0)
        >>> p[:16]  # first row of Rule 30

    """
    def __init__(self, rule=30, size=16, row=0, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)
        self.args = (rule, size, row)
        self.rule = rule
        self.size = size
        self.start_row = row
        self._grid = []
        self._compute_grid(256)

    def _compute_grid(self, num_rows):
        rulemap = {}
        for i in range(8):
            neighborhood = ((i >> 2) & 1, (i >> 1) & 1, i & 1)
            rulemap[neighborhood] = (self.rule >> i) & 1

        row = [0] * self.size
        row[self.size // 2] = 1
        self._grid = [row[:]]

        for _ in range(num_rows - 1):
            new_row = [0] * self.size
            for j in range(self.size):
                left = row[(j - 1) % self.size]
                center = row[j]
                right = row[(j + 1) % self.size]
                new_row[j] = rulemap[(left, center, right)]
            self._grid.append(new_row)
            row = new_row

    def func(self, index):
        r = self.start_row + (index // self.size)
        c = index % self.size
        if r >= len(self._grid):
            self._compute_grid(r + 256)
        return self._grid[r][c]


class PLSystem(GeneratorPattern):
    """L-system string rewriting mapped to numeric values.

    Default: Fibonacci L-system {"A": "AB", "B": "A"}.
    Pre-computes the rewritten string, maps characters via mapping dict.

        >>> p = PLSystem("A", {"A": "AB", "B": "A"}, generations=6, mapping={"A": 0, "B": 4})
        >>> p[:13]

    """
    def __init__(self, axiom="A", rules=None, generations=6, mapping=None, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)

        if rules is None:
            rules = {"A": "AB", "B": "A"}
        if mapping is None:
            mapping = {"A": 0, "B": 1}

        self.args = (axiom, rules, generations, mapping)
        self.rules = rules
        self.mapping = mapping
        self._sequence = self._generate(axiom, generations)

    def _generate(self, axiom, generations):
        current = axiom
        for _ in range(generations):
            current = "".join(self.rules.get(ch, ch) for ch in current)
        return [self.mapping.get(ch, 0) for ch in current]

    def func(self, index):
        return self._sequence[index % len(self._sequence)]


class PEvolve(RandomGenerator):
    """Genetic algorithm pattern generator.

    Evolves a population of sequences using tournament selection,
    single-point crossover, and random mutation. Walks through
    individuals, evolves when the population is exhausted.

        >>> p = PEvolve([0, 2, 4, 5, 7], fitness=lambda x: 7 - abs(x - 4), mutation=0.2)
        >>> p[:20]

    """
    def __init__(self, population, fitness=None, mutation=0.1, crossover=0.7, pop_size=8, **kwargs):
        RandomGenerator.__init__(self, **kwargs)
        self.args = (population, fitness, mutation, crossover, pop_size)
        self.kwargs = kwargs
        self.source = list(population)
        self.fitness_fn = fitness if fitness is not None else (lambda x: x)
        self.mutation_rate = mutation
        self.crossover_rate = crossover
        self.pop_size = pop_size
        self._population = [self.source[:] for _ in range(pop_size)]
        self._current_idx = 0
        self._individual_idx = 0
        self.init_random(**kwargs)

    def _evaluate(self, individual):
        return sum(self.fitness_fn(gene) for gene in individual)

    def _tournament(self, k=3):
        contestants = [self.choice(self._population) for _ in range(k)]
        return max(contestants, key=self._evaluate)

    def _crossover(self, parent1, parent2):
        if self.random.random() < self.crossover_rate and len(parent1) > 1:
            point = self.random.randint(1, len(parent1) - 1)
            child = parent1[:point] + parent2[point:len(parent1)]
        else:
            child = parent1[:]
        return child

    def _mutate(self, individual):
        result = individual[:]
        for i in range(len(result)):
            if self.random.random() < self.mutation_rate:
                result[i] = self.choice(self.source)
        return result

    def _evolve(self):
        new_pop = []
        for _ in range(self.pop_size):
            p1 = self._tournament()
            p2 = self._tournament()
            child = self._crossover(p1, p2)
            child = self._mutate(child)
            new_pop.append(child)
        self._population = new_pop
        self._current_idx = 0
        self._individual_idx = 0

    def func(self, index):
        if self._current_idx >= len(self._population):
            self._evolve()
        individual = self._population[self._current_idx]
        value = individual[self._individual_idx % len(individual)]
        self._individual_idx += 1
        if self._individual_idx >= len(individual):
            self._individual_idx = 0
            self._current_idx += 1
        return value
