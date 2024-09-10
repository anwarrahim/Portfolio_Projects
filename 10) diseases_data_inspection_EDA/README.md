# EDA: Inspect, Clean, and Validate a Dataset
### Learn how EDA can inform the data cleaning process.

# Introduction

One of the most challenging parts of data cleaning is diagnosing data issues and figuring out HOW to most effectively address them. In order to accomplish this, exploratory data analysis (EDA) can be an extremely useful tool. In this article, we’ll walk through an example dataset to demonstrate how EDA can inform the initial data inspection, cleaning, and validation process.

While this article serves as an introduction to EDA for data cleaning, it is important to note that every dataset is different, and therefore will require different exploration. EDA is all about following the data, verifying your assumptions, and investigating anything that is unexpected.

# Initial Data Inspection

Before analysis or cleaning, it is useful to print a few rows of data. This helps ensure that the data is properly loaded. It also allows us to compare the observed data to the data dictionary and determine whether the coding appears to match our expectations. For example, let’s load and inspect the first few rows of a dataset of heart disease patients (downloaded from the UCI Machine Learning Repository(https://archive.ics.uci.edu/ml/datasets/heart+disease) ).

```
import pandas as pd
heart = pd.read_csv('processed.cleveland.data.csv')
print(heart.head()) 
```






