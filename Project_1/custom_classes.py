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
