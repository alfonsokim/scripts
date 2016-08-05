import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('spark.input')

print dir(bucket)

"""
response = bucket.create(
    ACL='authenticated-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    }
)
print response
"""

for s3_file in bucket.objects.all():
    print s3_file
    print s3_file.key
    print dir(s3_file)
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': 'spark.input',
            'Key': 'key-name'
        }
    )