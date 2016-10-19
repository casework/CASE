# File Example

*Note: For brevity, all the provenence records and forensic actions are not shown.*

This example shows how we can represent a file or piece of data can be
represented within the CASE ontology. By using a combination of Traces and
Relationship objects we can show the entire extraction of a file no matter the
complexities of how it was stored.

In this example we care going to show a pieced data that was extracted in the
following way:

1. A forensic image `android_image` is taken of an android device `android_device1` and 
has been stored on an examiner's computer `forensic_lab_computer1`.
1. A disk parition `image_partition` is carved from the image.
1. A SQLite database `sqlite_database` is extracted from the disk partition.
1. An encrypted SQLite blob `sqlite_blob` is extracted from teh AttachmentTable of the SQLite database.
1. The SQLite blob is AES decrypted resulting in a TAR archive `decrypted_blob`.
1. A base64 encoded file `tar_archive_file` is extracted from the TAR archive.
1. The TAR sub file is base64 decoded resulting in a JPG file `decoded_attachment`.
1. A particular range of data `chunk_of_data` is extracted from the decoded JPG file.


## Trace objects

Between each step, we represent the data as it currently is with a **Trace** object. 
This Trace object contains property bundles that describe the data itself.

The most used property bundle will be **ContentData**. This property bundle will
contain raw information about the data like byte order, hashes, size, as well
as optionally include the data itself.

Another common property bundle used will be **File**. This property bundle will
contain file format information such as magic number, mime type, and whether or not
its a directory.

## Relationship objects

Each extraction step performed is represented by a **Relationship** object using one of the 
special keywords (*contained-within* or *stored-on*). This object will contain property bundles
that describe how the Trace pointed to by the `source` property was extracted from the
Trace pointed to by the `target` property.

For the extraction of a file within a [file system](../glossary.md#File-System) (EXT4, NTFS, TAR, etc)
we use the property bundle **FileSystem**. This proeprty bundle will contain file path
information needed to extract the file out of the file system.

For encryption steps, we use the **Encryption** property bundle which provide the 
encryption algorithm and parameters needed to decrypt the `target` file. 

For encoding steps, we use the **Encoding** property bundle which provide the 
encoding algorithm used to decode the `target` file.
 
For the extraction of an embedded section of raw bytes within the `target` file, we
use the **DataRange** property bundle which provide the offset and size within the `target` file.


