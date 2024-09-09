from unittest import TestCase
from rubik.view.solve import solve
<<<<<<< HEAD
from rubik.model.cube import Cube  
from test.test_set import cube
=======
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
import random
 
>>>>>>> refs/heads/increment4

class SolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    def test100_solve_returnStubbedSolution(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))
    
    def test110_solve_test(self):
        parms = {}
        parms['cube'] = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        result = solve(parms)
        theCube = Cube(parms['cube'])
        self.assertEqual(theCube.rotate('lbbLBfuuFFURRuuBBULL'), 'yywobgybrrryrrryrooywyggwgbgyooobwobrgbbybgobrwgwwwowg')
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('lbbLBfuuFFURRuuBBULL', result.get('solution'))
    
    def test_rotate_930_checkInvalidCube(self):
        encodedCube = 'wbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywryg'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
        
    def test_rotate_940_checkInvalidCube(self):
        encodedCube = 'ooyrbwbbwgyoor/rbowbrg gwwrybwygoggorwwbrygbboyygywryg'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
     
    def test_rotate_930_checkNoneCube(self):
        parms = {}
        parms['cube'] = None
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test_rotate_930_checkShortCube(self):
        parms = {}
        parms['cube'] = 'T0x0TxJ40JxxJ0440004DD'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test_rotate_930_checkLongCube(self):
        parms = {}
        parms['cube'] = 'ssEtsHkXkXkHEEtXkXEXskXHHtHEEkskXXXHtHsststttsEtkHHkEEssEtsHkXkXkHEEtXkXEXskXHHtHEEk'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test_rotate_930_checkIllegalCharInCube(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbb         rrrrrrrrroooooooooyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
    
    def test_rotate_940_checkInvalidKey(self):
        encodedCube = 'ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        parms['key3'] = '123'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: extraneous key detected', result['status'])
        
    def test_rotate_950_checkUniqueMiddleElementsInCube(self):
        encodedCube = 'rbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('error: invalid cube', result['status'])
<<<<<<< HEAD
    
    def test_slove_bottomFaceCrosForNominalCube(self):
        encodedCube = 'OTaqTnOnqnOnOOORRqqaTRaqaRRqqRRqaOOnRnTnnTTqOTTaaRTaan'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        theCube = Cube(encodedCube)
        self.assertEqual(theCube.rotate('brBbLBFRfRFRfRBUFFURRuuBBULL'), 'OqqnTTaTTTTqROannnRnORaaqOaTqnOqqRqRRaTanOaTnqnORROORa')
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn(result, 'integrity')
        self.assertEqual('brBbLBFRfRFRfRBUFFURRuuBBULL', result.get('solution'))
        
    def test110_slove_bottomLayerForNominalCube(self):
        encodedCube = 'gbwrryrrobroggyyggyoyoogoogbrwobgrbbrbgyybryowwbwwwyww'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        theCube = Cube(encodedCube)
        self.assertEqual(theCube.rotate('UUbuBUbuBURUrruRruRUUBUbUUUfuFluLluLUUbuBuUUFUf'), 'oggyrrrrrobrbgogggggrgoboooyryobobbbbryyyybyywwwwwwwww')
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn(result, 'integrity')
        self.assertEqual('UUbuBUbuBURUrruRruRUUBUbUUUfuFluLluLUUbuBuUUFUf', result.get('solution'))
        
    def test120_slove_bottomLayerwithBottomCross(self):
        encodedCube = 'gbbgbbgbbrrorrorrobggbggbggroorooroowwywywwwyyywywyyyw'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        theCube = Cube(encodedCube)
        self.assertEqual(theCube.rotate('FFRRBBLLluLluLFUfUUbuBuLUlUbuBLUlLUlULUlfuFUULUl'), 'yoyobgbbbrboyrrrrryyyggbgggbbbrogooorrgoyyoygwwwwwwwww')
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn(result, 'integrity')
        self.assertEqual('UUbuBUbuBURUrruRruRUUBUbUUUfuFluLluLUUbuBuUUFUf', result.get('solution'))
        
=======
        
    def test_800_isBottomCrossSolved(self):
        encodedCube = 'ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg'
        parms = {}
        parms['cube'] = encodedCube
        result = solveBottomCross(encodedCube)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('UUBlBLLFFUUFFLLFFUUFFBBU', result.get('solution'))

    def test_810_isBottomCrossSolved(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solveBottomCross(encodedCube)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))
           
    def test_rotate_820_isBottomLayerSolved(self):
        encodedCube = 'yoyrgroyyorwwogogwrrgwbyrorwogbrgbwwobbgyyrbbbogbwyywg'
        parms = {}
        parms['cube'] = encodedCube
        result = solveBottomLayer(encodedCube)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('UUBlBLLFFUUFFLLFFUUFFBBU', result.get('solution'))

    def test_rotate_830_isBottomLayerSolved(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solveBottomLayer(encodedCube)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))

    def test_rotate_840_isMiddleLayerSolved(self):
        encodedCube = 'yoyrgroyyorwwogogwrrgwbyrorwogbrgbwwobbgyyrbbbogbwyywg'
        parms = {}
        parms['cube'] = encodedCube
        result = solveMiddleLayer(encodedCube)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('UUBlBLLFFUUFFLLFFUUFFBBU', result.get('solution'))
    
    def test_rotate_850_isMiddleLayerSolved(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solveMiddleLayer(encodedCube)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))
>>>>>>> refs/heads/increment4
