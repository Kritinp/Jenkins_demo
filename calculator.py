import math
# Error Code to signify a value is uncomputable


class trig_calculator:
    def __init__(self):
        print("Starting")

    def tan(self, x):
        return round(math.tan(x),2)

    def sin(self, x):
        return round(math.sin(x),2)

    def cos(self, x):
        return round(math.cos(x),2)