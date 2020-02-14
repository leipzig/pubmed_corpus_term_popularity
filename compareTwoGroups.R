library(ggplot2)
library(dplyr)
library(stringr)

read.table("compare.txt", header = TRUE) %>% dplyr::filter(pubmedFreq>0) %>% dplyr::filter(stringr::str_detect(string=word,pattern='^[^0-9]+$')) -> words

ggplot(words, aes(log(corpusFreq), log(pubmedFreq))) +
  geom_point(aes(color=category)) + geom_text(
                     label = words$word,
                     nudge_x = 0.20,
                     nudge_y = 0.15,
                     check_overlap = T
                   ) +
  geom_smooth(method = "lm")

words %>% dplyr::group_by(category) %>% dplyr::mutate(normalizedPubmedFreq=pubmedFreq/sum(corpusFreq)) -> statWord

t.test(normalizedPubmedFreq~category,statWord)
