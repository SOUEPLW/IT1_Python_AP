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
        
abeceda = ["A", "F", "C", "D"]
abeceda.sort()
print(abeceda)

abeceda.sort(reverse = True)
print(abeceda)

myList.sort()
print(myList)

myList.sort(key=str.lower)
print(myList)

nums = [100, 50, 65, 82, 23]
nums.sort()
print(nums)

nums.reverse()
print(nums)

myList2 = myList
print(myList)
print(myList2)
myList2[0] = "malina"
print(myList2)
print(myList)

copyList = myList.copy()
copyList[0] = "ořech"
print(myList)
print(copyList)
