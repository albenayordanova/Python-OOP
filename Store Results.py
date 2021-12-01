class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        func_result = self.func(*args)
        output = f'Function {self.func.__name__} was add called. Result: {func_result}'
        with open('result.txt', 'a') as file:
            file.write(output)
            file.write('\n')



@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)