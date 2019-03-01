setwd("C:/Users/njathar/Desktop/parcap-github/business-education/Machine-Learning-Toolbox")

library(readxl)
library(writexl)
library(caret)

donors <- read.csv("donors.csv")

table(donors$donated)

donation_model <- glm(donated ~ bad_address + interest_religion + interest_veterans,
                      data = donors,
                      family = "binomial")

summary(donation_model)

donors$donation_prob <- predict(donation_model, type = "response")

donors$donation_pred <- ifelse(donors$donation_prob > mean(donors$donated), 1, 0)

mean(donors$donated == donors$donation_pred)


# stocks <- read_xlsx("AMD_data.xlsx")
# stocks <- stocks[!is.na(stocks$Return_1SF), c(5, 7)]
# 
# set.seed(42)
# 
# obs <- nrow(stocks)
# stocks <- stocks[sample(obs), ]
# 
# stocks$Great_Return <- as.factor(stocks$Great_Return)
# 
# split <- round(obs * 0.6)
# 
# stocks_train <- stocks[1:split, ]
# stocks_test <- stocks[(split + 1):obs, ]
# 
# model <- glm(Great_Return ~ ., family = "binomial", stocks_train)
# prediction <- predict(model, stocks_test, type = "response")
# prediction_class <- ifelse(prediction > 0.5, 1, 0)
# prediction_cf <- factor(prediction_class, levels = levels(stocks_test$Great_Return))
# confusionMatrix(prediction_cf, stocks_test$Great_Return)