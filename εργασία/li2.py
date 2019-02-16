
def sumInterval():
	x=[]
	n=input("poses listes thes?")
	n= int(n)
	sum=0
	l=[]
	pl=0
	p=0
	
	for y in range(n):
		li=[]
		num=int(input("dwse prwto arithmo gia thn lista"))
		li.append(num)
		num2=int(input("dwse deutero arithmo gia thn lista"))
		li.append(num2)
		x.append(li)
	
		y=num2 - num
		sum=sum +y
		k= sum 
	for i in range (0,n-1,1):
		if (x[i][1]<x[i+1][0]):
			p=0
		else:
			p=1
	if p==0:
		print (k)
	else:
		for i in range(len(x)):
			for m in range(2):
				l.append(x[i][m])
		t=[]
		t=sorted(l, key=int)
	
		for i in range(1,len(t) -1,):
			s=t[i+1]- t[i]
			pl=pl + s
		print (pl)
			
	
			
		
	
	
	
sumInterval()
	





