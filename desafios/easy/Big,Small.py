def BigSmal(numbers):
    if not numbers:
        return None, None
    
    n_bigger = n_smaller = numbers[0]

    for c in range(0, len(numbers)): 
        n = numbers[c]
        if n > n_bigger:
            n_bigger = n
        if n < n_smaller:
            n_smaller = n
    return n_bigger, n_smaller