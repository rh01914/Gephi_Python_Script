import numpy

def multipleRandomGraph(b,k):
  t=0
  A = numpy.zeros((len(b),len(b)));

  while t<k:
    M = randomGraphFromDegreeSequence(b)
    A = numpy.A + numpy.M
    #drawCircGraph(M)
    t=t+1

adj2edgeL(A)