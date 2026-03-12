class Calculator:
    def __init__(self):
        # Başına tek alt tire koyarak "private" (internal) olduğunu belirttik
        self._current_val = 0
    def sub(self, value):
        self._current_val -= value
    def add(self, value):
        self._current_val += value

    def div(self, num):
        if num != 0:
            self._current_val /= num
        else:
            print("Cannot divide by zero!")
    def mul(self, x):
        self._current_val *= x

if __name__ == "__main__":
    a = Calculator()
    a.add(5)
    print(a._current_val)  # Output: 5
    a.sub(2)
    print(a._current_val)  # Output: 3
    a.mul(4)
    print(a._current_val)  # Output: 12
    a.div(3)
    print(a._current_val)  # Output: 4.0
    a.div(0)  # Output: Cannot divide by zero!