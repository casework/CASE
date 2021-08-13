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

all:

# This recipe guarantees that 'git submodule init' and 'git submodule update' have run at least once.
# The recipe avoids running 'git submodule update' more than once, in case a user is testing with the submodule at a different commit than what CASE tracks.
.git_submodule_init.done.log: \
  .gitmodules
	# UCO
	test -r dependencies/UCO/README.md \
	  || (git submodule init dependencies/UCO && git submodule update dependencies/UCO)
	@test -r dependencies/UCO/README.md \
	  || (echo "ERROR:Makefile:UCO submodule README.md file not found, even though that submodule is initialized." >&2 ; exit 2)
	touch $@

.lib.done.log:
	$(MAKE) \
	  --directory lib
	touch $@

check: \
  .lib.done.log
	$(MAKE) \
	  --directory ontology \
	  check

clean:
	@rm -f .lib.done.log
	@$(MAKE) \
	  --directory ontology \
	  clean
