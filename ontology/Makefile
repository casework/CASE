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

top_srcdir := ..

all: \
  all-investigation \
  all-master \
  all-vocabulary

.PHONY: \
  all-investigation \
  all-master \
  all-vocabulary \
  check-investigation \
  check-master \
  check-vocabulary \
  clean-investigation \
  clean-master \
  clean-vocabulary

all-investigation:
	$(MAKE) \
	  --directory investigation

all-master:
	$(MAKE) \
	  --directory master

all-vocabulary:
	$(MAKE) \
	  --directory vocabulary

check: \
  check-master \
  check-investigation \
  check-vocabulary

check-investigation: \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory investigation \
	  check

check-master: \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory master \
	  check

check-vocabulary: \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory vocabulary \
	  check

clean: \
  clean-investigation \
  clean-master \
  clean-vocabulary

clean-investigation:
	@$(MAKE) \
	  --directory investigation \
	  clean

clean-master:
	@$(MAKE) \
	  --directory master \
	  clean

clean-vocabulary:
	@$(MAKE) \
	  --directory vocabulary \
	  clean
