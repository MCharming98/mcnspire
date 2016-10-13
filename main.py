print("""
      Welcome to MC's calculator
      Here are the things you can do:

      Number:
      Basic calculations(+,-,*,/)
      All trigonometry functions(sin(x), cos(x), etc.)
          note: radian(sin(pi)) and degree(sin(180,degrees)) measure supported.
      root(x, n)
      exponential(x, n)
      simple_frac(numerator, denominator)
      convert_to_frac(number)

      Probability:
      factorial(n)
      permutation(n, r)
      combination(n, r)

      Statitics:
      note: data should be separated by comma, e.g: [1,2,3,3,4]
      sort([data])
      max([data])
      min([data])
      mean([data])
      mode([data])
      median([data])
      variance([data])
      S_Deviation([data])
      
      """)

from math import pi, e
degrees = True

#Number
##################################################

def sin(x, degrees=None):
    if degrees:
        x = (x*pi)/180
    while abs(x) > (2*pi):
        x = x%(2*pi)
    n = 1
    degree = 1
    result = 0
    while degree<=10: #10th degree taylor polynomial
        if degree % 2 == 1:
            result += (exponential(x, n)/factorial(n))
        else:
            result -= (exponential(x, n)/factorial(n))
        degree += 1
        n += 2
    if abs(result) < 1e-5:
        result = 0
    return result

def cos(x, degrees=None):
    if degrees:
        x = (x*pi)/180
    while abs(x) > (2*pi):
        x = x%(2*pi)
    n = 0
    degree = 1
    result = 0
    while degree<=10: #10th degree taylor polynomial
        if degree % 2 == 1:
            result += (exponential(x, n)/factorial(n))
        else:
            result -= (exponential(x, n)/factorial(n))
        degree += 1
        n += 2
    if abs(result) < 1e-5:
        result = 0
    return result

def tan(x, degrees=None):
    if degrees:
        x = (x*pi)/180
    if not cos(x): #Avoid ZeroDivisionError
        return 'Undefined.'
    return (sin(x)/cos(x))

def sec(x, degrees=None):
    if degrees:
        x = (x*pi)/180
    if not cos(x):
        return 'Undefined.'
    return 1/cos(x)

def csc(x, degrees=None):
    if degrees:
        x = (x*pi)/180
    if not sin(x):
        return 'Undefined.'
    return 1/sin(x)

def cot(x, degrees=None):
    if degrees:
        x = (x*pi)/180
    if x/(pi/2)==1:
        return 0
    if not tan(x):
        return 'Undefined.'
    return 1/tan(x)

def root(x, n):
    initial = x/2
    result = 0
    degree = 1
    while degree<=1000: #Newton-Raphson Algorithm
        result = initial - ((exponential(initial, n)-x)/(n*(exponential(initial, (n-1)))))
        initial = result
        degree += 1
    return result

def exponential(x, n):
    result = x
    if n == 0 and x != 0:
        return 1
    if x ==0:
        return 0
    i = abs(n)
    while i > 1:
        result*=x
        i -= 1
    if n < 0:
        return 1/result
    return result

def simple_frac(numer, denom):
    for i in range(2, min(numer, denom)+1):
        if numer%i == 0 and denom%i == 0:
            numer, denom = numer//i, denom//i
            
    for i in range(2, min(numer, denom)+1):
        if numer%i == 0 and denom%i == 0:
            return simple_frac(numer, denom)
    
    return (str(numer) + '/' + str(denom))
    
def convert_to_frac(number):
    """Caution: too much decimals will cause error"""
    numer = number
    denom = 1
    while numer % 1 > 1e-10:
        numer *= 10
        denom *= 10
    return simple_frac(int(numer), denom)

##################################################
#End of Number

#Probability
##################################################

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def permutation(n, r):
    if r>n:
        return 0
    elif r == 0:
        return 1
    return factorial(n)/factorial(n-r)

def combination(n, r):
    if r>n:
        return 0
    elif r == 0:
        return 1
    return permutation(n, r)/factorial(r)

##################################################
#End of Probability

#Statistics
##################################################

def mean(lst):
    result = 0
    for data in lst:
        result += data
    return result/len(lst)

def mode(lst):
    def counter(data, lst):
        count = 0
        while data in lst:
            lst.remove(data)
            count += 1
        return count
    sets = set(lst)
    if len(sets)==1:
        return lst[0]
    time_counter = []
    result = []
    for data in sets:
        time_counter.append(counter(data, lst))
    max_time = max(time_counter)
    new_lst = [i for i in sets]
    for i in range(len(time_counter)):
        if time_counter[i] == max_time:
            result.append(new_lst[i])
            
    if len(set(time_counter))==1:
       return ('No mode.')
    else:
        if len(result)==1:
            return result[0]
        else:
            for i in result:
                print (i)
            return result

def median(lst):
    lst.sort()
    if len(lst)%2 == 0:
        return (lst[(len(lst)//2)-1]+lst[(len(lst)//2)])/2
    else:
        return lst[(len(lst)-1)//2]
    
def variance(lst):
    result = 0
    E = mean(lst)
    for i in lst:
        result += exponential((i-E) ,2)
    return result/len(lst)
    
def S_Deviation(lst):
    return root(variance(lst),2)

def sort(lst):
    lst.sort()
    for i in lst:
        print (i)
    return lst

##################################################
#End of Statistics

#User Interactive Method
##################################################
while True:
    try:
        call = input()
        if call == 'CAS':
            CAS()
        else:
            final_result = eval(call)
            print(final_result)
    except NameError:
        print('Command not found.')
    except SyntaxError:
        print('Invaild syntax')
    except ZeroDivisionError:
        print('Zero division.')
    except:
        print('Unknown error.')
##################################################
#End of User Interactive Method

    
    
    
        
        
    
    
