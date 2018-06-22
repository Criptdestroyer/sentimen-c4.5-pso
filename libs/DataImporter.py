import pandas as pd

class DataImporter():

	def __init__(self, filename):
		self.df = pd.read_excel(filename)
		self.labels = { "Positive": 0, "Negative": 0, "Neutral": 0 }

	def count_labels(self):
		for index, row in self.df.iterrows():
			if row["Label"] == "Berdampak positif":
				self.labels["Positive"] += 1
			elif row["Label"] == "Berdampak negatif":
				self.labels["Negative"] += 1
			elif row["Label"] == "Netral":
				self.labels["Neutral"] += 1

	def get_labels(self):
		return self.labels

	def get_data(self):
		return self.df
