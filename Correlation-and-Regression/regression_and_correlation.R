library(readxl)
library(dplyr)

Anscombe <- read_xlsx("anscombes_quartet.xlsx")

Anscombe_stats <- Anscombe %>% group_by(set) %>%
                               summarise(N = n(), mean(x), sd(x), mean(y), sd(y), cor(x, y))

print(Anscombe_stats)