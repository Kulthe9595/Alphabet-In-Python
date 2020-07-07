for row in range(4):
    for col in range(4):
        if row in {0,3} and col in {1,2}:
            print('*',end=' ')
        elif row in {1,2} and col in {0,3}:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()