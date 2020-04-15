# Cyber-investigation Analysis Standard Expression (CASE)

_Read the [Wiki tab](https://github.com/casework/CASE/wiki) to learn **everything** you need to know about the Cyber-investigation Analysis Standard Expression (CASE) ontology._
_For learning about the Unified Cyber Ontology, CASE's parent, see [UCO](https://github.com/ucoProject/UCO)._

## Development guidelines

The CASE Ontology Committee models domain concepts, developing the knowledge encodings for the CASE ontology.  When these concepts are ready to be encoded as ontology entries, the following guidelines govern their entered forms:
1. Style guidance - The [Style Guide for Documentation of the CASE Ontology](https://caseontology.org/resources/downloads/Style%20Guide%20for%20Documentation%20of%20the%20CASE%20Ontology.pdf) governs the style of ontology entries.  An overview presentation on the style guide is available [here](https://caseontology.org/resources/references/CASE%20Style%20Guide%20v1.0%202020-01-14.pdf).
2. Turtle serialization - CASE uses [rdf-toolkit](https://github.com/edmcouncil/rdf-toolkit) to normalize the syntax of ontology Turtle files.

## Examples in this Repository
_These will eventually be moved to the Wiki (likely [Mapping Guide](https://github.com/casework/CASE/wiki/Mapping-Guide))._
Mapping notes & respective JSON-LD output:
- [Bulk Extractor Forensic Path](examples/bulk_extractor_forensic_path.json) (*[info](examples/bulk_extractor_forensic_path.md)*)
- [Call Log](examples/call_log.json)
- [Device](examples/device.json)
- [Email](examples/email.json)
- [EXIF Data](examples/exif_data.json)
- [Files](examples/file.json) (*[info](examples/file.md)*)
- [Forensic Lifecycle](examples/forensic_lifecycle.json)
- [Location](examples/location.json)
- [Message](examples/message.json)
- [Multipart File](examples/multipart_file.json) (*[info](examples/multipart_file.md)*)
- [Oresteia](examples/Oresteia.json) (*[info](examples/Oresteia.md)*)
- [Raw Data](examples/raw_data.json)
- [Reconstructed File](examples/reconstructed_file.json) (*[info](examples/reconstructed_file.md)*)
- [SMS and Contacts](examples/sms_and_contacts.json)

## I have a question!

Before you post a Github issue or send an email ensure you've done this checklist:

1. [Determined scope](https://caseontology.org/ontology/start.html#scope) of your task. It is not necessary for most parties to understand all aspects of the ontology, mapping methods, and supporting tools.

2. Familiarize yourself with the [labels](https://github.com/casework/CASE/labels) and search the [Issues tab](https://github.com/casework/CASE/issues). Typically, only light-blue and red labels should be used by non-admin Github users while the others should be used by CASE Github admins.
*All but the red `Project` labels are found in every [`casework`](https://github.com/casework) repository.*
