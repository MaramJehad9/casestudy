import rubik.model.constants
from rubik.model.cube import Cube
from rubik.controller.bottomCross import solveBottomCross
from test.test_set import cube

def solveBottomLayer(theCube: Cube) -> str:
    rotation = ""
    triggerRight = [2, 11, 20, 29]
    downRightTrigger = [8,17, 26, 35]
    triggerLeft =  [0, 9, 18, 27]
    downLeftTrigger = [ 6, 15, 24, 33]
    upperface = [36, 38, 42, 44]
    bottomCorner = [6, 8, 15, 17, 24, 26,33, 35]
    cube = theCube.get()
    while not IsTheBottomSloved(theCube):
        elementFound = theCube.get()[:-9].index(theCube.get()[49])
        if elementFound in triggerLeft or elementFound in triggerRight:
            r =  solveTopCorner(theCube, elementFound)
            rotation += r
            elementSide = updateIndex(elementFound, r)
            elementFound = SideIndex(elementSide)
            if elementFound in triggerRight:
                rotation += doRightTrigger(theCube, elementSide)
            elif elementFound in triggerLeft:
                rotation += doLeftTrigger(theCube, elementSide)
        elif elementFound in downRightTrigger:
            rotation += doRightTrigger(theCube, elementFound)
        elif elementFound in downLeftTrigger:
            rotation += doLeftTrigger(theCube, elementFound)
        elif elementFound in upperface: 
            rotation += doTwoTriggers(theCube, elementFound)
    
    print("i am done")
    return rotation  

def updateIndex(elementFound, r):
    if r == 'U':
        elementFound += 9
    elif r == 'UU':
        elementFound += 18
    elif r == 'u':
        elementFound += 27
    return elementFound  
    
def IsSidesMatch(theCube, side, middle):
    if theCube.get()[side] == theCube.get()[middle]:
        return True
    return False
    
def solveTopCorner(theCube, elementFound):
    rotation = ""
    elementFound = theCube.get()[:-9].index(theCube.get()[49])
    elementSide = SideIndex(elementFound)
    return matchSide(theCube, elementSide)

def IsTheBottomSloved(theCube):
    cube = theCube.get()
    for i in range(45,54):
        if cube[i] != cube[49]:
            return False
    return True

def Face(elementFound):
    if elementFound in range(0,9):
        return 'F'
    if elementFound in range(9,18):
        return 'R'
    if elementFound in range(18,27):
        return 'B'
    if elementFound in range(27,36):
        return 'L'
    if elementFound in range(36,45):
        return 'U'
    return ""
    
def SideIndex(elementFound): 
       if elementFound == 0 : 
           return 29
       elif elementFound == 29 : 
           return 0
       elif elementFound == 2: 
           return 9
       elif elementFound == 9 : 
           return 2
       elif elementFound == 11: 
           return 18
       elif elementFound == 18: 
           return 11
       elif elementFound == 20 : 
           return 27
       elif elementFound == 27 : 
           return 20
       return -1
   
def doRightTrigger(theCube, elementFound): 
    
    sideIndex = SideIndex(elementFound)
    if sideIndex != -1:
        face = Face(sideIndex)
    else: 
        face = Face(elementFound)
        
<<<<<<< HEAD
    if face == 'F': 
        theCube.rotate("RUr")
        return 'RUr'
    elif face == 'R':
        theCube.rotate("BUb")
        return 'BUb'
    elif face == 'B':
        theCube.rotate("LUl")
        return 'LUl'
    elif face == 'L':
        theCube.rotate("FUf")
        return 'FUf'
    
    
def doLeftTrigger(theCube, elementFound):
    sideIndex = SideIndex(elementFound)
    if sideIndex != -1:
        face = Face(sideIndex)
    else: 
        face = Face(elementFound)
        
    if face == 'F': 
        theCube.rotate("luL")
        return 'luL'
    elif face == 'R':
        theCube.rotate("fuF")
        return 'fuF'
    elif face == 'B':
        theCube.rotate("ruR")
        return 'ruR'
    elif face == 'L':
        theCube.rotate("buB")
        return 'buB'

def doTwoTriggers(theCube, elementFound):
    rotation = ""
    if elementFound == 36 : 
        theCube.rotate("LUl")
        theCube.rotate("LUl")
        rotation += 'LUlLUl'
    elif elementFound == 38: 
        theCube.rotate("ruR")
        theCube.rotate("ruR")
        rotation += 'ruRruR'
    elif elementFound == 42 : 
        theCube.rotate("luL")
        theCube.rotate("luL")
        rotation += 'luLluL'
    elif elementFound == 44 : 
        theCube.rotate("RUr")
        theCube.rotate("RUr")
        rotation += 'RUrRUr'
    return rotation

def theMiddle (theCube, index):
    if index in range(0,9):
        return 4
    if index in range(9,18):
        return 13
    if index in range(18,27):
        return 22
    if index in range(27,36):
        return 31
    if index in range(36,45):
        return 41
    
