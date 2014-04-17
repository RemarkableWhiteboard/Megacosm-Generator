
import random
import json
from generators.Generator import Generator
from util import Filters
import logging



class Street(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)
        self.logger=logging.getLogger(__name__)
        if 'trailer' not in self.name:
            self.name['trailer']=self.kind
            self.name['full']+=" "+self.kind

        self.name['full']= self.name['full'].title()

