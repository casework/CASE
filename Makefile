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

PYTHON3 ?= $(shell which python3)

all: \
  .venv.done.log
	$(MAKE) \
	  --directory ontology

# This recipe guarantees that 'git submodule init' and 'git submodule update' have run at least once.
# The recipe avoids running 'git submodule update' more than once, in case a user is testing with the submodule at a different commit than what CASE tracks.
.git_submodule_init.done.log: \
  .gitmodules
	# UCO
	test -r dependencies/UCO/README.md \
	  || (git submodule init dependencies/UCO && git submodule update dependencies/UCO)
	@test -r dependencies/UCO/README.md \
	  || (echo "ERROR:Makefile:UCO submodule README.md file not found, even though that submodule is initialized." >&2 ; exit 2)
	$(MAKE) \
	  --directory dependencies/UCO \
	  .git_submodule_init.done.log
	touch $@

.lib.done.log: \
  .git_submodule_init.done.log
	$(MAKE) \
	  --directory dependencies/UCO \
	  .lib.done.log
	touch $@

# The two CASE-Utility... files are to trigger rebuilds based on command-line interface changes or version increments.
.venv.done.log: \
  .git_submodule_init.done.log \
  dependencies/UCO/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/case_shacl_inheritance_reviewer/__init__.py \
  dependencies/UCO/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/setup.cfg \
  dependencies/UCO/requirements.txt \
  requirements.txt
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
	    dependencies/UCO/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer
	source venv/bin/activate \
	  && pip install \
	    --requirement dependencies/UCO/requirements.txt
	source venv/bin/activate \
	  && pip install \
	    --requirement requirements.txt
	touch $@

check: \
  .lib.done.log \
  .venv.done.log
	$(MAKE) \
	  --directory ontology \
	  check
	$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory tests \
	  check

clean:
	@$(MAKE) \
	  --directory tests \
	  clean
	@$(MAKE) \
	  --directory ontology \
	  clean
	@test ! -r dependencies/UCO/README.md \
	  || $(MAKE) \
	    --directory dependencies/UCO \
	    clean
	@# Restore UCO validation output files that do not affect CASE build process.
	@test ! -r dependencies/UCO/README.md \
	  || ( \
	    cd dependencies/UCO \
	      && git checkout \
	        -- \
	        tests/examples \
	        || true \
	  )
	@rm -f \
	  .*.done.log
	@rm -rf \
	  venv

dependencies/UCO/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/case_shacl_inheritance_reviewer/__init__.py: \
  .git_submodule_init.done.log
	$(MAKE) \
	  --directory dependencies/UCO \
	  dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/case_shacl_inheritance_reviewer/__init__.py

dependencies/UCO/dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/setup.cfg: \
  .git_submodule_init.done.log
	$(MAKE) \
	  --directory dependencies/UCO \
	  dependencies/CASE-Utility-SHACL-Inheritance-Reviewer/setup.cfg
