from print_n_prime_numbers import print_n_prime_numbers

def sum_n_prime_numbers(n):
    prime_numbers = print_n_prime_numbers(n)
    total_sum = sum(prime_numbers)
    print(f"\nThe sum of the first {n} prime numbers is: {total_sum}")
    return total_sum

n = int(input("Enter n: "))
sum_n_prime_numbers(n)
