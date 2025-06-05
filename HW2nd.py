#List
# list= ["cherry","apple","banana",]
# list.append("date") #להוסיף ערך בסוף הליסט
# print(len(list)) #להדפיס אורך ליסט
# list.remove("apple") #להסיר ערך מהליסט
# print (list)
# list.sort() #לסדר לפי א',ב
# print(list)

#Set
# set= {3,1,4,1,5,9}
# contains_7= 7 in set #בודק האם הערך קיים בסט
# print (contains_7)
# print (type(set))

#Tuple
# tuple= ("dog","cat","fish")
# print (tuple[2])
# listconv= list(tuple) #המרת טופל לליסט
# print(listconv) 

#שאלות רנדומליות מש.ב.
# twoDlist= [[10,20],[30,40]]
# print(twoDlist[1][1]) 
# print

# list1=[12,5,8]
# maxnum=max(list1) #מציאת ערך מקסימלי
# print (maxnum)

# list2=[6,4,2]
# revlist2=[6,4,2][::-1] #מסדר בסדר הפוך את הרשימה
# print(revlist2)

# Function1
def multipy_numbers (num1,num2): #פונקציית מכפלה של 2 מספרים
    return (num1*num2)
# mult=(multipy_numbers(4,7))
# print(mult)

# Function2
def calculate_square (number): #פונקציה של להעלות מספר בריבוע
    return (number*number)
# squarenum=calculate_square(6)
# print (squarenum)

# Function 3
def calculate_average (list): #פונקציה שעושה ממוצע לרשימה
    total=sum(list) #פעולה שסוכמת רשימה
    length=len(list)
    return (total/length)
# avg=calculate_average([4,7,2,1,6,9])
# print (avg)
