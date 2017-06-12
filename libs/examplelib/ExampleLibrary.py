# -*- coding: utf-8 -*-

class ExampleLibraryException(Exception):
    '''It is generally a good practice to throw library specific exceptions so
    that you know when the exception is coming from your code (as should) or
    something else is failing'''
    pass


class ExampleLibrary(object):
    '''Libraries should be documented as per Robot Framework User Guide'''

    def library_keyword(self):
        '''Document library's keywords as well'''
        return True

