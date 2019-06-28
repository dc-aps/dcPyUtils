📦 dcPyUtils
============

This is a python utils from DataCanvas APS.


Installation
-----

```bash
pip install dcPyUtils

```


Usages
-----

* add support to connect private s3 compatible host (eg: ceph rgw) from pandas

    Just set host url / access key / secret key by `dcutils.mix_pd_s3()`:
    ```python
    from dcutils import mix_pd_s3
    
    s3_host = 'http://xxx.xxx.xxx.xxx:12345'
    access_key = 'xxxxxxxxx'
    secret_key = 'xxxxxxxxxxxxxxxxxxxxxxx'
    
    mix_pd_s3(s3_host, access_key, secret_key)
    
    ```

    Then, read/write data from s3 host with url `"s3://<bucket>/<object_name>"`
    ```python
    import pandas as pd
    
    local_file = 'foo.csv'
    s3_bucket = 'test'
    s3_object = "s3://%s/%s" % (s3_bucket, local_file)
    
    # load orignal data from file system
    df = pd.read_csv(local_file)
    
    # save df into s3
    df.to_csv(s3_object, index=False, header=True)
    
    ```

