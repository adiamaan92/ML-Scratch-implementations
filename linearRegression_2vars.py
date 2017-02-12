# From Scratch implementation of linear regression
# Covariance, Correlation, SD are also calculated without pandas or numpy

x = [-1,1,2,4,6,7]
y = [-1,2,3,3,5,8]

def summation(x):
    sum = 0
    for i in x:
        sum += i
    return sum
    
def mult(x,y):
    return [a*b for a,b in zip(x,y)]

def subt(x,y):
    return [a-b for a,b in zip(x,y)]
    
    
def mean(x):
    return summation(x)/len(x)
    
def sd(x):
    return round(((summation([(y - mean(x))**2 for y in x])/(len(x)-1))**(0.5)),4)

def covariance(x,y):
    xx = [(i - mean(x)) for i in x]
    yy = [(j - mean(y)) for j in y]
    return (summation(mult(xx,yy))/(len(x)-1))
    
def correlation(x,y):
    return round(covariance(x,y)/(sd(x)*sd(y)),4)
    
def slope(x,y):
    return round(((summation(x)*summation(y) - len(x)*summation(mult(x,y)))/(summation(x)**2 - len(x)*summation(mult(x,x)))),4)

def intercept(x,y):
    return round(((summation(x)*summation(mult(x,y)) - summation(y)*summation(mult(x,x)))/(summation(x)**2 - len(x)*summation(mult(x,x)))),4)
    
def linearRegression(x,y):
    return "Linear Regression line is : " + str(slope(x,y)) + "x" + " + " + str(intercept(x,y))

def CorrelationCoefficient(x,y):
    return round((sd(x)/sd(y))*slope(x,y),4)
    
    
print(linearRegression(x,y))

# Correlation Coefficient can be calculated via two ways slope * slope x/slope y or using the summation formula

print(CorrelationCoefficient(x,y))
print(correlation(x,y))
print(covariance(x,y))