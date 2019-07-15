# Airbnb-Boston-Data-Visualisation

Question 1:
Can you describe the vibe of each Boston neighborhood using listing descriptions?

Approach:
The input file contains one column called description which has the description of the Airbnb guests and another row for different Boston neighborhoods. I will be using the Scikit-Learn NLP Library for sentiment analysis to get the result. The description column would cluster around descriptive words thereby giving us the vibe of each Boston neighbourhood. Sentiment analysis to get the sentiment attached and Summarisation to fetch highly associated and informative words from the description. Using clustering, we can find common cluster center's which define the vibe of the neighbourhood.
Reference: https://www.kaggle.com/bnsmith3/phrases-that-charactertize-each-neighborhood 


Question 2:
What are the busiest times of the year to visit Boston? By how much do prices spike?

Approach:
1) For busiest times of the year: 
From one of the files, I get the dates in the format YYYYMMDD and get information regarding whether the hotel is available or not. I first convert all the dates in the given format to day of the year. For example, 3th February 2016 will be written as "34". 7. Period with the global maxima would be my busiest period. Using this, I plotted the availability and identified the busiest period of the year. The availability options are given as 't' for available and 'f' for not available. I plot this availability data against the converted day of the year and plot the graph. The maximum number of points in the 'f', which is unavailable section will give me the busiest time of the year. 

Output Plot:
![](filename Availability.png)


2) For price spike:
In the same file, keeping the x-axis date convertion the same, I plotted the average price of the hotels on the y-axis. the highest average price spikes upto $120. The period with the spike is day 345 to day 365 of the year. This is equivalent to December 11, 2016 to 31st December, 2016. 


Question 3:
Is there a general upward trend of both new Airbnb listings and total Airbnb visitors to Boston?

Approach: No new listings are present in the given file. After quick analysis, I did not find any new listings in the availability dataset, hence we cannot find any trend that might exist between the new Airbnb listings and the total Airbnb visitors to Boston.


Question 4:
Given the context and data, what kind of machine learning techniques can be used to address the problem?

Approach: One large scale Analysis where all this can come together is predicting if a new listing will have good reviews or not. And a deeper analysis of what leads to bad reviews. The machine learning technique used for question one to get the vibe of the data involves technique naturally involves NLP, where each word in sentences of the "description" column gave a sentiment of the Airbnb guest. In question two, for both the parts of busiest times and price hike, there is a time series analysis done. 


