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

top_srcdir := ../..

all:

.check-vocabulary.ttl: \
  $(top_srcdir)/.lib.done.log \
  vocabulary.ttl
	java -jar $(top_srcdir)/dependencies/UCO/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source vocabulary.ttl \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	mv _$@ $@

check: \
  .check-vocabulary.ttl
	diff vocabulary.ttl .check-vocabulary.ttl

clean:
	@rm -f \
	  .check-*.ttl \
	  _*
