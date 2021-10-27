def intersect(set1, set2):
    new_set = set()
    for x in set1:
        for y in set2:
            if x == y:
                new_set.add(y)
    return new_set