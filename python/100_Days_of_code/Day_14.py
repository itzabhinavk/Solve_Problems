# Problem — user ne "AVINAV" type kiya, database me "avinav" hai
# Bina lower() ke match nahi hoga!

username_input = "AVINAV"
stored_username = "avinav"

# Wrong way
if username_input == stored_username:  # False! match nahi hua
    print("Login success")

# Correct way
if username_input.lower() == stored_username:  # True!
    print("Login success")



# title() — naam display karne me
name = input("Enter your name: ")  # user: "avinav kumar"
print(f"Welcome, {name.title()}!")  # Welcome, Avinav Kumar!



# use of strip() — extra spaces remove karne me
# User ne accidentally spaces type kar diye
email = "   avinav@gmail.com   "



# ADM Classes me registration form pe kuch aisa hoga:
def register_user(name, email, password):
    name  = name.strip()
    email = email.strip().lower()  # strip + lowercase dono!
    # ab save karo


# use of replace() — unwanted characters remove karne me
# 1. Phone number clean karna
phone = "+91-98765-43210"
clean = phone.replace("-", "").replace("+91", "")
print(clean)  # "9876543210"

# 2. Email template banana
template = "Dear {NAME}, your order {ORDER_ID} is confirmed!"
message = template.replace("{NAME}", "Avinav")
message = message.replace("{ORDER_ID}", "ORD-2024")
print(message)
# Dear Avinav, your order ORD-2024 is confirmed!

# 3. Bad words filter (basic)
comment = "This is stupid content"
clean = comment.replace("stupid", "****")
print(clean)  # "This is **** content"


# use of split() — string ko list me convert karne me

# 1. CSV file process karna
line = "Avinav,20,CSE,8.5"
data = line.split(",")
name, age, dept, gpa = data
print(f"Name: {name}, GPA: {gpa}")
# Name: Avinav, GPA: 8.5

# 2. URL se parts nikalna
url = "https://admclasses.in/course/python/lesson/1"
parts = url.split("/")
print(parts[-1])   # "1"  — lesson number
print(parts[-2])   # "lesson"

# 3. User se multiple values ek saath lena
user_input = input("Enter marks (comma separated): ")
# user types: 85,90,78,92,88
marks = user_input.split(",")
marks = [int(m) for m in marks]
print(f"Average: {sum(marks)/len(marks)}")



# use of join() — list ko string me convert karne me

# 1. Tags banana (blog/course me)
tags = ["python", "flask", "web", "backend"]
tag_string = ", ".join(tags)
print(tag_string)  # "python, flask, web, backend"

# 2. File path banana
folders = ["home", "avinav", "projects", "adm-classes"]
path = "/".join(folders)
print(path)   # "home/avinav/projects/adm-classes"

# 3. SQL query banana dynamically
columns = ["name", "email", "age", "dept"]
query = f"SELECT {', '.join(columns)} FROM students"
print(query)
# SELECT name, email, age, dept FROM students

# 4. Words reverse karke sentence banana
sentence = "I love Python"
words = sentence.split()          # ["I", "love", "Python"]
reversed_sentence = " ".join(reversed(words))
print(reversed_sentence)           # "Python love I"


# use of find and count — string me search karne me

# 1. Email validation (basic)
email = "avinav@gmail.com"
if email.find("@") == -1:
    print("Invalid email — @ missing!")
else:
    print("Email looks valid")

# 2. Password me special character check
password = "Avinav@123"
if password.find("@") == -1 and password.find("#") == -1:
    print("Password must have special character!")

# 3. Word frequency — kitni baar word aaya paragraph me
paragraph = "Python is great. Python is easy. I love Python."
count = paragraph.count("Python")
print(f"'Python' mentioned {count} times")  # 3 times


# use of startswith and endswith — string ke start ya end me check karne me

# 1. File upload validation
filename = "profile_photo.jpg"

if filename.endswith(".jpg") or filename.endswith(".png"):
    print("Valid image file!")
else:
    print("Only jpg/png allowed!")

# Better way — tuple use karo
allowed = (".jpg", ".png", ".jpeg", ".webp")
if filename.endswith(allowed):
    print("Valid!")

# 2. URL check
url = "https://admclasses.in"
if url.startswith("https://"):
    print("Secure connection!")
else:
    print("Warning — not secure!")

# 3. File type se kaam karna
files = ["report.pdf", "image.jpg", "data.csv", "notes.pdf"]
pdfs = [f for f in files if f.endswith(".pdf")]
print(pdfs)  # ["report.pdf", "notes.pdf"]

# use of isdigit(), isalpha() and isalnum() — string me check karne me

# 1. Age input validate karna
age = input("Enter age: ")
if age.isdigit():
    age = int(age)
    print(f"Your age is {age}")
else:
    print("Age must be a number!")

# 2. Username validation
username = input("Enter username: ")
if username.isalnum():
    print("Valid username!")
else:
    print("Username can only have letters and numbers!")

# 3. OTP validate karna
otp = input("Enter OTP: ")
if otp.isdigit() and len(otp) == 6:
    print("Valid OTP format!")
else:
    print("OTP must be 6 digits!")



# use of zfill() / center() / ljust() / rjust()

# 1. Roll number formatting
roll = "5"
formatted = roll.zfill(3)   # "005"
print(f"Roll No: {formatted}")

# 2. Bill/Receipt banana
print("=" * 30)
print("ITEM".ljust(15) + "PRICE".rjust(10))
print("-" * 30)
print("Python Course".ljust(15) + "Rs.499".rjust(10))
print("DBMS Notes".ljust(15) + "Rs.199".rjust(10))
print("=" * 30)

# Output:
# ==============================
# ITEM               PRICE
# ------------------------------
# Python Course        Rs.499
# DBMS Notes           Rs.199
# ==============================

# 3. Loading bar style
for i in range(1, 6):
    bar = ("█" * i).ljust(5)
    print(f"\rLoading: [{bar}] {i*20}%", end="")


def register_student(name, email, phone, age):
    # 1. strip — spaces hatao
    name  = name.strip().title()
    email = email.strip().lower()
    phone = phone.strip().replace("-", "").replace(" ", "")

    # 2. Validations
    if not name.replace(" ", "").isalpha():
        return "❌ Name can only have letters!"

    if email.find("@") == -1 or email.find(".") == -1:
        return "❌ Invalid email!"

    if not phone.isdigit() or len(phone) != 10:
        return "❌ Phone must be 10 digits!"

    if not age.isdigit():
        return "❌ Age must be a number!"

    # 3. Format karo
    roll = str(1001 + 1).zfill(4)  # "1002"

    return f"""
✅ Registration Successful!
---------------------------
Name  : {name}
Email : {email}
Phone : {phone}
Roll  : {roll}
"""

# Test karo
print(register_student(
    "  avinav kumar  ",
    "  AVINAV@Gmail.COM  ",
    "98765-43210",
    "20"
))