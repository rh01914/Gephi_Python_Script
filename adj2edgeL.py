import numpy

def adj2edgeL(adj):
  print 'Hey'
  n = len(adj) # number of nodes
  edges = numpy.nonzero(numpy.array(adj))  # indices of all edges

  el=[]
  for e in range(len(edges[0])):
    [i,j]=[edges[0][e] + 1, edges[1][e] + 1] # node indices of edge e  
    el=[el, [i ,j]]
    
   print el
