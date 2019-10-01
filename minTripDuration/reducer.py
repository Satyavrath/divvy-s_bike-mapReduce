x = open("Mapperoutput.txt","r")
y = open("reduceroutput.txt","w")

k = []
for line in x:
    data = line.strip().split("\t")
    if(data[0] == "Subscriber"):
            k.append(int(float(data[1])))
y.write("{0}\t{1}\n".format("Subscriber",min(k)))            
print(min(k))
        