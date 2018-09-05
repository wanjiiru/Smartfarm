from PIL import Image
import numpy as np
import cv2, sys, os
import tensorflow as tf
from .funcs import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
BASE_PATH = os.path.dirname(__file__)
PATH_TO_MODEL = os.path.join(BASE_PATH, 'model.pb')
PATH_TO_LABELS = os.path.join(BASE_PATH, 'labels.txt')

graph_def = tf.GraphDef()
labels = [*open(PATH_TO_LABELS, 'r').read().split('\n')]

with tf.gfile.FastGFile(PATH_TO_MODEL, 'rb') as f:
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')
    sess = tf.Session()
prob_tensor = sess.graph.get_tensor_by_name('loss:0')

def recognise(uploads):
    image = Image.open(uploads).convert('RGB')
    augmented_image = prepareimage(image)
    predictions, = sess.run(prob_tensor, {'Placeholder:0': [augmented_image]})
    results = list(enumerate(map(lambda d: '{:.2f}'.format(d * 100), predictions)))
    results.sort(key=lambda x: -float(x[1]))
    return results


if __name__ == '__main__':
    recognise(sys.argv[1])
