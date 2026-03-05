from PIL import Image, UnidentifiedImageError
from numpy import array


def ft_load(path: str):
    try:
        assert isinstance(path, str), "The path isn't a str"
        img = Image.open(path)
        arr = array(img)
        print("The shape of image is:", arr.shape)
        return (arr)
    except AssertionError as msg:
        print("Error:", msg)
        return (None)
    except FileNotFoundError:
        print("Error: File not found")
        return (None)
    except UnidentifiedImageError:
        print("Error: Image can't process")
        return (None)
