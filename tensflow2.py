import tensorflow as tf
print(tf.__version__)
mnist=tf.keras.datasets.fashion_mnist
(training_images,training_labels),(testing_images,testing_labels)=mnist.load_data()
training_images=training_images/255.0
testing_images=testing_images/255.0
model=tf.keras.models.Sequential([tf.keras.layers.Flatten(),tf.keras.layers.Dense(124,activation=tf.nn.relu),tf.keras.layers.Dense(10,activation=tf.nn.softmax)])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(training_images,training_labels,epochs=5)
model.evaluate(testing_images,testing_labels)

print("Classification:\n")
classification=model.predict(testing_images)
print(classification[3])
print(test_labels[3])
