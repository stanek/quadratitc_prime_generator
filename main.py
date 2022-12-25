from sympy import *

n = 2
prime_list = dict.fromkeys({})


def evaluate_formula(num):
    return num * num + (num - 1)


def custom_prime_checker(num):
    for prime_list_element in prime_list:
        if num % prime_list_element == 0:
            prime_factor_list = primefactors(num)
            for prime_factor_element in prime_factor_list:
                if prime_factor_element not in prime_list:
                    prime_list[prime_factor_element] = None
            return False
    prime_list[num] = None
    return True


while n < 1000000:

    evaluated_expression = evaluate_formula(n)
    is_prime_truth = isprime(evaluated_expression)
    is_prime_custom = custom_prime_checker(evaluated_expression)

    if is_prime_truth != is_prime_custom:
        print(str(n) + "\t\t\t\t\t" +
              str(evaluated_expression) + "\t\t\t\t\t\t\t\t\t" +
              str(is_prime_truth) + "\t" +
              str(is_prime_custom) + "\t" +
              str(prime_list.keys()))
        break
    if is_prime_truth is True:
        print(str(n) + "\t\t\t" + str(evaluated_expression))

    n = n + 1
