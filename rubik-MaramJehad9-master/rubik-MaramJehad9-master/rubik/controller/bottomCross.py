import rubik.model.constants
from rubik.model.cube import Cube
from distutils.command.check import check


def solveBottomCross(theCube: Cube) -> str:
    rotations = ""
    upIndexes = [37, 39, 41, 43]
    if isUpDaizzySolved(theCube, upIndexes):
        return ''
    else:
        while not isUpDaizzySolved(theCube, upIndexes):
            rotations += solveUpperDaizy(theCube, upIndexes)
            
        rotations += partialSolutionOfBottomPart(theCube)
        return rotations

def isUpDaizzySolved(theCube, upIndexes):
    for index in upIndexes:
        if theCube.getindex(index) != theCube.getindex(49):
            return False
    return True

def solveUpperDaizy(theCube, upIndexes):
    rotations = ''
    for index in upIndexes:
        if theCube.getindex(index) != theCube.getindex(49):
            rotations += createDaizzy(theCube, index)
    return rotations
    
def createDaizzy(theCube, index):
    rotations = ""
    '''BottomIndexs = [14, 52, 30,3, 48, 23, 21, 50, 5, 12, 46, 32]
    rotation = ["B", 'BB', 'b', 'l', 'll', 'L', 'r', 'rr', 'R', 'f', 'ff', 'F' ]'''
    
    if index == 37:
        if theCube.getindex(14) == theCube.getindex(49):
            theCube.rotate('B')
            rotations += 'B'
        elif theCube.getindex(52) == theCube.getindex(49):
            theCube.rotate('BB')
            rotations += 'BB'
        elif theCube.getindex(30) == theCube.getindex(49):
            theCube.rotate('b')
            rotations += 'b'
        else: 
            rotations += notInDaizzy(theCube, index)
    elif index ==39:    
        if theCube.getindex(3) == theCube.getindex(49):
            theCube.rotate('l')
            rotations += 'l'
        elif theCube.getindex(48) == theCube.getindex(49):
            theCube.rotate('ll')
            rotations += 'll'
        elif theCube.getindex(23) == theCube.getindex(49):
            theCube.rotate('L')
            rotations += 'L'
        else: 
            rotations += notInDaizzy(theCube, index)
    elif index ==41:    
        if theCube.getindex(21) == theCube.getindex(49):
            theCube.rotate('r')
            rotations += 'r'
        elif theCube.getindex(50) == theCube.getindex(49):
            theCube.rotate('rr')
            rotations += 'rr'
        elif theCube.getindex(5) == theCube.getindex(49):
            theCube.rotate('R')
            rotations += 'R'
        else: 
            rotations += notInDaizzy(theCube, index)
    elif index ==43:    
        if theCube.getindex(12) == theCube.getindex(49):
            theCube.rotate('f')
            rotations += 'f'
        elif theCube.getindex(46) == theCube.getindex(49):
            theCube.rotate('ff')
            rotations += 'ff'
        elif theCube.getindex(32) == theCube.getindex(49):
            theCube.rotate('F')
            rotations += 'F'
        else: 
            rotations += notInDaizzy(theCube, index)
            
    return rotations

def partialSolutionOfBottomPart(theCube):
    r =''
    if theCube.get()[37] == theCube.get()[49]:
        theCube.alignedIndexToItsProperFace(19)
        theCube.rotate('bb')
        r+='bb'
        
    if theCube.get()[41] == theCube.get()[49]:
        theCube.alignedIndexToItsProperFace(10)
        theCube.rotate('rr')
        r+='rr'
        
    if theCube.get()[43] == theCube.get()[49]:
        theCube.alignedIndexToItsProperFace(1)
        theCube.rotate('ff')
        r += 'ff'
        
    if theCube.get()[39] == theCube.get()[49]:
        theCube.alignedIndexToItsProperFace(28)
        theCube.rotate('ll')
        r+='ll'
    return r
    
