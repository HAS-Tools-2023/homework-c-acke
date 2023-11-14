### Claire Acke
### HWRS 501
### Forecast 9

### Grade: 8/9
Readability: 2.75/3 
    - There were comments throughout but a lot of them were notes on things that could be done differently and not all steps were clearly commented. Totally fine to have notes to yourself in drafts but for this graded script the assignment was to provide as close to a clean code as possible with just comments on whats happening along the way for other people running the code. 
    - In general your variable names were good but some of them were very long and specific to the date range you are testing. I would consider how to make this code more generalizable with your variable names. 
Style: 2.75/3
    - Consider adding some breaks to your code to make the sections clearer
    - There were still multiple linting issues with spaces around function parameters and comments that I cleaned up. Hopefully some of the things I cleaned up for you will answer the questions you had about linting below. Feel free to stop by office hours if you have more questions though.  
Code:  2.25/3
    - The code wouldn't run because of local file paths (-0.5). 
    - I left some comments throughout your code on ways you can make it more efficient. 
    - Overall the biggest suggestion I have is to modify your code so that its not all hard coded to a specific forecast date and that your variable names are more flexible. 
    - I would also suggest you experiment a bit more with creating functions. The mean one from class is a good starting point but I would like to see you expand from there. 



**Forecast** 
My forecast for week one is 132.34, and my forecast for week two is 137.87.

**1:** I created this forecast by taking the mean of all historical values for the dates in week one and in week two, then subtracting 50 because we are lower than average with rainfall.

**2:** This week, I added a function that can find the mean of a dataframe. I wanted to make a function that could create a function that pull flow values over a week period when the timeperiod is over two different months, so then two different indices.

**3:** I like to do a lot of means, and it may be easier to do a function if we want to mean an isolated row or dataframe.

**4. Remaining questions:** I have a few questions about the linting process because some of the things that I got don't really make sense to me. How do I get rid of 'trailing whitespace' when using the linter? It comes up for my line 15. Also, does it matter how long my lines are if they are comments? I tend to write myself comments a lot for my future self so I don't forget things. Third, I'm confused by how my parenthesis in my return function are unnecessary because it says it is. Lastly, my two warnings are about an expression not being assigned to the print statements at the bottom and I didn't think that was required. 