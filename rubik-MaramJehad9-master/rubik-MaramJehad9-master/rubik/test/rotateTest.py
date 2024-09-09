from unittest import TestCase
from rubik.view.rotate import rotate
from pickle import NONE
 
class RotateTest(TestCase):      
# Happy path
#    Test that the stubbed rotate returns the correct result
    def test_rotate_0910_returnStubbedSolution(self):
        encodedCube = 'ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual("brobbowwybyobroobowbrggwwrybwygoygogwwbrygrgyrogywrryg", result.get('cube'))
        
    def test_rotate_0920_checkInvalidSingleDirection(self):
        encodedCube = 'BlHJHJJBulueeJJeBBBlBBeHlBJluJJluuuuHHJlBeHeuellHueHHe'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'd'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid dir', result['status'])
    
    def test_rotate_0930_checkInvalidMultipleDirection(self):
        encodedCube = '6G2q9069099G2GG26626G9q0qq092G902qq020qG6296096q02q6GG'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfRrBbLlUuDd'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid dir', result['status'])
    
    def test_rotate_0940_checkInvalidCube(self):
        encodedCube = 'wbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywryg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'b'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_rotate_0950_checkInvalidCube(self):
        encodedCube = 'ooyrbwbbwgyoor/rbowbrg gwwrybwygoggorwwbrygbboyygywryg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'f'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
          
    def test_rotate_0960_checkInvalidDirectionAndCube(self):
        encodedCube = 'ooyrbwbbwgyoororbowbrggwwrybwygog--rwwbrygbboyygywrryg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'd'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid dir and invalid cube', result['status'])
    
    def test_rotate_0970_checkNoneCube(self):
        parms = {}
        parms['cube'] = None
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test_rotate_0980_checkShortCube(self):
        parms = {}
        parms['cube'] = 'T0x0TxJ40JxxJ0440004DD'
        parms['dir'] = 'r'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test_rotate_0990_checkLongCube(self):
        parms = {}
        parms['cube'] = 'ssEtsHkXkXkHEEtXkXEXskXHHtHEEkskXXXHtHsststttsEtkHHkEEssEtsHkXkXkHEEtXkXEXskXHHtHEEk'
        parms['dir'] = 'r'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test_rotate_1000_checkIllegalCharInCube(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbb         rrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        parms['dir'] = 'r'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test_rotate_1100_checkInvalidKey(self):
        encodedCube = 'ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        parms['key3'] = '123'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: extraneous key detected', result['status'])
    
    def test_rotate_1200_checkNoneDir(self):
        encodedCube = '7pkk79hp999lhk7hhlh79hpppkhkkl9h99pl7l77l7kkppl7h9lplk'
        parms = {}
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual("hk7p7p99kk9lkk7phlh79hpppkhkkp9hl9p77l77l7l9lhh9h9lplk", result.get('cube'))
        
    def test_rotate_1300_checkUniqueMiddleElementsInCube(self):
        encodedCube = 'rbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        parms = {}
        parms['dir'] = 'l'
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test_rotate_1400_checkCubeWith9OccurrencesOfLegalCharacters(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwb'
        parms = {}
        parms['dir'] = 'B'
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    