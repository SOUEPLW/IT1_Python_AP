myList = ["pomeranč", "jablko", "citron", "kumqat", "papája"]
print(myList)
print(len(myList))
print(myList[2])
duplist = myList[2:5]
print(duplist)
if "jablko" in myList:
    print("Jablko tam je ")
myList[2] = "samice hrabáče"
myList.append("mango")
myList.insert(1, "banán")
print(myList)