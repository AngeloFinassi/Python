def make_count():
    count = 0
    
    def plus_count():
        nonlocal count
        count += 1
        print(f'Number of times {count}')

    #return the function that can allowed to be call later as a object
    return plus_count

counter = make_count()

counter()
counter()
counter()

