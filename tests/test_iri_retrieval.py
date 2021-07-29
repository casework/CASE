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

import os

import pytest
import rdflib

NS_OWL = rdflib.OWL
NS_RDF = rdflib.RDF

@pytest.fixture
def top_srcdir():
    """
    Identify top_srcdir by presence of assumed file in repository's root.
    """
    srcdir = os.path.dirname(__file__)
    retval = os.path.abspath(os.path.join(srcdir, ".."))
    assert os.path.isfile(os.path.join(retval, "LICENSE")), "top_srcdir does not seem to be ontology repository root."
    return retval

@pytest.fixture
def investigation_ttl_filepath(top_srcdir):
    filepath = os.path.join(top_srcdir, "ontology", "investigation", "investigation.ttl")
    assert os.path.isfile(filepath), "investigation.ttl not found in expected location."
    return filepath

def test_concept_iri(investigation_ttl_filepath):
    """
    This test confirms the IRI for InvestigativeAction matches an expected hard-coded value when retrieved from the investigation ontology file.
    """
    expected = "https://caseontology.org/ontology/case/investigation#InvestigativeAction"

    graph = rdflib.Graph()
    graph.parse(investigation_ttl_filepath, format="turtle")

    n_ontology = None
    for triple in graph.triples((
      None,
      NS_RDF.type,
      NS_OWL.Ontology
    )):
        n_ontology = triple[0]
    assert not n_ontology is None, "Ontology unversioned IRI not found in investigation.ttl file."
    ontology_str = n_ontology.toPython()

    NS_CASE_INVESTIGATION = rdflib.Namespace(ontology_str + "#")

    n_investigative_action = NS_CASE_INVESTIGATION.InvestigativeAction
    computed = n_investigative_action.toPython()

    assert computed == expected
