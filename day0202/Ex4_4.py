for i in range(1,10):
    for j in range(1,10):
        if i % 2 == 0:
            continue
        if i*j > 50:
            break
        print(i*j,end=' ')
    print()
