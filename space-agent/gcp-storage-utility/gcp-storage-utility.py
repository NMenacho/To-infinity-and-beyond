from google.cloud import storage
import os

def upload_local_file_to_bucket(
    local_file_path,
    bucket_name,
    path_in_bucket,
    name_in_bucket
):
    message=  'everything went fine'
    rc = 0
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(os.path.join(path_in_bucket, name_in_bucket))
        blob.upload_from_filename(local_file_path)
    except Exception as e:
        message = 'there was an error: '+e
        rc = 1
    return rc, message

def download_file_from_bucket(
    local_file_path,
    bucket_name,
    path_in_bucket,
    name_in_bucket
):
    message=  'everything went fine'
    rc = 0
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.get_blob(os.path.join(path_in_bucket, name_in_bucket))
        blob.download_to_filename(local_file_path)
    except Exception as e:
        message = 'there was an error: '+e
        rc = 1
    return rc, message

def test01():
    images_location = '/Users/svinchon/code/NMenacho/To-infinity-and-beyond-data/data/images_cropped'
    object_ID = '1237646797600326400'
    image_path = f'{images_location}/{object_ID}.jpeg'
    bucket_name = 'to-infinity-and-beyond'
    path_in_bucket = os.path.join('images', 'cropped')
    name_in_bucket = object_ID+'.jpeg'
    rc, message = upload_local_file_to_bucket(
        image_path,
        bucket_name,
        path_in_bucket,
        name_in_bucket
    )
    print(rc)
    print(message)

def test02():
    images_location = '/Users/svinchon/code/NMenacho/To-infinity-and-beyond-data/data/images_cropped'
    object_ID = '1237646797600326400'
    image_path = f'{images_location}/{object_ID}_downloaded.jpeg'
    bucket_name = 'to-infinity-and-beyond'
    path_in_bucket = os.path.join('images', 'cropped')
    name_in_bucket = object_ID+'.jpeg'
    rc, message = download_file_from_bucket(
        image_path,
        bucket_name,
        path_in_bucket,
        name_in_bucket
    )
    print(rc)
    print(message)

if __name__ == '__main__':
    images_location = '../../To-infinity-and-beyond-data/data/images_cropped'
    object_ID = '1237646797600326400'
    image_path = f'{images_location}/{object_ID}.jpeg'
    test02()
