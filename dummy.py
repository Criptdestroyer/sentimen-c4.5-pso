from sklearn.decomposition import PCA
from entities.Storage import Storage
from libs.TFIDF import TFIDF
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

s = Storage()
data = s.load("../pckl2/preprocessed/preprocessed.pckl")
tfidf = TFIDF(data["Review"])
# english_labels = {
# 	"Berdampak positif": "Positive Review",
# 	"Berdampak negatif": "Negative Review",
# 	"Netral": "Neutral Review"	
# }
english_labels = {
	"Berdampak positif": "Berdampak positif",
	"Berdampak negatif": "Berdampak negatif",
	"Netral": "Netral"	
}
# groups = {
# 	"Positive Review": "green",
# 	"Negative Review": "red",
# 	"Neutral Review": "blue"
# }
groups = {
	"Berdampak positif": "green",
	"Berdampak negatif": "red",
	"Netral": "blue"	
}
translated_labels = [english_labels[label] for label in data["Label"]]
colors = np.array([groups[x] for x in translated_labels])

pca = PCA(n_components=2).fit(tfidf.weights)
data2D = pca.transform(tfidf.weights)
x_std = np.std(data2D[:, 0])
y_std = np.std(data2D[:, 1])

plt.xlabel("Komponen 1")
plt.ylabel("Komponen 2")
plt.title("Distribusi Titik Data Ulasan Grafik 2D")

for label in set(data["Label"]):
	plt.scatter(data2D[data[data["Label"] == label].index.values][:,0], data2D[data[data["Label"] == label].index.values][:,1], c=colors[data[data["Label"] == label].index.values], label=english_labels[label], edgecolors='black')
plt.legend(loc="lower right")
plt.grid()
plt.show()

# print(data2D.shape)
# true_x = data2D[:, 0] <= x_std
# data2D = data2D[data2D[:, 0] <= x_std]
# true_y = data2D[:, 1] <= y_std
# data2D = data2D[data2D[:, 1] <= y_std]

# data = data.iloc[true_x].reset_index(drop=True)
# data = data.iloc[true_y].reset_index(drop=True)
# print(data2D.shape)

# plt.xlabel("Component 1")
# plt.ylabel("Component 2")
# plt.title("Data Distribution in 2D Scatter Plot")

# for label in set(data["Label"]):
# 	plt.scatter(data2D[data[data["Label"] == label].index.values][:,0], data2D[data[data["Label"] == label].index.values][:,1], c=colors[data[data["Label"] == label].index.values], label=english_labels[label], edgecolors='black')
# plt.legend(loc="lower right")
# plt.grid()
# plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
pca = PCA(n_components=3).fit(tfidf.weights)
data3D = pca.transform(tfidf.weights)
for label in set(data["Label"]):
	ax.scatter(data3D[data[data["Label"] == label].index.values][:,0], data3D[data[data["Label"] == label].index.values][:,1], c=colors[data[data["Label"] == label].index.values], label=english_labels[label], edgecolors='black')
ax.legend(loc="lower left")
ax.grid()
ax.set_xlabel('Komponen 1')
ax.set_ylabel('Komponen 2')
ax.set_zlabel('Komponen 3')
plt.title("Distribusi Titik Data Ulasan Grafik 3D")

plt.show()

# import numpy as np, matplotlib.pyplot as plt

