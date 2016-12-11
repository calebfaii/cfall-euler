##Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def SumOfSquares(value):
    sum_squares = 0
    for i in range(1,(value + 1)):
        square = (i*i)
        sum_squares += square
    return sum_squares


def SquareOfSums(value):
    seq_sum = 0
    for n in range(1,(value + 1)):
        seq_sum += n
    square_sums = ((seq_sum)**2)
    return square_sums

a = SumOfSquares(100)
b = SquareOfSums(100)
c = abs(a-b)
print c



