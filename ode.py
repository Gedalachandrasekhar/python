def f1(t, x, v):
    return v

def f2(t, x, v):
    return -1 * x

t0 = 0
x0 = 1
v0 = 0
t = 10
dt = 0.1
n = int((t - t0) / dt)

t = t0
x = x0
v = v0
for i in range(n):
    k1 = dt * f1(t, x, v)
    l1 = dt * f2(t, x, v)
    k2 = dt * f1(t + dt/2, x + k1/2, v + l1/2)
    l2 = dt * f2(t + dt/2, x + k1/2, v + l1/2)
    k3 = dt * f1(t + dt/2, x + k2/2, v + l2/2)
    l3 = dt * f2(t + dt/2, x + k2/2, v + l2/2)
    k4 = dt * f1(t + dt, x + k3, v + l3)
    l4 = dt * f2(t + dt, x + k3, v + l3)
    x = x + (k1 + 2*k2 + 2*k3 + k4) / 6
    v = v + (l1 + 2*l2 + 2*l3 + l4) / 6
    t = t + dt

print("Displacement:", x)
print("Velocity:", v)
