def hanoi(n, from_, to_, via_): 
    if n == 1:
        print("numero {}, {} -> {}".format(n,from_,to_))
    else:
        hanoi(n-1, from_, via_, to_)
        print("numero {}, {} -> {}".format(n,from_,to_))
        hanoi(n-1, via_, to_, from_)

n = int(input("Digite o numero de discos: "))
hanoi(n, 'A', 'C', 'B')