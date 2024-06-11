from PIL import Image
import numpy as np
from os.path import join as os_path_join
from os import environ as os_environ
from os.path import exists as os_exists

def create_three_rotations_of_image(
    source_image_path,
    target_images_path,
):
    message=  'RAS'
    rc = 0
    try:
        image_name = source_image_path.split('/')[-1].replace('.jpg', '')
        #image_path = '/'.join(source_image_path.split('/')[0:-1])
        image_class = image_name.split('_')[3]
        image_name90 = f'{image_name}_90.jpg'
        image_path90 = os_path_join(target_images_path, image_class, image_name90)
        if not os_exists(image_path90):
            # load image in np array
            image_data = np.array(Image.open(source_image_path))
            # create rotated images
            id90 = np.rot90(image_data)
            id180 = np.rot90(id90)
            id270 = np.rot90(id180)
            # save rotated image
            im90 = Image.fromarray(id90)
            im180 = Image.fromarray(id180)
            im270 = Image.fromarray(id270)
            im90.save(image_path90)
            image_name180 = f'{image_name}_180.jpg'
            image_path180 = os_path_join(target_images_path, image_class, image_name180)
            im180.save(image_path180)
            image_name270 = f'{image_name}_270.jpg'
            image_path270 = os_path_join(target_images_path, image_class, image_name270)
            im270.save(image_path270)
            message =  f'rotated copies of {image_name} saved to {image_class}'
    except Exception as e:
        message = 'there was an error: '+e
        rc = 1
    return rc, message

def test_create_three_rotations_of_image():
    image_dir = os_environ['IMAGE_FOLDER']
    source_image_path = f'{image_dir}/1237645943973610080_44.211129087325_0.973934515533952_STAR_0.2834576.jpg'
    target_images_path = f'{image_dir}/../images_cropped_from_augmentation'
    rc, message = create_three_rotations_of_image(source_image_path, target_images_path)
    print(message)

if __name__ == '__main__':
    test_create_three_rotations_of_image()
