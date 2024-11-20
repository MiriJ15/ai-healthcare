library(dplyr)
setwd("~/Desktop/MSCB_2024_Fall/AI for Healthcare/ai-healthcare")

sleep <- read.csv("sleep.csv", header=TRUE, sep=" ")
ema <- read.csv("general_ema.csv", header=TRUE)
ema <- ema %>% select(id, date, current_stress_level)

# Add ema data to their corresponding sleep data.
comb <- left_join(sleep, ema, by=c("id"="id", "date"="date"))

# Stress level surveys were not done daily.
# Therefore, impute the days without stress information with the first survey done after that day.
# This is done seperately for each ID.
fill_na_up <- function(x) {
  for(i in length(x):1) {
    if (is.na(x[i]) && i < length(x) && !is.na(x[i+1])) {
      x[i] <- x[i+1]
    }
  }
  return(x)
}
comb <- comb %>%
  group_by(id) %>%
  mutate(current_stress_level_imputed = fill_na_up(current_stress_level)) %>%
  ungroup()

# Remove rows with no stress information.
comb <- comb[!is.na(comb$current_stress_level_imputed),]

write.table(comb[comb$date<=20200311,], file="pre_covid_sleep_stress.csv", sep=",", row.names = FALSE, quote=FALSE)
write.table(comb[comb$date>20200311,], file="covid_sleep_stress.csv", sep=",", row.names = FALSE, quote=FALSE)
write.table(comb, file="all_sleep_stress.csv", sep=",", row.names = FALSE, quote=FALSE)
