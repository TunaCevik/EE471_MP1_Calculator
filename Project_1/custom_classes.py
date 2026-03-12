class Calculator:
    def __init__(self):
        # Başına tek alt tire koyarak "private" (internal) olduğunu belirttik
        self._current_val = 0
    def mul(self, x):
        self._current_val *= x
