from mod01_05 import checkLinearIndependence, checkIdentity, getIdentity, getHadamond
import numpy

def test_checkLinearIndependence():   
    assert numpy.allclose(checkLinearIndependence([[1,0,0],[1,1,0],[1,1,1]]), 3)
    assert numpy.allclose(checkLinearIndependence([[1,1,2],[1,1,2],[1,0,1]]), False)
    
def test_checkIdentity():
    assert numpy.allclose(checkIdentity([[1,0,0],[0,1,0],[0,0,1]]), 3)
    assert numpy.allclose(checkIdentity([[1,0,0],[0,1,0]]), False)

def test_getIdentity():
    assert numpy.allclose(getIdentity(3), [[1,0,0],[0,1,0],[0,0,1]])

def test_getHadamond():
    assert numpy.allclose(getHadamond(), [[ 0.70710678,  0.70710678], [ 0.70710678, -0.70710678]])
