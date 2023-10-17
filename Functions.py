# DOCSTRINGS
def calculate_pyramid_volume(height: 'int | float', length:'int | float', width: 'int | float')-> 'int | float':
    """ Calculates the volumes of a pyramid.
    
    Args:
        length ( int | float ): The length of the pyramid base
        height ( int | float ): The pyramid height
        width ( int | float ): The width of the pyramid base
        
    Returns:
        A float containing the pyramid volume
    """
    product = (height * length * width)
    volume = product/3
    return volume

my_list = [2,3,4]
my_tuple = (2,3,4)
my_dict = {1:2, 2:3, 3:4}

# to unpack list, tuple or dictionary will put * before the list name
#result = calculate_pyramid_volume(*my_dict.values())
result = calculate_pyramid_volume(*my_list)
print(result)