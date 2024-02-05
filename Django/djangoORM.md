## [Django ORM](#django-ORM)

### [# Models](#models)

#### [Model Parameters](#model-parameters)

#### [Model Relationships](#model-relationships)

##### [One to One](#one-to-one)

##### [One to Many](#one-to-many)

##### [Many to Many](#many-to-many)

##### [Many To Many Via Through](#many-to-many-via-through)

##### [on_delete methods](#on_delete-methods)

### [# QuerySets](#querysets)

#### [Filtering](#filtering)

#### [Query modifiers](#query-modifiers)

#### [Field selection](#field-selection)

#### [Aggregation](#aggregation)

#### [Slicing](#slicing)

#### [Prefetch](#prefetch)

#### [Bulk Operations](#bulk-operations)

#### [Annotate](#annotate)

# Django ORM

## Object-Relational Mapping

#### Django Provides a high-level API for reading and writing complex querys to the database. perform database operations using Python objects and methods, rather than writing raw SQL queries.

## Models

#### A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

```python
# sample model

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

### Model Parameters

#### Field: This parameter specifies the type of data that the column will store. For example, CharField, IntegerField, DateField, etc.

#### verbose_name: This parameter allows you to specify a human-readable name for the field. It's used as the label in forms and other parts of the Django admin interface.

#### name: This parameter allows you to specify the name of the database column explicitly. By default, Django will use the name of the attribute as the column name.

#### primary_key: If set to True, this parameter makes the field the primary key for the model's table.

#### unique: If set to True, this parameter ensures that each value in the column is unique across all rows in the table.

#### null: If set to True, this parameter allows the column to store NULL values. By default, it's set to False.

#### blank: If set to True, this parameter allows the field to be blank in forms. It doesn't affect the database schema.

#### default: This parameter allows you to specify a default value for the column.

#### choices: If provided, this parameter restricts the values that the column can store to a predefined list of choices.

#### db_column: This parameter allows you to specify the name of the database column explicitly, similar to the name parameter.

#### db_index: If set to True, this parameter creates an index on the column in the database, which can improve query performance.

#### editable: If set to False, this parameter prevents the field from being displayed in forms or the admin interface.

#### help_text: This parameter provides additional descriptive text for the field, which is displayed alongside the field in forms.

#### validators: If provided, this parameter specifies a list of validation functions or classes that are applied to the field's value.

#### error_messages: If provided, this parameter allows you to override the default error messages for the field.

```python

from django.db import models

class MyModel(models.Model):
    name = models.CharField(
        max_length=50,
        error_messages={
            'blank': 'Please provide a name.',
            'unique': 'This name is already taken.',
            'max_length': 'The name must be at most 50 characters long.'
        }
    )

```

#### auto_now_add: If set to True, this parameter automatically sets the field to the current date and time when the object is first created.

#### auto_now: If set to True, this parameter automatically updates the field to the current date and time every time the object is saved.

```python
#  sample validation
from django.core.validators import MinValueValidator, MaxValueValidator


def custom_validator(value):
    if value < 0:
        raise ValidationError('Value must be greater than 0.')


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    age = models.IntegerField(validators=[custom_validator])
```

#### sample validators

##### EmailValidator: Validates that a value is a valid email address.

##### MaxLengthValidator: Validates that a string value does not exceed a certain maximum length.

##### MinLengthValidator: Validates that a string value meets a certain minimum length requirement.

##### MaxValueValidator: Validates that a numeric value does not exceed a certain maximum value.

##### MinValueValidator: Validates that a numeric value meets a certain minimum value requirement.

##### URLValidator: Validates that a value is a valid URL.

##### RegexValidator: Validates that a value matches a specified regular expression pattern.

##### BaseValidator: A base class for building custom validators.

##### DecimalValidator: Validates that a decimal value is within a certain range.

## Model Relationships

#### A relationship is a connection between two models. Django supports three types of relationships: one-to-many, one-to-one, and many-to-many.

### One to One

#### A one-to-one relationship is a relationship in which a single record in one table is related to a single record in another table. For example, a single person can have a single passport, so the relationship between the Person and Passport models is a one-to-one relationship.

```python

