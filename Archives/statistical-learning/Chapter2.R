college <- read.csv("College.csv")

# fix(college)    <- this function is used to view the data frame

rownames(college) <- college[, 1]
college <- college[, -1]

summary(college)

pairs(college[, 1:10])

plot(college$Private, college$Outstate, xlab = "Is Private?", ylab = "Out-of-State Tuition")