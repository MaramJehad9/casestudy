import rubik.model.constants
from rubik.model.cube import Cube
from rubik.controller.bottomLayer import solveBottomLayer
from pickle import TRUE

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    ''' 
    #check if the upper elements has top color, if so skip the element , else return the top value and front value of the element 
    rotation = ""
    #print("I am in middleLayer solve")
    if isMiddleLayerSolved(theCube):
        return ""
    else: 
        while isMiddleLayerSolved(theCube) == False:
            frontIndex, topIndex = theCube.HasTopFaceColor() 
            if topIndex != -1:
                rotation += solveMiddleBaseCase(theCube, rotation, topIndex, frontIndex)
            else: 
                index1, index2 = HasColoredInSidesMiddle(theCube)
                rotation += theCube.dotrigger(index1)
                solveBottomLayer(theCube)
                topIndex, frontIndex = theCube.HasTopFaceColor() 
                rotation += solveMiddleBaseCase(theCube, rotation, topIndex, frontIndex)
        return rotation    

def isMiddleLayerSolved(theCube):
    if theCube.get()[3] == theCube.get()[4]:
        if theCube.get()[5] == theCube.get()[4]:
            if theCube.get()[12] == theCube.get()[13]:
                if theCube.get()[14] == theCube.get()[13]:
                    if theCube.get()[21] == theCube.get()[22]:
                        if theCube.get()[23] == theCube.get()[22]:
                            if theCube.get()[31] == theCube.get()[30]:
                                if theCube.get()[31] == theCube.get()[32]:
                                    return True
    return False

def HasColoredInSidesMiddle(theCube):
    if theCube.get()[3] != theCube.get()[4] and theCube.get()[32] != theCube.get()[31]:
        return 3,32
    elif theCube.get()[5] != theCube.get()[4] and theCube.get()[12] != theCube.get()[13]:
        return 5,12
    elif theCube.get()[21] != theCube.get()[22] and theCube.get()[14] != theCube.get()[13]:
        return 21,14
    elif theCube.get()[23] != theCube.get()[22] and theCube.get()[30] != theCube.get()[31]:
        return 23,30     
    return -1,-1

def solveMiddleBaseCase (theCube, rotation, topIndex, frontIndex):
    rotation += theCube.alignedIndexToItsProperFace(frontIndex)
    rotation += theCube.alignTopElement(topIndex, frontIndex)
    rotation += solveBottomLayer(theCube)
            
    return rotation
