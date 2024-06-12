
# TODO: Add methods to be called from outside here

import os
from space_agent.gcp_storage_utility.gcpsu_main import upload_local_file_to_bucket
from space_agent.gcp_storage_utility.gcpsu_main import list_available_files_in_bucket
from space_agent.data_augmentation.dataaug_main import create_three_rotations_of_image
import shutil

def upload_images_to_gcp():
    images_location = os.environ['IMAGE_FOLDER']
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
    images_location = os.environ['IMAGE_FOLDER']
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

    images_location = os.environ['IMAGE_FOLDER']
    image_names = [f for f in os.listdir(images_location)]
    for index, image_name in enumerate(image_names):
        image_path = f'{images_location}/{image_name}'
        target_images_path = f'{images_location}/../images_cropped_from_augmentation'
        try:
            rc, message = create_three_rotations_of_image(
                source_image_path=image_path,
                target_images_path=target_images_path
            )
        except Exception as e:
            print(f'error with {image_name}')
            print(e)

        print(f'index: {index} - rc: {rc} - {message}')

def copy_images_sorted():
    images_location = os.environ['IMAGE_FOLDER']
    image_names = [f for f in os.listdir(images_location)]
    for index, image_name in enumerate(image_names):
        try:
            image_path = f'{images_location}/{image_name}'
            image_class = image_name.split('_')[3]
            target_images_path = f'{images_location}/../images_cropped_sorted/{image_class}/{image_name}'
            shutil.copyfile(image_path, target_images_path)
            print(f'index: {index} - image {image_name} copied to {image_class}')
        except Exception as e:
            print(f'error with {image_name}')
            print(e)

def get_directory_file_count(directory_path):
    return len([name for name in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, name))])

def determine_images_needed():
    images_location = os.environ['IMAGE_FOLDER']
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
    print(f'needed augmented stars count: {needed_stars}')
    print(f'needed augmented galaxies count: {needed_galaxies}')
    print(f'total stars count: {stars_count+needed_stars}')
    print(f'total stars count: {galaxy_count+needed_galaxies}')
    return stars_count, galaxy_count, needed_stars, needed_galaxies

def generate_balanced_dataset(galaxy_dir, star_dir, galaxy_aug_dir, star_aug_dir, balanced_dir):
    # Ensure the balanced directory exists
    if not os.path.exists(balanced_dir):
        os.makedirs(balanced_dir)
    # Get the list of files in each directory
    galaxy_files = os.listdir(galaxy_dir)
    star_files = os.listdir(star_dir)
    galaxy_aug_files = os.listdir(galaxy_aug_dir)
    star_aug_files = os.listdir(star_aug_dir)
    # Count the number of images in each directory
    galaxy_count = len(galaxy_files)
    star_count = len(star_files)
    galaxy_aug_count = len(galaxy_aug_files)
    star_aug_count = len(star_aug_files)
    # Copy all original images to the balanced directory
    for file in galaxy_files:
        shutil.copy(os.path.join(galaxy_dir, file), balanced_dir)
    for file in star_files:
        shutil.copy(os.path.join(star_dir, file), balanced_dir)
    if galaxy_aug_count > star_aug_count:
        # Copy all star augmented images to the balanced directory
        for file in star_aug_files:
            shutil.copy(os.path.join(star_aug_dir, file), balanced_dir)
        # Copy star_aug_count - (galaxy_count - star_count) galaxy augmented images to the balanced directory
        additional_files = random.sample(galaxy_aug_files, star_aug_count - (galaxy_count - star_count))
        for file in additional_files:
            shutil.copy(os.path.join(galaxy_aug_dir, file), balanced_dir)
    else:
        # Copy all galaxy augmented images to the balanced directory
        for file in galaxy_aug_files:
            shutil.copy(os.path.join(galaxy_aug_dir, file), balanced_dir)
        # Copy galaxy_aug_count - (star_count - galaxy_count) star augmented images to the balanced directory
        additional_files = random.sample(star_aug_files, galaxy_aug_count - (star_count - galaxy_count))
        for file in additional_files:
            shutil.copy(os.path.join(star_aug_dir, file), balanced_dir)

if __name__ == '__main__':
    # upload_images_to_gcp()
    # upload_missing_local_images_to_gcp()
    create_rotated_images()
    sort_images()
    determine_images_needed()
    # pass