def notInDaizzy(theCube, index):
    rotations = ""
    '''BottomIndexs = [5, 14, 23, 32, 3, 12, 21, 30]
    rotation = ['uR', 'uB', 'uL', 'uF', 'Ul', 'Uf', 'Ur', 'Ub']'''
    if index == 37:
        if theCube.getindex(23) == theCube.getindex(49):
            theCube.rotate('uL')
            rotations += 'uL'
        elif theCube.getindex(21) == theCube.getindex(49):
            theCube.rotate('Ur')
            rotations += 'Ur'
        elif theCube.getindex(25) == theCube.getindex(49):
            theCube.rotate('buL')
            rotations += 'buL'
        elif theCube.getindex(19) == theCube.getindex(49):
            theCube.rotate('BuL')
            rotations += 'BuL'
    elif index == 39:
        if theCube.getindex(30) == theCube.getindex(49):
            theCube.rotate('Ub')
            rotations += 'Ub'
        elif theCube.getindex(32) == theCube.getindex(49):
            theCube.rotate('uF')
            rotations += 'uF'
        elif theCube.getindex(34) == theCube.getindex(49):
            theCube.rotate('luF')
            rotations += 'luF'
        elif theCube.getindex(28) == theCube.getindex(49):
            theCube.rotate('LuF')
            rotations += 'LuF'
    elif index == 41:
        if theCube.getindex(12) == theCube.getindex(49):
            theCube.rotate('Uf')
            rotations += 'Uf'
        elif theCube.getindex(14) == theCube.getindex(49):
            theCube.rotate('uB')
            rotations += 'uB'
        elif theCube.getindex(16) == theCube.getindex(49):
            theCube.rotate('ruB')
            rotations += 'ruB'
        elif theCube.getindex(10) == theCube.getindex(49):
            theCube.rotate('RuB')
            rotations += 'RuB'
    elif index == 43:
        if theCube.getindex(3) == theCube.getindex(49):
            theCube.rotate('Ul')
            rotations += 'Ul'
        elif theCube.getindex(5) == theCube.getindex(49):
            theCube.rotate('uR')
            rotations += 'uR'
        elif theCube.getindex(7) == theCube.getindex(49):
            theCube.rotate('fuR')
            rotations += 'fuR'
        elif theCube.getindex(1) == theCube.getindex(49):
            theCube.rotate('FuR')
            rotations += 'FuR'
    return rotations


































