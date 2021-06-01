# Ontology data normalization

CASE uses a normalization process to help prevent errors and confusion during version control. This makes sure that the ontology files will reflect only substantive changes.

This file describes the normalization requirement for submitting revisions to the CASE ontology's Turtle files.

The CASE ontology, encoded as Turtle, follows a procedure based on the [`rdf-toolkit`](https://github.com/edmcouncil/rdf-toolkit) utility.  For CASE, the "normalized" form of Turtle is the form that results from an idempotent application of rules to settle questions of Turtle style, such as:

* Definition sort order
* Whitespace usage
* Prefix usage
* Comma placement
* Expansion of [collections](https://www.w3.org/TR/turtle/#collections)
* Blank node placement

The CASE community considers the ontology serialization to be "normalized" when an application of rules to decide the above "stylistic" matters no longer changes a Turtle file.


## Normalization command

This invocation of `rdf-toolkit` shows the flags to be used.  "`INPUT_TTL_FILE`" is the CASE Turtle file that is not necessarily normalized. "`OUTPUT_TTL_FILE`" is the resulting Turtle file after normalization.  This same command run on "`OUTPUT_TTL_FILE`" as input should produce a file with no further changes.

```
java -jar rdf-toolkit.jar \
  --inline-blank-nodes \
  --source INPUT_TTL_FILE \
  --source-format turtle \
  --target OUTPUT_TTL_FILE \
  --target-format turtle
```


## Review procedure

As part of reviewing any Pull Request to the ontology, `rdf-toolkit` is used on the proposed Turtle files.  If there is any change from application of `rdf-toolkit`, the ontology maintainers will request the Pull Request be re-submitted.  This is to simplify review, and to keep the edit history to ontology files minimal, reducing the potential for confusion in future analysis of revisions.
