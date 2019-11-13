def print_primes_up_to_a_number(number):
    for j in range(2, number):
        number_is_prime = True
        for i in range(2, j):
            if(j%i == 0):
                number_is_prime = False
                break
        if(number_is_prime):
            print(j)

number = int(input("Give a number: "))
print_primes_up_to_a_number(number)