def showSubjecName():
	print("AI for Robot System")
	

def showStudentYear():
	a = int(input())
	digits = [int(i) for i in str(a)]
	b = 6 - digits[1]
	print("year ",b)
	
	
	
def calculator():
	a = input ()
	b = int(input())
	c = int(input())
	if a == "+" :
		print(b+c)
		
	if a == "-":
		print(b-c)
	if a == "*" : 
		print(b*c)
	if a == "/" :
		print(b/c)

def main():
	a = input()
	if a == "subject" : 
		showSubjecName()
	if a == "year" :
		showStudentYear()
	if a == "calc" :
		calculator()

x = 0 		
while x == 0 :
	main()
	x = 0		

