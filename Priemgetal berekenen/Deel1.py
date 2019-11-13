def is_prime(number):
    if(number > 1):
        number_is_prime = True
        for i in range(2, number):
            if(number%i == 0):
                number_is_prime = False
                break
        return number_is_prime
    else:
        return False
        

print(is_prime(13)) # prints True
print(is_prime(4)) # prints False

#code om meerdere getallen te testen

#for i in range(2,50):
#    print(str(i) + ": " + str(is_prime(i)))