N, t = input().split()
N  = int(N)
A = input().split()
A = [int(i) for i in A]  # Turn strings into int
if t == "1":
    print(7)
elif t == "2":
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] < A[1]:
        print("Smaller")
    elif A[0] == A[1]:
        print("Equal")
elif t == "3":
    print(sorted(A[:3])[1])
elif t == "4":
    print(sum(A))
elif t == "5":
    print(sum([i for i in A if i%2 == 0]))
elif t == "6":
    after_modulo_A = [i%26 for i in A]
    import string
    mapping = string.ascii_lowercase  # a - z
    output = list()
    for i in after_modulo_A:
        if i < 26:
            output.append(mapping[i])
    print("".join(output))
elif t == "7":
    current_index = 0
    loop_number = 0
    while True:
        current_index = A[current_index]
        if current_index > (N-1):
            print("Out")
            break
        elif current_index == (N-1):
            print("Done")
            break
        elif loop_number > (N):
            print("Cyclic")
            break
        loop_number += 1
