import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

X=np.loadtxt("matrix.txt",  delimiter=",")

y=[]
co=[]
for row in X:
    a = row.tolist()
    b=a.index(max(a))
    if b==0:
        c='255,31,31,0.8'
    elif b==1:
        c = '28,217,44,0.8'
    elif b==2:
        c = '37,171,226,0.8'
    elif b==3:
        c = '255,255,31,0.8'
    elif b==4:
        c = '123,104,238,0.8'
    else:
        c = '2,255,255,0.8'
    co.append(c)
    y.append(b)

File = open("colour.txt", "w")
for Index in co:
    File.write(str(Index) + "\n")
File.close()


pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_)

print(pca.explained_variance_)
X_new = pca.transform(X)


scaler = MinMaxScaler( )
scaler.fit(X_new)
scaler.data_max_
mat=scaler.transform(X_new)

plt.scatter(mat[:, 0], mat[:, 1],marker='o',c=y)

plt.show()
np.savetxt("pca.txt", mat, fmt="%.5f", delimiter=",")


lda = LinearDiscriminantAnalysis(n_components=2)
lda.fit(X,y)
X_lda = lda.transform(X)

scaler.fit(X_lda)
scaler.data_max_
X_lda=scaler.transform(X_lda)
plt.scatter(X_lda[:, 0], X_lda[:, 1],marker='o',c=y)
plt.show()
np.savetxt("lda.txt", X_lda, fmt="%.5f", delimiter=",")

tsne = TSNE(n_components=2, n_iter=300).fit_transform(X)

scaler.fit(tsne)
scaler.data_max_
tsne1=scaler.transform(tsne)
plt.scatter(tsne1[:, 0], tsne1[:, 1],marker='o',c=y)
plt.show()

np.savetxt("sne.txt", tsne1, fmt="%.5f", delimiter=",")