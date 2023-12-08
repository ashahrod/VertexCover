from os import sendfile
import sys
import graph
import vertex_cover as vc
graph_g = graph.Graph()

# build the graph as we did in lecture, then complement it, run vertex cover, look at everything thats not in the vertex cover, and thats your satisfying assignment.

def main():
   props = read_file(sys.argv[1])
   seen_literals = []
   addProps(props, seen_literals)
   # print(graph_g)
   connectEdges()
   num_clauses = len(props)
   num_vertices = countVertices()
   k = num_vertices - num_clauses
   # print(graph_g)
   vertex_cover = vc.vertex_cover(graph_g, int(k))
   if vertex_cover == None:
      other_vertices = None
   else:
      other_vertices = allOtherVertices(vertex_cover)
   solution(other_vertices)
   

def read_file(file_name):
   f = open(file_name, 'r')
   line = f.readline()
   splitted = line.split('&')
   props = []
   for line in splitted:
      line = line.strip()
      line = line.replace("(", "")
      line = line.replace(")", "")
      line = line.strip()
      line = line.replace(" | ", ",")
      line = line.split(",")
      props.append(line)
   # print(props)
   return props

def allOtherVertices(vertex_cover):
   # gets all the vertices that are not in the vertex cover
   other_vertices = []
   for vertex in graph_g:
      if vertex in vertex_cover:
         continue
      else:
         other_vertices.append(vertex)
   return other_vertices

def solution(other_vertices):
   if other_vertices == None:
      print("No satisfying assignments.")
   elif len(other_vertices) == 1:
      print("Satisfying assignment:")
      sorted_sat = sortVariables(other_vertices)
      print(sorted_sat[0])

   elif len(other_vertices) > 1:
      sorted_sat = sortVariables(other_vertices)
      print("Satisfying assignment:")
      final_point = len(sorted_sat)
      i = 1
      for vertex in sorted_sat:
         if (final_point == i):
            print(str(vertex), end='')
         else:
            print(str(vertex) + ", ", end='')
         i += 1
      print()


def sortVariables(other_vertices):
   # vars is just the letters, sorted_vars is vars sorted, finished is completed with everything done, intermediate is letters and negation
   vars = [] 
   finished = []
   intermediate = []
   for vertex in other_vertices:
      if len(vertex) == 2:
         vars.append(vertex[0])
         intermediate.append(vertex[0])
      elif len(vertex) == 3:
         vars.append(vertex[1:2])
         intermediate.append(vertex[:2])
   vars = list(set(vars))
   sorted_vars = sorted(vars)
   # print("sorted_vars:" + str(sorted_vars))
   for vertex in sorted_vars:
      # print("vertex: " + vertex + "other_vertices: " + str(other_vertices))
      if vertex in intermediate:
         finished.append(vertex)
      elif vertex not in intermediate:
         finished.append("~" + vertex)
   return finished
      


def addProps(props, seen_literals):
   # need dictionary to keep track of the vertices to make edge with new vertices
   # not sure on if duplicates should get another identifier THEY SHOULDN"T BE ADDED SAID CHRIS
   # add vertex's individually first then run nested for loop with conditions to add edges
   clause_count = 1
   for clause in props:
      for literal in clause:
         if literal not in seen_literals:
            if len(literal) == 1:
               seen_literals.append(literal)
               negated = '~' + literal
               seen_literals.append(negated)

            # case where literal is negated
            elif len(literal) == 2:
               unnegated = literal[1]
               seen_literals.append(unnegated)
               seen_literals.append(literal)
         withNum = literal + str(clause_count)
         graph.add_vertex(graph_g, withNum)
      clause_count += 1

def connectEdges():
   num = 0
   for vertex in graph_g:
      if len(vertex) == 2:
         vertex_clause_num = vertex[1]
         # vertex_literal ex: ~r, r, ~p, p, etc.
         vertex_literal = vertex[:1]
      elif len(vertex) == 3:
         vertex_clause_num = vertex[2]
         vertex_literal = vertex[:2]
      for other in graph_g:
         same_clause = None
         negation = None

         # case where vertex and other are the same, we skip
         if(vertex == other):
            # print("CONTINUE")
            continue
         
         if len(other) == 2:
            other_clause_num = other[1]
            other_literal = other[:1]
         elif len(other) == 3:
            other_clause_num = other[2]
            other_literal = other[:2]
         # print("vertex: cn = " + vertex_clause_num + " literal: "  + vertex_literal + " other: cn = " + other_clause_num + " literal: " + other_literal)

         if(vertex_clause_num == other_clause_num):
            same_clause = True
         else:
            same_clause = False
         # trying to do negation of same variable here, we know if the lengths differ they are opposite sign (not negated vs negated)
         # if(len(vertex_literal) != len(other_literal)):
         #    print("In negated")
         if len(vertex_literal) == 2:
            letter1 = vertex_literal[1]
         else:
            letter1 = vertex_literal[0]
         if len(other_literal) == 2:
            letter2 = other_literal[1]
         else:
            letter2 = other_literal[0]
         if(letter1 == letter2 and len(vertex_literal) != len(other_literal)):
            negation = True
            # print("NEGATED SAME HERE")
         else:
            negation = False
         # print("same_clause: " + str(same_clause) + " negation: " + str(negation))
         if same_clause == True or negation == True:
            graph.add_edge(graph_g, vertex, other)
               
      num += 1

def countVertices():
   count = 0
   for vertex in graph_g:
      count += 1
   return count
      
   
main()