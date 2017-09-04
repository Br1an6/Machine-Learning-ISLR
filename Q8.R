LoadLibraries = function (){
  library(ISLR)
  library(MASS)
  print("The libraries have been loaded .")
}

LoadLibraries()
#Auto=read.table("Auto.data", header =T,na.strings ="?")
lm.fit =lm(mpg~horsepower ,data=Auto) # v1: mpg v4: horsepower
attach(Auto) # for plot
lm.fit =lm(mpg~horsepower)
summary(lm.fit)

# Confidence Intervals
print("Confidence Intervals:")
confint(lm.fit)

# start plotting
plot(horsepower, mpg)
abline(lm.fit)
abline (lm.fit ,lwd =3, col ="red")