'''    
    rotationStr = ""    
    relatedTo37_ = [14, 52, 30]
    associatedRotate37_ = ['B', 'BB', 'b']
    relatedTo37 =  [10, 16, 28, 34]
    associatedRotate37 = ['RB','rB','lb','Lb']
    relatedTo39_ = [3, 48, 23]
    associatedRotate39_ = ['l', 'll', 'L']
    relatedTo39 = [ 7, 25, 19]
    associatedRotate39 = ['Fl', 'bL','BL']
    relatedTo41_ = [5, 50, 21]
    associatedRotate41_ = ['R', 'RR', 'r']
    relatedTo41 = [1, 7, 19, 25]
    associatedRotate41 = ['FR','fR', 'br', 'Br']
    relatedTo43_ = [12, 46, 32]
    associatedRotate43_ = ['f','FF', 'F']
    relatedTo43 = [28, 34, 16, 11]
    associatedRotate43 = ['LF', 'lF', 'Rf', 'rf']
    if allDone(theCube.get()): #does it need any rotationStr? 
        return ''
    if isUpEqualsCubeIndex49(theCube.get()):
        rotationStr += rotateFRBLSides(theCube.get(), theCube)
    else: 
        while not isUpEqualsCubeIndex49(theCube.get()):
            if isAnyAvailable(theCube.get()) == 37:
                rotationStr += availablity37(theCube, relatedTo37_, associatedRotate37_)
                if not Is37Equals49(theCube.get()):
                    rotationStr  += availablity37(theCube, relatedTo37, associatedRotate37) 
                print(theCube.get())
            elif isAnyAvailable(theCube.get()) == 39:
                rotationStr +=availablity39(theCube, relatedTo39_, associatedRotate39_)
                if not Is39Equals49(theCube.get()):
                    rotationStr +=availablity39(theCube, relatedTo39, associatedRotate39)
                print(theCube.get())
            elif isAnyAvailable(theCube.get()) == 41:
                rotationStr +=availablity41(theCube, relatedTo41_, associatedRotate41_)
                if not Is41Equals49(theCube.get()):
                    rotationStr += availablity41(theCube, relatedTo41, associatedRotate41)
                print(theCube.get())
            elif isAnyAvailable(theCube.get()) == 43:
                rotationStr +=availablity43(theCube, relatedTo43_, associatedRotate43_)
                if not Is43Equals49(theCube.get()):
                    rotationStr += availablity43(theCube, relatedTo43, associatedRotate43)
                print(theCube.get())
            else: break
    print("up is done")     
    if isUpEqualsCubeIndex49(theCube.get()):
        rotationStr += rotateFRBLSides(theCube.get(), theCube)
    print(theCube.get())
    return rotationStr

def checkIsEqual49(theCube, relatedToIndex):
    for i in relatedToIndex:
        if theCube[i] == theCube[49]:
            return True
    return False

def isAnyAvailable(theCube):
    relatedTo37 = [10, 14, 16, 52, 28, 30, 34, 32]    
    relatedTo39 = [3, 7, 48, 25, 23]
    relatedTo41 = [1, 5, 7, 50]
    relatedTo43 = [10, 12, 16, 46, 28, 32, 34 ]

    for index in relatedTo37: 
        if theCube[index] == theCube[49]: 
            return 37
    for index in relatedTo39: 
        if theCube[index] == theCube[49]: 
            return 39
    for index in relatedTo41: 
        if theCube[index] == theCube[49]: 
            return 41
    for index in relatedTo43: 
        if theCube[index] == theCube[49]: 
            return 43
        

def concatRotations (cubeObj, rotationStr, strRotations):
    cubeObj.rotate(strRotations)
    rotationStr += strRotations
    return rotationStr

def availablity37(theCube, indexes, rotation):
    rotationStr =""
    if not Is37Equals49(theCube.get()):
            rotationStr+=  doIndex37(theCube.get(), theCube, indexes, rotation)
    elif not Is39Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "U")
            rotationStr+=  doIndex37(theCube.get(), theCube, indexes, rotation)
    elif not Is41Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "u")
            rotationStr+=  doIndex37(theCube.get(), theCube,  indexes, rotation)
    elif not Is43Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "UU")
            rotationStr+=  doIndex37(theCube.get(), theCube,  indexes, rotation)
    return rotationStr

def availablity39(theCube,  indexes, rotation):
    rotationStr =""
    if not Is37Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "u")
            rotationStr+=  doIndex39(theCube.get(),  theCube, indexes, rotation) 
    elif not Is39Equals49(theCube.get()):
            rotationStr+=  doIndex39(theCube.get(), theCube,  indexes, rotation) 
    elif not Is41Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "uu")
            rotationStr+=  doIndex39(theCube.get(), theCube,  indexes, rotation) 
    elif not Is43Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "U")
            rotationStr+=  doIndex39(theCube.get(), theCube,  indexes, rotation) 
    return rotationStr

def availablity41(theCube,  indexes, rotation):
    rotationStr =""
    if not Is37Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "U")
            rotationStr+=  doIndex41(theCube.get(), theCube,  indexes, rotation)
    elif not Is39Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "UU")
            rotationStr+=  doIndex41(theCube.get(), theCube,  indexes, rotation)
    elif not Is41Equals49(theCube.get()):
            rotationStr+=  doIndex41(theCube.get(), theCube,  indexes, rotation)
    elif not Is43Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "u")
            rotationStr+=  doIndex41(theCube.get(), theCube,  indexes, rotation)
    return rotationStr

def availablity43(theCube,  indexes, rotation):
    rotationStr =""
    if not Is37Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "UU")
            rotationStr+= doIndex43(theCube.get(), theCube, rotation)
    elif not Is39Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "u")
            rotationStr+=  doIndex43(theCube.get(), theCube,  indexes, rotation)
    elif not Is41Equals49(theCube.get()):
            concatRotations(theCube, rotationStr, "U")
            rotationStr+=  doIndex43(theCube.get(), theCube,  indexes, rotation)
    elif not Is43Equals49(theCube.get()):
            rotationStr+=  doIndex43(theCube.get(), theCube,  indexes, rotation)
    return rotationStr

def doIndex37(theCube, _theCube, indexes, rotation):
    rotationStr = ""
    if Is37Equals49(theCube):
        return ''
    else:
        j = 0 
        if checkIsEqual49(theCube, indexes):
            for i in indexes: 
                if theCube[i] == theCube[49]:
                    _theCube.rotate(rotation[j])
                    rotationStr += rotation[j]
                    break
                j+=1
                
    return rotationStr

def doIndex39(theCube, _theCube,  indexes, rotation):
    rotationStr= ""
    if Is39Equals49(theCube):
        return ''
    else : 
        j = 0 
        for i in indexes: 
            if theCube[i] == theCube[49]:
                _theCube.rotate(rotation[j])
                rotationStr += rotation[j]
                break
            j+=1
    print("in doIndex39")
    return rotationStr

def doIndex41(theCube, _theCube, indexes, rotation):
    rotationStr =""
    if Is41Equals49(theCube):
        return ''
    else : 
        j = 0 
        for i in indexes: 
            if theCube[i] == theCube[49]:
                _theCube.rotate(rotation[j])
                rotationStr += rotation[j]
                break
            j+=1
    return rotationStr

def doIndex43(theCube, _theCube, indexes, rotation):
    rotationStr =""
    if Is43Equals49(theCube):
        return ''
    else : 
        j = 0 
        for i in indexes: 
            if theCube[i] == theCube[49]:
                _theCube.rotate(rotation[j])
                rotationStr += rotation[j]
                break
            j+=1

    return rotationStr

def allDone(theCube):
    bottomIndexes = [46,50,48,52]
    for i in bottomIndexes: 
        if theCube[49] != theCube[i]:
            return False  
         
    if theCube[4] != theCube[7] or theCube[13] != theCube[16] or theCube[22] != theCube[25] or theCube[31] != theCube[34]:
        return False 
    return True

def isUpEqualsCubeIndex49(theCube):
    upIndexes = [37, 39, 41, 43]
    flag = True
    for i in upIndexes: 
        if theCube[49]!= theCube[i]:
            flag = False
    return flag
  
def rotateFRBLSides (theCube, _theCube)  -> str:
    rotationStr =""
    print("sides is working") 
    indexes = [1, 10, 19, 28]
    relatedIndexInUp = [43,41, 37, 39]
    rotationsFor4 = ["FF","U", "uu", "u"]
    rotationsFor13 = ["u", "RR", "U", "uu"]
    rotationsFor31 = ['U', 'UU', 'u', 'LL']  
    rotationsFor22 = ['uu', 'u', 'BB', 'U']

    j=0
    for i in indexes: 
        if _theCube.get()[49] == _theCube.get()[relatedIndexInUp[j]] and _theCube.get()[i] == _theCube.get()[4]:
            _theCube.rotate(rotationsFor4[j])
            rotationStr += rotationsFor4[j]
            break
        j+=1
    if  _theCube.get()[49] == _theCube.get()[43] and _theCube.get()[1] == _theCube.get()[4]:
        rotationStr = concatRotations(_theCube, rotationStr, 'FF')
    j=0
    for i in indexes: 
        if _theCube.get()[49] == _theCube.get()[relatedIndexInUp[j]] and _theCube.get()[i] == _theCube.get()[13]:
            _theCube.rotate(rotationsFor13[j])
            rotationStr += rotationsFor13[j]
            break
        j+=1
    if _theCube.get()[49] == _theCube.get()[41] and _theCube.get()[10] == _theCube.get()[13] : 
        rotationStr = concatRotations(_theCube, rotationStr, "RR")     
    j=0
    for i in indexes: 
        if _theCube.get()[49] == _theCube.get()[relatedIndexInUp[j]] and _theCube.get()[i] == _theCube.get()[22]:
            _theCube.rotate(rotationsFor22[j])
            rotationStr += rotationsFor22[j]
            break
        j+=1
    if _theCube.get()[19] == _theCube.get()[22] and _theCube.get()[49] == _theCube.get()[37]: 
        rotationStr = concatRotations(_theCube, rotationStr, "BB")   
    j=0
    for i in indexes: 
        if  _theCube.get()[49] == _theCube.get()[relatedIndexInUp[j]] and _theCube.get()[i] == _theCube.get()[31]:
            _theCube.rotate(rotationsFor31[j])
            rotationStr += rotationsFor31[j]
            break
        j+=1
    if _theCube.get()[28] == _theCube.get()[31] and _theCube.get()[49] == _theCube.get()[39]: 
        rotationStr = concatRotations(_theCube, rotationStr, "LL")
    print(_theCube.get())   
    return rotationStr

def Is37Equals49(theCube_):
    #theCube_ = theCube.get()
    return theCube_[37] == theCube_[49]

def Is39Equals49(theCube):
    return theCube[39] == theCube[49]
    
def Is41Equals49(theCube):
    return theCube[41] == theCube[49]

def Is43Equals49(theCube):
    return theCube[43] == theCube[49]
<<<<<<< HEAD

#        input:  an instance of the cube class
 #       output: the rotations required to transform the input cube into the down-face cross 
    '''  
    if checkForDownEdges(theCube):
        return 'empty'
    else:
        BMMChar = checkIndexBMM(theCube)
        TopIndexes = [37,39,41,43]
        for index in TopIndexes:
            while theCube.getIndex(index)!= BMMChar:
                if checkRight(theCube,index):
                    break
                elif checkLeft(theCube,index):
                    break
                elif checkRightTop(theCube,index):
                    break
                elif checkLeftTop(theCube,index):
                    break
        
            
                
        return listOfRotations(theCube)
    
    
    
