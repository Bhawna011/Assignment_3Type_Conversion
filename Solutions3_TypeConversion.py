                                  # Assignment-3: Type Conversion
 # 1. Write a python script to convert a number into str type.
x=34
print((type (str(x))) , x)

#2. Write a python script to print Unicode of the character ‘m’.
print(ord('m'))

#3. Write a python script to print character representation of a given unicode 100.
print(chr(100))

#4. Write a python script to print any number and its binary equivalent
x=100
print(bin(x), x)
#5. Write a python script to print any number and its octal equivalent.
y=10
print(oct(y), y)
#6. Write a python script to print any number and its hexadecimal equivalent.
z=150
print(hex(z) , z)
#7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
a=0b1100101
print(a)

#8. Write a python script to store a hexadecimal number 2F in a variable and print it in
#octal format.
b=0x2f
print(oct(b),b)

#9. Write a python script to store an octal number 125 in a variable and print it in binary format.
c=0o125
print(bin(c), c)

#10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
#display the result in binary format.
p=0o25
q=0x39
result=p+q
print(bin(result),"result in binary format :-" , result)