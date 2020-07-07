for row in range(6):
    for col in range(6):
        if row in {0,5} and col in {0,5}:
            print('*',end=' ')
        elif row==1 and col in {0,1,5}:
            print('*',end=' ')
        elif row==2 and col in {0,2,5}:
            print('*',end=' ')
        elif row==3 and col in {0,3,5}:
            print('*',end=' ')
        elif row==4 and col in {0,4,5}:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()