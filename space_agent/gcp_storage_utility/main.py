from google.cloud import storage
import os

def upload_local_file_to_bucket(
    local_file_path,
    bucket_name,
    path_in_bucket,
    name_in_bucket,
    if_not_exist_only=True,
):
    message=  'everything went fine'
    rc = 0
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(os.path.join(path_in_bucket, name_in_bucket))
        if if_not_exist_only == False:
            blob.upload_from_filename(local_file_path)
        elif not blob.exists():
            blob.upload_from_filename(local_file_path)
        else:
            message += ' (file exists)'
    except Exception as e:
        message = 'there was an error: '+ e
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

def test_upload():
    images_location = '/Users/svinchon/code/NMenacho/To-infinity-and-beyond/data/images_cropped_sample'
    object_ID = '1237645943973610080_44.211129087325_0.973934515533952_STAR_0.2834576'
    image_path = f'{images_location}/{object_ID}.jpg'
    bucket_name = 'to-infinity-and-beyond'
    path_in_bucket = os.path.join('images', 'cropped', 'sample')
    name_in_bucket = object_ID+'.jpg'
    rc, message = upload_local_file_to_bucket(
        image_path,
        bucket_name,
        path_in_bucket,
        name_in_bucket
    )
    print(rc)
    print(message)

def test_download():
    images_location = '/Users/svinchon/code/NMenacho/To-infinity-and-beyond/data/images_cropped_sample'
    object_ID = '1237645943973610080_44.211129087325_0.973934515533952_STAR_0.2834576'
    image_path = f'{images_location}/{object_ID}_downloaded.jpg'
    bucket_name = 'to-infinity-and-beyond'
    path_in_bucket = os.path.join('images', 'cropped', 'sample')
    name_in_bucket = object_ID+'.jpg'
    rc, message = download_file_from_bucket(
        image_path,
        bucket_name,
        path_in_bucket,
        name_in_bucket
    )
    print(rc)
    print(message)

if __name__ == '__main__':
    test_upload()
