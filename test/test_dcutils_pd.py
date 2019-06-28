from datacanvas.dcutils import mix_pd_s3

access_key = 'N0GF745VYE91E5EDKCQC'
secret_key = '6PN7fDMsdGSDhJJn8zm65uTzteubC6JAItsmjPbe'
s3_host = 'http://172.20.50.208:31642'

mix_pd_s3(s3_host, access_key, secret_key)

################################################################
import pandas as pd

local_file = 'foo.csv'
s3_bucket = 'test'
s3_object = "s3://%s/%s" % (s3_bucket, local_file)
s3_object_par = "s3://%s/%s.par" % (s3_bucket, local_file)

# load orignal data from file system
df = pd.read_csv(local_file)
print("=== original data: ===")
print(df)

# save df into s3
df.to_csv(s3_object, index=False, header=True)
df.to_parquet(s3_object_par, index=False)

df_csv = pd.read_csv(s3_object)
print("=== s3 csv data: ===")
print(df_csv)

df_par = pd.read_parquet(s3_object_par)
print("=== s3 parquet data: ===")
print(df_par)
