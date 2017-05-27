# Data Preprocessing

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]


# Create a linear model for comperasion
lin_reg = lm(formula = Salary ~ ., 
             data = dataset)
summary(lin_reg)


# Fitting polynomial regression to the dataset
dataset$Level2 = dataset$Level ^ 2
dataset$Level3 = dataset$Level ^ 3
poly_reg = lm(formula = Salary ~ .,
              data = dataset)
summary(poly_reg)

