import numpy as np

def df(f, p, k, step=1e-5):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

def grad(f, p, step=1e-5):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return np.array(gp)

def gradient_descent(f, initial_params, learning_rate=0.01, tolerance=1e-6, max_iterations=1000):
    params = np.array(initial_params)
    
    for i in range(max_iterations):
        gradient = grad(f, params)
        params = params - learning_rate * gradient
        
        if np.linalg.norm(gradient) < tolerance:
            print(f"Converged after {i+1} iterations.")
            break
    
    return params

def target_function(p):
    return p[0]**2 + p[1]**2

initial_params = [1.0, 1.0]

learning_rate = 0.1
tolerance = 1e-8
max_iterations = 1000

result_params = gradient_descent(target_function, initial_params, learning_rate, tolerance, max_iterations)

print("Result:", result_params)
print("Optimal Value:", target_function(result_params))
