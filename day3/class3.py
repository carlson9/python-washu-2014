# for numbers divisible by 3 print "Fizz"
# for numbers divisible by 5 print "Buzz"
# for numbers divisible by both print "FizzBuzz"

def FizzBuzz(i):
    if i%3==0:
        return "Fizz"
    if i%5==0:
        return "Buzz"
    return str(i)

for i in range(10):
    print str(i) + ": " + FizzBuzz(i)
