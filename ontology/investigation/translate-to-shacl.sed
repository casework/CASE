# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

/a owl:Restriction ;/d
s/a owl:Class ;/a owl:Class, sh:NodeShape ;/
s/owl:cardinality "1"^^xsd:nonNegativeInteger ;/sh:maxCount "1"^^xsd:integer ; sh:minCount "1"^^xsd:integer ;/
s/owl:maxCardinality "1"^^xsd:nonNegativeInteger ;/sh:maxCount "1"^^xsd:integer ;/
s/owl:maxQualifiedCardinality "1"^^xsd:nonNegativeInteger ;/sh:maxCount "1"^^xsd:integer ;/
s/owl:minCardinality "0"^^xsd:nonNegativeInteger ;/sh:minCount "0"^^xsd:integer ;/
s/owl:minQualifiedCardinality "1"^^xsd:nonNegativeInteger ;/sh:minCount "1"^^xsd:integer ;/
s/owl:onClass/sh:class/
s/owl:onDataRange/sh:datatype/
s/owl:onProperty/sh:path/
