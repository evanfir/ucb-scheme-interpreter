    num_rolls0 = 0
    num_rolls1 = 0
    prev_num_rolls0 = 0
    prev_num_rolls1 = 0
    while score0 < goal and score1 < goal:
        if not player:
            num_rolls0 = strategy0(score0, score1)
            score0 += take_turn(num_rolls0, score1, dice = dice)
            # score1 += take_turn(strategy1(score0, score1), score0, dice = dice)

        else:
            num_rolls1 = strategy1(score0, score1)
            score1 += take_turn(num_rolls1, score0, dice = dice)
            # score0 += take_turn(strategy0(score0, score1), score1, dice = dice)

        # print("\nDEBUG: BEFORE is_swap: score0:", score0, "\n")
        # print("\nDEBUG: BEFORE is_swap: score1:", score1, "\n")
        # if is_swap(score0, score1):
            # score0, score1 = score1, score0
        player = other(player)
    # print("\nDEBUG: AFTER is_swap: score0:", score0, "\n")
    # print("\nDEBUG: AFTER is_swap: score1:", score1, "\n")
            if feral_hogs:
            if abs(prev_num_rolls0 - num_rolls0) == 2:
                score0 += 3
            if abs(prev_num_rolls1 - num_rolls1) == 2:
                score1 += 3
        prev_num_rolls0 = num_rolls0
        prev_num_rolls1 = num_rolls1
        if is_swap(score0, score1):
            score0, score1 = score1, score0
