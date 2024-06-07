print("Hello")
print('Hello')


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)


#string is an array
a = "Bye, moron!"
print(a[1])
print(len(a)) #length

#check
txt = "What is the meaning of life?!"
print("meaning" in txt)
print("death" not in txt) #not in text

if "expensive" not in txt:
  print("No, there is no 'expensive'.")


#Slicing
#    0  3 5 7  11 13  17
x = "such a funny story"
print(x[7:12])
print(x[13:])
print(x[:4])
print(x[-5:-1])


j = "Happy!"
print(j.upper())

k = "ANGER"
print(k.lower())

p = "Ajuzhan"
print(p.replace("j", "r"))

u = "Get the hell out"
print(u.split("the hell"))

z = "cruel"
c = "path"
m = z + " " + c
print(m)

#F-string
age = 36
txt = f"Is being {age} considered old?"
print(txt)




price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#escape character
txt = "We are the so-called \"Vikings\" from the north."