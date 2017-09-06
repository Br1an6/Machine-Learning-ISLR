set.seed(1)
x = rnorm(100, 0, 1)
eps = rnorm(100, 0, 0.25)

y = -1 + 0.5*x + eps
length(y)
summary(y)

lm.fit = lm(y~x)
summary(lm.fit)

# start plotting
plot(x,y)

abline(lm.fit)

lm2.fit = lm(y~poly(x, 2))
summary(lm2.fit)