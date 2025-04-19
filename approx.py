def greedy_set_cover(U, subsets):
    U = set(U)  # make a copy to keep track of uncovered elements
    covered = set()
    chosen = []
    used = [False] * len(subsets)

    while covered != U:
        best_idx = -1
        best_cover_count = 0

        for i, subset in enumerate(subsets):
            if used[i]:
                continue
            # Count how many new elements this subset can cover
            new_cover = len(subset - covered)
            if new_cover > best_cover_count:
                best_cover_count = new_cover
                best_idx = i

        if best_idx == -1:
            break  # No subset can contribute anything new (should not happen with valid input)

        chosen.append(best_idx)
        covered.update(subsets[best_idx])
        used[best_idx] = True

    return chosen
