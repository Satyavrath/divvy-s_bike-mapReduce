input_mapper = open("../data/Divvy_Trips_2018_Q1.txt","r") # open file, read-only raw data
output_mapper = open("output_mapper.txt","w")# open file, write - just our key, value pairs
# For loop for reading each line from the text file
for line in input_mapper:
       # splits the line separated by comma
    data = line.strip().split(',')
     # Checking the length of array
    if (len(data) == 12):
        # assign list to each variable
        trip_id, start_time, end_time, bikeid, tripduration, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthyear = data
        output_mapper.write(usertype+","+birthyear+"\n")
                # printing usertype and birthyear to console input
        print(usertype+","+birthyear+"\n")
        #closing files
input_mapper.close()
output_mapper.close()