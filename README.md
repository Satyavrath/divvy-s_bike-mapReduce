# Divvy Bike Data
 Our project group is 03.
## List of developers
- Akhila Gandra
- Jyoshna Boppidi
- Preetham Potu
- Satyavrath Injamuri
## Links
- https://github.com/Satyavrath/divvy-s_bike-mapReduce
## Introduction
This project is based on dataset containing data related to bike rentals. This is also used to implement map reduce functionality on this dataset. We have selected this dataset because it contains various coloumns which gave us various options to implement map reduce.
## Datasource 
This dataset contains a data from 1st quarter of 2018 which contains information of the bike rentals.The datasource is structured in excel sheet.
## Link to datasource
- https://www.kaggle.com/michaelshoemaker/divvy-bike-chicago-2018
## The Challenge
What makes it a big data problem? 
- Volume: There is 50.97MB of data in this dataset and 364,653 records. 1 quarter of 2018 data available in this dataset.
- Variety: This dataset is structured and it is in excel format.
- Velocity: Data will be generated based on people rented bike.  
- Veracity: Data is fully clear and clean. The  data is collected from divvybikes.com and it seems to be trustworthy and reliable.
- Value: With the data available we can figure out how many members subscribed for each quarter and the amount of distance on average people are using divvy's bike to travel. This data will be helpful in analyzing how many more bikes can be increased in the next quarter.

## Big Data Questions
For each Subscribe User type, find the maximum male gender. (Satyavrath Injamuri)
For each Subscriber User type, find the maximum tripduration. (Preetham Potu)

## Big Data Solutions

- #### Satyavrath Injamuri
  * Mapper Input: One line of data that mapper will read.
     * 17536702 1/1/2018 0:12 1/1/2018 0:17 3304 323 69 Damen Ave & Pierce Ave 159 Claremont Ave & Hirsch St Subscriber Male 1988
  * Mapper output / Reducer input: Tne below is the example of an intermediate key, value pair output by our mapper.
     * Subscribe Male
     * Subscribe Male
     * Subscribe Female
     * Customer Male
     * Customer Female
  * Reducer output:  show an example of a final key, value pair output by your reducer.
     * For Subscriber user type maximum male subscribed is 293,487 members.
  * Language used:
     * I am using python as a programming language to solve mapReduce.
  * What type of chart will you use to display your results?
     * I will use Bar Chart to display my result.
- #### Preetham Potu
  * Mapper Input: One line of data that mapper will read.
     * 17536702 1/1/2018 0:12 1/1/2018 0:17 3304 323 69 Damen Ave & Pierce Ave 159 Claremont Ave & Hirsch St Subscriber Male 1988
  * Mapper output / Reducer input: Tne below is the example of an intermediate key, value pair output by our mapper.
     * Subscribe 323
     * Subscribe 377
     * Subscribe 266
     * Customer  2782
     * Customer  74977
  * Reducer output:  show an example of a final key, value pair output by your reducer.
     * For each Subscriber user type maximum tripduration is 13557600 minutes.
  * Language used:
     * I am using python as a programming language to solve mapReduce.
  * What type of chart will you use to display your results?
     * I will use Bar Chart to display my result.

      
     



