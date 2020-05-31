import numpy as np
a=np.array([1,2,3])
print(a*3)
print(a+2)

b=np.array([2,2,0])
print(a+b)

#0除算
# print(a/b)

print(a*b)

#内積
print(np.dot(a,b))

print(np.arange(10))
print(np.arange(0,10,2))
print(np.linspace(0,10,15)) #0~10を15等分

c=np.array([[1,2,3],[4,5,6]])
print(c)

print(c.shape) #2*3行列なので(2,3)を返す

print(np.sum(c))
print(np.sum(c,axis=0)) #[5 7 9]
print(np.sum(c,axis=1)) #[6 15]

print(c.reshape(3,2)) #3*2行列に変換
print(c.reshape(6,1))

print(c.T) #転置
print(np.transpose(c))

print(np.random.randn()) #標準正規分布に従う
print(np.random.rand()) #[0,1]の値
print(np.random.randn(2,3)) #2*3行列