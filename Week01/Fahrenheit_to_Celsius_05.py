# F to C
# A program for converting Fahrenheit to Celsius
# by Kam Behi

def main():
       Fahrenheit = eval(input("Temperature in Fahrenheit "))
       Celsius = (Fahrenheit - 32) * 5/9
       if (int (Celsius) == -1) or (int (Celsius) == 0) or (int (Celsius) == 1):
              print ("The temperature is ", int (Celsius), "degree Celsius.")
       else:
              print ("The temperature is ", int (Celsius), "degrees Celsius.")
main()
