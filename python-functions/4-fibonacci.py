def fibonacci_sequence(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        fCounter= [0, 1]
        while len(fCounter) < num:
            next_num = fCounter[-1] + fCounter[-2]
            fCounter.append(next_num)
        return fCounter