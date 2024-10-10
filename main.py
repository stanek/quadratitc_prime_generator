import sympy

prime = dict()
mistakes = []
def count():
    stop_at = 377000471
    i = 2
    num = formula(i)
    while num <= stop_at:
        # print("#######" + str(i) + " " + str(num))
        factored_number = num
        if num == 1:
            i = i + 1
            num = formula(i)
            continue
        is_prime = True
        for key,value in prime.items():
            while value < num:
                value += key
            prime[key] = value
            if value == num:
                factored_number = factor(factored_number, key)
                is_prime = False
        if is_prime:
            prime[num] = num
            print(str(i) + " " + str(num) + " is prime")
            if not sympy.isprime(num):
                mistakes.append(num)
                print(str(num) + " is mistake")
                keys_string = ', '.join(str(key) for key in prime.keys())
                print(keys_string)
        else:
            if factored_number != 1:
                if factored_number not in prime:
                    prime[factored_number] = factored_number
                print(str(i) + " " + str(num) + " is not prime")

        i = i + 1
        num = formula(i)

def factor(num, fact):
    while num % fact == 0:
        num = num / fact
    return num

def formula(x):
    # return pow(x, 2) + (x - 1)
    # return pow(x, 2) - (x - 1)
    # return pow(x, 2) + (x + 1)
    # return pow(x, 2) - (x + 1)
    # return pow(x, 3) - pow(x - 1, 2)
    return pow(2, x) - 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count()
    total_factors = 0
    for key in prime.keys():
        total_factors = total_factors + 1
    print(str(total_factors) + " factors")
