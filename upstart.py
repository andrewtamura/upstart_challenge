'''
Challenge 1
'''

def how_many_ones(num):
    counter = 0
    for digit in hex(num)[2:]:
        if digit == '1':
            counter += 1
    return counter
    
'''
Challenge #2

Implement a function that takes takes 3 (x,y) coordinates which define the vertices of a triangle, and a 4th (x,y) coordinate, as inputs. Return true if the 4th point falls inside the triangle defined by the first 3 points; false otherwise.


'''

def in_or_out(v1, v2, v3, p):
    '''
    area = (1x(2y-3y)+2x(3y-1y)+3x(1y-2y))/2
    
    Take the point and create three triangles with the given three points of the triangle. The sum of these three triangles' area will be greater than the given triangle's area if the point lies outside. If the point lies inside, then the area will be equal. 
    
    '''
    triangle_area = abs(
        (v1[0]*(v2[1]-v3[1])+
        v2[0]*(v3[1]-v1[1])+
        v3[0]*(v1[1]-v2[1]))/2.0)
        
    area1 = abs(
        (p[0]*(v2[1]-v3[1])+
        v2[0]*(v3[1]-p[1])+
        v3[0]*(p[1]-v2[1]))/2.0)
    area2 = abs(
        (v1[0]*(p[1]-v3[1])+
        p[0]*(v3[1]-v1[1])+
        v3[0]*(v1[1]-p[1]))/2.0)
    area3 = abs(
        (v1[0]*(v2[1]-p[1])+
        v2[0]*(p[1]-v1[1])+
        p[0]*(v1[1]-v2[1]))/2.0)
    
    
    total_area = area1 + area2 + area3
    
    if total_area == triangle_area:
        return True
    else:
        return False
