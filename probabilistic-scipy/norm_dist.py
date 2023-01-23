import scipy.stats
import matplotlib.pyplot as plt
import numpy

n1 = scipy.stats.norm(0.0, 1.0) # mean at 0.0, standard deviation of 1.0
print(f"mean={n1.mean()},  std={n1.std()},  probability density function={n1.pdf(0)}")

x = numpy.linspace(-2, 2, 3000)
mean = 0
sigma = 1

probability_density_function = scipy.stats.norm.pdf(x, mean, sigma)
cumulative_distribution_function = scipy.stats.norm.cdf(x, mean, sigma)

plt.plot(x, probability_density_function, label='Probability Density Function')
plt.plot(x, cumulative_distribution_function, label='Cumulative Distribution Function')
plt.legend();
plt.show()