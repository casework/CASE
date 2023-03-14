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

top_srcdir := ../..

uco_srcdir := $(top_srcdir)/dependencies/UCO

ttl_basenames := case.ttl

all: \
  catalog-v001.xml

.check-case.ttl: \
  $(top_srcdir)/.lib.done.log \
  case.ttl
	java -jar $(top_srcdir)/dependencies/UCO/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source case.ttl \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	mv _$@ $@

catalog-v001.xml: \
  $(top_srcdir)/.venv.done.log \
  $(top_srcdir)/etc/domain_directories.tsv \
  $(top_srcdir)/etc/dependency_files.tsv \
  $(uco_srcdir)/ontology/uco/master/catalog-v001.xml \
  $(uco_srcdir)/src/create-catalog-v001.xml.py
	rm -f _$@
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(uco_srcdir)/src/create-catalog-v001.xml.py \
	    --catalog-xml $(uco_srcdir)/ontology/uco/master/catalog-v001.xml \
	    _$@ \
	    $(top_srcdir)/etc/domain_directories.tsv \
	    $(top_srcdir)/etc/dependency_files.tsv \
	    "$(top_srcdir)" \
	    $(ttl_basenames)
	mv _$@ $@

check: \
  .check-case.ttl \
  catalog-v001.xml
	diff case.ttl .check-case.ttl

clean:
	@rm -f \
	  .check-*.ttl \
	  _* \
	  catalog-v001.xml
