import matplotlib.pyplot as plt

__author__ = "Aaditya Kumar Rai"
__version__ = "1.0.0"
__maintainer__ = "Aaditya Kumar Rai"
__email__ = "raiaaditya999@gmail.com"

class PlotGraph:
	def plot(self,dataSet):
		lines = [line.strip() for line in open(dataSet)]
		plt.plot(lines)
		plt.ylabel('rate')
		plt.show()
		print lines
