def sol(x0, epsilon, max_iterations):
    print(f"x = {x0}  f(x) = {x0**2 - 3*x0 + 1}")
    
    for iteration in range(1, max_iterations + 1):
        fx = x0**2 - 3*x0 + 1
        f_prime_x = 2*x0 - 3
        x1 = x0 - fx / f_prime_x

        print(f"x = {x1}  f(x) = {x1**2 - 3*x1 + 1}")

        if abs(x1 - x0) < epsilon:
            return x1

        x0 = x1

    return None

initial_guess = -100
epsilon = 0.001
max_iterations = 100

sol = sol(initial_guess, epsilon, max_iterations)
