# Migration data

This directory contains tab-separated files to assist with migrating data from the CASE 0.1 prototype implementation to the CASE 0.2.0 and UCO 0.3.0 implementations.


## Status

This directory contains data under draft.


## Files

* `concepts.tsv` - two columns.  The first is the spelling of the CASE 0.1 concepts, without prefixes because the original example files had omitted prefixes.  The second column is the prefixed concept released since CASE 0.1.

* `concepts_ambiguous.tsv` - As with `concepts.tsv`, except other contextual information needs to be observed to determine what the destination concept should be.  E.g. with `Relationship`, the `kindOfRelationship` enumerant will indicate whether to declare this a `uco-core:Relationship` or a `uco-observable:CyberRelationship`.

* `properties.tsv` - two required columns, third optional.  The first two columns are as with `concepts.tsv`.  The third is the literal-type that should be assigned to a literal value.

* `properties_ambiguous.tsv` - As with `properties.tsv`, except other contextual information needs to be observed to determine what the destination property should be.

* `kindOfRelationship_enumerants.tsv` - Enumerations for `uco-core:Relationship` or `uco-observable:CyberRelationship`.  An absent second column indicates no enumerant was found in UCO 0.3.0.
