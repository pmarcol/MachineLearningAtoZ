# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')
### JUST IN NEED WE WILL NEED TO TAKE A SUBSET OF THE IMPORTED DATASET.
# dataset = [, 2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

###  IN THE MOST OF THE TIMES WE WILL NOT NEED TO DO THE FEATURE SCALING,
### BECAUSE IT WILL BE A PART OF THE ALGORITHM.
# # Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])