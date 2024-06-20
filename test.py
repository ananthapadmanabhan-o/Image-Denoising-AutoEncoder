import tensorflow as tf 


device = tf.config.list_physical_devices('GPU')
print(device)
tf.config.experimental.set_memory_growth(device[0],True)
