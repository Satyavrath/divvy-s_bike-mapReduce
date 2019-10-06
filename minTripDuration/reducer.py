x = open("Mapperoutput.txt","r")
y = open("reduceroutput.txt","w")

k = []
for line in x:
    data = line.strip().split("\t")
    usertype,tripduration = data
    if(data[0] == "Subscriber"):
            k.append(int(float(data[1])))
def minTripDuration(l):
    low = l[0]
    for find_min in l:
        if low > find_min:
            low = find_min
    return low  
print(minTripDuration(k))      
y.write("{0}\t{1}\n".format(usertype,minTripDuration(k)))            

        