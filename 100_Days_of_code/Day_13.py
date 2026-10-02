# Day 13 - 100 Days of Code Challenge


#string methods
#String are immutable 
a1="!!!!!!! Abhinav !!!!!!!! Abhinavji !!!!!"
print(len(a1))  # len() ye string ke length ko count karke batata hai 
print(a1.lower()) # ye string a1 ko lower case me convert nhi karega 
                  # kiyuki sting ek immutable tada type. Ye ek new string bana deta hai 

print(a1.upper()) # uppper() ye method string ke saare letters ko upper case me convert karta hai 
print(a1.strip("!"))  # strip()  methoda string ke aage or piche lage "!" ko hata dete hai ,ya ji bhi chizz ko hatana ho.
print(a1.replace("Abhinav", "varsha")) # replace() methrode string me word ka character ko replace karne ke kaam me aate hai 
print(a1.split(" ")) # split() method string ko list me convert kar dete hai or har spacse ke baad baale character ko ek element manta hai 
b="radhaKrishna"  
print(b.capitalize())  #capitalize() method string ke first character ko capital me conver kar deta hai 
str1="welcome to my coding journey"
print(len(str1))    # lenght of the string 
print(str1)
print(len(str1.center(50)))  # add 25 blank sp
print(str1)
print(a1.count("Abhinav"))  # count() method string me count karte haia ki Abhinav kitne baar hai 
print(a1.endswith("v"))     #endwith() method boolean value return karti hai agr string "v" se end ho rahi hai 
print(a1.endswith("i"))
print(a1.endswith("i", 2, 4)) # yaha check kar rahe hai ki index 2 se 4 ke bich ke string ka end "i" se hua hai ya nhi
print(str1.find("is")) 
