for row in range(7):
    for col in range(5):
        if row in {0,1,2,3,4,5} and col==0:
            print('*',end=' ')
        elif row==6:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()