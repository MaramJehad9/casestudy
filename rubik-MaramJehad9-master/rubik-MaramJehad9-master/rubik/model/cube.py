from rubik.model.constants import *
from jinja2.nodes import Or
from _operator import index
from math import ceil
from pickle import TRUE
from pip._vendor.typing_extensions import Self

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cube = str(encodedCube)
    
    def getIndex(self, index):
        if index>=0:
            return self._cube[index]
        return -1   
        
    def getindex(self, index):
        return self._cube[index]
    
    def rotate(self, direction):
        if direction== None:
            direction = 'F'
        for x in direction:  
            if x == 'F':
                self._rotateF()
                
            elif x == 'f':
                self._rotatef()
               
            elif x == 'B':
                self._rotateB()
               
            elif x == 'b':
                self._rotateb()
            elif x == 'R':
                self._rotateR()
               
            elif x == 'r':
                self._rotater()
              
            elif x == 'U':
                self._rotateU()
           
            elif x == 'u':
                self._rotateu()
   
            elif x == 'L':
                self._rotateL()

            elif x == 'l':
                self._rotatel()
   
            
        return self._cube
        
    def _rotateF(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
    
        #rotate front face
        rotatedCubeList[FTR] = cubeList[FTL]
        rotatedCubeList[FMR] = cubeList[FTM]
        rotatedCubeList[FBR] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FMR]
        rotatedCubeList[FTL] = cubeList[FBL]
        rotatedCubeList[FML] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FBR]
    
        #rotate up to right
        rotatedCubeList[RTL] = cubeList[UBL]
        rotatedCubeList[RML] = cubeList[UBM]
        rotatedCubeList[RBL] = cubeList[UBR]
    
        #rotate right to bottom
        rotatedCubeList[DTR] = cubeList[RTL]
        rotatedCubeList[DTM] = cubeList[RML]
        rotatedCubeList[DTL] = cubeList[RBL]
    
        #rotate bottom to left    
        rotatedCubeList[LTR] = cubeList[DTL]
        rotatedCubeList[LMR] = cubeList[DTM]
        rotatedCubeList[LBR] = cubeList[DTR]
    
        #rotate left to top    
        rotatedCubeList[UBR] = cubeList[LTR]
        rotatedCubeList[UBM] = cubeList[LMR]
        rotatedCubeList[UBL] = cubeList[LBR]
        self._cube = "".join(rotatedCubeList)

    def _rotatef(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]    
        #rotate front face
        rotatedCubeList[FTL] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FMR]
        rotatedCubeList[FTR] = cubeList[FBR]
        rotatedCubeList[FML] = cubeList[FTM]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FMR] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FTL]
        rotatedCubeList[FBM] = cubeList[FML]
        rotatedCubeList[FBR] = cubeList[FBL]
    
        #rotate up to right
        rotatedCubeList[UBL] = cubeList[RTL]
        rotatedCubeList[UBM] = cubeList[RML]
        rotatedCubeList[UBR] = cubeList[RBL]
    
        #rotate right to bottom
        rotatedCubeList[RTL] = cubeList[DTR]
        rotatedCubeList[RML] = cubeList[DTM]
        rotatedCubeList[RBL] = cubeList[DTL]
    
        #rotate bottom to left    
        rotatedCubeList[DTL] = cubeList[LTR]
        rotatedCubeList[DTM] = cubeList[LMR]
        rotatedCubeList[DTR] = cubeList[LBR]
    
        #rotate left to top    
        rotatedCubeList[LTR] = cubeList[UBR]
        rotatedCubeList[LMR] = cubeList[UBM]
        rotatedCubeList[LBR] = cubeList[UBL]
        self._cube = "".join(rotatedCubeList)

    def _rotateR(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
    
        #rotate front face
        rotatedCubeList[RTR] = cubeList[RTL]
        rotatedCubeList[RMR] = cubeList[RTM]
        rotatedCubeList[RBR] = cubeList[RTR]
        rotatedCubeList[RTM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RBM] = cubeList[RMR]
        rotatedCubeList[RTL] = cubeList[RBL]
        rotatedCubeList[RML] = cubeList[RBM]
        rotatedCubeList[RBL] = cubeList[RBR]
    
        #rotate Front to Top
        rotatedCubeList[UTR] = cubeList[FTR]
        rotatedCubeList[UMR] = cubeList[FMR]
        rotatedCubeList[UBR] = cubeList[FBR]
    
        
        rotatedCubeList[BTL] = cubeList[UBR]
        rotatedCubeList[BML] = cubeList[UMR]
        rotatedCubeList[BBL] = cubeList[UTR]
    
           
        rotatedCubeList[DTR] = cubeList[BBL]
        rotatedCubeList[DMR] = cubeList[BML]
        rotatedCubeList[DBR] = cubeList[BTL]
    
           
        rotatedCubeList[FTR] = cubeList[DTR]
        rotatedCubeList[FMR] = cubeList[DMR]
        rotatedCubeList[FBR] = cubeList[DBR]
        self._cube = "".join(rotatedCubeList)

    def _rotater(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
    
        #rotate front face
        rotatedCubeList[9] = cubeList[11]
        rotatedCubeList[10] = cubeList[14]
        rotatedCubeList[11] = cubeList[17]
        rotatedCubeList[12] = cubeList[10]
        rotatedCubeList[13] = cubeList[13]
        rotatedCubeList[14] = cubeList[16]
        rotatedCubeList[15] = cubeList[9]
        rotatedCubeList[16] = cubeList[12]
        rotatedCubeList[17] = cubeList[15]
    
        #rotate Front to Top
        rotatedCubeList[2] = cubeList[38]
        rotatedCubeList[5] = cubeList[41]
        rotatedCubeList[8] = cubeList[44]
    
        
        rotatedCubeList[44] = cubeList[18]
        rotatedCubeList[41] = cubeList[21]
        rotatedCubeList[38] = cubeList[24]
    
           
        rotatedCubeList[24] = cubeList[47]
        rotatedCubeList[21] = cubeList[50]
        rotatedCubeList[18] = cubeList[53]
    
           
        rotatedCubeList[47] = cubeList[2]
        rotatedCubeList[50] = cubeList[5]
        rotatedCubeList[53] = cubeList[8]
        self._cube = "".join(rotatedCubeList)
        
    def _rotateU(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
    
        #rotate up face
        rotatedCubeList[UTR] = cubeList[UTL]
        rotatedCubeList[UMR] = cubeList[UTM]
        rotatedCubeList[UBR] = cubeList[UTR]
        rotatedCubeList[UTM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UBM] = cubeList[UMR]
        rotatedCubeList[UTL] = cubeList[UBL]
        rotatedCubeList[UML] = cubeList[UBM]
        rotatedCubeList[UBL] = cubeList[UBR]
    
        #rotate Front to left
        rotatedCubeList[LTL] = cubeList[FTL]
        rotatedCubeList[LTM] = cubeList[FTM]
        rotatedCubeList[LTR] = cubeList[FTR]
    
        #rotate right to front
        rotatedCubeList[FTL] = cubeList[RTL]
        rotatedCubeList[FTM] = cubeList[RTM]
        rotatedCubeList[FTR] = cubeList[RTR]
    
        #rotate left to back    
        rotatedCubeList[BTL] = cubeList[LTL]
        rotatedCubeList[BTM] = cubeList[LTM]
        rotatedCubeList[BTR] = cubeList[LTR]
    
        #rotate back to bottom    
        rotatedCubeList[RTL] = cubeList[BTL]
        rotatedCubeList[RTM] = cubeList[BTM]
        rotatedCubeList[RTR] = cubeList[BTR]
        self._cube = "".join(rotatedCubeList)
    
    def _rotateu(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
    
        #rotate up face
        rotatedCubeList[UTL] = cubeList[UTR]
        rotatedCubeList[UTM] = cubeList[UMR]
        rotatedCubeList[UTR] = cubeList[UBR]
        rotatedCubeList[UML] = cubeList[UTM]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UMR] = cubeList[UBM]
        rotatedCubeList[UBL] = cubeList[UTL]
        rotatedCubeList[UBM] = cubeList[UML]
        rotatedCubeList[UBR] = cubeList[UBL]
    
        #rotate Front to left
        rotatedCubeList[FTL] = cubeList[LTL]
        rotatedCubeList[FTM] = cubeList[LTM]
        rotatedCubeList[FTR] = cubeList[LTR]
    
        #rotate right to front
        rotatedCubeList[RTL] = cubeList[FTL]
        rotatedCubeList[RTM] = cubeList[FTM]
        rotatedCubeList[RTR] = cubeList[FTR]
    
        #rotate left to back    
        rotatedCubeList[LTL] = cubeList[BTL]
        rotatedCubeList[LTM] = cubeList[BTM]
        rotatedCubeList[LTR] = cubeList[BTR]
    
        #rotate back to bottom    
        rotatedCubeList[BTL] = cubeList[RTL]
        rotatedCubeList[BTM] = cubeList[RTM]
        rotatedCubeList[BTR] = cubeList[RTR]
        self._cube = "".join(rotatedCubeList)
    
    
    def _rotateB(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
    
        #rotate back face
        rotatedCubeList[BTL] = cubeList[BBL]
        rotatedCubeList[BTM] = cubeList[BML]
        rotatedCubeList[BTR] = cubeList[BTL]
        rotatedCubeList[BML] = cubeList[BBM]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BMR] = cubeList[BTM]
        rotatedCubeList[BBL] = cubeList[BBR]
        rotatedCubeList[BBM] = cubeList[BMR]
        rotatedCubeList[BBR] = cubeList[BTR]
    
        #rotate right to up
        rotatedCubeList[36] = cubeList[11]
        rotatedCubeList[37] = cubeList[14]
        rotatedCubeList[38] = cubeList[17]
    
        #rotate up to left
        rotatedCubeList[27] = cubeList[38]
        rotatedCubeList[30] = cubeList[37]
        rotatedCubeList[33] = cubeList[36]
    
        #rotate left to bottom    
        rotatedCubeList[53] = cubeList[33]
        rotatedCubeList[52] = cubeList[30]
        rotatedCubeList[51] = cubeList[27]
    
        #rotate bottom to right    
        rotatedCubeList[11] = cubeList[53]
        rotatedCubeList[14] = cubeList[52]
        rotatedCubeList[17] = cubeList[51]
        self._cube = "".join(rotatedCubeList)
    
    
    def _rotateb(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
    
        #rotate back face
        rotatedCubeList[BBL] = cubeList[BTL]
        rotatedCubeList[BML] = cubeList[BTM]
        rotatedCubeList[BTL] = cubeList[BTR]
        rotatedCubeList[BBM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BTM] = cubeList[BMR]
        rotatedCubeList[BBR] = cubeList[BBL]
        rotatedCubeList[BMR] = cubeList[BBM]
        rotatedCubeList[BTR] = cubeList[BBR]
    
        #rotate right to up 
        rotatedCubeList[11] = cubeList[36]
        rotatedCubeList[14] = cubeList[37]
        rotatedCubeList[17] = cubeList[38]
    
        #rotate up to left
        rotatedCubeList[38] = cubeList[27]
        rotatedCubeList[37] = cubeList[30]
        rotatedCubeList[36] = cubeList[33]
    
        #rotate left to bottom    
        rotatedCubeList[33] = cubeList[53]
        rotatedCubeList[30] = cubeList[52]
        rotatedCubeList[27] = cubeList[51]
    
        #rotate bottom to right    
        rotatedCubeList[53] = cubeList[11]
        rotatedCubeList[52] = cubeList[14]
        rotatedCubeList[51] = cubeList[17]
        self._cube = "".join(rotatedCubeList)
        
    def _rotatel(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate back face
        rotatedCubeList[27] = cubeList[29]
        rotatedCubeList[28] = cubeList[32]
        rotatedCubeList[29] = cubeList[35]
        rotatedCubeList[30] = cubeList[28]
        rotatedCubeList[31] = cubeList[31]
        rotatedCubeList[32] = cubeList[34]
        rotatedCubeList[33] = cubeList[27]
        rotatedCubeList[34] = cubeList[30]
        rotatedCubeList[35] = cubeList[33]
    
        #rotate right to up
        rotatedCubeList[36] = cubeList[0]
        rotatedCubeList[39] = cubeList[3]
        rotatedCubeList[42] = cubeList[6]
    
        #rotate up to left
        rotatedCubeList[0] = cubeList[45]
        rotatedCubeList[3] = cubeList[48]
        rotatedCubeList[6] = cubeList[51]
    
        #rotate left to bottom    
        rotatedCubeList[45] = cubeList[26]
        rotatedCubeList[48] = cubeList[23]
        rotatedCubeList[51] = cubeList[20]
    
        #rotate bottom to right    
        rotatedCubeList[20] = cubeList[42]
        rotatedCubeList[23] = cubeList[39]
        rotatedCubeList[26] = cubeList[36]
        self._cube = "".join(rotatedCubeList)
    
    def _rotateL(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        
        #rotate back face
        rotatedCubeList[29] = cubeList[27]
        rotatedCubeList[32] = cubeList[28]
        rotatedCubeList[35] = cubeList[29]
        rotatedCubeList[28] = cubeList[30]
        rotatedCubeList[31] = cubeList[31]
        rotatedCubeList[34] = cubeList[32]
        rotatedCubeList[27] = cubeList[33]
        rotatedCubeList[30] = cubeList[34]
        rotatedCubeList[33] = cubeList[35]
    
        #rotate right to up
        rotatedCubeList[0] = cubeList[36]
        rotatedCubeList[3] = cubeList[39]
        rotatedCubeList[6] = cubeList[42]
    
        #rotate up to left
        rotatedCubeList[45] = cubeList[0]
        rotatedCubeList[48] = cubeList[3]
        rotatedCubeList[51] = cubeList[6]
    
        #rotate left to bottom    
        rotatedCubeList[26] = cubeList[45]
        rotatedCubeList[23] = cubeList[48]
        rotatedCubeList[20] = cubeList[51]
    
        #rotate bottom to right    
        rotatedCubeList[42] = cubeList[20]
        rotatedCubeList[39] = cubeList[23]
        rotatedCubeList[36] = cubeList[26]
        self._cube = "".join(rotatedCubeList)
        
    def alignedToTheMiddleMatch(self, index):
        #rotate the sending index to the middle which has the same char
        #FMM, RMM, BMM, LMM, UMM, DMM
        middleIndex = 0
        if self._cube[index] == self._cube[RMM]: 
            middleIndex = RMM
        elif self._cube[index] == self._cube[FMM]: 
            middleIndex = FMM
        elif self._cube[index] == self._cube[BMM]: 
            middleIndex = BMM
        elif self._cube[index] == self._cube[LMM]: 
            middleIndex = LMM
        elif self._cube[index] == self._cube[UMM]: 
            middleIndex = UMM
        elif self._cube[index] == self._cube[DMM]: 
            middleIndex = DMM
                
        while self._cube[index] != self._cube[middleIndex]:
            self._rotate('U')
    

    def checkUniqueElements(self):
        indexes = [4,13,22,31,40,49]
        for x in indexes:
            for y in indexes:
                if x != y:
                    if self._cube[x] != self._cube[y]:
                        continue
                    return False
        return True
    
    def isValid(self):
        if self._cube == None:
            return True
        if len(self._cube) != 54: 
            return True
        elif self._cube.isalnum() == False:
            return True
        elif self.checkUniqueElements() == False:
            return True


    def get(self):
        return self._cube
    
    def alignedIndexToItsProperFace(self, index):
        #find the crossponding middle eemet 
        distance = self.distanceBetweenIndexToMiddle(index)
        #do appropriate rotation depending on the distance between the index and appropriate middle element 
        return self.doAppropriateRotation(distance)
        
    def distanceBetweenIndexToMiddle(self, index):
        #value = self._cube[index]
        middle = self.findMiddle(index)
        #print("its middle", middle)
        #print(self._cube[middle], self._cube[index])
        
        differ = ceil((index - middle)/9)
        #print (index, middle)
        return differ
    
    def doAppropriateRotation (self, differ):
        #print('differ', differ)
        if differ == 2 or differ == -2:
            self._rotateU()
            self._rotateU()
            return "UU"
        elif differ == 1 or differ == -3:
            self._rotateU()
            return "U"
        elif differ == -1:
            self._rotateu()
            return "u"
        elif differ == 3 :
            self._rotateu()
            return "u"
        elif differ == 0:
            return ''
        return ""
    def HasTopFaceColor (self):
        A1 = [10, 41]
        A2 = [19, 37]
        A3 = [1, 43]
        A4 = [28, 39]
        val = self._cube[40]
        flag = False
        
        if any(self._cube[i] == val for i in A1):
            flag = True
        else:
            return A1
        if any(self._cube[i] == val for i in A2):
            flag = True
        else:
            return A2
        if any(self._cube[i] == val for i in A3):
            flag = True
        else:
            return A3
        if any(self._cube[i] == val for i in A4):
            flag = True
        else:
            return A4
        
        return [-1, -1]
    
    
    def alignTopElement (self, topElement, frontElement):
        topMiddle = self.findMiddle(topElement)
        frontMiddle = self.findMiddle(frontElement)
        rotation = ''
        
        if topMiddle == 4 and frontMiddle == 13:
          self._rotateu()
          rotation += self.leftTrigger(frontMiddle)
          return 'u' +rotation
        elif topMiddle == 13 and frontMiddle == 4:
          self._rotateU()
          rotation += self.rightTrigger(frontMiddle)
          return 'U' +rotation
        elif topMiddle == 4 and frontMiddle == 31:
          self._rotateU()
          rotation += self.rightTrigger(frontMiddle)
          return 'U' + rotation
        elif topMiddle == 31 and frontMiddle == 4:
          self._rotateu()
          rotation += self.leftTrigger(frontMiddle)
          return  'u' + rotation
        elif topMiddle == 31 and frontMiddle == 22:
          self._rotateU()
          rotation += self.rightTrigger(frontMiddle)
          return 'U' + rotation
        elif topMiddle == 22 and frontMiddle == 31:
          self._rotateu()
          rotation += self.leftTrigger(frontMiddle)
          return  'u' + rotation
        elif topMiddle == 22 and frontMiddle == 13:
          self._rotateU()
          rotation += self.rightTrigger(frontMiddle)
          return 'U' + rotation
        elif topMiddle == 13 and frontMiddle == 22:
          self._rotateu()
          rotation += self.leftTrigger(frontMiddle)
          return  'u' + rotation 
        return ''
    
    def findCurrentMiddle(self, index):
        if index in range(0,9):
           return 4
        elif index in range(9,18):
            return 13
        elif index in range(18,27):
            return 22
        elif index in range(27,36):
            return 31
        elif index in range(36,45):
            return 40
        elif index in range(45,54):
            return 49
        return -1
        
    def findMiddle(self, index):
        if self._cube[index] == self._cube[4]:
           return 4
        elif self._cube[index] == self._cube[13]:
            return 13
        elif self._cube[index] == self._cube[22]:
            return 22
        elif self._cube[index] == self._cube[31]:
            return 31
        elif self._cube[index] == self._cube[40]:
            return 40
        elif self._cube[index] == self._cube[49]:
            return 49
        return -1
    
    def leftTrigger(self, frontIndex):
        middle = self.findCurrentMiddle(frontIndex)
        if middle == 13 :
            self.rotate("fuF")
            return "fuF"
        elif middle == 4 :
            self.rotate("luL")
            return "luL"
        elif middle == 31 :
            self.rotate("buB")
            return "buB"
        elif middle == 22 :
            self.rotate("ruR")
            return "ruR"
        return ''
    
    def rightTrigger(self, frontIndex):
        middle = self.findCurrentMiddle(frontIndex)
        if middle == 13 :
            self.rotate("BUb")
            return "BUb"
        elif middle == 4 :
            self.rotate("RUr")
            return"RUr"
        elif middle == 31 :
            self.rotate("FUf")
            return "FUf"
        elif middle == 22 :
            self.rotate("LUl")
            return "LUl"
        return ''
    
    def dotrigger (self, index):
        middle = self.findMiddle(index)
        if index > middle:
            return self.rightTrigger(index)
        elif index < middle:
            return self.leftTrigger(index)
        return ""