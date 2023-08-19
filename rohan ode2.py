def infection_model(x, beta, gamma):
    dx = beta * x * (1000 - x) - gamma * x
    return dx

def euler_method(x0, t, beta, gamma):
    N = len(t)
    X = [0] * N
    X[0] = x0
    dt = t[1] - t[0]
    
    for i in range(N-1):
        X[i+1] = X[i] + dt * infection_model(X[i], beta, gamma)
        
    return X

# Initial conditions
x0 = 10
beta = 0.1
gamma = 0.05

# Time grid
t = [i for i in range(31)]

# Solve ODE
X = euler_method(x0, t, beta, gamma)

# Print solution
for i in range(len(t)):
    print("Day", t[i], ":", X[i], "infected individuals")
