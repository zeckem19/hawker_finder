from sklearn.metrics.pairwise import haversine_distances
from math import radians

def find_distance(a,b) -> float:
    '''
    Inputs
    - List of float (a: [lat,lon], b: [lat,lon])
    
    Output
    - float representing haversine distance between points a & b
    '''

    a_in_radians = [radians(_) for _ in a]
    b_in_radians = [radians(_) for _ in b]
    
    # multiply by Earth radius
    result = haversine_distances([a_in_radians, b_in_radians])* 6371000
    return result[0][1]   