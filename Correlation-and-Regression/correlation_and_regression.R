library(readxl)
library(dplyr)
library(ggplot2)

setwd("C:/Users/njathar/Desktop/parcap-github/business-education/Correlation-and-Regression")

returns <- read_xlsx("StockData.xlsx")

stock_cor <- returns %>% group_by(Security) %>% 
               summarise(obs = n(),
                         corr = cor(StockReturn, SP500Return, use = "pairwise.complete.obs")) %>% 
               arrange(desc(corr))
               
selected_stock <- "BYD"

ggplot(data = filter(returns, Security == selected_stock), aes(y = StockReturn, x = SP500Return)) +
     geom_point()

ggplot(data = stock_cor , aes(y = corr, x = reorder(Security, corr))) +
     geom_bar(position = "dodge", stat = "identity") +
     coord_flip()