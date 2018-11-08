library(readxl)
library(dplyr)
library(ggplot2)
library(tidyr)

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

current_managers <- pfg %>% filter(Date == max_date)

selected_manager <- "Bart"

single_manager_scatter <- ggplot(data = pfg %>% filter(Manager == selected_manager), aes(y = Performance, x = SP500)) +
                              geom_point()

facet_manager_scatter <- ggplot(data = pfg %>% filter(Manager %in% unique(current_managers$Manager)), aes(y = Performance, x = SP500)) +
                             geom_point() +
                             geom_smooth(method = "lm", se = FALSE) +
                             facet_wrap(~Manager, ncol = 7)

facet_manager_boxplot <- ggplot(data = pfg %>% filter(Manager %in% unique(current_managers$Manager)), aes(y = Performance, x = cut(SP500, breaks = 5))) +
                             geom_boxplot() +
                             facet_wrap(~Manager, ncol = 7)


facet_manager_boxplot