import os
from space_agent.gcp_storage_utility.main import upload_local_file_to_bucket

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

def preprocess():
    pass

if __name__ == '__main__':
    upload_images_to_gcp()
