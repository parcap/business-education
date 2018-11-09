library(readxl)
library(dplyr)
library(ggplot2)
library(tidyr)
library(broom)

setwd("C:/Users/njathar/Desktop/parcap-github/business-education/Correlation-and-Regression")

# Read in data external file
pf <- read_xlsx("par_performance_data.xlsx", sheet = "performance_ts")
pf$Date <- as.Date(pf$Date)

# Isolate SP500 column for downstream joining to gathered pf dataframe 
sp500 <- pf %>% select(Date, SP500)

# Store some useful variables here
max_date <- max(pf$Date)

# Gather the original pf dataframe and join to the sp500 dataframe
pfg <- pf %>% gather(Manager, Performance, -Date) %>% filter(!(Manager == "SP500")) %>% 
              right_join(sp500, by = "Date") %>%
              filter(!is.na(Performance))

# Various filtering objects
current_managers <- pull(pfg %>% filter(Date == max_date & !(Manager %in% c("Ed"))) %>% select(Manager) %>% unique(), Manager)

selected_manager <- "Bart"

# Various filtered datasets
pfg_selected_manager <- pfg %>% filter(Manager == selected_manager)
pfg_current_managers <- pfg %>% filter(Manager %in% current_managers)

list_pfg_current_managers <- list()

for (i in current_managers) list_pfg_current_managers[[i]] <- pfg_current_managers %>% filter(Manager == i)

selected_manager_scatter <- ggplot(data = pfg_selected_manager, aes(y = Performance, x = SP500)) +
                              geom_point()

facet_manager_scatter <- ggplot(data = pfg_current_managers, aes(y = Performance, x = SP500)) +
                             geom_point() +
                             geom_smooth(method = "lm", se = FALSE) +
                             facet_wrap(~Manager, ncol = 6)

facet_manager_boxplot <- ggplot(data = pfg_current_managers, aes(y = Performance, x = cut(SP500, breaks = 5))) +
                             geom_boxplot() +
                             facet_wrap(~Manager, ncol = 6)

lm_pfg_current_managers <- lapply(list_pfg_current_managers, function(x) lm(Performance ~ SP500, x))

#slopes <- sapply(lm_pfg_current_managers, function(x) coef(x))


