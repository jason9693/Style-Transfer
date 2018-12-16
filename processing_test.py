#from style_tansfer.image_utils import load_image, preprocess_image, deprocess_image , save_image,save_to_black_white

from style_transfer.image_utils import *

content_img_test = preprocess_image(load_image('styles/tubingen.jpg', size=192))[None]
style_img_test = preprocess_image(load_image('styles/starry_night.jpg', size=192))[None]

print(content_img_test.min(), content_img_test.max())