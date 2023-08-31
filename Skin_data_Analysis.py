#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PIL import Image
import streamlit as st


# In[6]:


import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '1'


# In[ ]:


import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import os
import pandas as pd
import numpy as np


# In[ ]:


train_datagen=ImageDataGenerator(
                rescale=1./255,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True)


# In[ ]:


training_set=train_datagen.flow_from_directory(
    'D:/archive (1)/train',  # Path to the directory containing subdirectories of class-specific images
    target_size=(224, 224),   # Target size for resizing the images
    batch_size=32,            # Batch size for each iteration
    class_mode='categorical'  # Type of classification problem: 'categorical' or 'binary'
)


# In[ ]:


from shutil import move

# Path to the directory containing the images
image_dir = 'D:/archive/HAM10000_images_part_1'

# Path to the CSV file containing labels
csv_file = 'D:/archive/HAM10000_metadata.csv'

# Load CSV data using Pandas
data = pd.read_csv(csv_file)

# Iterate through each row in the CSV file
for index, row in data.iterrows():
    # Extract filename and label from the row

    filename = row['image_id'] + '.jpg'
    label = row['dx']  # 'dx' column contains the label
    print(filename)
    print(label)

    # Full path to the source image
    source_path = os.path.join(image_dir, filename)
    print(source_path)

    # Full path to the destination directory for labeled images
    dest_dir = os.path.join(image_dir, label)
    print(dest_dir)
    # Move the image to the destination directory
    move(source_path, dest_dir)


# In[ ]:


from shutil import copyfile

# Path to the directory containing the images
image_dir = 'D:/archive/HAM10000_images_part_1/'

# Path to the CSV file containing labels
csv_file = 'D:/archive/HAM10000_metadata.csv'

# Load CSV data using Pandas
data = pd.read_csv(csv_file)

# Create a new directory to store the organized images
organized_dir = 'D:/images/'

# Iterate through each row in the CSV file
for index, row in data.iterrows():
    # Extract filename and label from the row
    filename = row['image_id'] + '.jpg'
    label = row['dx']  # 'dx' column contains the label
    print(filename)
    print(label)

    # Full path to the source image
    source_path = os.path.join(image_dir, filename)
    print(source_path)
    # Full path to the destination directory for labeled images
    dest_dir = os.path.join(organized_dir, label)
    print(dest_dir)
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Copy the image to the destination directory
    destination_path = os.path.join(dest_dir, filename)
    print(destination_path)
    copyfile(source_path, destination_path)
#copyfile is used to copy the content of the source file to destination file


# In[ ]:


training_set=train_datagen.flow_from_directory(
    'D:/organized_images',  # Path to the directory containing subdirectories of class-specific images
    target_size=(224, 224),   # Target size for resizing the images
    batch_size=32,            # Batch size for each iteration
    class_mode='categorical'  # Type of classification problem: 'categorical' or 'binary'
)


# In[ ]:


lower_bound=1
upper_bound=10000
no_of_random=2000



# In[ ]:


import random
random_numbers=[random.randrange(lower_bound,upper_bound) for _ in range(no_of_random)]
print(random_numbers)


# In[ ]:


from shutil import move
from shutil import copyfile
image_dir = 'D:/archive/HAM10000_images_part_1/'
images=[]
# Path to the CSV file containing labels
csv_file = 'D:/archive/HAM10000_metadata.csv'

# Load CSV data using Pandas
data = pd.read_csv(csv_file)

# Create a new directory to store the organized images
organized_test = 'D:/tests/'

# Iterate through each row in the CSV file
for index, row in data.iterrows():
    # Extract filename and label from the row
    if index in random_numbers:
        filename = row['image_id'] + '.jpg'
        label = row['dx']  # 'dx' column contains the label
        images.append(filename)
        print(filename)
        print(label)

    # Full path to the source image
        source_path = os.path.join(image_dir, filename)
        print(source_path)
        # Full path to the destination directory for labeled images
        dest_dir = os.path.join(organized_test, label)
        print(dest_dir)
        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Copy the image to the destination directory
        destination_path = os.path.join(dest_dir, filename)
        print(destination_path)
        copyfile(source_path, destination_path)
#copyfile is used to copy the content of the source file to destination file


# In[ ]:


l=["akiec","bcc","bkl","df","mel","nv","vasc"]


# In[ ]:


images


# In[ ]:


image_dir = 'D:/organized_images/'
for filename in images:
    for i in l:
        file_path=os.path.join(image_dir,i,filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print("file removed")
            print(file_path)


# In[ ]:


train_datagen=ImageDataGenerator(
                rescale=1./255,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True)


# In[ ]:


training_set=train_datagen.flow_from_directory(
    'D:/organized_images/train',  # Path to the directory containing subdirectories of class-specific images
    target_size=(64, 64),   # Target size for resizing the images
    batch_size=32,            # Batch size for each iteration
    class_mode='categorical'  # Type of classification problem: 'categorical' or 'binary'
)


# In[ ]:


test_datagen=ImageDataGenerator(
                rescale=1./255)


# In[ ]:


testing_set=test_datagen.flow_from_directory(
    'D:/organized_images/test',  # Path to the directory containing subdirectories of class-specific images
    target_size=(64,64),   # Target size for resizing the images
    batch_size=32,            # Batch size for each iteration
    class_mode='categorical'  # Type of classification problem: 'categorical' or 'binary'
)


# In[ ]:


cnn=tf.keras.models.Sequential()


# In[ ]:


cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu',input_shape=[64,64,3]))


# In[ ]:


cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))


# In[ ]:


cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))


# In[ ]:


cnn.add(tf.keras.layers.Flatten())


# In[ ]:


cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))


# In[ ]:


cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))


# In[ ]:


cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# In[ ]:


cnn.fit(x = training_set, validation_data = testing_set, epochs = 25)


# In[ ]:


cnn.save('modelnew.h5')


# In[ ]:




