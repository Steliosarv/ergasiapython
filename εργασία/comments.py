code = open("com.py","r")
code_back = open("new_com.py","w")

for line in code:
    if not line.startswith("#"):  
        code_back.write(line)
		

code.close()
code_back.close()