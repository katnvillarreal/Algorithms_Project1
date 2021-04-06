# Algorithms Project 3
# Group Members: Kile Adams, Monique Dashner, Kathryn Villarreal

# Question 1
# Undirected and Unweighted
# Both DFS and BFS
# A: B,F,E
# B: A,C,F
# C: B,G,D
# D: C,G
# E: A,F,I
# F: A,B,E,I
# G: C,D
# H: K,L
# I: E,F,J,M
# J: I
# K: H,L,O
# L: H,K,P
# M: I,N
# N: M
# O: K
# P: L

# Question 2
# Directed and unweighted
# Find the strongly connected components 
# 1: 3
# 2: 1
# 3: 2,5
# 4: 1,2,12
# 5: 6,8
# 6: 7,8,10
# 7: 10
# 8: 9,10
# 9: 5,11
# 10: 9,11
# 11: 12
# 12: nothing

# Question 3
# Undirected and weighted
# Dijkstra's
# A: (B,22), (C,9), (D,12)
# B: (A,22), (C,35), (F,36), (H,34)
# C: (A,9), (B,35), (F,42), (E,65), (D,4)
# D: (A,12), (C,4), (E,33), (I,30)
# E: (C,65), (D,33), (F,18), (G,23)
# F: (B,36), (C,42), (E,18), (G,39), (H,24)
# G: (E,23), (F,39), (H,25), (I,21)
# H: (B,34), (F,24), (G,25), (I,19)
# I: (D,30), (G,21), (H,19)
