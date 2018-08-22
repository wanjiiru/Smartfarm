from PIL import Image
import numpy as np
import cv2,sys,os
import tensorflow as tf
from funcs import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
PATH_TO_MODEL = './model.pb'
PATH_TO_LABELS = './labels.txt'

graph_def = tf.GraphDef()
labels = [*open(PATH_TO_LABELS, 'r').read().split('\n')]

with tf.gfile.FastGFile(PATH_TO_MODEL, 'rb') as f:
	graph_def.ParseFromString(f.read())
	tf.import_graph_def(graph_def, name='')
	sess=tf.Session()

def recognise(image):
	image=Image.open(image)
	augmented_image = prepareimage(image)
	prob_tensor = sess.graph.get_tensor_by_name('loss:0')
	predictions, = sess.run(prob_tensor, {'Placeholder:0': [augmented_image] })
	results=list(zip(labels,predictions))
	results.sort(key=lambda x: -x[1])
	print(results)
	return results

if __name__ == '__main__':
	recognise(sys.argv[1])