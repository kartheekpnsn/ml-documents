library(doParallel)

cl <- makeCluster(detectCores())
registerDoParallel(cl)
clusterEvalQ(cl, library(randomForest))

data <- data.frame(ntrees = c(100, 200), mtry = c(2, 3))
foreach(row = iter(data, by="row"), .combine=c) %dopar% {
  fit = randomForest(Species ~ ., data = iris, ntrees = row[[1]], mtry = row[[2]])
  sum(fit$predicted == 'setosa')
}
stopCluster(cl)
