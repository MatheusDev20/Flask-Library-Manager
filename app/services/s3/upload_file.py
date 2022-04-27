from .s3_config import S3
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from app.utils import UseFullFunctions

class UploadFile(S3):
    def __init__(self):
        S3.__init__(self)

    def sendToS3(self, file, resource):
        filename = secure_filename(file.filename.split(' ')[0])
        extension = filename.split('.')[-1]
        # Local upload to uploads folder.

        if UseFullFunctions().allowed_file_extensions(extension): 
            file_path = secure_filename(f'uploads/{filename}')
            file.save(file_path)

            with open(file_path, 'rb') as f:
                content = f.read()
                s3_path = UseFullFunctions().generate_s3_path(filename, resource)    
                file_s3_link = self.upload(s3_path, content)

            return file_s3_link
        
        else:
            raise Exception(f'Extension {extension} not allowed')