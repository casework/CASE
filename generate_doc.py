"""Generate Markdown documentation base on ontology."""

import os
import rdflib

CASE_FILE = os.path.join(os.path.dirname(__file__), 'case.ttl')

DOC_FILE = os.path.join(os.path.dirname(__file__), 'case.md')


case = rdflib.Namespace('http://case.example.org/core#')

graph = rdflib.Graph()
graph.namespace_manager.bind('case', case)


def iter_list(value):
  """Iterates an RDF list."""
  for item in graph.objects(value, rdflib.RDF.first):
    yield item
    for rest in graph.objects(value, rdflib.RDF.rest):
      for item in iter_list(rest):
        yield item

def get_name(value, linkify=False):
  # OWL Restriction
  if (value, rdflib.RDF.type, rdflib.OWL.Restriction) in graph:
    on_property = None
    restrictions = []
    for predicate, object in graph.predicate_objects(value):
      if predicate == rdflib.OWL.onProperty:
        on_property = get_name(object, linkify=linkify)
      elif object != rdflib.OWL.Restriction:
        restrictions.append('{} {}'.format(get_name(predicate), get_name(object, linkify=linkify)))
    return '(Restriction on property {} with [{}])'.format(get_name(on_property, linkify=linkify), ', '.join(restrictions))

  # Anonymous class
  if (value, rdflib.RDF.type, rdflib.OWL.Class) in graph and (value, rdflib.OWL.unionOf, None) in graph:
    # Get list of objects.
    list_object = list(graph.objects(value, rdflib.OWL.unionOf))[0]
    items = [get_name(item, linkify=linkify) for item in iter_list(list_object)]
    return '({})'.format(' or '.join(items))

  elif isinstance(value, rdflib.URIRef):
    term = value.n3(graph.namespace_manager)
    prefix, _, name = term.partition(':')
    if name and linkify:
      name = '[{}](#{})'.format(name, name.lower().replace(' ', '-'))
    return name if not prefix else term

  elif isinstance(value, rdflib.Literal):
    return '({} : {})'.format(str(value), get_name(value.datatype, linkify=linkify))
  else:
    return str(value)


def get_domains(uri_ref):
  """Returns list of all the domains of a particular uri_ref."""
  results = graph.query("""
    SELECT ?attribute
    WHERE {
      ?attribute rdfs:domain/(owl:unionOf/rdf:rest*/rdf:first)* ?uri_ref .
    }
    """, initBindings={'uri_ref': uri_ref})
  return [result[0] for result in results]

def object_documention(uri_ref):
  """Produces markdown documenation of object and its attributes."""
  string = ''
  comment = graph.objects(uri_ref, rdflib.RDFS.comment)
  if comment:
    string += '\n\n'.join(comment)
  string += '\n\n'

  sub_types = graph.subjects(rdflib.RDF.type, uri_ref)
  sub_types = map(get_name, sub_types)
  if sub_types:
    string += '**SubTypes:**  {}\n\n'.format(', '.join(sorted(sub_types)))

  # TODO: Add multiplicity.
  attributes = sorted(get_domains(uri_ref))
  if attributes:
    string += 'Attribute | Range | Comment\n---: | --- | ---\n'
    for attribute in attributes:
      ranges = [get_name(range, linkify=True) for range in graph.objects(attribute, rdflib.RDFS.range)]

      comment = graph.objects(attribute, rdflib.RDFS.comment)
      string += '*{}* | {} | {}\n'.format(
          get_name(attribute), ', '.join(sorted(ranges)), ', '.join(sorted(comment)))

  string += '\n\n'
  return string


def subclass_documentation(uri_ref, level='###'):
  """Produces the documentation of the subclasses of the given object."""
  string = ''
  for sub_class in sorted(graph.subjects(rdflib.RDFS.subClassOf, uri_ref)):
    string += '{} {}\n'.format(level, get_name(sub_class))
    string += object_documention(sub_class)

  return string



with open(CASE_FILE) as file_object:
  graph.parse(file_object, publicID='http://case.example.org/core#', format='turtle')


with open(DOC_FILE, mode='w') as file_object:

  file_object.write('''
- [Enumeration](#enumeration)
- [Supporting Classes](#supporting-classes)
- [Object](#object)
- [Property Bundle](#property-bundle)

''')

  file_object.write('# Enumeration\n\n')
  file_object.write(object_documention(case.Enumeration))
  file_object.write(subclass_documentation(case.Enumeration))

  file_object.write('# Supporting Classes\n\n')
  file_object.write(object_documention(case.SupportingClasses))
  file_object.write(subclass_documentation(case.SupportingClasses))

  file_object.write('# Object\n\n')
  file_object.write(object_documention(case.Object))
  file_object.write('### Descriptive\n\n')
  file_object.write(object_documention(case.Descriptive))
  file_object.write(subclass_documentation(case.Descriptive, level='#####'))

  file_object.write('# Property Bundle\n\n')
  file_object.write(object_documention(case.PropertyBundle))
  file_object.write(subclass_documentation(case.PropertyBundle))

