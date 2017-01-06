# Bulk Extractor Forensic Path Example

This example shows how to represent a *forensic_path* created by the 
[Bulk Extractor](https://github.com/simsong/bulk_extractor) tool by
converting the forensic path seen on page 63 of
the [2013 COSE paper](https://github.com/simsong/bulk_extractor/blob/master/doc/2013.COSE.bulk_extractor.pdf):

```
946315592-GZIP-64000-GZIP-1600   nelson@crynwr.com
946315592-GZIP-64000-GZIP-16095  strk@keybit.com
```

This example takes advantage of the file mechanisms as described in
[file.md](file.md) in order to create **Relationship** and **Trace** objects 
to represent each offset and gzip decompression performed to
extract out the email addresses. 

- **disk_image**
    - *relationship6* (DataRange : 946315592) -> **compressed_gzip1**
        - *relationship5* (Compression : GZIP) -> **decompressed_gzip1**
            - *relationship4* (DataRange : 64000) -> **compressed_gzip0**
                - *relationship3* (Compression : GZIP)  -> **decompressed_gzip0**
                    - *relationship0* (DataRange : 1600) -> **extracted_email_address0**
                    - *relationship1* (DataRange : 16095) -> **extracted_email_address1**
