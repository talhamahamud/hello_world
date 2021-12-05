#Password craking via python. Fully programed and all logic created by myself !!! 
import random

while True:
    x = ["1", "2", "3", "4","5","6","7","8","9","0"]
    rr = random.choice(x)
    hh = random.choice(x)
    gg = random.choice(x)
    tt = random.choice(x)
    pp = int(rr + hh + gg + tt)#converting all string into int.
    print("trying.....")
    if pp==1324: #here 1324 is the password
        print("Congratulaion! we have got the password!!! and that is 1324")
        break

