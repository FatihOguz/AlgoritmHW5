###############################################
def sumZeroCheck(set):
	s=sum(set)
	if(s==0):
		return True
	return False
###############################################
def dynamicSubSet(set):
	for i in range(len(set)):
		for j in range(i+1):
			subSets[i].append(set[j])
		check.append(sumZeroCheck(subSets[i]))
	return subSets		

###############################################
subSets=[[], [], [] ,[],[],[]] 
check=[]
set=[2, 3, -5, -8, 6, -1]
dynamicSubSet(set)
for i in range(len(subSets)):
	print(subSets[i])
	print(check[i])
###############################################