#!/usr/bin/env python3

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

import os
from typing import Generator, Optional, Set

import pytest
from rdflib import Graph, Namespace, OWL, RDF, RDFS, SH, URIRef


@pytest.fixture(scope="module")
def graph() -> Generator[Graph, None, None]:
    graph = Graph()
    graph.parse(os.path.join(os.path.dirname(__file__), "case_monolithic.ttl"))
    assert len(graph) > 0, "Failed to load case_monolithic.ttl."
    yield graph


def test_rdf_design_vocabularies_defined(graph: Graph) -> None:
    """
    (This test is copied verbatim from UCO.  Alternative methods of
    importing the review from UCO are welcome.)

    This test performs a typo review of RDF-, RDFS-, and OWL-namespaced concepts.

    The mechanism used is rdflib's ClosedNamespace.  The imported
    objects RDF, RDFS, and OWL are instances of this Python class.
    """

    expected: Set[URIRef] = set()  # This set is intentionally empty.
    computed: Set[URIRef] = set()

    concepts_used: Set[URIRef] = set()
    for triple in graph.triples((None, None, None)):
        for triple_member in triple:
            if not isinstance(triple_member, URIRef):
                continue
            concepts_used.add(triple_member)

    OWL_str = str(OWL)
    RDF_str = str(RDF)
    RDFS_str = str(RDFS)
    SH_str = str(SH)

    def _concept_in_design_vocabulary(concept: URIRef) -> Optional[bool]:
        """
        Return True -> Concept is defined in some design vocabulary.
        Return False -> Concept is not defined in design vocabulary.
        Return None -> N/A.
        """
        design_vocabulary: Namespace
        if concept.startswith(OWL_str):
            concept_fragment = concept.replace(OWL_str, "")
            design_vocabulary = OWL
        elif concept.startswith(RDF_str):
            concept_fragment = concept.replace(RDF_str, "")
            design_vocabulary = RDF
        elif concept.startswith(RDFS_str):
            concept_fragment = concept.replace(RDFS_str, "")
            design_vocabulary = RDFS
        elif concept.startswith(SH_str):
            concept_fragment = concept.replace(SH_str, "")
            design_vocabulary = SH
        else:
            return None

        try:
            _ = design_vocabulary[concept_fragment]
        except AttributeError:
            return False

    assert (
        _concept_in_design_vocabulary(
            URIRef(
                "http://www.w3.org/2002/07/owl#NonExistentConcept-f287fb8b-433b-45a2-82b8-9b53bfa35c64"
            )
        )
        is False
    ), "ClosedNamespace functionality used in this test did not detect a known-erroneous value.  This test needs revising."

    for concept_used in concepts_used:
        if _concept_in_design_vocabulary(concept_used) is False:
            computed.add(concept_used)

    assert expected == computed
