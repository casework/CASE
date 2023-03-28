#!/usr/bin/make -f

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

SHELL := /bin/bash

top_srcdir := $(shell cd .. ; pwd)

case_turtle_files := $(shell /bin/ls $(top_srcdir)/ontology/*/*.ttl)
uco_turtle_files := $(shell /bin/ls $(top_srcdir)/dependencies/UCO/ontology/*/*.ttl $(top_srcdir)/dependencies/UCO/ontology/*/*/*.ttl)

uco_imported_ontology_files := \
  $(top_srcdir)/dependencies/UCO/dependencies/collections-ontology/collections.owl \
  $(top_srcdir)/dependencies/UCO/dependencies/error/docs/current/error.owl

all:

# Ensure the CASE-internal shapes pass their own tests.
.shapes.done.log: \
  $(top_srcdir)/.venv.done.log \
  shapes/case-qc.ttl
	$(MAKE) \
	  --directory shapes \
	  check
	touch $@

case_monolithic.ttl: \
  $(top_srcdir)/.lib.done.log \
  $(top_srcdir)/dependencies/UCO/tests/thing.ttl \
  $(case_turtle_files) \
  $(uco_turtle_files) \
  .shapes.done.log
	source $(top_srcdir)/venv/bin/activate \
	  && rdfpipe \
	    --output-format turtle \
	    $(case_turtle_files) \
	    $(uco_turtle_files) \
	    > __$@
	# Review CASE closure for versioning consistency.
	source $(top_srcdir)/venv/bin/activate \
          && rdfpipe \
	  __$@ \
	  $(imported_ontology_files) \
	  > ___$@
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl $(top_srcdir)/dependencies/UCO/tests/shapes/uco-closure-qc.ttl \
	    --shacl-file-format turtle \
	    ___$@
	# Review CASE closure with SHACL-SHACL.
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --metashacl \
	    --shacl ___$@ \
	    --shacl-file-format turtle \
	    $(top_srcdir)/dependencies/UCO/tests/thing.ttl
	# Closure tests have passed; remove closure file.
	rm ___$@
	# Review CASE for practice conformance.
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl $(top_srcdir)/dependencies/UCO/tests/shapes/uco-qc.ttl \
	    --shacl-file-format turtle \
	    __$@
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl shapes/case-qc.ttl \
	    --shacl-file-format turtle \
	    __$@
	# Review CASE for OWL 2 DL conformance.
	source $(top_srcdir)/venv/bin/activate \
	  && pyshacl \
	    --data-file-format turtle \
	    --format turtle \
	    --inference none \
	    --shacl $(top_srcdir)/dependencies/UCO/ontology/owl/owl.ttl \
	    --shacl-file-format turtle \
	    __$@
	java -jar $(top_srcdir)/dependencies/UCO/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

# Note these recipe dependencies are ordered to build the faster inheritance review first.
check: \
  inheritance_review.ttl \
  case_monolithic.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && pytest \
	    --ignore examples \
	    --log-level=DEBUG
	$(MAKE) \
	  --directory examples \
	  check

clean:
	@$(MAKE) \
	  --directory examples \
	  clean
	@rm -f \
	  .*.done.log \
	  case_monolithic.ttl

inheritance_review.ttl: \
  $(case_turtle_files) \
  $(uco_turtle_files) \
  $(top_srcdir)/.venv.done.log
	rm -f _$@
	source $(top_srcdir)/venv/bin/activate \
	  && case_shacl_inheritance_reviewer \
	    --strict \
	    _$@ \
	    $(case_turtle_files) \
	    $(uco_turtle_files) \
	    || (cat _$@ && exit 1)
	mv _$@ $@
