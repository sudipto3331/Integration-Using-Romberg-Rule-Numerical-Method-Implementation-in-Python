def function(x):
    return x*3 + x*2 + x + 1

def trapezoidal(function, a, b, n):
    h = (b - a) / n
    integration = function(a) + function(b)

    for i in range(1, n):
        k = a + i * h
        integration += 2 * function(k)

    integration *= h / 2
    return integration

def simp_one_third(function, a, b, n):
    h = (b - a) / n
    integration = function(a) + function(b)

    for interval in range(1, n):
        x = a + interval * h
        if interval % 2 == 0:
            integration += 2 * function(x)
        else:
            integration += 4 * function(x)

    integration *= h / 3
    return integration

def simp_third_eight(function, a, b, n):
    h = (b - a) / n
    integration = function(a) + 3 * function(a + h) + 3 * function(a + 2 * h) + function(b)

    for i in range(3, n, 2):
        integration += 4 * function(a + i * h)

    for i in range(4, n, 2):
        integration += 2 * function(a + i * h)

    integration *= 3 * h / 8
    return integration

def romberg_integration(method, function, a, b, n):
    table = []
    for i in range(n + 1):
        row = [0] * (n + 1)
        table.append(row)
    for i in range(0, n+1):
        if method == "trapezoidal":
            table[i][0] = trapezoidal(function, a, b, 2**i)
        elif method == "simpson_one_third":
            table[i][0] = simp_one_third(function, a, b, 2**i)
        elif method == "simpson_three_eight":
            table[i][0] = simp_third_eight(function, a, b, 3*2**i)

    for j in range(1, n+1):
        for i in range(j, n+1):
            table[i][j] = (4*j * table[i][j-1] - table[i-1][j-1]) / (4*j - 1)
            
    return table[n][n]


lower_limit = float(input("Enter lower limit: "))
upper_limit = float(input("Enter upper limit: "))
num_intervals = int(input("Enter number of intervals: "))

print("Choose the method to solve Romberg integration:")
print("1. Trapezoidal")
print("2. Simpson's 1/3")
print("3. Simpson's 3/8")

method_choice = int(input("Enter method choice (1, 2, or 3): "))

if method_choice == 1:
    method = "trapezoidal"
elif method_choice == 2:
    method = "simpson_one_third"
elif method_choice == 3:
    method = "simpson_three_eight"
else:
    print("Invalid method choice. Please choose a valid method.")
    

result = romberg_integration(method, function, lower_limit, upper_limit, num_intervals)
print("Integration result using Romberg with %s method: %0.4f" % (method, result))
