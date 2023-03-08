class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def convertFarenheit(self):
        return (self.celsius * 1.8) + 32

    def convertCelsius(self, fahrenheit):
        return (fahrenheit - 32) / 1.8

temp = Temperature(7)

print("Temperature in Fahrenheit:", temp.convertFarenheit())   
print("Temperature in Celsius:", temp.convertCelsius(77))