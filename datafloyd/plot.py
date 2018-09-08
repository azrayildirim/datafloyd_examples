import matplotlib.pyplot as plt
import numpy as np

# Scikit Learn ile kullanılmak üzere hazırlanan karar alanlarını çizen fonksiyon
def plot_decision_region(X, y, classifier, legend=[], resolution=0.02):
    # marker ve renk seçimi
    # burada sınıf sayısı kadar modifiye etmek gerekiyor aksi takdirde hata alınır.
    markers = ('o', 'o', 'o')
    colors = ('red', 'blue', 'green')

    # karar bölgesi ayarlanıyor
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap="coolwarm")
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # legend kısmını düzgün göstermek için eklendi
    line_list = []
    # örnekler çizdiriliyor
    for idx, cl in enumerate(np.unique(y)):
        dummy = plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                            alpha=0.8, c=colors[idx],
                            marker=markers[idx], label=cl)
        line_list.append(dummy)

    plt.legend(line_list, legend)