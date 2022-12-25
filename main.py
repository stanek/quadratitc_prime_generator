from sympy import *
from timeit import default_timer as timer
import bisect

n = 2
prime_list = []
truth_time = 0
custom_time = 0


def evaluate_formula(num):
    return num * num + (num - 1)


def custom_prime_checker(num):
    max_divisor = num**0.5
    for prime_list_element in prime_list:
        if prime_list_element > max_divisor:
            break
        if num % prime_list_element == 0:
            known_reduced_factor = num / prime_list_element
            prime_factor_list = primefactors(known_reduced_factor)
            for prime_factor_element in prime_factor_list:
                if prime_factor_element not in prime_list:
                    bisect.insort(prime_list, prime_factor_element)
            return False
    bisect.insort(prime_list, num)
    return True


while True:

    evaluated_expression = evaluate_formula(n)

    start = timer()
    is_prime_truth = isprime(evaluated_expression)
    end = timer()
    truth_time += (end - start)

    start = timer()
    is_prime_custom = custom_prime_checker(evaluated_expression)
    end = timer()
    custom_time += (end - start)

    if is_prime_truth != is_prime_custom:
        print(str(n) + "\t\t\t\t\t" +
              str(evaluated_expression) + "\t\t\t\t\t\t\t\t\t" +
              str(is_prime_truth) + "\t" +
              str(is_prime_custom) + "\t" +
              str(prime_list))
        break
    if is_prime_truth is True:
        print(str(n) + "\t\t\t" +
              str(evaluated_expression) + "\t\t\t\t\t" +
              str("{:.3f}".format(truth_time)) + "\t\t" +
              str("{:.3f}".format(custom_time)))

    n = n + 1
