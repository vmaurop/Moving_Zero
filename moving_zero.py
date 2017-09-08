
#coding=utf8
number_list=[]
while (1):
    user_input=raw_input("Give a number or enter to end the entry:")
    if user_input == "":
	break  
    number_list.append(int(user_input))  
for i in number_list:
    if i == 0:      
        number_list.append(i)  
        number_list.remove(i)   
print number_list


