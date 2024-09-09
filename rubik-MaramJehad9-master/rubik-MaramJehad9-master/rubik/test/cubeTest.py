'''
Created on Jan 29, 2023

@author: MaramJehad
'''
import unittest
import rubik.model.cube as cube

class CubeTest(unittest.TestCase):
    def test_rotate_010_ShouldRotateCubeInFDirection(self):
        CubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual(rotatedCube, 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
    
    def test_rotate_020_ShouldRotateCubeInfDirection(self):
        CubeToRotate = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('f')
        self.assertEqual(rotatedCube, 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy')


    def test_rotate_030_ShouldRotateCubeInRDirection(self):
        CubeToRotate = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('R')
        self.assertEqual(rotatedCube, 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb')

    def test_rotate_040_ShouldRotateCubeInrDirection(self):
        CubeToRotate = 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('r')
        self.assertEqual(rotatedCube, 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy')
            
    def test_rotate_050_ShouldRotateCubeInUDirection(self):
        CubeToRotate = 'gbgvoggugprweghlrhbeasbbsbbogojkonoddazxwwhhywwyytffaa'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('U')
        self.assertEqual(rotatedCube, 'prwvoggugbeaeghlrhogosbbsbbgbgjkonodhxdhwaywzwwyytffaa')
    
    def test_rotate_060_ShouldRotateCubeInuDirection(self):
        CubeToRotate = 'prwvoggugbeaeghlrhogosbbsbbgbgjkonodhxdhwaywzwwyytffaa'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('u')
        self.assertEqual(rotatedCube, 'gbgvoggugprweghlrhbeasbbsbbogojkonoddazxwwhhywwyytffaa')
    
    def test_rotate_070_ShouldRotateCubeInBDirection(self):
        CubeToRotate = 'YEOOll3CCE3C3Y33CYEYlCEllOOOCCY3lE3E3EYlOElO3CYlOCEYYO'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('B')
        self.assertEqual(rotatedCube, 'YEOOll3CCE3O3YY3CYlCEOEYOllYCCE3l33EC3YlOElO3CYlOCEOYE')
    
    def test_rotate_080_ShouldRotateCubeInbDirection(self):
        CubeToRotate = 'YEOOll3CCE3O3YY3CYlCEOEYOllYCCE3l33EC3YlOElO3CYlOCEOYE'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('b')
        self.assertEqual(rotatedCube, 'YEOOll3CCE3C3Y33CYEYlCEllOOOCCY3lE3E3EYlOElO3CYlOCEYYO')
         
    def test_rotate_090_ShouldRotateCubeInLDirection(self):
        CubeToRotate = 'dddeeefffggghhhiiimmmnnnoooaaabbbcccqqqrrrsssjjjkkklll'                                       
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('L')
        self.assertEqual(rotatedCube, 'qddreesffggghhhiiimmlnnkoojcbacbacbaoqqnrrmssdjjekkfll')                        
                         
    def test_rotate_100_ShouldRotateCubeInlDirection(self):
        CubeToRotate = 'qddreesffggghhhiiimmlnnkoojcbacbacbaoqqnrrmssdjjekkfll'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate('l')
        self.assertEqual(rotatedCube, 'dddeeefffggghhhiiimmmnnnoooaaabbbcccqqqrrrsssjjjkkklll')
    
    def test_rotate_110_ShouldRotateCubeInDefaultDirection(self):
        CubeToRotate = 'ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg'
        theCube = cube.Cube(CubeToRotate)
        rotatedCube = theCube.rotate(None)
        self.assertEqual(rotatedCube, 'brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg')
    
    def test_rotate_120_ShouldRotateCubeInMultiDirection(self):
        CubeToRotate = 'EE7WWbbWyqbyyqybyEbqy7bbbWE7Eq7yEWyqW77qEqWbW7qEE7Wy7q'
        theCube = cube.Cube(CubeToRotate)
        print("multi dir BFlLUu")
        rotatedCube = theCube.rotate('BFlLUu')
        self.assertEqual(rotatedCube, 'bWEWWEyb7Wbqbq7Wyyb7bWbqEby7E77yqWyEyyEqEqqEqbyqE7W77W')
    
    #def test_rotate_130_alignedToMiddle(self):
        