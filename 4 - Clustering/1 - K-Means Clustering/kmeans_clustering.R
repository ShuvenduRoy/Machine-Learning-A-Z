# K-means clustering

dataset <- read.csv('mall.csv')
x <- dataset[4:5]


# Using the elbow method to find the optimal number of clusters
set.seed(6)
wcss <- vector()
for (i in 1:10) wcss[i] <- sum(kmeans(x, i)$withinss)
plot(1:10, wcss, type = 'b')

# applying k-means to the mall
kmeans <- kmeans(x, 5, iter.max = 300, nstart = 10)


# Vialuslizing the cluesters
library(cluster)
clusplot(x,
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste('Clusters of clients')
         )