from micrograd.engine import Value

def df(f, p, k):
    p_val = Value(p[k])
    f_val = f([Value(x) for x in p])
    f_val.backward()
    return p_val.grad

def grad(f, p):
    p_vals = [Value(x) for x in p]
    f_val = f(p_vals)
    f_val.backward()
    return [p_val.grad for p_val in p_vals]

def gradient_descent(f, initial_params, learning_rate=0.01, tolerance=1e-6, max_iterations=1000):
    params = [Value(x) for x in initial_params]
    
    for i in range(max_iterations):
        gradient = grad(f, params)
        params = [p - learning_rate * g for p, g in zip(params, gradient)]
        
        if max(abs(g.data) for g in gradient) < tolerance:
            print(f"Converged after {i+1} iterations.")
            break
    
    return [p.data for p in params]

def target_function(p):
    return p[0]**2 + p[1]**2

initial_params = [1.0, 1.0]
learning_rate = 0.1
tolerance = 1e-8
max_iterations = 1000

result_params = gradient_descent(target_function, initial_params, learning_rate, tolerance, max_iterations)

print("Result:", result_params)
print("Optimal Value:", target_function(result_params))
