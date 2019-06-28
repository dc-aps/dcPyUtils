from dcutils import get_s3_fs as s3fs

access_key = 'N0GF745VYE91E5EDKCQC'
secret_key = '6PN7fDMsdGSDhJJn8zm65uTzteubC6JAItsmjPbe'
s3_host = 'http://172.20.50.208:31642'

fs = s3fs(s3_host, access_key, secret_key)
print(fs.du("s3://test"))
