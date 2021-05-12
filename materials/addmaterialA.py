lines = 3
listref = []
a = {}
a["Quantity"]={}
a["component_name"]={}
for line in lines:
    d = line.split(',')
    if len(d) != 3 or d[2]=='':
        print(d)
        continue
    index = d[1]
    if d[1]=='':
        index = d[0]
    listref.append(index)
    a["component_name"][index]=d[0]
    a["Quantity"][index]=d[2]


for ref in listref:
    try:
        Material.objects.create(component_name = a["component_name"][ref],reference = ref,Quantity = a["Quantity"][ref])
    except IntegrityError:
        print(ref+" is duplicate") 
