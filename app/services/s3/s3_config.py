import boto3
from flask import current_app as app
class S3:
    def __init__(self):
        self.__connect()
        self.bucket_name = 'library-manager-app'
        self.bucket_region = 'us-east-1'

    def __connect(self):
        self.s3_client = boto3.resource(
            's3',
            aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY']
        )

    def generateS3FileLink(self, path_file):
        return f'https://{self.bucket_name}.s3.{self.bucket_region}.amazonaws.com/{path_file}'

    def upload(self, s3_file, content):
        try:
            ret = self.s3_client.Object(
                self.bucket_name,
                s3_file).put(
                    Body=content,
                    ACL='public-read'
                )
            
            link = self.generateS3FileLink(s3_file)
            return link

        except Exception as e:
            print(e)
            print('An error ocurred Uploading the file to S3 Bucket')