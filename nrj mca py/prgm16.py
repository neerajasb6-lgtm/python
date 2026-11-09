data={"apple":50,"banana":20,"orange":30,"grapes":100}
ascending=sorted(data,key=lambda key:key)
descending=sorted(data,key=lambda key:key,reverse=True)
print("Ascending",ascending)
print("Descending",descending)
