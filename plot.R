library(ggplot2)

read.table("compare.txt", header = TRUE)
words <- read.table("compare.txt", header = TRUE)

ggplot(words, aes(corpusFreq, log(pubmedFreq))) +
  geom_point(aes(label =
                   word)) + geom_text(
                     label = words$word,
                     nudge_x = 0.25,
                     nudge_y = 0.15,
                     check_overlap = T
                   ) +
  geom_smooth(method = "lm")
