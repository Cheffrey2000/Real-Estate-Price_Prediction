# Module 1 Final Project
You can view my slide show here [Slide Show](https://docs.google.com/presentation/d/1ITFa71krhKkX4C8HIySYpUEuFkMvZifwNCHB182ttTc/edit?usp=sharing)


## Introduction

An analysis of the housing data from King county Washington.  This data set includes house sales in the county between May 2014 and May 2015.

## Goals
We are attempting to help realtors select profitable properties for their clients such as:
* New home buyers
* Families Relocating
* Investors looking for short term or long term investments
* Contractors looking to buy land and build


## The Dataset

The dataset consists of home sales from May 2014 through May 2015.  
The information provided for each home consists of the following categories:  
- **Price** - This is our target  
- **ID** - This is a unique identifier for each House in the dataset  
- **Date** - This is the date of sale  
- **Bedrooms** - This is the number of bedrooms in the house  
- **Bathrooms** - This is the number of bathrooms in the house  
- **Sqft_living** - This is the number of square feet in the living space  
- **Sqft_lot** - This is the number of square feet in the total lot area  
- **Floors** - This is the number of levels in the house  
- **Waterfront** - This denotes whether or not the property is on the water  
- **View** - This identifies how many times the house was viewed  
- **Condition** - This tells the condition of the house from 1 (worn out) to 5 (excellent)  
- **Grade** - The grade of the house based on the King County grading system of 1(poor) to 13(excellent)  
- **Sqft_above** - Total square feet without basement  
- **Sqft_basement** - Square footage of the basement alone  
- **Yr_built** - The year the house was originally built  
- **Yr_renovated** - The year the house was renovated if it has been  
- **Zipcode** - The zip code of the house  
- **Lat** - The latitude location of the house  
- **Long** - The longitude location of the house  
- **Sqft_living15** - The square footage of the home in the year 2015  
- **Sqft_lot15** - The square footage of the lot in 2015  


## Preparing the Data
To begin, we loaded the data set and took a look at it using visualizations like Seaborn's Pairplot.
Here is a summary of our observations:

- __*id*__ is simply an identifier<br>
    This will be removed as it is not pertinent to the data analysis.<br>
- __*date*__ is a string.<br>
    Our initial impression is that it reflects sale dates for the property.<br>
    This should be converted to a numerical value for processing.<br>
- There are two columns related to the size, __*sqft_living and sqft_lot*__ <br>
    We will explore their relationship and determine if they are dependent on each other or not<br>
- __*floors*__ is a numerical value.<br>
    Based on our knowledge of houses we believe this may be better suited to a categorical value.<br>
    We will explore the data and convert it to either a single or multiple<br> 
    or decide if each value of floors needs it's own category.<br>
- __*waterfront*__ is definitely categorical sine a home can only be either on or off the water.<br>
    We will convert this to a binary value to represent either on or off the water.<br>
- __*sqft_basement*__ <br>
    This along with __*sqft_above*__ combined are the same as __*sqft_living*__ so we will deal with it<br>
    since the presence of a basement is more significant than the size.<br>
    'sqft_basement will then be converted to categories which will identify the presence of a basement<br>
- __*zipcode*__ and __*lat*__ and __*long*__ are both location data.<br>
    We will determine if all are necessary and treat them accordingly<br>
- __*yr_renovated*__ has many null values so they will be used to create a new feature.<br>
    we will subtract it from the last date in the database and create __*ren_period*__

### Initial EDA
After cleaning the data, we took another look at it and found that there were some outliers.  
The outliers were:
- __*bathrooms*__ above 10
- __*bedrooms*__ above 10
- __*sqft_living*__ above 10000
- __*grade*__ of 13 which is a top of the line custom home.  
- __*sqft_lot*__ above 750000

They were then dropped from the working data

### Multicolinearity  

There were a few features that were multicolinear so we engineered some features to combine those.
- __*bathrooms*__ and __*grade*__ are colinear, so we will create a new feature combining the  
two into one feature, __*grade_bathroom*__.
- __*sqft_living*__ and __*grade*__ have a high correlation so those were engineered into  
     a feature called __*sqft_living_bedrooms*__

After feature engineering and running a few test models, we settled on the following features:
- sqft_lot
- waterfront
- condition
- sqft_basement
- ren_period
- sqft_living_bedrooms
- grade_bathroom


Using these features, we ran the model with a few different combinations and found some multicolinearity.  
We settled on:
- 'sqft_living_bedrooms'
- 'condition'
- 'lat'
Our R-squared is at .63 so this is a pretty good model  
and our mean squared error is .09 so it is pretty accurate. 

### Conclusion
Price is affected mainly by 'sqft_living_bedrooms' 'lat' and 'condition'
