###############################################################################
# Name: _efactory.py                                                          #
# Purpose: Generic Factory Pattern implementation.                            #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2011 Cody Precord <staff@editra.org>                         #
# Licence: wxWindows Licence                                                  #
###############################################################################

"""
Editra Business Model Library: Factory

Provides base functionality for implementing class factories.

class FactoryMixin:
    
class Meta:
    - Don't use directly is used by classes that use the MetaData metaclass

class MetaData:
    - Meta data class - allows classes to be created with nested meta data
    dynamically.
    Example:
        class FooBar(object):
            __metaclass__ = MetaData
        class MyFoo(FooBar):
            class meta:
                name = 'MyFoo'

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__cvsid__ = "$Id: _efactory.py 70229 2012-01-01 01:27:10Z CJP $"
__revision__ = "$Revision: 70229 $"

__all__ = [ 'FactoryMixin', 'MetaData' ]

#-----------------------------------------------------------------------------#
# imports
import copy

#-----------------------------------------------------------------------------#

class Meta:
    """Metadata namespace, acts as a container object for meta attributes
    for classes using the FactoryMeta metaclass.
    @see: FactoryMeta

    """
    def __init__(self, cls, meta_attrs):
        assert hasattr(cls, 'GetMetaDefaults')
        for (attr,default) in cls.GetMetaDefaults().items():
            attr_val = meta_attrs.get(attr, default)
            setattr(self, attr, copy.copy(attr_val))

class MetaData(type):
    """Metaclass for applying meta data to a class"""
    def __new__(mcls,name,bases,attrs):
        cls = super(MetaData,mcls).__new__(mcls,name,bases,attrs)
        meta_attrs = { 'id' : None }
        if hasattr(cls, 'meta'):
            for attr in dir(cls.meta):
                if not attr.startswith("_"):
                    meta_attrs[attr] = getattr(cls.meta,attr)
        cls.meta = Meta(cls, meta_attrs)
        return cls

class FactoryMixin:
    """Factory implementation.
    All classes derived from classes using this mixin should declare a nested
    subclass 'meta' that has at least one member 'id' that is used to identify
    and instantiate the class in the factory.

    Example:
        class Foo(MyFactoryClass):
            class meta:
                id = 'foo'

    Any arbitrary identifier may be specified. Additional meta data attributes
    can be specified as well to suit the needs of the implementation. When
    adding additional meta data to a class it is necessary that the base class
    overrides the GetMetaDefaults method to return the appropriate default
    values for each supported meta field.

    Example:
        class meta:
            id = 'foo'
            size = 100

    In order to properly support the size meta field the factory base class must
    override GetMetaDefaults and return a dictionary object as follows.
    
    Example:
        \@classmethod
        def GetMetaDefaults(cls):
            return dict(id=None, size=0)

    """
    __metaclass__ = MetaData
    @classmethod
    def FactoryCreate(cls, identifier, *args, **kwargs):
        """Create an object of the appropriate type
        @param identifier: id value (see meta)
        @param args: Arguments to pass to object constructor
        @param kwargs: Keyword arguments to pass to object constructor
        @return: Subclass instance of cls or None if no appropriate constructor
                 is found in the factory.

        """
        obj = None
        for scls in cls.__subclasses__():
            if scls.meta.id == identifier:
                obj = scls(*args, **kwargs)
                break
        else:
            obj = cls(*args, **kwargs) # Return base class
        return obj

    @classmethod
    def GetMetaDefaults(cls):
        """Get all default meta values for this classes meta data.
        @return: dict(string=value,...)

        """
        return dict()
