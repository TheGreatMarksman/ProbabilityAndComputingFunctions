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
    def range(self):
        RV_range = []
        for i in self.sample_space:
            result = self.evaluate_at(i)
            if not RV_range.__contains__(result):
                RV_range.append(result)
        return RV_range

# L14-4
# Returns if a biased coin comes up heads
class IsHeads:
    def __init__(self, probability):
        self.sample_space = self.make_sample_space()
        self.probability = probability
    def make_sample_space(self):
        sample_space = [0, 1]
        return sample_space
    def evaluate_at(self, event):
        return event
    def equals(self, num):
        event = []
        for i in self.sample_space:
            if num == self.evaluate_at(i):
                event.append(i)
        return event
    def probability_of(self, event):
        if event == 1:
            return self.probability
        elif event == 0:
            return 1 - self.probability
        else:
            return 10
    def range(self):
        RV_range = []
        for i in self.sample_space:
            result = self.evaluate_at(i)
            if not RV_range.__contains__(result):
                RV_range.append(result)
        return RV_range


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

# L12-7
def PDF(x, random_variable):
    RV_range = random_variable.range()
    if(RV_range.__contains__(x)):
        return random_variable.probability_of(random_variable.equals(x))
    else:
        return 0
    
def CDF(x, random_variable):
    sum = 0
    RV_range = random_variable.range()
    for i in RV_range:
        if i < x:
            sum += random_variable.probability_of(random_variable.equals(i))
    return sum
  
if __name__ == "__main__":
    RV = NumHeads()
    print(f"Let A = the number of heads that show up when 3 coins are tossed")
    print(f"A([True, True, False]): {RV.evaluate_at([True, True, False])}")
    print(f"A = 2: {RV.equals(2)}")
    
    print(f"PDF(2) = {PDF(2, RV)}")
    print(f"CDF(2.3) = {CDF(2.3, RV)}")