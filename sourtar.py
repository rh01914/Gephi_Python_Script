import numpy

def edge=sourtar(b,t):
  M = graphFromDegreeSequence(b);
  L = adj2edgeL(M);

  L(:,3)=[];
  L(:,1)=L(:,1)+t;
  L(:,2)=L(:,2)+t
