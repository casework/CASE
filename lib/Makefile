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

all: \
  rdf-toolkit.jar

# Downloading rdf-toolkit is done here following the directions at:
#   https://github.com/edmcouncil/rdf-toolkit
# Checksum is confirmed before moving file into position.  (This
# practice will probably require frequent updates, unless signed
# checksum can be retrieved somehow.)
# Checksum is not a dependency of the file to avoid timestamp-based
# re-downloads.
rdf-toolkit.jar:
	test -r rdf-toolkit.jar.sha512
	wget \
	  --output-document $@_ \
	  https://jenkins.edmcouncil.org/job/rdf-toolkit-build/lastSuccessfulBuild/artifact/target/scala-2.12/rdf-toolkit.jar
	test \
	  "x$$(openssl dgst -sha512 $@_ | awk '{print($$NF)}')" \
	  == \
	  "x$$(head -n1 rdf-toolkit.jar.sha512)"
	mv $@_ $@
