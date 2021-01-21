import numpy as np
import tensorflow as tf
x = np.array([[1,1],[1,0],[0,1],[0,0]])
y = np.array([[1],[1],[1],[0]])
w = tf.random.normal([2],0,1)
b = tf.random.normal([1],0,1)

for i in range(2000):
  for j in range(4):
    output = tf.math.sigmoid(np.sum(x*w)+b)
    error = output - y[j][0]
    w = w - x[j] * 0.1 * error
    b = b - b * 0.1 * error
  
  if i%199 == 1:
    print(w,b,error)
  