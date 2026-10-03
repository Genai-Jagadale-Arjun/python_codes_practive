
def print_n_prime_numbers(n):
    prime_numbers = []
    count = 0
    num = 2

    while count < n:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")
            prime_numbers.append(num)
            count += 1

        num += 1

    return prime_numbers

def main():
    n= int(input("Enter n: "))
    print_n_prime_numbers(n)

if __name__ == "__main__":
    main()