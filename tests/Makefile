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

PYTHON3 ?= $(shell which python3.9 2>/dev/null || which python3.8 2>/dev/null || which python3.7 2>/dev/null || which python3.6 2>/dev/null || which python3)

case_turtle_files := $(shell /bin/ls $(top_srcdir)/ontology/*/*.ttl)
uco_turtle_files := $(shell /bin/ls $(top_srcdir)/dependencies/UCO/ontology/*/*.ttl)

all:

# The two CASE-Utility... files are to trigger rebuilds based on command-line interface changes or version increments.
.venv.done.log: \
  $(top_srcdir)/.git_submodule_init.done.log \
  $(top_srcdir)/dependencies/UCO/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/case_shacl_inheritance_reviewer/__init__.py \
  $(top_srcdir)/dependencies/UCO/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/setup.cfg \
  $(top_srcdir)/dependencies/UCO/tests/requirements.txt
	rm -rf venv
	$(PYTHON3) -m venv \
	  venv
	source venv/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools \
	    wheel
	source venv/bin/activate \
	  && pip install \
	    $(top_srcdir)/dependencies/UCO/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer
	source venv/bin/activate \
	  && pip install \
	    --requirement $(top_srcdir)/dependencies/UCO/tests/requirements.txt
	touch $@

case_monolithic.ttl: \
  $(top_srcdir)/.lib.done.log \
  $(top_srcdir)/dependencies/UCO/tests/src/glom_graph.py \
  $(case_turtle_files) \
  $(uco_turtle_files) \
  .venv.done.log
	source venv/bin/activate \
	  && python3 $(top_srcdir)/dependencies/UCO/tests/src/glom_graph.py \
	    __$@ \
	    $(case_turtle_files) \
	    $(uco_turtle_files)
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --infer-base-iri \
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
	$(MAKE) \
	  --directory examples \
	  check

clean:
	@$(MAKE) \
	  --directory examples \
	  clean
	@rm -f \
	  .venv.done.log \
	  case_monolithic.ttl
	@rm -rf \
	  venv

inheritance_review.ttl: \
  $(case_turtle_files) \
  $(uco_turtle_files) \
  .venv.done.log
	rm -f _$@
	source venv/bin/activate \
	  && case_shacl_inheritance_reviewer \
	    --strict \
	    _$@ \
	    $(case_turtle_files) \
	    $(uco_turtle_files) \
	    || (cat _$@ && exit 1)
	mv _$@ $@
