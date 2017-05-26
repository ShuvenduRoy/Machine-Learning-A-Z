# Data Preprocessing

# Importing the dataset
dataset = read.csv('Salary_Data.csv')


# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


# Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])


# Fitting simple linear Regression to the training set
regressor = lm(formula = Salary ~ YearsExperience,
               data=training_set)


# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             color = 'red') +
  geom_line(aes(x = training_set$YearsExperience, predict(regressor, newdata = training_set)),
            color = 'blue') +
  ggtitle('Salary VS Experience ( Training Set)')+
  xlab('Years of experience') +
  ylab('Salary')


ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             color = 'red') +
  geom_line(aes(x = training_set$YearsExperience, predict(regressor, newdata = training_set)),
            color = 'blue') +
  ggtitle('Salary VS Experience ( Test Set)')+
  xlab('Years of experience') +
  ylab('Salary')


