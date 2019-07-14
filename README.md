# Airbnb-Boston-Data-Visualisation

Question 1:
Can you describe the vibe of each Boston neighborhood using listing descriptions?

Approach:
The input file contains one column for the comments and another row for different Boston neighborhoods. I will be using the Scikit-Learn NLP Library for sentiment analysis to get the result. The result will be in terms of the commentns being positive or negative or neutral in each Boston neighbourhood, thereby giving the vibe of each Boston neighbourhood.


Question 2:
What are the busiest times of the year to visit Boston? By how much do prices spike?

Approach:
1) For busiest times of the year: 
From one of the files, I get the dates in the format YYYYMMDD and get information regarding whether the hotel is available or not. I first convert all the dates in the given format to day of the year. For example, 30th January 2016 will be written as "30". This will make me identify the busiest time of the year easier. The availability options are given as 't' for available and 'f' for not available. I keep them as is. I plot this availability data against the converted day of the year and plot the graph. The maximum number of points in the 'f', which is unavailable section will give me the busiest time of the year. 


2) For price spike:
In the same file, keeping the x-axis date convertion the same, I plotted the average price of the hotels on the y-axis. The price spike is $120. The period with the spike is day 250 tp day 365 of the year. This is equivalent to September 7, 2016 to 31st December, 2016. 


Question 3:
Is there a general upward trend of both new Airbnb listings and total Airbnb visitors to Boston?

Approach: No new listings are present in the given file. Because there are no new listings, I cannot find any trend that might exist between the new Airbnb listings and the total Airbnb visitors to Boston.

