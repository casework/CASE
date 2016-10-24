# Reconstructed File Example

This example shows how we can use the mechanisms described by [file.md](file.md) and
[multipart_file.md](multipart_file.md) to define how a file was reconstructed by
data carving software.

The `forensic_action0` object describe how the carving tool was run in order to create
the provenance records that describe the resulting objects created by the tool.

The `provenance_record2` object points the the reconstructed file itself (`reconstructed_file`) 
and the relationships that connect the data fragments to the created file.

The `provenance_record3` object points to the carved fragments `data_piece1` and `data_piece2`
along with the relationships `relationship3` and `relationship4` which describe where 
data pieces where extracted from within the `android_image`. 

The `provenance_record4` object points to the JPG file header (`data_piece0`) that was added
by the carving tool in order to reconstruct a working file.
