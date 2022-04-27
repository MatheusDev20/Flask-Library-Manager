from datetime import datetime

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class UseFullFunctions:


    @classmethod
    def allowed_file_extensions(self, extension):
        return True if extension in ALLOWED_EXTENSIONS else False

    @classmethod
    def generate_s3_path(self, filename: str, resource: str):
        return f'{datetime.now().year}/{datetime.now().month}/{resource}/{filename}'

    @classmethod
    def sql_alchemy_to_dict(self, row):
        return {column: str(getattr(row, column)) for column in row.__table__.c.keys()}
