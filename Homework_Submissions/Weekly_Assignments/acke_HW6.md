### Claire Acke
### HWRS 501
### Forecast 6

### Grade
3/3 Great job!
- Note if you have a lot of numbers to report you can either use a markdown table or you can just take a screenshot of the table in vs code and insert that image into your markdown. 
- 
###

**Forecast Summary:** For the one week forecast, I have gone with 76cfs. For the second week forcast, I have gone with 82cfs. Both of these I feel like I have guessed closer to the minimum streamflow for October due to how little rain we have gotten recently. 

**1. Provide a summary of the dataframe properties (what are the column names, what is its index, what data types do each of the columns have?)**
Our dataframe contains a lot of information. The column names are 'agency_cd' (object), 'site_no' (integer), 'datetime' (object), 'flow' (float), 'code' (object), 'year' (integer), 'month' (integer), 'day' (integer). The index is 0-12698.

**2. Provide a summary of the flow column including the min, mean, max, standard deviation, and quartiles**
The min value of the flow is 19. Max value is 63400. Mean values is about 352.47. The standard deviation is about 1462.94. The values located at first, second, and third quartile are 93, 157, and 215. 

**3. Provide the same information but on a monthly basis (i.e., for all January, February, etc.) Should be able to do this with one of two lines of code**
**Jan** *Min:* 158 *Max:* 63400 *Mean:* 693.936 *STD:* 2641.52 *25%:* 202 *50%:* 220 *75%:* 314
**Feb** *Min:* 136 *Max:* 61000 *Mean:* 877.008 *STD:* 3208.74 *25%:* 199 *50%:* 238 *75%:* 612.5
**Mar** *Min:* 97 *Max:* 42200 *Mean:* 1064.49 *STD:* 2416.1 *25%:* 180 *50%:* 378 *75%:* 1070
**Apr** *Min:* 64.9 *Max:* 4690 *Mean:* 323.223 *STD:* 584.313 *25%:* 111 *50%:* 141 *75%:* 218.75
**May** *Min:* 39.9 *Max:* 546 *Mean:* 103.846 *STD:* 49.9289 *25%:* 76.6 *50%:* 92 *75%:* 118
**Jun** *Min:* 22.1 *Max:* 481 *Mean:* 65.0668 *STD:* 28.1913 *25%:* 48.325 *50%:* 60 *75%:* 76
**Jul** *Min:* 19 *Max:* 5270 *Mean:* 105.944 *STD:* 214.175 *25%:* 52 *50%:* 70 *75%:* 110
**Aug** *Min:* 29.6 *Max:* 5360 *Mean:* 170.844 *STD:* 288.914 *25%:* 78 *50%:* 116 *75%:* 178
**Sep** *Min:* 37.5 *Max:* 5590 *Mean:* 166.602 *STD:* 274.595 *25%:* 86.15 *50%:* 117 *75%:* 166
**Oct** *Min:* 55.7 *Max:* 1910 *Mean:* 144.805 *STD:* 110.96 *25%:* 106 *50%:* 126 *75%:* 153 
**Nov** *Min:* 117 *Max:* 4600 *Mean:* 199.985 *STD:* 225.677 *25%:* 153 *50%:* 171.5 *75%:* 197
**Dec** *Min:* 153 *Max:* 28700 *Mean:* 330.377 *STD:* 1052 *25%:* 189 *50%:* 203 *75%:* 225

**4. Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month, and flow values in your summary (Hint: you will want to use the sort_values function for this)**
| Flow Value | Date    | Month |
| ---------- | ------- | ----- |
| 19         | 7/1/12  | July  |
| 20.1       | 7/2/12  | July  |
| 22.1       | 6/30/12 | June  |
| 22.5       | 6/29/12 | June  |
| 23.4       | 7/3/12  | July  |
| 63400      | 1/8/93  | Jan   |
| 61000      | 2/20/93 | Feb   |
| 45500      | 2/15/95 | Feb   |
| 42200      | 3/22/23 | Mar   |
| 35600      | 2/12/05 | Feb   |

**5. Provide a list of historical dates with flows that are within 10% of your week 1 forecast value for the month of September. If there are none then increase the 10% window until you have at least one other value and report the date and the new window you used**
 
Overall, there are 970 dates that have a value within 10% of my forecast. Some dates would include 5/5/89-5/11/89, 8/2/95-8/10/95, and most recently 10/5/23-10/8/23. 


