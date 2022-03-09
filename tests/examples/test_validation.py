#!/usr/bin/env python3

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

"""
Tests in this file confirm that the JSON-LD files with "PASS" in the
name pass SHACL validation, and JSON-LD files with "XFAIL" in the name
not only fail SHACL validation, but also report a set of properties used
in their JSON-LD that triggered SHACL validation errors.

This test was written to be called with the pytest framework, expecting
the only functions to be called to be named "test_*".
"""

import logging
from typing import Set

import pytest
import rdflib.plugins.sparql  # type: ignore

NS_CASE_INVESTIGATION = rdflib.Namespace("https://ontology.caseontology.org/case/investigation/")
NS_SH = rdflib.SH
NS_UCO_ACTION = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/action/")
NS_UCO_CORE = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/core/")
NS_UCO_LOCATION = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/location/")
NS_UCO_OBSERVABLE = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/observable/")

NSDICT = {"sh": NS_SH}

def load_validation_graph(
  filename : str,
  expected_conformance : bool
) -> rdflib.Graph:
    g = rdflib.Graph()
    g.parse(filename, format="turtle")
    g.namespace_manager.bind("sh", NS_SH)

    query = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?lConforms
WHERE {
  ?nReport
    a sh:ValidationReport ;
    sh:conforms ?lConforms ;
    .
}
""", initNs=NSDICT)

    computed_conformance = None
    for result in g.query(query):
        (l_conforms,) = result
        computed_conformance = bool(l_conforms)
    assert expected_conformance == computed_conformance
    return g

def confirm_validation_errors(
  filename : str,
  expected_error_iris : Set[str]
) -> None:
    g = load_validation_graph(filename, False)

    computed_error_iris = set()

    query = rdflib.plugins.sparql.prepareQuery("""\
SELECT DISTINCT ?nResultPath
WHERE {
  ?nReport
    a sh:ValidationReport ;
    sh:result ?nValidationResult ;
    .

  ?nValidationResult
    a sh:ValidationResult ;
    sh:resultPath ?nResultPath ;
    .
}
""", initNs=NSDICT)

    for result in g.query(query):
        (n_result_path,) = result
        computed_error_iris.add(str(n_result_path))

    try:
        assert expected_error_iris == computed_error_iris
    except:
        logging.error("Please review %s and its associated .json file to identify the ground truth validation error mismatch pertaining to data properties noted in this function.", filename)
        raise

def test_investigative_action_PASS_validation() -> None:
    """
    Confirm the PASS instance data passes validation.
    """
    g = load_validation_graph("investigative_action_PASS_validation.ttl", True)
    assert isinstance(g, rdflib.Graph)

@pytest.mark.xfail(strict=True)
def test_investigative_action_XFAIL_validation_XPASS_wrong_property_placement() -> None:
    """
    Report the XFAIL instance data XPASSes one of the induced errors - the property uco-observable:sizeInBytes is not reported as an error.
    Should a SHACL mechanism later be identified to detect this error, this test can be retired, adding NS_UCO_OBSERVABLE.sizeInBytes to the expected IRI set in test_investigative_action_XFAIL_validation().
    """
    confirm_validation_errors(
      "investigative_action_XFAIL_validation.ttl",
      {
        str(NS_UCO_OBSERVABLE.sizeInBytes)
      }
    )

def test_investigative_action_XFAIL_validation() -> None:
    """
    Confirm the XFAIL instance data fails validation based on an expected set of properties not conforming to shape constraints.
    """
    confirm_validation_errors(
      "investigative_action_XFAIL_validation.ttl",
      {
        str(NS_CASE_INVESTIGATION.exhibitNumber),
        str(NS_CASE_INVESTIGATION.rootExhibitNumber)
      }
    )
