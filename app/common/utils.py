import os
import uuid

import boto3
from botocore.exceptions import ClientError

from config import settings


def is_image_extension(file_name):
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    _, ext = os.path.splitext(file_name)
    return ext.lower() in valid_extensions


class S3ImgUploader:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3", aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        self.bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    def upload(self, image_file, prefix: str):
        try:
            # 이미지 파일인지 확장자를 검사함
            if not is_image_extension(image_file.name):
                raise ValueError("Not a valid image file")

            file_name = prefix + uuid.uuid4().hex
            extra_args = {"ContentType": image_file.content_type}

            self.s3_client.upload_fileobj(
                image_file,  # 업로드할 이미지 파일
                self.bucket_name,  # 업로드 되는 버킷의 이름
                file_name,  # 업로드 될 이미지의 이름변경
                ExtraArgs=extra_args,  # 파일 확장자
            )
            return f"https://{self.bucket_name}.s3.ap-northeast-2.amazonaws.com/{file_name}"
        except ValueError as ve:
            raise ve
        except ClientError as ce:
            raise Exception(f"Failed to upload image to S3: {ce}")
        except Exception as e:
            raise Exception(f"Failed to upload image: {e}")

    def delete_img_file(self, image_url):
        try:
            file_name = image_url.split("/")[-1]  # url에서 이미지 파일이름 추출

            response = self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_name)
            if response["ResponseMetadata"]["HTTPStatusCode"] in [200, 204]:
                # 정상적인 삭제가 처리되면 응답코드와 성공메시지를 반환.
                return {"msg": "Successfully deleted at S3", "status": response["ResponseMetadata"]["HTTPStatusCode"]}
            # 정상적인 처리가 안됐을 때 응답 코드와 실패메시지 반환
            return {"msg": "Failed to delete image file", "status": response["ResponseMetadata"]["HTTPStatusCode"]}
        except Exception as e:
            raise Exception(f"Failed to delete image: {e}")
