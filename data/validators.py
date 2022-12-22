import os
from django.core.exceptions import ValidationError

def file_image(value):
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.jpg', '.png']
  if not ext.lower() in valid_extensions:
    raise ValidationError('Unsupported file extension')