# # c45_scores = np.array([51.58, 56.38, 56.38, 50.00, 55.32, 53.19, 57.45, 51.06, 56.38, 57.45])
# c45_scores = np.array([54.74, 53.19, 56.38, 50.00, 57.45, 57.45, 55.32, 52.13, 55.32, 60.64])
# # c45_scores = np.array([49.47, 56.38, 55.32, 48.94, 58.51, 55.32, 58.51, 46.81, 53.19, 62.77])
# # c45_scores = np.array([44.79, 57.29, 57.29, 50.00, 56.84, 57.89, 54.74, 51.58, 56.84, 50.53])
# # c45_scores = np.array([63.92, 56.70, 51.55, 55.67, 49.48, 56.70, 52.58, 53.61, 51.55, 55.67])
# # c45_scores = np.array([53.54, 57.58, 60.61, 46.94, 50.00, 46.94, 52.04, 41.84, 57.14, 55.10])
# # c45_scores = np.array([51.52, 53.54, 51.52, 47.47, 49.49, 51.52, 42.42, 44.44, 53.06, 51.02])
# # c45_scores = np.array([47.92, 54.14, 52.63, 42.11, 42.11, 47.37, 44.21, 43.16, 47.37, 47.37])
# pso_c45_scores_1 = np.array([61.05, 55.32, 56.38, 53.19, 57.45, 59.57, 56.38, 52.13, 55.32, 61.70])
# # pso_c45_scores_1 = np.array([51.04, 55.21, 53.68, 47.37, 45.26, 51.58, 47.37, 43.16, 50.53, 48.42])
# pso_c45_scores_2 = np.array([60.00, 55.32, 56.38, 54.26, 58.21, 62.77, 55.32, 52.13, 56.38, 60.64])
# # pso_c45_scores_2 = np.array([55.79, 57.45, 56.38, 52.13, 58.51, 57.45, 59.57, 48.94, 57.45, 56.38])
# # pso_c45_scores_2 = np.array([50.00, 55.21, 53.68, 44.21, 45.26, 49.47, 47.37, 43.16, 52.63, 46.32])
# pso_c45_scores_3 = np.array([55.79, 55.32, 56.38, 52.13, 59.57, 62.77, 56.38, 52.13, 56.38, 61.70])
# # pso_c45_scores_3 = np.array([50.00, 56.25, 54.74, 46.32, 45.26, 49.47, 47.37, 44.21, 52.63, 47.37])
# print(np.mean(c45_scores))
# print(pso_c45_scores_1 - c45_scores, np.mean(pso_c45_scores_1))
# print(pso_c45_scores_2 - c45_scores, np.mean(pso_c45_scores_2))
# print(pso_c45_scores_3 - c45_scores, np.mean(pso_c45_scores_3))
# result_mean_1 = np.mean(pso_c45_scores_1 - c45_scores)
# result_mean_2 = np.mean(pso_c45_scores_2 - c45_scores)
# result_mean_3 = np.mean(pso_c45_scores_3 - c45_scores)
# x_axis = np.linspace(0, 10, 10)
# c45_mean = np.mean(c45_scores)
# y_axis = [c45_mean - 15, c45_mean, c45_mean + 15]

# plt.plot(x_axis, c45_scores, label="Akurasi C4.5")
# plt.scatter(x_axis, c45_scores)
# plt.plot(x_axis, pso_c45_scores_1, label="Akurasi PSO - C4.5")
# plt.scatter(x_axis, pso_c45_scores_1)
# plt.title(f"Akurasi C4.5 dan PSO - C4.5 Konfigurasi 1 (+{round(result_mean_1, 2)}%)")
# plt.grid()
# plt.legend()
# plt.xlabel("k")
# plt.ylabel("Accuracy(%)")
# plt.yticks(y_axis)
# plt.show()

# plt.plot(x_axis, c45_scores, label="Akurasi C4.5")
# plt.scatter(x_axis, c45_scores)
# plt.plot(x_axis, pso_c45_scores_2, label="Akurasi PSO - C4.5")
# plt.scatter(x_axis, pso_c45_scores_2)
# plt.title(f"Akurasi C4.5 dan PSO - C4.5 Konfigurasi 2 (+{round(result_mean_2, 2)}%)")
# plt.grid()
# plt.legend()
# plt.xlabel("k")
# plt.ylabel("Accuracy(%)")
# plt.yticks(y_axis)
# plt.show()

# plt.plot(x_axis, c45_scores, label="Akurasi C4.5")
# plt.scatter(x_axis, c45_scores)
# plt.plot(x_axis, pso_c45_scores_3, label="Akurasi PSO - C4.5")
# plt.scatter(x_axis, pso_c45_scores_3)
# plt.title(f"Akurasi C4.5 dan PSO - C4.5 Konfigurasi 3 (+{round(result_mean_3, 2)}%)")
# plt.grid()
# plt.legend()
# plt.xlabel("k")
# plt.ylabel("Accuracy(%)")
# plt.yticks(y_axis)
# plt.show()


# from entities.Storage import Storage

# s = Storage()
# for i in range(10):
# 	clf = s.load(f"data/particles/particle{i + 1}.pckl")
# 	print(round(clf.best * 100, 2))