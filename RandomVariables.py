class RandomVariable:
    def RandomVariable(self, function, sample_space):
        self.function = function
        self.sample_space = sample_space

# L12-5
# Heads are 0, tails are 1
# Bernoulli and indicator r.v.
def num_heads(event):
    return event.count(True)

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

# L12-8
def num_heads_equals(num, sample_space):
    event = []
    for i in sample_space:
        if num == num_heads(i):
            event.append(i)
    return event

def uniform_probability_of(event, sample_space):
    return event.__len__() / sample_space.__len__()



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
def PDF(x, random_variable, sample_space):
    RV_range = range_of_random_variable(random_variable, sample_space)
    if(RV_range.__contains__(x)):
        return uniform_probability_of(x, sample_space)
    else:
        return 0
    
def CDF(x, random_variable, sample_space):
    sum = 0
    RV_range = range_of_random_variable(random_variable, sample_space)
    for i in RV_range:
        if i < x:
            sum += uniform_probability_of(i, sample_space)
    
def range_of_random_variable(random_variable, sample_space):
    RV_range = []
    for i in sample_space:
        result = random_variable(i)
        if not RV_range.__contains__(result):
            RV_range.append(result)
    return RV_range
  
if __name__ == "__main__":
    #sample_space = make_sample_space(3)
    sample_space = [[False, False, False], [True, False, False], [True, True, False],
                    [True, True, True], [True, False, True], [False, True, False],
                    [False, True, True], [False, False, True]]
    #event = [True, False, True]
    #print(f"Number of heads: {num_heads(event)}")
    print(f"num_heads = 2: {num_heads_equals(2, sample_space)}")
    print(f"probability of num_heads = 2: {uniform_probability_of(num_heads_equals(2, sample_space),
          sample_space)}")
    #event = [3, 5]
    #print(f"Both prime: {both_prime(event)}")
    random_variable = RandomVariable(num_heads, sample_space)
    print(f"sample space of rv: {sample_space}")