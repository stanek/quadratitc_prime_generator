import sympy
import timeit
import bisect

class OrderedSet:
    def __init__(self, iterable=None):
        self._data = []    # List to maintain order and allow indexing
        self._set = set()  # Set to ensure uniqueness

        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, item):
        if item not in self._set:
            self._data.append(item)
            self._set.add(item)

    def add_at_end(self, item):
        if item not in self._set:
            self._data.append(item)
            self._set.add(item)

    def insert_in_sorted_location(self, item):
        if item in self._set:
            pass
        else:
            bisect.insort(self._data, item)
            self._set.add(item)

    def insert(self, index, item):
        if item in self._set:
            # Optional: Move the existing item to the new index
            self._data.remove(item)
            self._data.insert(index, item)
        else:
            self._data.insert(index, item)
            self._set.add(item)

    def remove(self, item):
        if item in self._set:
            self._data.remove(item)
            self._set.remove(item)
        else:
            raise KeyError(f"Item {item} not found in OrderedSet.")

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, item):
        # Remove the old item
        old_item = self._data[index]
        self._set.remove(old_item)

        # Insert the new item
        if item in self._set:
            raise ValueError(f"Item {item} already exists in OrderedSet.")
        self._data[index] = item
        self._set.add(item)

    def __delitem__(self, index):
        item = self._data.pop(index)
        self._set.remove(item)

    def __contains__(self, item):
        return item in self._set

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def index(self, item):
        return self._data.index(item)

    def __repr__(self):
        return f"OrderedSet({self._data})"

prime_set = OrderedSet()
def new_count():
    stop_at = 250
    i = 1
    num = formula(i)
    while i <= stop_at:
        factored_number = num
        if num <= 1:
            print(str(i) + " " + str(num) + " is One")
            i = i + 1
            num = formula(i)
            continue
        is_prime = True
        total_factors = []
        sqrt_value = num ** 0.5
        for x in prime_set:
            if x > sqrt_value:
                break
            if num % x == 0:
                factored_number, factors = factor(factored_number, x)
                for fac in factors:
                    total_factors.append(fac)
                is_prime = False
        if is_prime:
            prime_set.add_at_end(num)
            print(str(i) + " " + str(num) + " is Prime" + " {" + str(len(prime_set)) + "}")
            if not sympy.isprime(num):
                print(str(i) + " " + str(num) + " is a Mistaken Prime")
                exit(num)
        else:
            if factored_number != 1:
                prime_set.insert_in_sorted_location(factored_number)
                total_factors.append(int(factored_number))

            print(str(i) + " " + str(num) + " factors " + " x ".join(map(str, total_factors)) + " {" + str(len(prime_set)) + "}")

        i = i + 1
        num = formula(i)

def factor(num, fact):
    factors = []
    while num % fact == 0:
        num = num / fact
        factors.append(fact)
    return int(num), factors

def formula(x):
    return x
    # return pow(x, 2) + (x - 1)
    # return pow(x, 2) - (x - 1)
    # return pow(x, 2) + ((3*x) - 1)
    # return pow(x, 2) + ((5*x) - 1)
    # return pow(x, 2) + ((7*x) - 1)
    # return pow(x, 2) + ((6546546545*x) - 1)
    # return pow(x, 2) + (x + 1)
    # return pow(x, 2) - (x + 1)
    # return pow(x, 3) - pow(x, 2) - pow(x, 1) - 2
    # return pow(2, x) - 1

if __name__ == '__main__':
    execution_time = timeit.timeit(new_count, number=1)
    print("new_count() in " + str(execution_time) + " seconds")
