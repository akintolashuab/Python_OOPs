# def generate_even_number(limit):
#     num = 0
#     while num<=limit:
#         yield num  #the yield tells the function it is generator
#         num+=2

# even = generate_even_number(40)
# print(even)
# lists = []
# for i in even:
#     lists.append(i)
# print(lists)



# def generate_prime_number():
#     primes = []
#     num = 2
#     while True:
#         if all(num % prime !=0 for prime in primes):  #the yield tells the function it is generator
#             yield num
#             primes.append(num)
#         num +=1
        
# prime_generator = generate_prime_number()
# primes = [next(prime_generator) for i in range(10)]
# print(primes)

def generate_even_number():
    evens = []
    num = 1
    while True:
        if num % 2 ==0:  #the yield tells the function it is generator
            yield num
            evens.append(num)
        num +=1
        
even_generator = generate_even_number()
evens = [next(even_generator) for i in range(100)]
print(evens)
