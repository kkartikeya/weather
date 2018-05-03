# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weather.proto

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
  name='weather.proto',
  package='com.kkartikeya.home.weather',
  syntax='proto3',
  serialized_pb=_b('\n\rweather.proto\x12\x1b\x63om.kkartikeya.home.weather\"\x7f\n\x07Weather\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0c\n\x04temp\x18\x02 \x01(\x02\x12\x10\n\x08humidity\x18\x03 \x01(\x02\x12\x11\n\twindspeed\x18\x04 \x01(\x02\x12\r\n\x05\x63loud\x18\x05 \x01(\x02\x12\x0f\n\x07sunrise\x18\x06 \x01(\x03\x12\x0e\n\x06sunset\x18\x07 \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_WEATHER = _descriptor.Descriptor(
  name='Weather',
  full_name='com.kkartikeya.home.weather.Weather',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='com.kkartikeya.home.weather.Weather.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temp', full_name='com.kkartikeya.home.weather.Weather.temp', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='humidity', full_name='com.kkartikeya.home.weather.Weather.humidity', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='windspeed', full_name='com.kkartikeya.home.weather.Weather.windspeed', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cloud', full_name='com.kkartikeya.home.weather.Weather.cloud', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sunrise', full_name='com.kkartikeya.home.weather.Weather.sunrise', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sunset', full_name='com.kkartikeya.home.weather.Weather.sunset', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=46,
  serialized_end=173,
)

DESCRIPTOR.message_types_by_name['Weather'] = _WEATHER

Weather = _reflection.GeneratedProtocolMessageType('Weather', (_message.Message,), dict(
  DESCRIPTOR = _WEATHER,
  __module__ = 'weather_pb2'
  # @@protoc_insertion_point(class_scope:com.kkartikeya.home.weather.Weather)
  ))
_sym_db.RegisterMessage(Weather)


# @@protoc_insertion_point(module_scope)
