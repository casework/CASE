#!/usr/bin/make -f

# Portions of this file contributed by NIST are governed by the
# following statement:
#
# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to Title 17 Section 105 of the
# United States Code, this software is not subject to copyright
# protection within the United States. NIST assumes no responsibility
# whatsoever for its use by other parties, and makes no guarantees,
# expressed or implied, about its quality, reliability, or any other
# characteristic.
#
# We would appreciate acknowledgement if the software is used.

SHELL := /bin/bash

top_srcdir := ../..

uco_srcdir := $(top_srcdir)/dependencies/UCO

ttl_basenames := investigation.ttl

all: \
  catalog-v001.xml

.check-investigation.ttl: \
  $(top_srcdir)/.lib.done.log \
  investigation.ttl
	java -jar $(top_srcdir)/dependencies/UCO/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source investigation.ttl \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	mv _$@ $@

catalog-v001.xml: \
  $(top_srcdir)/.venv.done.log \
  $(top_srcdir)/etc/domain_directories.tsv \
  $(top_srcdir)/etc/dependency_files.tsv \
  $(uco_srcdir)/ontology/uco/action/catalog-v001.xml \
  $(uco_srcdir)/ontology/uco/role/catalog-v001.xml \
  $(uco_srcdir)/src/create-catalog-v001.xml.py
	rm -f _$@
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(uco_srcdir)/src/create-catalog-v001.xml.py \
	    --catalog-xml $(uco_srcdir)/ontology/uco/action/catalog-v001.xml \
	    --catalog-xml $(uco_srcdir)/ontology/uco/role/catalog-v001.xml \
	    _$@ \
	    $(top_srcdir)/etc/domain_directories.tsv \
	    $(top_srcdir)/etc/dependency_files.tsv \
	    "$(top_srcdir)" \
	    $(ttl_basenames)
	mv _$@ $@

check: \
  .check-investigation.ttl \
  catalog-v001.xml
	diff investigation.ttl .check-investigation.ttl

clean:
	@rm -f \
	  .check-*.ttl \
	  _* \
	  catalog-v001.xml
