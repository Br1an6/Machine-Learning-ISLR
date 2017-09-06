LoadLibraries = function (){
  library(ISLR)
  library(MASS)
  print("The libraries have been loaded .")
}

LoadLibraries()
#Auto=read.table("Auto.data", header =T,na.strings ="?")
pairs(Auto) # scatterplot matrix
cor(Auto[,1:8]) # correlations between the variables without names

lm.fit =lm(mpg~.-name,data=Auto)
attach(Auto) # for plot
lm.fit =lm(mpg~.-name)
summary(lm.fit)

# start plotting
plot(lm.fit)

Auto2 = Auto[,1:8]
lm2.fit = lm(mpg~.*., data = Auto2)
summary(lm2.fit)

plot(log(horsepower), mpg)
plot(sqrt(horsepower), mpg)
plot((horsepower)^2, mpg)
