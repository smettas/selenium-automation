import pytest

a=10
b=20

@pytest.mark.xfail(reason="Known Issue")
def test_1():
    assert a==b, "Test is failed" #######Fail......Pass

@pytest.mark.num    
def test_2():
    assert a>b  ########Fail

@pytest.mark.num 
def test_3():
    assert a<b  #######Pass
    
@pytest.mark.num 
def test_4():
    assert a!=b ########Pass

@pytest.mark.num 
def test_5():
    assert (a+b)==(a-b) #####Fail

@pytest.mark.media
def test_fb_user():
    name="Krishna"
    assert name=="KRISHNA" #######Fail

@pytest.mark.media
def test_insta_user():
    name="Krishna"
    assert name.upper()=="KRISHNA" ###### Pass