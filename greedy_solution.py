def eval_cost(solution, target):
    return sum(solution) - target


def get_combo(items, n):
    if n:
        if len(items):
            c = map(lambda x: [items[0]] + x, get_combo(items, n - 1))
            return list(c) + get_combo(items[1:], n)
        return []
    else:
        return [[]]


def greedy_capacity_finder(requested_load, container_choices):
    """
    Greedy search to explore the best solution for
    capacity needed for requested load
    :param requested_load: eg. 6
    :param container_choices: eg. [1, 2, 3]
    :return: The optimum solution for the containers to be used for
    requested load
    """

    local_sol, local_score = None, None
    container_choices.sort(reverse=True)
    num_containers_used = 1

    while num_containers_used:
        # Early exit if the largest container cannot satisfy requested load
        if sum([container_choices[0] * num_containers_used]) < requested_load:
            num_containers_used += 1
            continue

        # Early exit if there are no more possible solutions after this
        if sum(container_choices[-1:] * num_containers_used) > requested_load:
            return local_sol

        for combination in get_combo(container_choices, num_containers_used):
            cost = eval_cost(combination, requested_load)
            if cost == 0:
                return combination

            if local_score is None or (cost < local_score and cost > 0):
                local_score = cost
                local_sol = combination

        num_containers_used += 1
