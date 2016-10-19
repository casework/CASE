# Multipart File Example

*Note: For brevity, all the provenance records and forensic actions are not shown.*

In this example we show how to represent a file that has been fragmented into multiple parts.
This types of files can be things like multipart zip files, reconstructed files, or fragmented
files from memory.

To represent this we take advantage of the same mechanisms used to represent files
that is explained in [file.md](file.md). By using the special keyword *has-fragment*
(**TODO: Determine if this is the best keyword to use.**) we can create **Relationship** objects
that point to each fragment or part of the overall file. This object will then have a
**Fragment** property bundle that describes the position (*fragmentIndex*) of this particular fragment
within the reconstructed file. The *totalFragments* property is used to help serializer
know how many total fragments to look for.

