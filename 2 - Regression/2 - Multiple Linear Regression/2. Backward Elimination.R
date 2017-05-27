# Data Preprocessing

# Importing the dataset
dataset = read.csv('50_Startups.csv')

dataset$State = factor(dataset$State,
                         levels = c('New York', 'California', 'Florida'),
                         labels = c(1, 2, 3))


# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting multiple linear regressor
# regressor = lm(formula = Profit ~ .,
#                data = training_set)

# Step 1,2 : Taking all possible independent variable (full model)
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = dataset)
summary(regressor)

# Step 3, 4, 5 : remove less significant column/ feature and fit model again 
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, data = dataset)
summary(regressor)

# Step 3, 4, 5 : remove less significant column/ feature and fit model again 
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend, data = dataset)
summary(regressor)


# Step 3, 4, 5 : remove less significant column/ feature and fit model again 
# Removing even .06 p value
regressor = lm(formula = Profit ~ R.D.Spend, data = dataset)
summary(regressor)

# Predecting with MLR model
y_pred = predict(regressor, newdata = test_set)

