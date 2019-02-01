# Data Preprocessing

# Importing Libraries
library(caTools)

# Set Working Directory
setwd("C:/Users/njathar/Desktop/parcap-github/udemy/MachineLearning/Part 1 - Data Preprocessing")

# Importing Datasets
dataset <- read.csv("Data.csv")
# dataset <- dataset[ , 2:3]

# Determine which variable is the dependent variable and which are the independent variables (features).

# Handle missing values
dataset$Age <- ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(dataset$Age, na.rm = T)), dataset$Age)
dataset$Salary <- ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(dataset$Salary, na.rm = T)), dataset$Salary)

# Encoding Categorical Data
dataset$Country <- factor(dataset$Country, levels = c("France", "Spain", "Germany"), labels = c(1, 2, 3))

dataset$Purchased <- factor(dataset$Purchased, levels = c("No", "Yes"), labels = c(0, 1))

# Splitting Data into a Training Set (usually 80% of the data) and a Test Set
set.seed(123)

split <- sample.split(dataset$Purchased, SplitRatio = 0.8)

training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

# Feature Scaling
training_set[ , 2:3] <- scale(training_set[ , 2:3])
test_set[ , 2:3] <- scale(test_set[ , 2:3])