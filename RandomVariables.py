# L12-5
# Heads are 0, tails are 1
# Bernoulli and indicator r.v.
def num_heads(event):
    return event.count(True)

# L12-8
def num_heads_equals(num, sample_space):
    event = []
    for i in sample_space:
        if num == num_heads(i):
            event.insert(i)
    return event

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

  
if __name__ == "__main__":
    event = [True, False, True, False, True]
    print(f"Number of heads: {num_heads(event)}")
    print(f"num_heads = 3: {num_heads_equals(3, event)}")
    event = [3, 5]
    print(f"Both prime: {both_prime(event)}")