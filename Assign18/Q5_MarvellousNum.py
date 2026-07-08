# Write a program which accepts N numbers from user and store it into  List.
#  Return addition of all prime numbers from that list.

# Module:

def ChkPrime(No):
    if No <= 1:   # 0 and 1 are not prime
        return False
    for i in range(2, int(No ** 0.5) + 1):  # check divisibility up to sqrt(No)
        if No % i == 0:
            return False
    return True
