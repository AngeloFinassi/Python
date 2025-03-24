def plusOne():
    List = [1,2,3]

    for c in (len(List) - 1, -1, -1):
        if List[c] < 9:
            List[c] += 1
            return List
        List[0] = 0
        return [1] + List
