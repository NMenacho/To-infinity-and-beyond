import os
from space_agent.gcp_storage_utility.gcpsu_main import upload_local_file_to_bucket
from space_agent.gcp_storage_utility.gcpsu_main import list_available_files_in_bucket
from space_agent.data_augmentation.dataaug_main import create_three_rotations_of_image

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

# def preprocess():
#     pass

if __name__ == '__main__':
    # upload_images_to_gcp()
    upload_missing_local_images_to_gcp()
    # create_rotated_images()
