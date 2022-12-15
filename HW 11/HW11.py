storage = {}


def call_times(file_name):
    def write_to_file(func):
        def wrapper(*args):
            with open(file_name, "w") as new_file:
                result = func(*args)
                function_name = func.__name__
                if storage.get(file_name):
                    if storage[file_name].get(function_name):
                        storage[file_name][function_name] += 1
                    else:
                        storage[file_name].update({function_name: 1})
                else:
                    storage[file_name] = {function_name: 1}

                for func_name in storage[file_name].keys():
                    count = storage[file_name][func_name]
                    new_file.write(f"{func_name} была вызвана {count} раза.\n")
            return result
        return wrapper
    return write_to_file


@call_times('foo.txt')
def foo():
    pass


@call_times('foo.txt')
def boo():
    pass


@call_times('calls.txt')
def doo():
    pass


foo()
boo()
foo()
foo()
boo()
doo()
