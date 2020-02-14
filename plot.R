#!/usr/bin/env Rscript

library(ggplot2)
library(optparse)

option_list = list(
  make_option(c("-f", "--file"), type="character", default="results.txt", 
              help="dataset file name", metavar="character")
)

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

read.table(opt$file, header = TRUE) %>% dplyr::filter(pubmedFreq>0) %>% dplyr::filter(stringr::str_detect(string=word,pattern='^[^0-9]+$')) -> words

ggplot(words, aes(log(corpusFreq), log(pubmedFreq))) +
  geom_point() + geom_text(
                     label = words$word,
                     nudge_x = 0.25,
                     nudge_y = 0.15,
                     check_overlap = T
                   ) +
  geom_smooth(method = "lm")
