# Decision Tree Regression
library(rpart)

# Importing the dataset
setwd("C:/Users/njathar/Desktop/parcap-github/udemy/MachineLearning/Part 2.8 - Decision Tree Regression")

dataset <-  read.csv('Position_Salaries.csv')
dataset <-  dataset[2:3]

regressor <- rpart(formula = Salary ~ ., data = dataset)