class Person(models.Model):
    name = models.CharField(max_length=100)

class Passport(models.Model):
    number = models.CharField(max_length=100)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

```

### One to Many

#### A one-to-many relationship is a relationship in which a single record in one table can be related to multiple records in another table. For example, a single author can write multiple books, so the relationship between the Author and Book models is a one-to-many relationship.

```python

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

```

### Many to Many

#### A many-to-many relationship is a relationship in which a record in one table can be related to multiple records in another table, and vice versa. For example, a single book can have multiple genres, and a single genre can be associated with multiple books, so the relationship between the Book and Genre models is a many-to-many relationship.

```python

class Book(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField('Genre')
    # ManyToManyField can be used with a string reference to the related model, which can be useful when the related model is defined later in the same file.

class Genre(models.Model):
    name = models.CharField(max_length=100)

```

### Many To Many Via Through

#### In Django ORM, you can use the through parameter to specify a custom intermediary model for a many-to-many relationship. This allows you to add extra fields to the intermediary model, which can be useful when you need to store additional information about the relationship. By default, Django creates an intermediary model for many-to-many relationships, but you can use the through parameter to specify a custom model. It helps to store additional information about the relationship.

#### For example, you can use the through parameter to specify a custom intermediary model for the many-to-many relationship between the Book and Genre models.

```python

class Book(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField('Genre', through='BookGenre')

class Genre(models.Model):
    name = models.CharField(max_length=100)

class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

```

### on_delete methods

#### The on_delete parameter specifies the behavior to adopt when the referenced object is deleted. It accepts the following values:

##### CASCADE: When the referenced object is deleted, also delete the objects that have a foreign key pointing to it.

##### PROTECT: Forbid the deletion of the referenced object. To delete it, you will need to delete all objects that reference it manually.

##### SET_NULL: Set the foreign key to NULL when the referenced object is deleted. This is only possible if the field is nullable.

##### SET_DEFAULT: Set the foreign key to its default value when the referenced object is deleted.

##### SET() {sets custom value}: Set the foreign key to the value passed to the SET() function when the referenced object is deleted. If a callable is passed, it will be evaluated at the time of deletion.

##### DO_NOTHING: Do nothing when the referenced object is deleted. It's up to you to manually delete the references to the deleted object.

##### RESTRICT: Prevent deletion of the referenced object by raising ProtectedError, a subclass of django.db.IntegrityError.

## QuerySets

#### A QuerySet is a collection of objects from your database, which can have filters to restrict the results.

```python

# sample query

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

```

### Filtering

#### Get all records

```python
Person.objects.all()
```

#### Get the first record or last record

```python
Person.objects.first()
Person.objects.last()
```

#### get a specific record , throw an error if not found (If multiple records are found, gets first one according to filters)

```python
Person.objects.get(id=1)
```

#### get a specific record , return None if not found (If multiple records are found, gets first one according to filters)

```python
Person.objects.filter(id=1).first()

# filter Parameters

Person.objects.filter(first_name='John') # get all records with first_name = 'John' exact match

Person.objects.filter(first_name__iexact='john') # get all records with first_name = 'john' case insensitive exact match

Person.objects.filter(first_name__contains='John') # get all records with first_name contains 'John'

Person.objects.filter(first_name__icontains='john') # get all records with first_name contains 'john' case insensitive

Person.objects.filter(first_name__startswith='John') # get all records with first_name starts with 'John'

Person.objects.filter(first_name__istartswith='john') # get all records with first_name starts with 'john' case insensitive

Person.objects.filter(first_name__endswith='John') # get all records with first_name ends with 'John'

Person.objects.filter(first_name__iendswith='john') # get all records with first_name ends with 'john' case insensitive

Person.objects.filter(date_of_birth__year=1990) # get all records with date_of_birth year = 1990 only works with date fields

Person.objects.filter(date_of_birth__month=1) # get all records with date_of_birth month = 1 only works with date fields

Person.objects.filter(date_of_birth__day=1) # get all records with date_of_birth day = 1 only works with date fields

Person.objects.filter(date_of_birth__gt='1990-01-01') # get all records with date_of_birth greater than '1990-01-01'

Person.objects.filter(date_of_birth__gte='1990-01-01') # get all records with date_of_birth greater than or equal to '1990-01-01'

Person.objects.filter(date_of_birth__lt='1990-01-01') # get all records with date_of_birth less than '1990-01-01'

Person.objects.filter(date_of_birth__lte='1990-01-01') # get all records with date_of_birth less than or equal to '1990-01-01'

Person.objects.filter(date_of_birth__range=('1990-01-01', '1990-12-31')) # get all records with date_of_birth in range '1990-01-01' to '1990-12-31'

Person.objects.filter(first_name__in=['John', 'Jane']) # get all records with first_name in ['John', 'Jane']

```

#### filter with multiple conditions

```python

# get all records with first_name = 'John' and last_name = 'Doe'  AND
Person.objects.filter(first_name='John', last_name='Doe')
Person.objects.filter(first_name='John').filter(last_name='Doe')

# get all records with first_name = 'John' or last_name = 'Doe'  OR
Person.objects.filter(Q(first_name='John') | Q(last_name='Doe'))  # from django.db.models import Q

```

#### exclude records

```python

# get all records with first_name != 'John'
Person.objects.exclude(first_name='John')
```

### Query modifiers:

#### order records

```python

# get all records ordered by date of birth

Person.objects.order_by('date_of_birth') # ascending order, default , gets oldest first
Person.objects.order_by('-date_of_birth') # descending order, gets youngest first

```

#### distinct records

```python

# get all distinct records

Person.objects.distinct()   # get all distinct records , compare all fields remaining before applying distinct

# distinct with specific field
Person.objects.distinct('first_name')   # get all distinct records with first_name

# distinct with order by

# distinct can not be used with order_by, if distinct field is not in order_by

Person.objects.order_by('first_name').distinct('first_name')   # get all distinct records with first_name and order by first_name

```

### Field selection:

#### select specific fields

```python

# get all records with only first_name and last_name fields

Person.objects.values('first_name', 'last_name')
# Returns a queryset with dictionaries instead of model instances, containing only specified field values.

```

#### select specific fields with list of dictionaries

```python

# get all records with only first_name and last_name fields

Person.objects.values_list('first_name', 'last_name')
#  Returns a queryset with tuples instead of model instances, containing only specified field values.
```

### Aggregation:

```python

# get count of all records

Person.objects.count()

from django.db.models import Sum, Avg, Max, Min

# get sum of all records

Person.objects.aggregate(Sum('age'))
```

### Slicing:

```python

# get first 10 records

Person.objects.all()[:10]
# in most cases pagination is used for slicing
```

### Prefetch:

#### Prefetching related objects: Use prefetch_related() to efficiently retrieve related objects in a separate query. it is used to reduce the number of database queries by fetching related objects in a single query rather than making separate queries for each related object. This can significantly improve performance, especially when dealing with many-to-many or reverse foreign key relationships.

```python

# get all records with related objects

Person.objects.all().prefetch_related('passport', 'address')
# here qs will contain all records with related passport and address objects if any relation is defined
```

### Bulk Operations:

```python

# bulk create records
instances = [Person(**data) for data in data_list]
Person.objects.bulk_create(instances)

# bulk update records

Person.objects.filter(last_name='Doe').update(last_name='Smith')

# bulk delete records

Person.objects.filter(last_name='Doe').delete()

```

### Annotate

#### annotate(): Adds annotations (extra data) to each object in the queryset based on related objects or aggregated values.

```python
# annotate age of all records using date_of_birth column

from django.db.models import F, ExpressionWrapper, fields
# F is used to reference a field value in the database, and ExpressionWrapper is used to perform arithmetic operations on fields.

Person.objects.annotate(
    age=ExpressionWrapper(
        fields.DateField(auto_now=True) - F('date_of_birth'),
        output_field=fields.IntegerField()
    )
)

```
