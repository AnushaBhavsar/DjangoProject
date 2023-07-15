qlist=[]
print("Quiz Application")
print('''Select your choice:
	1. Attemp the Quiz
	2. Add a question
	3. Exit''')
ch=0
while(ch != 3):
	ch=int(input("Enter your chioce : "))
	if ch==1:
		print("Attemp the quiz")
		for q in qlist:
			rans=0
			wans=0
			print(q['qt'])
			print(q['a'])
			print(q['b'])
			print(q['c'])
			print(q['d'])
			ans=input("Ans")
			if q['CAns']==ans:
				rans=rans+1
			else:
				wans=wans+1

			print("Right Ans : ",+rans)
			print("Wrong Ans : ",+wans)

		if ans!=q:
			print("Choose correct option")

		
	if ch == 2:
		q={}
		q['qt']=input("Enter Question")
		q['a']=input("Option A")
		q['b']=input("Option B")
		q['c']=input("Option C")
		q['d']=input("Option D")
		q['CAns']=input("Correct Option")
		qlist.append(q)
		print("Add New Question Here:")

