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

zeleninaList = ["paprika", "mrkev", "okurka"]
myList.extend(zeleninaList)
print(myList)

myList.remove("kumqat") #odstraní kumqat
print(myList)

myList.pop(2) #odstraní položku podle indexu
print(myList)

print(zeleninaList)
zeleninaList.clear() #vyprázdní list
print(zeleninaList)

del zeleninaList #definitivne odstraní list

for i in myList:
    print(i)

    for i in range(len(myList)):
        print(myList[i])
