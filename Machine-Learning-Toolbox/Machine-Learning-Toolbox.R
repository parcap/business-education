library(readxl)
library(writexl)

setwd("C:/Users/njathar/Desktop/parcap-github/business-education/Machine-Learning-Toolbox")

stock_data <- read_xlsx("StockData.xlsx")

months <- 12

train <- stock_data[2:(months + 1), ]
test <- stock_data[14:25, ]

stock_model <- lm(StockRet ~ BenchRet, train)

stock_predict <- predict(stock_model, test)

stock_model_error <- stock_predict - test$StockRet

stock_model_os_rmse <- sqrt(mean(stock_model_error ^ 2))

stock_is_predict <- predict(stock_model, train)

stock_model_is_error <- stock_is_predict - train$StockRet

stock_model_is_rmse <- sqrt(mean(stock_model_is_error ^ 2))