from pytest_total import total, join

def test_total_empty() -> None:
    '''Test for total'''
    assert total([]) == 0.0
    
    
def test_total_single() -> None:
    '''Test for total'''
    assert total([10.0]) == 10.0
    
def test_total_multiple() -> None:
    '''Test for total'''
    assert total([1,2,3,10]) == 16
    
def test_join_use_case() -> None:
    '''Test for use case'''
    assert join([1,2,3], ', ') == '1, 2, 3'
    
def test_join_single_use_case() -> None:
    '''Test for single use case'''
    assert join([1], ', ') == '1'
    
def test_join_empty_delimiter_use_case() -> None:
    '''Test for use case'''
    assert join([1,2,3], '') == '123'
    
    
    


