def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
     if  maximum < num :
       maximum = num
    return maximum
