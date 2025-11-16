try:
    import librosa
    print("librosa: Success")
except Exception as e:
    print("librosa: ERROR ->", e)

try:
    import soundfile
    print("soundfile: Success")
except Exception as e:
    print("soundfile: ERROR ->", e)

try:
    import scipy
    print("scipy: Success")
except Exception as e:
    print("scipy: ERROR ->", e)

try:
    import cv2
    print("opencv (cv2): Success")
except Exception as e:
    print("opencv: ERROR ->", e)

try:
    from PIL import Image
    print("Pillow (PIL): Success")
except Exception as e:
    print("Pillow: ERROR ->", e)

try:
    import skimage
    print("scikit-image: Success")
except Exception as e:
    print("scikit-image: ERROR ->", e)

try:
    import matplotlib
    print("matplotlib: Success")
except Exception as e:
    print("matplotlib: ERROR ->", e)

try:
    import moviepy
    print("moviepy: Success")
except Exception as e:
    print("moviepy: ERROR ->", e)

try:
    import numpy
    print("numpy: Success")
except Exception as e:
    print("numpy: ERROR ->", e)

try:
    import pandas
    print("pandas: Success")
except Exception as e:
    print("pandas: ERROR ->", e)