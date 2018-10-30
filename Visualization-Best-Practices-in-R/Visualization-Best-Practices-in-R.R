library(ggplot2)
library(dplyr)
library(waffle)

who_disease <- read.csv("who_disease.csv", stringsAsFactors = FALSE)

print(who_disease)
str(who_disease)

ggplot(who_disease, aes(x = region)) + geom_bar()

amr_cases_by_year <- who_disease %>%
                       filter(region == "AMR")

ggplot(amr_cases_by_year, aes(x = year, y = cases)) + geom_point(alpha = 0.5)

# Pie Chart
disease_counts <- who_disease %>%
                    mutate(disease = ifelse(disease %in% c('measles', 'mumps'), disease, 'other')) %>%
                    group_by(disease) %>%
                    summarise(total_cases = sum(cases))


ggplot(disease_counts, aes(x = 1, y = total_cases, fill = disease)) +
         geom_col()

ggplot(disease_counts, aes(x = 1, y = total_cases, fill = disease)) +
         geom_col() +
         coord_polar(theta = "y") +
         theme_void() +
         ggtitle(("Proportion of Diseases"))

# Waffle Chart
all_disease_counts <- who_disease %>%
                        group_by(disease) %>% 
                        summarise(total_cases = sum(cases)) %>% 
                        mutate(percent = round(total_cases / sum(total_cases) * 100))

all_disease_case_count_pct <- all_disease_counts$percent
names(all_disease_case_count_pct) <- all_disease_counts$disease

waffle(all_disease_case_count_pct)