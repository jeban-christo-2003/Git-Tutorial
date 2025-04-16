def greet(name):
    """A simple function that prints a greeting"""
    return f"Hello, {name}!"

def main():
    # Example usage
    result = greet("World")
    print(result)
    
    # Basic arithmetic
    x = 10
    y = 5
    print(f"Sum: {x + y}")
    print(f"Product: {x * y}")

if __name__ == "__main__":
    main()