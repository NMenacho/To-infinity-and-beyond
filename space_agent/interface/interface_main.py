
# TODO: Add methods to be called from outside here

import os
from space_agent.gcp_storage_utility.gcpsu_main import upload_local_file_to_bucket
from space_agent.gcp_storage_utility.gcpsu_main import list_available_files_in_bucket
from space_agent.data_augmentation.dataaug_main import create_three_rotations_of_image
import shutil

def upload_images_to_gcp():
    images_location = os.environ['IMAGES_FOLDER']
    image_names = [f for f in os.listdir(images_location)]
    #client.list_blobs('bucketname', prefix='abc/myfolder
    for index, image_name in enumerate(image_names):
        image_path = f'{images_location}/{image_name}'
        bucket_name = 'to-infinity-and-beyond'
        path_in_bucket = os.path.join('images', 'cropped', 'sample')
        name_in_bucket = image_name
        rc, message = upload_local_file_to_bucket(
            image_path,
            bucket_name,
            path_in_bucket,
            name_in_bucket,
            if_not_exist_only=True
        )
        print(f'index: {index} - rc: {rc} - {message}')

def upload_missing_local_images_to_gcp():
    images_location = os.environ['IMAGES_FOLDER']
    image_names = [f for f in os.listdir(images_location)]
    bucket_name = 'to-infinity-and-beyond'
    path_in_bucket = os.path.join('images', 'cropped', 'sample')
    rc, message, blob_list = list_available_files_in_bucket(
        bucket_name,
        path_in_bucket
    )
    for index, image_name in enumerate(image_names):
        if image_name not in blob_list:
            image_path = f'{images_location}/{image_name}'
            name_in_bucket = image_name
            rc, message = upload_local_file_to_bucket(
                image_path,
                bucket_name,
                path_in_bucket,
                name_in_bucket,
                if_not_exist_only=True
            )
            print(f'index: {index} - rc: {rc} - {message}')
        else:
            print(f'image already in bucket')

def create_rotated_images():
    images_location = os.environ['IMAGES_FOLDER']
    image_names = [f for f in os.listdir(images_location)]
    for index, image_name in enumerate(image_names):
        image_path = f'{images_location}/{image_name}'
        target_images_path = f'{images_location}/../images_cropped_from_augmentation'
        rc, message = create_three_rotations_of_image(
            source_image_path=image_path,
            target_images_path=target_images_path
        )
        print(f'index: {index} - rc: {rc} - {message}')

def sort_images():
    images_location = os.environ['IMAGES_FOLDER']
    image_names = [f for f in os.listdir(images_location)]
    for index, image_name in enumerate(image_names):
        image_path = f'{images_location}/{image_name}'
        image_class = image_name.split('_')[3]
        target_images_path = f'{images_location}/../images_cropped_sorted/{image_class}/{image_name}'
        shutil.copyfile(image_path, target_images_path)
        print(f'index: {index} - image {image_name} copied')

def get_directory_file_count(directory_path):
    return len([name for name in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, name))])

def determine_images_needed():
    images_location = os.environ['IMAGES_FOLDER']
    sorted_images_location = os.path.join(images_location, '..', 'images_cropped_sorted')
    stars_count = get_directory_file_count(os.path.join(sorted_images_location, 'STAR'))
    galaxy_count = get_directory_file_count(os.path.join(sorted_images_location, 'GALAXY'))
    augmented_star_count = stars_count * 3
    augmented_galaxy_count = galaxy_count * 3
    needed_stars = 0
    needed_galaxies = 0
    dominant_class = 'galaxy'
    if stars_count > galaxy_count:
        dominant_class = 'star'
    if dominant_class == 'galaxy':
        needed_stars = augmented_star_count
        needed_galaxies = stars_count + needed_stars - galaxy_count
    else:
        needed_galaxies = augmented_galaxy_count
        needed_stars = galaxy_count + needed_galaxies - stars_count
    print(f'{dominant_class} class is dominant')
    print(f'stars count: {stars_count}')
    print(f'galaxy count: {galaxy_count}')
    print(f'needed stars count: {needed_stars}')
    print(f'needed galaxies count: {needed_galaxies}')

if __name__ == '__main__':
    # upload_images_to_gcp()
    # upload_missing_local_images_to_gcp()
    create_rotated_images()
    sort_images()
    determine_images_needed()
    # pass
