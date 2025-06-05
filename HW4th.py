"""this
is
a
multi
line
comment!!!!!!!!!"""

########### file operations
#read:
# #open a file:
# file1=open("test.txt","r") #שם הקובץ וההרשאות שלנו

# #read the file:
# read_content=file1.read()
# print (read_content) #ידפיס את תוכן הטקסט

# file1.close() #חשוב כאשר נפסיק להשתמש במשאבים מאותו קובץ ונוריד עומס על המערכת

# # דרך נוספת להשתמש בקובץ ולסגור אותו מיד אח"כ היא
# with open ("test.txt","r") as file1:
#     read_content=file1.read()
#     print(read_content) #בסוף הוית' אופן הקובץ יסגר

#עוד דרך להשתמש בקובץ היא עם טריי ופיינלי
# try: #יש מצב שהקוד הזה יעשה ארור ולכן יש את החלק של פיינלי שהוא בטוח ירוץ גם אם יהיה ארור
#     file1=open("test.txt","r")
#     read_content=file1.read()
#     read_till10=file1.read(10) #קורא את 10 התווים הראשונים
#     print (read_content)
# finally: #נסגור את הקובץ בכל מקרה
#     file1.close()

#write:
# with open("test2.txt","w") as file2: #אם הקובץ לא קיים, ניצור קובץ חדש. אם הוא קיים, נמחק את תוכנו ונכתוב מחדש
#     file2.write("programming is fun.")
#קובץ חדש בשם test2.text
#יווצר ויהיו לו את כל התוכן שהוספנו

# try: #יכיל קוד שעלול לגרום לברירה כלשהי
#     numerator=10
#     denominator=0
#     result=numerator/denominator #נקבל 10 חלקי 0, לא תקין
#     print (result)
# except: #ירוץ כאשר ברירה כלשהי תתרחש
#     print ("Error: Denominator cannot be 0.")

# try:
#     even_numbers=[2,4,6,8]
#     print (even_numbers[5]) #יתן שגיאה כי אין שום דבר במיקום 5
# except ZeroDivisionError: #כאשר השגיאה היא חלוקה ב0
#     print ("Denominator cannot be 0.")
# except IndexError: #כאשר השגיאה היא אינדקס מחוץ לטווח
#     print ("Index out of bound.") 

# try: #נחלק 1 במספר זוג מסוים
#     num= int(input("Enter a number:"))
#     assert num%2==0 #מוודא שמשהו מתקיים, מייצר שגיאה במידה ומשהו לא מתקיים
# except:
#     print ("Not an even number!") #אם המספר אי-זוגי נגיע לפה
# else:
#     reciprocal = 1/num # אם המספר זוגי נגיע לפה
#     print (reciprocal)

# try:
#     numerator=10
#     denomirator=0
#     result=numerator/denomirator
#     print (result)

# except:
#     print ("Error: Denominator cannot be 0.") #נקבל ארור למעלה ונגיע לפה

# finally:
#     print ("This is finally block.") #תמיד נגיע לפה, זה פיינלי


# try:
#     x=int(input("enter a number:"))
#     y=10/x
#     print ("the result is ", y)
# except ZeroDivisionError: #יכנס לפה ולא למסלול מתחתיו. חשוב לדעת היכן ממוקם. אם היה ממוקם מתחת לאקספשן, האקספשן היה רץ קודם
#     print ("you cannot subside by 0")
# except Exception as e: #כל דבר, לא חייב להיות אי
#     print ("we have some error, the input is not valid")
#     print (e) #מדפיס את סוג השגיאה
# finally:
#     print ("End of program!")

#Q1
#

#Q2+3+4
# file=open("data.txt","r") #שם הקובץ וההרשאות שלנו
# content=file1.read(100)
# file.close()

#Q5
# try:
#     file=open("nonexistent_file.txt","r")
# except FileNotFoundError:
#     print ("File not found.")

#Q6
# with open("output.txt","w") as file: #אם הקובץ לא קיים, ניצור קובץ חדש. אם הוא קיים, נמחק את תוכנו ונכתוב מחדש
#     file.write("Hello,World!")
#     file.close()

#Q7
# try:
#     print (5/0)
# except ZeroDivisionError: #כאשר השגיאה היא חלוקה ב0
#     print ("cannot divide by 0.")

#Q8
# with open("output.txt","r+") as file:
#     file.write("New Data")
#     file.close()

#Q9
count=0 #Initialize a counter variable.

#Q10
# with open ("text_data.txt", "w") as file:
#     file.write("This is some text data")
#     file.close()

#Q11
# try: #נחלק 1 במספר זוג מסוים
#     num= int("abc")
# except ValueError:
#     print ("Value Error Occured") 
# else:
#     print ("No Error Occured")

#Q12
# def safe_divide (num1,num2):
#     try:
#         result=num1/num2
#         return (result)
#     except ZeroDivisionError:
#         print ("Cannot divide by 0")

# result=safe_divide(0,5)
# print (result)

print (__name__) #קשור לש.ב. 5