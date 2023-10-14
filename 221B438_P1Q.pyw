def check(email):
    result=[]
    temp1=[]
    temp2=[]
    name=[]
    domain=[]
    temp1+=email.split('@')
    temp2+=temp1[0].split('.')
    for i in range(len(temp2)) :
        name.append(temp2[i].capitalize())
    temp3=[]
    temp3+=temp1[1].split('.')
    domain.append(temp3[0].upper())
    result.append(name)
    result.append(domain)
    return result

email=input("enter email id : ")
print(check(email))
    
                   
        
        
    

