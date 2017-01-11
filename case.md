
- [Enumeration](#enumeration)
- [Supporting Classes](#supporting-classes)
- [Object](#object)
- [Property Bundle](#property-bundle)

# Enumeration





### AccountType




### ActionStatus




### AuthorizationType




### ByteOrder


**SubTypes:**  BigEndian, LittleEndian



### CompressionMethod


**SubTypes:**  BZIP2, Deflate, GZIP, LZMA, XZ, ZLIB



### DataType




### DeviceType




### DiskPartitionType




### DiskType




### EncodingMethod


**SubTypes:**  Base16, Base32, Base64



### EncryptionMethod


**SubTypes:**  AES, Blowfish, DES, DES3, RC4



### EncryptionMode


**SubTypes:**  CBC, CFB, ECB, OFB



### ErrorType


**SubTypes:**  Critical, Debug, Error, Info, Warning



### FileMismatchType




### FileSystemType


**SubTypes:**  BDEVolume, CPIO, EWF, EXT4, F2FS, NTFS, SevenZ, TAR, VSSVolume, ZIP



### GlobalFlagType




### HashMethod


**SubTypes:**  MD5, SHA, SHA-1, SHA-2



### ImageCompressionMethod


**SubTypes:**  BMP, Huffman, JPEG, LZW, PNG, TIFF, WebP



### Language
TODO: We probably can use an already existing schema for this.

**SubTypes:**  English, French, Spanish



### MimePartType




### MimeType




### PEType




### PasswordType




### ServiceStatus




### Servicetype




### StartType




### VisibilityType


**SubTypes:**  Private, Public



# Supporting Classes





### DictionaryItem


Attribute | Range | Comment
---: | --- | ---
*key* | xsd:string | 
*value* | xsd:string | 


### DomainName


Attribute | Range | Comment
---: | --- | ---
*isTLD* | xsd:boolean | 
*value* | xsd:string | 


### EmailAddress
TODO: Merge this into EmailAccount?

Attribute | Range | Comment
---: | --- | ---
*stringValue* | xsd:string | 


### FilePath
TODO: Determine if this object is wanted, or if we want to stick with strings.

Attribute | Range | Comment
---: | --- | ---
*delimiter* | xsd:string | 
*filePathSegments* | olo:OrderedList | 


### IPv4Address


Attribute | Range | Comment
---: | --- | ---
*value* | xsd:string | 


### IPv6Address


Attribute | Range | Comment
---: | --- | ---
*value* | xsd:string | 


### MACAddress


Attribute | Range | Comment
---: | --- | ---
*value* | xsd:string | 


### ReceivedEvent
Defines received events.
Contains information on who received it and when.

Attribute | Range | Comment
---: | --- | ---
*receivedTime* | xsd:dateTimeStamp | 
*receiver* | [Trace](#trace) | 


### URI


Attribute | Range | Comment
---: | --- | ---
*value* | xsd:string | 


### WindowsPEFileHeader
Properties of the PE file header, sometimes referred to as the COFF header.

Attribute | Range | Comment
---: | --- | ---
*characteristics* | xsd:hexBinary | 
*hash* | [Hash](#hash) | 
*machine* | xsd:hexBinary | 
*numberOfSections* | xsd:hexBinary | 
*numberOfSymbols* | xsd:hexBinary | 
*optionalHeader* | [WindowsPEOptionalHeader](#windowspeoptionalheader) | 
*pointerToSymbolTable* | xsd:hexBinary | 
*sizeOfOptionalHeader* | xsd:hexBinary | 
*timeDateStamp* | xsd:hexBinary | 


### WindowsPEOptionalHeader


Attribute | Range | Comment
---: | --- | ---
*addressOfEntryPoint* | xsd:hexBinary | 
*baseOfCode* | xsd:hexBinary | 
*checksum* | xsd:hexBinary | 
*dllCharacteristics* | xsd:hexBinary | 
*entropy* | xsd:float | 
*fileAlignment* | xsd:hexBinary | 
*hash* | [Hash](#hash) | 
*imageBase* | xsd:hexBinary | 
*loaderFlags* | xsd:hexBinary | 
*magic* | xsd:hexBinary | TODO: Is this different from the magicNumber propery used by ContentData?
*majorImageVersion* | xsd:hexBinary | 
*majorOSVersion* | xsd:hexBinary | 
*majorSubsystemVersion* | xsd:hexBinary | 
*majorlinkerVersion* | xsd:hexBinary | 
*minorImageVersion* | xsd:hexBinary | 
*minorLinkerVersion* | xsd:hexBinary | 
*minorOSVersion* | xsd:hexBinary | 
*minorSubsystemVersion* | xsd:hexBinary | 
*numberOfRVAAndSizes* | xsd:hexBinary | 
*sectionAlignment* | xsd:hexBinary | 
*sizeOfCode* | xsd:hexBinary | 
*sizeOfHeaders* | xsd:hexBinary | 
*sizeOfHeapCommit* | xsd:hexBinary | 
*sizeOfHeapReserve* | xsd:hexBinary | 
*sizeOfImage* | xsd:hexBinary | 
*sizeOfInitializedData* | xsd:hexBinary | 
*sizeOfStackCommit* | xsd:hexBinary | 
*sizeOfStackReserve* | xsd:hexBinary | 
*sizeOfUnintialializedData* | xsd:hexBinary | 
*subsystem* | xsd:hexBinary | 
*win32VersionValue* | xsd:hexBinary | 


### WindowsPESection


Attribute | Range | Comment
---: | --- | ---
*hash* | [Hash](#hash) | 
*name* | xsd:string | The name property defines a common word or phrase that describes the meaning of the object.
*sizeInBytes* | xsd:positiveInteger | Size of file in bytes.


### WindowsRegistryValue


Attribute | Range | Comment
---: | --- | ---
*dataType* | [DataType](#datatype) | 
*name* | xsd:string | The name property defines a common word or phrase that describes the meaning of the object.
*value* | xsd:string | 


### X509V3Extensions


Attribute | Range | Comment
---: | --- | ---
*authorityKeyIdentifier* | xsd:string | 
*basicContraints* | xsd:string | 
*certificatePolicies* | xsd:string | 
*crlDistributionPoints* | xsd:string | 
*extendedKeyUsage* | xsd:string | 
*inhibitAnyPolicy* | xsd:string | 
*issuerAlternativeName* | xsd:string | 
*keyUsage* | xsd:string | 
*nameContraints* | xsd:string | 
*policyConstraints* | xsd:string | 
*policyMappings* | xsd:string | 
*privateKeyUsagePeriodNotAfter* | xsd:dateTimeStamp | 
*privateKeyUsagePeriodNotBefore* | xsd:dateTimeStamp | 
*subjectAlternativeName* | xsd:string | 
*subjectDirectoryAttribute* | xsd:string | 
*subjectKeyIdentifier* | xsd:string | 


# Object





### Descriptive





# Property Bundle

A grouping of properties characterizing a particular aspect/facet of an object.



### AFFImage




### Account
The fundamental properties of an account.

Attribute | Range | Comment
---: | --- | ---
*accountIdentifier* | xsd:string | 
*accountIssuer* | xsd:string | 
*accountType* | [AccountType](#accounttype) | 
*createdTime* | xsd:dateTimeStamp | 
*expirationTime* | xsd:dateTimeStamp | 
*isActive* | xsd:boolean | 
*owner* | [UcoObject](#ucoobject) | A collection of appointments and meetings.


### AccountAuthentication
The authentication information related to an account.

Attribute | Range | Comment
---: | --- | ---
*password* | xsd:string | 
*passwordLastChanged* | xsd:dateTimeStamp | 
*passwordType* | [PasswordType](#passwordtype) | 


### ActionReferences
A grouping of properties characterizing the core elements (who, how, with what, where, etc.) for an action. The properties consist of identifier references to separate UCO objects detailing the particular property.

Attribute | Range | Comment
---: | --- | ---
*instrument* | [UcoObject](#ucoobject) | The instrument the acutator used to perform the action. (This is usually an item that contains a tool property bundle.)
*location* | [Location](#location) | 
*object* | [UcoObject](#ucoobject) | 
*participant* |  | Describes people who are involved in the Message. Participants are not necessarily the sender or recipients of the message.

This property is useful if the people involved with the Message are known, but the sender of the Message cannot be determined.
*performer* | [UcoObject](#ucoobject) | Defines the person, action, or thing that caused this action.
*result* | [UcoObject](#ucoobject) | 


### AndroidPackage




### Application
Characteristics of a software application.

Attribute | Range | Comment
---: | --- | ---
*applicationIdentifier* | xsd:string | 
*numberOfLaunches* | xsd:positiveInteger | 
*operatingSystem* | (Restriction on property [propertyBundle](#propertybundle) with [owl:someValuesFrom [OperatingSystem](#operatingsystem)]), [Trace](#trace) | 
*version* | xsd:string | 


### ApplicationAccount
Characteristics of an account within a particular application.

Attribute | Range | Comment
---: | --- | ---
*application* | [Trace](#trace) | Defines the application-like item used by this account.


### ArchiveFile
Properties specific to archive files.

Attribute | Range | Comment
---: | --- | ---
*comment* | xsd:string | 
*version* | xsd:string | 


### Attachment
Defines an object that is an attachment of a message.

Note: This property bundle is different. Instead of putting this as a property bundle of the attachment itself, you put this on the message.

Attribute | Range | Comment
---: | --- | ---
*object* | [UcoObject](#ucoobject) | 
*uri* | [URI](#uri) | 


### Audio


Attribute | Range | Comment
---: | --- | ---
*audioType* | xsd:string | 
*bitRate* | xsd:long | 
*duration* | xsd:duration | 
*format* | xsd:string | 


### Authorization


Attribute | Range | Comment
---: | --- | ---
*authorizationIdentifier* | xsd:string | 
*authorizationType* | [AuthorizationType](#authorizationtype) | 


### AutonomousSystem
Basic characteristics of an Internet autonomous system.

Attribute | Range | Comment
---: | --- | ---
*asHandle* | xsd:string | 
*number* | xsd:int | 
*regionalInternetRegistry* |  | 


### BDEVolume
The Bitlocker Drive Encryption (BDE) credentials.

Attribute | Range | Comment
---: | --- | ---
*password* | xsd:string | 
*recoveryPassword* | xsd:string | 
*startupKey* | xsd:base64Binary | 


### BirthInformation


Attribute | Range | Comment
---: | --- | ---
*birthDate* | xsd:dateTimeStamp | 


### BrowserBookmark
A bookmark to a web pages or files using a web browser.

Attribute | Range | Comment
---: | --- | ---
*accessedTime* | xsd:dateTimeStamp | 
*application* | [Trace](#trace) | Defines the application-like item used by this account.
*bookmarkPath* | xsd:string | 
*createdTime* | xsd:dateTimeStamp | 
*modifedTime* | xsd:dateTimeStamp | 
*urlTargeted* | [URI](#uri) | 
*visitCount* | xsd:int | 


### BrowserCookie
A piece of data used by a (remote) web page, stored on the local machine.

Attribute | Range | Comment
---: | --- | ---
*accessedTime* | xsd:dateTimeStamp | 
*application* | [Trace](#trace) | Defines the application-like item used by this account.
*cookieName* | xsd:string | 
*cookiePath* | xsd:string | 
*createdTime* | xsd:dateTimeStamp | 
*domain* | xsd:string | 
*expirationTime* | xsd:dateTimeStamp | 
*isSecure* | xsd:boolean | 


### BrowserHistory




### ByteRun




### Calendar


Attribute | Range | Comment
---: | --- | ---
*application* | [Trace](#trace) | Defines the application-like item used by this account.
*owner* | [UcoObject](#ucoobject) | A collection of appointments and meetings.


### CalendarEntry
Characteristics of an entry (appointment, meeting, event) within a calendar.

Attribute | Range | Comment
---: | --- | ---
*application* | [Trace](#trace) | Defines the application-like item used by this account.
*attendant* | [UcoObject](#ucoobject) | 
*category* | xsd:string | 
*createdTime* | xsd:dateTimeStamp | 
*duration* | xsd:duration | 
*endTime* | xsd:dateTimeStamp | 
*eventStatus* | xsd:string | 
*eventType* | xsd:string | 
*isPrivate* | xsd:boolean | 
*label* | xsd:string | 
*location* | [Location](#location) | 
*modifedTime* | xsd:dateTimeStamp | 
*owner* | [UcoObject](#ucoobject) | A collection of appointments and meetings.
*recurrence* | xsd:string | 
*remindTime* | xsd:dateTimeStamp | 
*startTime* | xsd:dateTimeStamp | 
*subject* | xsd:string | 


### Compression
Characteristics of compression applied to a body of data content.

Attribute | Range | Comment
---: | --- | ---
*compressionMethod* | [CompressionMethod](#compressionmethod) | 
*compressionRatio* | xsd:double | 


### ComputerSpecification
Characterizes a computer system (as a combination of both software and hardware).

Attribute | Range | Comment
---: | --- | ---
*biosVersion* | xsd:string | 
*cpuFamily* | xsd:string | 
*totalRam* | xsd:string | 


### Contact
Contact found in an application, for example an entry in an address book.

Attribute | Range | Comment
---: | --- | ---
*application* | [Trace](#trace) | Defines the application-like item used by this account.
*contactIdentifier* | xsd:string | 
*contactName* | xsd:string | 
*contactType* | xsd:string | 
*emailAddress* | xsd:string | 
*firstName* | xsd:string | 
*lastName* | xsd:string | 
*middleName* | xsd:string | 
*phoneNumber* | xsd:string | 
*screenName* | xsd:string | 


### ContentData
Characteristics of a block of digital data.

Attribute | Range | Comment
---: | --- | ---
*byteOrder* | [ByteOrder](#byteorder) | 
*dataPayload* | xsd:base64Binary | 
*dataPayloadReferenceURL* | xsd:string | 
*entropy* | xsd:float | 
*hash* | [Hash](#hash) | 
*isEncrypted* | xsd:boolean | 
*magicNumber* | xsd:base64Binary | 
*mimeClass* | xsd:string | TODO: Define proper range.
*mimeType* | [MimeType](#mimetype) | 
*sizeInBytes* | xsd:positiveInteger | Size of file in bytes.


### DataRange
Bounding characteristics of a range within a block of digital data.

Attribute | Range | Comment
---: | --- | ---
*rangeOffset* | xsd:positiveInteger | 
*rangeOffsetType* | xsd:string | 
*rangeSize* | xsd:positiveInteger | 


### Device


Attribute | Range | Comment
---: | --- | ---
*deviceType* | [DeviceType](#devicetype) | 
*manufacturer* | xsd:string | 
*model* | xsd:string | 
*serialNumber* | xsd:string | 


### DigitalAccount


Attribute | Range | Comment
---: | --- | ---
*accountLogin* | xsd:string | 
*displayName* | xsd:string | 
*firstLoginTime* | xsd:dateTimeStamp | 
*isDisabled* | xsd:boolean | 
*lastLoginTime* | xsd:dateTimeStamp | 


### Disk
DC3 needed

Attribute | Range | Comment
---: | --- | ---
*diskSize* | xsd:long | 
*diskType* | [DiskType](#disktype) | 
*freeSpace* | xsd:long | 
*hasPartition* | [Trace](#trace) | 


### DiskPartition
Characteristics of a region on a hard disk or other secondary storage.

Attribute | Range | Comment
---: | --- | ---
*createdTime* | xsd:dateTimeStamp | 
*diskPartitionType* | [DiskPartitionType](#diskpartitiontype) | 
*mountPoint* | xsd:string | 
*partitionIdentifier* | xsd:int | 
*partitionLength* | xsd:int | 
*partitionOffset* | xsd:long | 
*spaceLeft* | xsd:long | 
*spaceUsed* | xsd:long | 
*totalSpace* | xsd:long | 


### EWFImage


Attribute | Range | Comment
---: | --- | ---
*acquiryDate* | xsd:dateTimeStamp | 
*caseNumber* | xsd:integer | 
*compressionMethod* | [CompressionMethod](#compressionmethod) | 
*description* | xsd:string | 
*errorGranularity* | xsd:integer | 
*evidenceNumber* | xsd:string | 
*examinerName* | xsd:string | 
*format* | xsd:string | 
*guid* | xsd:string | 
*notes* | xsd:string | 
*operatingSystemUsed* | xsd:string | 
*password* | xsd:string | 
*sectorsPerChunk* | xsd:integer | 
*softwareVersionUsed* | xsd:string | 
*systemDate* | xsd:dateTimeStamp | 


### EXIF
TODO: Use imported exif ontology

Attribute | Range | Comment
---: | --- | ---
*exifData* | [DictionaryItem](#dictionaryitem) | 


### EmailAccount
Characteristics of an account within an email domain.

Attribute | Range | Comment
---: | --- | ---
*emailAddress* | xsd:string | 


### EmailMessage
The properties unique to an email message corresponding to the internet message format described in RFC 5322 and related RFCs.

Attribute | Range | Comment
---: | --- | ---
*bcc* | [Trace](#trace) | 
*bodyMultipart* | [MimePartType](#mimeparttype) | 
*bodyRaw* | [Trace](#trace) | 
*category* | xsd:string | 
*cc* | [Trace](#trace) | 
*contentDisposition* | xsd:string | 
*contentType* | xsd:string | 
*headerRaw* | [Trace](#trace) | 
*inReplyTo* | [Trace](#trace) | 
*isMimeEncoded* | xsd:boolean | 
*isMultipart* | xsd:boolean | 
*label* | xsd:string | 
*messageID* | [Trace](#trace) | 
*otherHeader* | [DictionaryItem](#dictionaryitem) | 
*priority* | xsd:string | 
*receivedLine* | xsd:string | 
*reference* | [Trace](#trace) | 
*xMailer* | xsd:string | 
*xOriginatingIP* | [Trace](#trace) | 


### Encoding
Represents the encoding-related properties of some encoded thing.

Attribute | Range | Comment
---: | --- | ---
*encodingMethod* | [EncodingMethod](#encodingmethod) | 


### Encryption
Represents the encryption-related properties of some encrypted data.

Attribute | Range | Comment
---: | --- | ---
*encryptionIV* | xsd:hexBinary | 
*encryptionKey* | xsd:hexBinary | 
*encryptionMethod* | [EncryptionMethod](#encryptionmethod) | 
*encryptionMode* | [EncryptionMode](#encryptionmode) | 


### Error




### Event




### ExtInode
Characterizes the details of a single EXT file.

Attribute | Range | Comment
---: | --- | ---
*extDeletionTime* | xsd:dateTimeStamp | 
*extFileType* | xsd:int | 
*extFlags* | xsd:int | 
*extHardLinkCount* | xsd:int | 
*extInodeChangeTime* | xsd:dateTimeStamp | 
*extInodeID* | xsd:int | 
*extPermissions* | xsd:int | 
*extSGID* | xsd:int | 
*extSUID* | xsd:int | 


### ExtractedFeatures


Attribute | Range | Comment
---: | --- | ---
*extractedCodeSnippet* | (Restriction on property [propertyBundle](#propertybundle) with [owl:someValuesFrom [ExtractedString](#extractedstring)]), [Trace](#trace) | 
*extractedImport* | (Restriction on property [propertyBundle](#propertybundle) with [owl:someValuesFrom [ExtractedString](#extractedstring)]), [Trace](#trace) | 
*extractedString* | (Restriction on property [propertyBundle](#propertybundle) with [owl:someValuesFrom [ExtractedString](#extractedstring)]), [Trace](#trace) | 


### ExtractedString
A string extracted from a cyber item.

Attribute | Range | Comment
---: | --- | ---
*byteStringValue* | xsd:base64Binary | 
*encodingMethod* | [EncodingMethod](#encodingmethod) | 
*englishTranslation* | xsd:string | 
*hash* | [Hash](#hash) | 
*language* | [Language](#language) | 
*length* | xsd:integer | 
*stringValue* | xsd:string | 


### File
The basic properties associated with the storage of a file on a file system.

Attribute | Range | Comment
---: | --- | ---
*accessedTime* | xsd:dateTimeStamp | 
*createdTime* | xsd:dateTimeStamp | 
*extension* | xsd:string | The file extension.
*fileName* | xsd:string | 
*filePath* | xsd:string | 
*isDirectory* | xsd:boolean | 
*metadataChangedTime* | xsd:dateTimeStamp | 
*modifedTime* | xsd:dateTimeStamp | 
*sizeInBytes* | xsd:positiveInteger | Size of file in bytes.


### FileMetadataMismatch


Attribute | Range | Comment
---: | --- | ---
*mismatchType* | [FileMismatchType](#filemismatchtype) | 


### FilePermissions
Characteristics of permissions or access rights for a file.

Attribute | Range | Comment
---: | --- | ---
*owner* | [UcoObject](#ucoobject) | A collection of appointments and meetings.


### FileSystem
Represents the properties of a file system.

Attribute | Range | Comment
---: | --- | ---
*clusterSize* | xsd:long | 
*fileSystemType* | [FileSystemType](#filesystemtype) | 


### Fragment
Characteristics of an individual fragment of a file.

Attribute | Range | Comment
---: | --- | ---
*fragmentIndex* | xsd:int | 
*totalFragments* | xsd:int | 


### GeoLocationEntry
Characteristics of a single application-specific geolocation entry.

Attribute | Range | Comment
---: | --- | ---
*createdTime* | xsd:dateTimeStamp | 
*location* | [Location](#location) | 


### GeoLocationLog
A log containing geolocation tracks and/or geolocation entries.

Attribute | Range | Comment
---: | --- | ---
*createdTime* | xsd:dateTimeStamp | 


### GeoLocationTrack
Characteristics of a set of contiguous geolocation entries representing a path/track taken.

Attribute | Range | Comment
---: | --- | ---
*endTime* | xsd:dateTimeStamp | 
*startTime* | xsd:dateTimeStamp | 


### HTTPConnection


Attribute | Range | Comment
---: | --- | ---
*httpMessageBodyData* | xsd:base64Binary | 
*httpMessageBodyLength* | xsd:integer | 
*httpRequestHeader* | xsd:base64Binary | 
*httpRequestLine* | xsd:base64Binary | 


### Hash


Attribute | Range | Comment
---: | --- | ---
*hashMethod* | [HashMethod](#hashmethod) | 
*hashValue* | xsd:hexBinary | 


### ICMPConnection


Attribute | Range | Comment
---: | --- | ---
*code* | xsd:string | 


### IOSPackage




### IdentityPropertyBundle




### Image
Defines the basic properties associated with a disk image file. (Ie. the full image of a disk, not just specific volumes.)



### LVMVolume




### LatLongCoordinates


Attribute | Range | Comment
---: | --- | ---
*latitude* | xsd:float | 
*longitude* | xsd:float | 


### LinuxPackage




### Memory




### Message
The properties associated with message (eg. email, sms, whatsapp, etc.)

Attribute | Range | Comment
---: | --- | ---
*body* | xsd:string | 
*from* | [Trace](#trace) | The designated sender of the Message.
*isRead* | xsd:boolean | 
*modifedTime* | xsd:dateTimeStamp | 
*participant* |  | Describes people who are involved in the Message. Participants are not necessarily the sender or recipients of the message.

This property is useful if the people involved with the Message are known, but the sender of the Message cannot be determined.
*received* | [ReceivedEvent](#receivedevent) | 
*sentTime* | xsd:dateTimeStamp | 
*to* | [Trace](#trace) | The designated recipients of the Message.


### MessageThread


Attribute | Range | Comment
---: | --- | ---
*displayName* | xsd:string | 
*identifier* | xsd:string | 
*messages* | (Restriction on property olo:slot with [owl:allValuesFrom (Restriction on property olo:item with [owl:allValuesFrom (Restriction on property [propertyBundle](#propertybundle) with [owl:someValuesFrom [Message](#message)])])]), olo:OrderedList | 
*visibility* | [VisibilityType](#visibilitytype) | 


### Mutex


Attribute | Range | Comment
---: | --- | ---
*name* | xsd:string | The name property defines a common word or phrase that describes the meaning of the object.


### NTFS


Attribute | Range | Comment
---: | --- | ---
*alternateDataStream* | xsd:string | 
*sid* | xsd:string | 


### NetworkConnection


Attribute | Range | Comment
---: | --- | ---
*destination* | [UcoObject](#ucoobject) | 
*endTime* | xsd:dateTimeStamp | 
*protocols* |  | 
*source* | [UcoObject](#ucoobject) | 
*startTime* | xsd:dateTimeStamp | 


### NetworkLocation


Attribute | Range | Comment
---: | --- | ---
*domain* | xsd:string | 
*ipAddress* | xsd:string | Change this to an already defined ip address type.


### NetworkPacket




### NetworkRoute




### NetworkSocket




### NetworkSubnet




### OperatingSystem


Attribute | Range | Comment
---: | --- | ---
*manufacturer* | xsd:string | 
*version* | xsd:string | 


### PDFFile


Attribute | Range | Comment
---: | --- | ---
*documentInformation* |  | 
*isOptimized* | xsd:boolean | 
*pdfId0* | xsd:string | 
*pdfId1* | xsd:string | 
*version* | xsd:string | 


### Package
Defines a software application package.

TODO: Determine which of these properties are valid and which need to go into a specific property bundle (AndoridPackage, iOSPackage, LinuxPackage, etc.)

Attribute | Range | Comment
---: | --- | ---
*applicationName* | xsd:string | The name of the application (friendly name)
*dataPath* | [Trace](#trace) | Path designated by the OS to be used by that package application.
*packageName* | xsd:string | The package name (identifier)
*packagePermission* | xsd:string | Defines a permission associated with the application.
*version* | xsd:string | 


### PathRelation
Defines path relationship between two pieces of data.
When placed on a Relationship object, the source data is related to the target data by its path.

Attribute | Range | Comment
---: | --- | ---
*path* | xsd:string | 


### PhoneAccount


Attribute | Range | Comment
---: | --- | ---
*phoneNumber* | xsd:string | 


### PhoneCall
NFI Needed
TODO: Community discuss

Attribute | Range | Comment
---: | --- | ---
*callType* | xsd:string | 
*duration* | xsd:duration | 
*endTime* | xsd:dateTimeStamp | 
*startTime* | xsd:dateTimeStamp | 


### Process


Attribute | Range | Comment
---: | --- | ---
*arguments* | xsd:string | 
*binary* | [Trace](#trace) | 
*createdTime* | xsd:dateTimeStamp | 
*creatorUser* | [Trace](#trace) | 
*currentWorkingDirectory* | [FilePath](#filepath) | 
*environmentVariable* | [DictionaryItem](#dictionaryitem) | 
*isHidden* | xsd:boolean | 
*parentProcess* | (Restriction on property [propertyBundle](#propertybundle) with [owl:onClass [Process](#process), owl:minQualifiedCardinality (1 : xsd:nonNegativeInteger)]), [Trace](#trace) | 
*pid* | xsd:integer | 


### QCOWImage




### RasterPicture


Attribute | Range | Comment
---: | --- | ---
*bitsPerPixel* | xsd:integer | 
*format* | xsd:string | 
*imageCompressionMethod* | [ImageCompressionMethod](#imagecompressionmethod) | 
*imageHeight* | xsd:positiveInteger | 
*imageWidth* | xsd:positiveInteger | 


### SMSMessage
The properties uniquely associated with an SMS message.
TODO: Add properties.



### SQLiteBlob


Attribute | Range | Comment
---: | --- | ---
*columnName* | xsd:string | 
*rowCondition* | xsd:string | 
*rowIndex* | xsd:positiveInteger | 
*tableName* | xsd:string | 


### SimpleAddress


Attribute | Range | Comment
---: | --- | ---
*locality* | xsd:string | 
*postalCode* | xsd:string | 
*region* | xsd:string | 
*street* | xsd:string | 


### SimpleName


Attribute | Range | Comment
---: | --- | ---
*familyName* | xsd:string | 
*givenName* | xsd:string | 


### SymbolicLink




### System




### TCPConnection


Attribute | Range | Comment
---: | --- | ---
*destinationFlags* | xsd:string | 
*destinationPort* | xsd:integer | 
*sourceFlags* | xsd:string | 
*sourcePort* | xsd:integer | 


### ToolArguments




### UDPConnection


Attribute | Range | Comment
---: | --- | ---
*destinationPort* | xsd:integer | 
*sourcePort* | xsd:integer | 


### UNIXAccount
Properties specific to an account on a UNIX system

Attribute | Range | Comment
---: | --- | ---
*gid* | xsd:integer | 
*groupName* | xsd:string | 
*shell* | xsd:string | 


### UNIXNetworkRoute




### UNIXProcess




### UNIXVolume




### UserAccount
Properties of an instance of a user account on a system.

Attribute | Range | Comment
---: | --- | ---
*canEscalatePrivs* | xsd:boolean | 
*homeDirectory* | [FilePath](#filepath) | 
*isPrivileged* | xsd:boolean | 
*isServiceAccount* | xsd:boolean | 


### VHDIImage




### VMDKImage




### VSSVolume


Attribute | Range | Comment
---: | --- | ---
*snapshotID* | xsd:string | 


### Volume


Attribute | Range | Comment
---: | --- | ---
*sectorSize* | xsd:long | 
*volumeID* | xsd:string | 


### WHOIS




### WindowsAccount
Properties specific to an account on a Microsoft Windows (tm) system.

Attribute | Range | Comment
---: | --- | ---
*groupName* | xsd:string | 


### WindowsActiveDirectoryAccount
Properties specific to a Windows Active Directory account.

Attribute | Range | Comment
---: | --- | ---
*groupName* | xsd:string | 
*objectGUID* | xsd:string | 


### WindowsComputerSpecification
Specifies Windows-specific system properties.

Attribute | Range | Comment
---: | --- | ---
*globalFlagList* | [GlobalFlagType](#globalflagtype) | 
*msProductID* | xsd:string | 
*msProductName* | xsd:string | 
*netBiosName* | xsd:string | 
*registeredOrganization* | [Identity](#identity) | 
*registeredOwner* | [Identity](#identity) | 
*windowsDirectory* | [Trace](#trace) | 
*windowsDomain* | xsd:string | 
*windowsSystemDirectory* | [Trace](#trace) | 
*windowsTempDirectory* | [Trace](#trace) | 


### WindowsMutex




### WindowsNetworkRoute




### WindowsPEBinaryFile
Properties specific to Windows portable executable (PE) files.

Attribute | Range | Comment
---: | --- | ---
*fileHeader* | [WindowsPEFileHeader](#windowspefileheader) | 
*impHash* | xsd:string | 
*peType* | [PEType](#petype) | 
*sections* | [WindowsPESection](#windowspesection) | 


### WindowsPackage




### WindowsPrefetch
Characterizes entries in the Windows prefetch files. Starting with Windows XP, prefetching was introduced to speed up application startup.

Attribute | Range | Comment
---: | --- | ---
*accessedDirectory* | [Trace](#trace) | 
*accessedFile* | [Trace](#trace) | 
*applicationFileName* | xsd:string | 
*firstRunTime* | xsd:dateTimeStamp | 
*lastRunTime* | xsd:dateTimeStamp | 
*prefetchHash* | xsd:string | 
*timesExecuted* | xsd:long | 
*volume* | [Trace](#trace) | 


### WindowsProcess
Properties specific to a Windows's process.

Attribute | Range | Comment
---: | --- | ---
*aslrEnabled* | xsd:boolean | 
*depEnabled* | xsd:boolean | 
*ownerSID* | xsd:string | 
*priority* | xsd:string | 
*startupInfo* |  | 
*windowsTitle* | xsd:string | 


### WindowsRegistryHive
(Undocumented)

Attribute | Range | Comment
---: | --- | ---
*hiveType* | xsd:string | 


### WindowsRegistryKey
Properties of a Windows registry key.

Attribute | Range | Comment
---: | --- | ---
*creator* | [Trace](#trace) | 
*modifedTime* | xsd:dateTimeStamp | 
*numberOfSubkeys* | xsd:integer | 
*registryKey* | xsd:string | 
*registryValue* | [WindowsRegistryValue](#windowsregistryvalue) | 


### WindowsService


Attribute | Range | Comment
---: | --- | ---
*displayName* | xsd:string | 
*groupName* | xsd:string | 
*serviceDescription* | xsd:string | 
*serviceStatus* | [ServiceStatus](#servicestatus) | 
*serviceType* | [Servicetype](#servicetype) | 
*startCommandLine* | xsd:string | 
*startType* | [StartType](#starttype) | 


### WindowsSystem




### WindowsVolume
Characterizes a Windows disk volume.

Attribute | Range | Comment
---: | --- | ---
*driveLetter* | xsd:string | 


### X509Certificate


Attribute | Range | Comment
---: | --- | ---
*hash* | [Hash](#hash) | 
*isSelfSigned* | xsd:boolean | 
*issuer* | xsd:string | 
*serialNumber* | xsd:string | 
*signatureAlgorithm* | xsd:string | 
*subjectPublicKeyAlgorithm* | xsd:string | 
*subjectPublicKeyExponent* | xsd:integer | 
*subjectPublicKeyModulus* | xsd:string | 
*validityNotAfter* | xsd:dateTimeStamp | 
*validityNotBefore* | xsd:dateTimeStamp | 
*version* | xsd:string | 
*x509V3Extensions* | [X509V3Extensions](#x509v3extensions) | 


