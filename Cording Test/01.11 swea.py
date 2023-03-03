

numer1=1
denom1=2
numer2=3
denom2=4



# def solution(numer1, denom1, numer2, denom2):
#     answer = []
    
if denom1 == 0 or denom2 == 0:
    raise ValueError("Denominators cannot be zero")

result = Fraction(numer1, denom1) + Fraction(numer2, denom2)

answer=[result.numerator, result.denominator]