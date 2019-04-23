
#Generators have a lazy approach to computing the function on the given element.
#Only when you ask for the result wil it actually do the computation and return.

def square_number_generator( nums ):
    for i in nums:
        yield (i * i)

mynums = square_number_generator([1,2,3,4,5])

for num in mynums:
    print(num)


def funct( list ):
    return list+5

#This is a better way to use generators which uses list comprehention
#By using parentheses instead of brackets it creates a generator.
my_nums = (funct(x) for x in [1,2,3,4,5])

my_num_funct = [funct(x) for x in [1,2,3,4,5]]

for num in my_nums:
    print(num)


print(my_num_funct)
