for row in range(7):
    for col in range(5):
        if row==0 and col in {1,2,3,4}:
            print('*', end=' ')
        elif row in {1,2} and col==0:
            print('*', end=' ')
        elif row==3 and col in {1,2,3}:
            print('*', end=' ')
        elif row in {4,5}and col==4:
            print('*', end=' ')
        elif row ==6 and col in {0,1, 2, 3}:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()