def matchSide(theCube, sideIndex):
    middleElements=[4,13,22,31]
    middle = theMiddle(theCube, sideIndex)
    
    if theCube.get()[sideIndex] == theCube.get()[middle]:
        return ""
    else: 
        for x in middleElements:
            if theCube.get()[sideIndex] == theCube.get()[x]:
                differences = abs(x-middle)
                if differences == 9:
                    theCube.rotate('U')
                    return 'U'
                elif differences == 18:
                    theCube.rotate('UU')
                    return 'UU'
                else: 
                    theCube.rotate('u')
                    return 'u'
    
=======
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''
    #print(theCube.get())  
    rotations = ""
    if isBottomLayerFullySolved(theCube):
        return ''
    else:
        while isBottomLayerFullySolved(theCube) == False:
            index = FindBottomLayerIndexes(theCube)
            #print(theCube.get())
            #print(index)
            #print(theCube.get()[index])
            if isIndexInUpperCorner(theCube, index):
                rotations += moveIndexInUpperCorner(theCube, index)
            elif isIndexInLowerCorner(theCube, index):
                r, triggerDir = moveIndexInLowerCorner(theCube, index)
                
                if triggerDir == 'l': 
                    r += theCube.rightTrigger(index)
                    r += theCube.rightTrigger(index)
                elif triggerDir == 'r':
                    r += theCube.leftTrigger(index)
                    r += theCube.leftTrigger(index)
                rotations += r  
            elif isIndexInveryTop(theCube, index):
                rotations += moveIndexInveryTop(theCube, index)
            elif index == -1:
                solveBottomCross(theCube)
    return rotations      #TODO:  remove this stubbed value

def isBottomLayerFullySolved(theCube: Cube):
    flag = True
    for index in range(45, 54):
        if theCube.getindex(index) != theCube.getindex(49):
            flag = False
            break
    return flag

def FindBottomLayerIndexes(theCube: Cube):
    possibleIndexes = [0, 2, 9, 11, 18, 20, 27, 29, 6, 8, 15, 17, 24, 26, 33, 35, 42, 44, 36, 38]
    for index in possibleIndexes:
        if theCube.getindex(index) == theCube.getindex(49):
            return index
    return -1
            
def decideTriggerDirection(index,theCube: Cube) -> str:
    middle = theCube.findCurrentMiddle(index)
    if index < middle: 
        if middle - index == 2: 
            return theCube.rightTrigger(index), 'r'
        elif middle - index == 4:
            return theCube.leftTrigger(index), 'l'
    elif index > middle: 
        if index - middle == 2: 
            return theCube.leftTrigger(index), 'l'
        elif index - middle == 4:
            return theCube.rightTrigger(index), 'r'
    return "", ''
   
def isIndexInUpperCorner(theCube: Cube, index):
    upperCornerElements = [0, 2, 9, 11, 18, 20, 27, 29]
    if index in upperCornerElements:
        return True
    return False

def isIndexInLowerCorner(theCube, index):
    #do trigger 
    lowerCornerElements=[6,8,15,17,24,26,33,35]
    if index in lowerCornerElements:
        return True
    return False

def isIndexInveryTop (theCube:Cube, index):
    #do trigger 
    veryTopElements=[36,38,42,44]
    if index in veryTopElements:
        return True
    return False

def moveIndexInUpperCorner(theCube : Cube, index):
    #print('I am in moveIndexInUpperCorner')
    rotations = "" 
    side = theSide(theCube, index)
    rotations += theCube.alignedIndexToItsProperFace(side)
    r , triggerDir = decideTriggerDirection(side, theCube)
    rotations += r
    #print(theCube.get())
    return rotations

def moveIndexInLowerCorner(theCube : Cube, index):
    return decideTriggerDirection(index, theCube)

def moveIndexInveryTop (theCube : Cube, index):
    #print("moveIndexInveryTop")
    if index == 42:
        theCube.rotate('LUl')
        theCube.rotate('LUl')
        return 'LUlLUl'
    elif index == 44:
        theCube.rotate('ruR')
        theCube.rotate('ruR')
        return 'ruRruR'
    elif index == 36:
        theCube.rotate('luL')
        theCube.rotate('luL')
        return 'luLluL'
    elif index == 38:
        theCube.rotate('RUr')
        theCube.rotate('RUr')
        #print("I am here")
        #print(theCube.get())
        return 'RUrRUr'
    #print(theCube.get())
    return ''

def theSide(theCube : Cube, index):
    if index == 0: 
        return 29
    elif index == 29:
        return 0
    elif index == 2:
        return 9
    elif index == 9:
        return 2
    elif index == 11:
        return 18
    elif index == 18:
        return 11
    elif index == 20:
        return 27
    elif index == 27:
        return 20
    return -1
>>>>>>> refs/heads/increment4
