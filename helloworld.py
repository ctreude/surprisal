import tensorflow as tf
a = tf.constant(12)
b = tf.constant(30)
sess = tf.Session()
print(sess.run(a+b))