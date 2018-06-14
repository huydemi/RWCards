# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contact.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contact.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rcontact.proto\"\xdb\x01\n\x07\x43ontact\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x14\n\x0ctwitter_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x13\n\x0bgithub_link\x18\x05 \x01(\t\x12\"\n\x04type\x18\x06 \x01(\x0e\x32\x14.Contact.ContactType\x12\x11\n\timageName\x18\x07 \x01(\t\"8\n\x0b\x43ontactType\x12\x0b\n\x07SPEAKER\x10\x00\x12\r\n\tATTENDANT\x10\x01\x12\r\n\tVOLUNTEER\x10\x02\"&\n\x08Speakers\x12\x1a\n\x08\x63ontacts\x18\x01 \x03(\x0b\x32\x08.Contactb\x06proto3')
)



_CONTACT_CONTACTTYPE = _descriptor.EnumDescriptor(
  name='ContactType',
  full_name='Contact.ContactType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPEAKER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTENDANT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUNTEER', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=181,
  serialized_end=237,
)
_sym_db.RegisterEnumDescriptor(_CONTACT_CONTACTTYPE)


_CONTACT = _descriptor.Descriptor(
  name='Contact',
  full_name='Contact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='Contact.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='Contact.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='twitter_name', full_name='Contact.twitter_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='Contact.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='github_link', full_name='Contact.github_link', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Contact.type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imageName', full_name='Contact.imageName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTACT_CONTACTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=237,
)


_SPEAKERS = _descriptor.Descriptor(
  name='Speakers',
  full_name='Speakers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contacts', full_name='Speakers.contacts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=277,
)

_CONTACT.fields_by_name['type'].enum_type = _CONTACT_CONTACTTYPE
_CONTACT_CONTACTTYPE.containing_type = _CONTACT
_SPEAKERS.fields_by_name['contacts'].message_type = _CONTACT
DESCRIPTOR.message_types_by_name['Contact'] = _CONTACT
DESCRIPTOR.message_types_by_name['Speakers'] = _SPEAKERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Contact = _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), dict(
  DESCRIPTOR = _CONTACT,
  __module__ = 'contact_pb2'
  # @@protoc_insertion_point(class_scope:Contact)
  ))
_sym_db.RegisterMessage(Contact)

Speakers = _reflection.GeneratedProtocolMessageType('Speakers', (_message.Message,), dict(
  DESCRIPTOR = _SPEAKERS,
  __module__ = 'contact_pb2'
  # @@protoc_insertion_point(class_scope:Speakers)
  ))
_sym_db.RegisterMessage(Speakers)


# @@protoc_insertion_point(module_scope)
