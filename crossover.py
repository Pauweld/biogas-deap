import random

def crossover(ind1, ind2):
    """Executes a one point crossover on the input :term:`sequence` individuals.
    The two individuals are modified in place. The resulting individuals will
    respectively have the length of the other.
    
    :param ind1: The first individual participating in the crossover.
    :param ind2: The second individual participating in the crossover.
    :returns: A tuple of two individuals.
    This function uses the :func:`~random.randint` function from the
    python base :mod:`random` module.
    """
    size = len(ind1[0])
    cxpoint = random.randint(1, size - 1)
    while((cxpoint % 2) != 0):
        cxpoint = random.randint(1, size - 1)
    ind1[0][cxpoint:], ind2[0][cxpoint:] = ind2[0][cxpoint:], ind1[0][cxpoint:]
    
    return ind1, ind2
