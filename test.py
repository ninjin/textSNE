#!/usr/bin/python

import cPickle
from common.file import myopen
#(example_metadata, examples) = cPickle.load(myopen("/u/turian/dev/python/nlpreprocess/wikipedia/work-legal/sparseexamples-bm25.unshuffled.pkl"))
(example_metadata, examples) = cPickle.load(myopen("/u/turian/dev/python/nlpreprocess/wikipedia/work-legal/sparseexamples.unshuffled.pkl"))
x = examples.todense()
titles = [e["title"] for e in example_metadata]
x = x[:500]

#import string, numpy
#o = open("/u/turian/data/word_embeddings.collobert-and-weston/lm-weights.txt")
#o.readline()
#x = [float(i) for i in string.split(o.readline())]
#x = numpy.array(x)
#x.resize(30000,50)
#titles = [string.strip(t) for t in open("/u/turian/data/word_embeddings.collobert-and-weston/words.asc")]
#x = x[:500]
#titles = titles[:500]

def normalize(x):
    import numpy
    return x / numpy.sum(x, axis=1)

x = normalize(x)

from calc_tsne import calc_tsne
#print x.shape
#x = x[:100,:100]
#print x.shape
out = calc_tsne(x, NO_DIMS=2, PERPLEX=30, INITIAL_DIMS=30, LANDMARKS=1, USE_PCA=False)

import render
render.render([(title, point[0], point[1]) for title, point in zip(titles, out)], "out.png", width=3000, height=1800)