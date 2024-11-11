import math

# Counts the number of heads of three coins tossed
class NumHeads:
    def __init__(self):
        self.sample_space = self.make_sample_space()
        
    def make_sample_space(self):
        sample_space = [[False, False, False], [True, False, False], [True, True, False],
                    [True, True, True], [True, False, True], [False, True, False],
                    [False, True, True], [False, False, True]]
        return sample_space
    
    # L12-5
    # Heads are 0, tails are 1
    # Bernoulli and indicator r.v.
    def evaluate_at(self, event):
        return event.count(True)
    # L12-8
    def equals(self, num):
        event = []
        for i in self.sample_space:
            if num == self.evaluate_at(i):
                event.append(i)
        return event
    def probability_of(self, event):
        return event.__len__() / self.sample_space.__len__()
    def get_range(self):
        RV_range = []
        for i in self.sample_space:
            result = self.evaluate_at(i)
            if not RV_range.__contains__(result):
                RV_range.append(result)
        return RV_range
    @staticmethod
    def test():
        RV = NumHeads()
        print(f"Let A = the number of heads that show up when 3 coins are tossed")
        print(f"A([True, True, False]): {RV.evaluate_at([True, True, False])}")
        print(f"A = 2: {RV.equals(2)}")
    
        print(f"PDF(2) = {PDF(2, RV)}")
        print(f"CDF(2.3) = {CDF(2.3, RV)}")

# L14-4
# Equals 1 if a biased coin comes up heads and 0 otherwise
class IsHeads:
    def __init__(self, probability):
        self.sample_space = self.make_sample_space()
        self.probability = probability
    def make_sample_space(self):
        sample_space = [[0], [1]]
        return sample_space
    def evaluate_at(self, event):
        return event[0]
    def equals(self, num):
        event = []
        for i in self.sample_space:
            if num == self.evaluate_at(i):
                event.append(i)
        return event
    def probability_of(self, event):
        if event == [[1]]:
            return self.probability
        elif event == [[0]]:
            return 1 - self.probability
        else:
            return 10
    def get_range(self):
        RV_range = []
        for i in self.sample_space:
            result = self.evaluate_at(i)
            if not RV_range.__contains__(result):
                RV_range.append(result)
        return RV_range
    @staticmethod
    def test(p):
        RV = IsHeads(p)
        print(f"Let A = 1 if a coin is heads and 0 otherwise. Biased coin has probability {p} to get heads")
        print(f"A([1]): {RV.evaluate_at([1])}")
        print(f"A = 0: {RV.equals(0)}")
    
        print(f"PDF(1) = {PDF(1, RV)}")
        print(f"CDF(0.5) = {CDF(0.5, RV)}")

# L14-5
# Returns number on die rolled with sides n = 6
class NumberRolled:
    def __init__(self):
        self.n = 6
        self.sample_space = self.make_sample_space()
    def make_sample_space(self):
        sample_space = []
        for i in range(1, self.n):
            event = [i]
            sample_space.append(event)
        return sample_space
    def evaluate_at(self, event):
        return event[0]
    def equals(self, num):
        if num > 0 and num < 7:
            return [num]
        return [ 10 ]
    def probability_of(self, event):
        if event[0] > 0 and event[0] < 7:
            return 1 / self.n
        return 0

    def get_range(self):
        RV_range = []
        for i in range(1, self.n):
            RV_range.append(i)
        return RV_range
    @staticmethod
    def test():
        RV = NumberRolled()
        print(f"Let A = number rolled on a dice")
        print(f"A([3]): {RV.evaluate_at([3])}")
        print(f"A = 6: {RV.equals(6)}")
    
        print(f"PDF(4) = {PDF(4, RV)}")
        print(f"CDF(4) = {CDF(4, RV)}")

# L14-6
# Counts the number of heads in the n = 3 coin tosses each with probability p
class NumBiasedHeads:
    def __init__(self, p):
        self.sample_space = self.make_sample_space()
        self.p = p
        self.n = 3
    def make_sample_space(self):
        sample_space = [[0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0], [1, 0, 0],
                        [1, 0, 1], [1, 1, 1]]
        return sample_space
    def evaluate_at(self, event):
        return event.count(1)
    def equals(self, num):
        event = []
        for i in self.sample_space:
            if num == self.evaluate_at(i):
                event.append(i)
        return event
    def probability_of(self, event):
        num = self.evaluate_at(event)
        return combination(self.n, num) * pow(self.p, num) * pow(1 - self.p, self.n - num)

    def get_range(self):
        RV_range = []
        for i in self.sample_space:
            result = self.evaluate_at(i)
            if not RV_range.__contains__(result):
                RV_range.append(result)
        return RV_range
    @staticmethod
    def test(p):
        RV = NumBiasedHeads(p)
        print(f"Let A = the number of heads in 3 coin tosses each with probability {p} to get heads")
        print(f"A([1, 0, 1]): {RV.evaluate_at([1, 0, 1])}")
        print(f"A = 2: {RV.equals(2)}")

        print(f"PDF(1) = {PDF(1, RV)}")
        print(f"PDF(2) = {PDF(2, RV)}")
        print(f"PDF(3) = {PDF(3, RV)}")

        print(f"CDF(2) = {CDF(2, RV)}")

# L14-8
# Counts the number of tosses needed to get the first heads
# Domain consists of numbers from 1 to 10 indicating how many tosses it took
class NumTossesUntilHead:
    def __init__(self, p):
        self.sample_space = self.make_sample_space()
        self.p = p
        self.MAX_TOSSES = 10
    def make_sample_space(self):
        sample_space = []
        for i in range(1, self.MAX_TOSSES + 1):
            sample_space.append(i)
        return sample_space
    def evaluate_at(self, event):
        return event
    def equals(self, num):
        return num
    def probability_of(self, event):
        return pow(1 - p, event - 1) * p

    def get_range(self):
        return self.make_sample_space()

# Incomplete
def make_sample_space(num_coins):
    a, b, c = 0
    sample_space = []
    while a < 2:
        subspace = [a, b, c]
        sample_space.append(subspace)
        a += 1
    a = 0
    
    return sample_space





# L12-6
# Indicator r.v.
def both_prime(event):
    num_primes = sum(is_prime(i) for i in event)
    return num_primes >= 2

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# L13-5
def PDF(x, random_variable):
    RV_range = random_variable.get_range()
    if(RV_range.__contains__(x)):
        return random_variable.probability_of(random_variable.equals(x))
    else:
        return 0

# Error because of i <= x, i < x issue
def CDF(x, random_variable):
    sum = 0
    RV_range = random_variable.get_range()
    for i in RV_range:
        if i <= x:
            sum += random_variable.probability_of(random_variable.equals(i))
    return sum

if __name__ == "__main__":
    # doesn't quite work
    NumBiasedHeads.test(0.5)