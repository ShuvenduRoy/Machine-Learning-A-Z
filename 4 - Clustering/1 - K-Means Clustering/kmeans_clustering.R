# K-means clustering

dataset <- read.csv('mall.csv')
x <- dataset[4:5]


# Using the elbow method to find the optimal number of clusters
set.seed(6)
wcss <- vector()
for (i in 1:10) wcss[i] <- sum(kmeans(x, i)$withinss)
plot(1:10, wcss, type = 'b')

