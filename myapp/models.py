from django.db import models

# Create your models here.
class User:
  name: str
  age: int
  def __init__(self, name, age):
    self.name = name
    self.age = age