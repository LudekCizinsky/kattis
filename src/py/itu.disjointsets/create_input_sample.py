import random as r
import sys

if __name__ == '__main__':
    size = int(sys.argv[1])
    with open(f'10_to_power_of_{size}', 'w') as file:
        final_result = f'{10**size} {10**size}\n'
        for i in range(10**size):
            final_result += f'{r.choice([0, 1, 2])} {r.randrange(10**size)} {r.randrange(10**size)}\n'
        file.write(final_result)

