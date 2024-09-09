from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
from rubik.view.rotate import rotate

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
    cube_ = {}
    
    if checkInvalidKeys(parms):
        result['status'] = 'error: extraneous key detected'  
        return result
    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    #print(theCube.get())
    if invalidCube(encodedCube):
        result['status'] = "error: invalid cube"
        return result
    else:         
<<<<<<< HEAD
        #rotations = ""
        result['status'] = 'ok'  
        result['solution']  = solveBottomCross(theCube)      #iteration 2
        result['solution'] += solveBottomLayer(theCube)      #iteration 3
        '''rotations += solveMiddleLayer(theCube)      #iteration 4
        rotations += solveUpCross(theCube)          #iteration 5
=======
        rotations = ""
        rotations += solveBottomCross(theCube)      #iteration 2
        cube_['cube'] = encodedCube
        cube_['dir'] = rotations
        theCube = Cube(rotate(cube_).get('cube'))
        rotations += solveBottomLayer(theCube)      #iteration 3
        #theCube.rotate(rotations)
        rotations += solveMiddleLayer(theCube)      #iteration 4
        '''rotations += solveUpCross(theCube)          #iteration 5
>>>>>>> refs/heads/increment4
        rotations += solveUpSurface(theCube)        #iteration 5
        rotations += solveUpperLayer(theCube)       #iteration 6
        '''
<<<<<<< HEAD
        # result['solution'] = rotations  
=======
       # result['solution'] = rotations
        result['solution']  = rotations
        result['status'] = 'ok'    
>>>>>>> refs/heads/increment4
        result['integrity'] = ''                    #iteration 3
        return result



def checkInvalidKeys (parms):
    if len(list(parms)) > 1:             
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