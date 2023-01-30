#1.) Use double precision, calculate the resulting values (format to 5 decimal places)
#  010000000111111010111001
def binaryToDecimal(n):
    return int(n,2)

if __name__ == '__main__':
    decimal = binaryToDecimal('010000000111111010111001')
    print("Decimal = ", decimal)

#2.) Repeat exercise 1 using three-digit chopping arithmetic. 
Chop = ('%.3f'% decimal)
print("Chop = ", Chop)

#3.) Repeat exercise 1 using three-digit rouding arithmetic. 
Round = (round(decimal, 3))
print("Round = ", Round)

#4.) Compute the absolute and relative error with the exact value from question 1 and its 3 digit rounding. 
absolute_error = abs(decimal - Round)
print("Absolute Error = ", absolute_error)
relative_error = (abs(decimal - Round))/(abs(decimal))
print("Relative Error = ", relative_error)

#5.) Consider the infinite series. 


#6.) Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 - 10 = 0 
#    with accuracy 10^-4 using a = -4 and b = 7. 
def bisection_method(left: float, right: float, given_function: str):
    tolerance: float = .003
    diff: float = right - left
    max_iterations = 20
    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1
if __name__ == "__main__":
    left = -4
    right = 7
    function_string = "x**3 - (4*(x**2)) - 10 = 0"
    bisection_method(left, right, function_string)