#arbitratry keyword
def child(**child1):
    print(child1)

child(chil2="andrew",child3="sam")

#default

def country(name="india"):
    print(name)

country()

# Function to calculate the mean of a list of numbers
def calculate_mean(numbers):
    if not numbers:
        return "The list is empty."
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    print(mean)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
calculate_mean(numbers)

