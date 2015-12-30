
import random
import json

from numpy import lil_matrix
from bidict import bidict

class Corpus:
    def __init__(self, filename):
        corpus_file = open(filename)
        corpus_data = json.load(corpus_file)
        corpus_file.close()

        if not corpus_data is dict:
            raise Exception("Invalid Corpus Format")

        num_keys = len(corpus_data)
        self.mapping = bidict()
        self.matrix = lil_matrix((num_keys,num_keys))

        highest_empty_index = 0

        for cur_key, cur_dict in corpus_data.items():

            if not cur_dict is dict:
                raise Exception("Invalid Corpus Format")

            if not cur_key in self.mapping:
                self.mapping[cur_key] = highest_empty_index
                highest_empty_index += 1
            
            start_index = self.mapping[cur_key]

            for target, probability in cur_dict:
                if not target in self.mapping:
                    self.mapping[target] = highest_empty_index
                    highest_empty_index += 1
                
                target_index = self.mapping[target]

                self.matrix[start_index, target_index] = probability


    def get_random_next(self, key):
        """Selects a random follower based on the key and the corpus probabilities"""
        start_index = self.mapping[key]
        coloumn = self.matrix.getrowview(start_index)
        nonzero_indices = coloumn.nonzero()[1]

        rand = random.random()

        for target_index in nonzero_indices:
            transition_prob = self.matrix[start_index,target_index]
            if transition_prob > rand:
                return self.mapping.inv(target_index)
            else:
                rand -= transition_prob

        #one should never land here
        raise Exception("Not enough possibilities for " + str(key)
