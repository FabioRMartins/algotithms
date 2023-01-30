def study_schedule(permanence_period, target_time):
    counter = 0

    if permanence_period is None or target_time is None:
        return None

    if not all(
        all(
            isinstance(i, int) for i in tuple) for tuple in permanence_period):
        return None

    for a, z in permanence_period:
        if a <= target_time <= z:
            counter += 1
    return counter
