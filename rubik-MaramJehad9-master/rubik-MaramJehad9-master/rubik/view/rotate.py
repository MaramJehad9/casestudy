from rubik.model.cube import Cube
from pkg_resources._vendor.jaraco.context import null
<<<<<<< HEAD
=======

>>>>>>> refs/heads/increment1

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    directions = parms.get('dir')
    result = valid(parms, result) 
    
    theCube.rotate(directions)
    result['status'] = 'ok'      
    result['cube'] = theCube.get()
           
    return result

def valid(parms, result):
    if checkInvalidKeys(parms):
        result['status'] = 'error: extraneous key detected'  
        return result
    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    directions = parms.get('dir')
    
    if invalidCube(encodedCube) and invalidDirections(directions):
        result['status'] = "error: invalid dir and invalid cube"
        return result
    elif invalidCube(encodedCube):
        result['status'] = "error: invalid cube"
        return result
    elif directions == None:
        directions = "F"
    elif invalidDirections(directions):
        result['status'] = "error: invalid dir"
        return result
    
def checkInvalidKeys (parms):
    if len(list(parms)) > 2 :             
        return True
    
 
def invalidCube(encodedCube):
    if encodedCube == None:
        return True
    if len(encodedCube) != 54: 
        return True
    elif encodedCube.isalnum() == False:
        return True
    elif checkUniqueElements(encodedCube) == False:
        return True
    elif checkEqual9(encodedCube) == False:
        return True
    
def checkEqual9(encodedCube):
    indexes = [4, 13, 22, 40,31, 49]
    flag = True
    for i in indexes:
        if encodedCube.count(encodedCube[i]) != 9 :
            flag = False
            break
    return flag
    
    
def checkUniqueElements(encodedCube):
    indexes = [4,13,22,31,40,49]
    for x in indexes:
        for y in indexes:
            if x != y:
                if encodedCube[x] != encodedCube[y]:
                    continue
                return False
    return True
    '''if encodedCube[4] != encodedCube[13] != encodedCube[22] != encodedCube[31] != encodedCube[40] != encodedCube[49]:
        return True
    return False 
    '''
def invalidDirections(direction):
    if direction == None:
        direction ="F"
        return False
    for x in direction:   
        if x == 'F':
            continue
        elif x == 'f':
            continue
        elif x == 'B':
            continue
        elif x == 'b':
            continue
        elif x == 'R':
            continue
        elif x == 'r':
            continue
        elif x == 'U':
            continue
        elif x == 'u':
            continue
        elif x == 'L':
            continue
        elif x == 'l':
            continue
        else: 
            return True
     
    return False
    