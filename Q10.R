LoadLibraries = function (){
  library(ISLR)
  library(MASS)
  print("The libraries have been loaded .")
}

LoadLibraries()
lm.fit =lm(Sales~Price + Urban + US, data = Carseats)
attach(Carseats) # for plot
lm.fit =lm(Sales~Price + Urban + US)
summary(lm.fit)

#uses the predictors for which there is evidence of association with the outcome
lm2.fit = lm(Sales~Price + US, data = Carseats)
summary(lm2.fit)

# Confidence Intervals
print("Confidence Intervals:")
confint(lm2.fit)

# start plotting
plot(lm.fit)
plot(lm2.fit)