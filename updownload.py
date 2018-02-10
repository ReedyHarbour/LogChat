from azure.storage.blob import BlockBlobService
block_blob_service = BlockBlobService(account_name='logchat', account_key='rloT8pyJsIbFpMUsT+tpXJ/FX1MBR5jgYsAwjC1KuJakozGIclYKlVfXnzIOcMHagpr6XAX509VKT9xEbotkyg==')

from azure.storage.blob import ContentSettings


def upload(filename,filepath):
    block_blob_service.create_blob_from_path(
        'mycontainer',
        filename,
        filepath,
        content_settings=ContentSettings(content_type='image/png')
                )

def download(filename, downpath):
    block_blob_service.get_blob_to_path('mycontainer', filename, downpath)

