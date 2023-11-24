
#distances represented by the time in minutes for a speed of 30km/h
g_scores = {(1, 2): 20,
            (2, 3): 17.0, (2, 9): 20.0, (2, 10): 7.0,
            (3, 4): 12.6, (3, 9): 18.8, (3, 13): 37.4,
            (4, 5): 26, (4, 8): 30.6, (4, 13): 25.6, (4, 14): 22,
            (5, 6): 6, (5, 7): 4.8, (5, 8): 60,
            (8, 9): 19.2, (8, 12): 12.8,
            (9, 11): 24.4,
            (13, 14): 10.2}

h_scores = {(1, 2): 20, (1, 3): 37.0, (1, 4): 49.6, (1, 5): 72.8, (1, 6): 77.6, (1, 7): 71.6, (1, 8): 50.8, (1, 9): 35.2, (1, 10): 18.2, (1, 11): 33.4, (1, 12): 54.6, (1, 13): 55.2, (1, 14): 59.6, 
            (2, 3): 17.0, (2, 4): 29.6, (2, 5): 53.2, (2, 6): 58.2, (2, 7): 52.2, (2, 8): 34.6, (2, 9): 20.0, (2, 10): 7.0, (2, 11): 31.0, (2, 12): 41.8, (2, 13): 38.2, (2, 14): 43.6, 
            (3, 4): 12.6, (3, 5): 36.4, (3, 6): 41.2, (3, 7): 35.2, (3, 8): 27.2, (3, 9): 18.8, (3, 10): 20.6, (3, 11): 39.0, (3, 12): 38.2, (3, 13): 24.2, (3, 14): 33.2, 
            (4, 5): 24.0, (4, 6): 28.8, (4, 7): 23.0, (4, 8): 24.8, (4, 9): 25.2, (4, 10): 33.4, (4, 11): 47.2, (4, 12): 37.2, (4, 13): 21.2, (4, 14): 30.8, 
            (5, 6): 6.0, (5, 7): 4.8, (5, 8): 38.8, (5, 9): 46.6, (5, 10): 56.4, (5, 11): 68.4, (5, 12): 49.6, (5, 13): 29.0, (5, 14): 35.8, 
            (6, 7): 6.6, (6, 8): 44.6, (6, 9): 51.4, (6, 10): 60.6, (6, 11): 73.4, (6, 12): 55.2, (6, 13): 30.4, (6, 14): 36.4, 
            (7, 8): 40.0, (7, 9): 46.0, (7, 10): 54.6, (7, 11): 68.4, (7, 12): 51.4, (7, 13): 24.8, (7, 14): 31.2, 
            (8, 9): 16.4, (8, 10): 40.6, (8, 11): 32.2, (8, 12): 12.8, (8, 13): 45.4, (8, 14): 55.2, 
            (9, 10): 27.0, (9, 11): 22.4, (9, 12): 21.8, (9, 13): 42.4, (9, 14): 53.2, 
            (10, 11): 35.2, (10, 12): 48.4, (10, 13): 37.4, (10, 14): 42.4, 
            (11, 12): 28.4, (11, 13): 63.0, (11, 14): 71.0, 
            (12, 13): 57.6, (12, 14): 67.2, 
            (13, 14): 10.2}

def g(i, j):
    if (i,j) in g_scores:
        return g_scores[(i,j)]
    elif (j,i) in g_scores:
        return g_scores[(j,i)]
    else:
        return 0
    
def h(i, j):
    if (i,j) in h_scores:
        return h_scores[(i,j)]
    elif (j,i) in h_scores:
        return h_scores[(j,i)]
    else:
        return 0