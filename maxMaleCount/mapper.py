fo = open("..\data\Divvy_Trips_2018_Q1.txt","r") # open file, read-only raw data
mapperOutput = open("mapperOutput.txt","w") # open file, write - just our key, value pairs
# print(len(fo))
value = 0
for line in fo:
    # parses for line starting with quotes
    if '"' in line:
        # replaces time duration with ',' to numerical format
        line = line.replace(line[line.index('"'):line.rindex('"')], line[line.index('"'):line.rindex('"')].replace(",", ""))
    # splits the line separated by comma
    data = line.split(",")
    # assign list to each variable
    trip_id,start_time,end_time,bikeid,tripduration,from_station_id,from_station_name,to_station_id,to_station_name,usertype,gender,birthyear = data
    # writes file into new mapperOutput.txt file
    mapperOutput.write("{0}\t{1}\n".format(usertype,gender))
    value+=1
  #  print(("{0}\t{1}\n".format(usertype,gender)))
print(value)
fo.close()
mapperOutput.close()           
    
       
