#!/usr/bin/env Rscript

library(optparse)
library(ggplot2)
library(dplyr)
library(stringr)

option_list = list(
  make_option(c("-f", "--file"), type="character", default="compare.txt", 
              help="dataset file name", metavar="character")
); 

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

read.table(opt$file, header = TRUE) %>% dplyr::filter(pubmedFreq>0) %>% dplyr::filter(stringr::str_detect(string=word,pattern='^[^0-9]+$')) -> words

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
