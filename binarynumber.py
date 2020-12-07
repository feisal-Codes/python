
def converter(number):
    answer= number//2
    remainder=number%2
    print(remainder)
    if answer != 0:
            converter(answer)
        

        
converter(58)