def checkIndexBMM(theCube):
    return theCube.getIndex(49)

def listOfRotations(rotationChar):
    
    return ''.join(rotationChar)

def checkRight(theCube, index):
    bmmChar = checkIndexBMM(theCube)
    if theCube.getIndex(14) == bmmChar:
        theCube.rotate('B')
        listOfRotations('B')
        return True
    return False

def checkLeft(theCube, index):
    bmmChar = checkIndexBMM(theCube)
    if theCube.getIndex(30) == bmmChar:
        theCube.rotate('b')
        listOfRotations('b')

def checkRightTop(theCube,index):
    bmmChar = checkIndexBMM(theCube)
    if theCube.getIndex(10) == bmmChar:
        theCube.rotate('RB')
        listOfRotations('RB')

def checkLeftTop(theCube,index):
    bmmChar = checkIndexBMM(theCube)
    if theCube.getIndex(28) == bmmChar:
        theCube.rotate('lb')
        listOfRotations('lb')

def checkForDownEdges(theCube):
    BMMChar = check
    flag = True
    if theCube.getIndex(46) != BMMChar:
        flag = False
    if theCube.getIndex(50) != BMMChar:
        flag = False
    if theCube.getIndex(52) != BMMChar:
        flag = False
    if theCube.getIndex(48) != BMMChar:
        flag = False
    
    if theCube.getIndex(7) != theCube.getIndex(5):
        flag = False
    if theCube.getIndex(13) != theCube.getIndex(16):
        flag = False
    if theCube.getIndex(22) != theCube.getIndex(26):
        flag = False
    if theCube.getIndex(31) != theCube.getIndex(34):
        flag = False
        
    return flag
'''
def FrontWithBMMChar(theCube):
    
    for i in range(0,9):
        if theCube.get[1] == theCube.get()[43]:
            theCube.rotate('F')
            theCube.rotate('R')
            
=======
'''
>>>>>>> refs/heads/increment4
