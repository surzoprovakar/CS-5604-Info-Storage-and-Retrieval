import pickle as pkl
import math
class Idf:
    """Build idf dictionary and return idf of a term, whether in or not in built dictionary.
        Recall from HW1 that postings_dict maps termID to a 3 tuple of 
        (start_position_in_index_file, number_of_postings_in_list, length_in_bytes_of_postings_list)
        
        Remember that it's possible for a term to not appear in the collection corpus.
        Thus to guard against such a case, we will apply Laplace add-one smoothing.
        
        Note: We expect you to store the idf as {term: idf} and handle term which is not in posting_list

        Hint: For term not in built dictionary, we should return math.log10(total_doc_num / 1.0).
    """
    def __init__(self):
        """Build an idf dictionary"""
        try:
            # We provide docs.dict, terms.dict and BSBI.dict
            with open("data/docs.dict", 'rb') as f:
                docs = pkl.load(f)
            self.total_doc_num = len(docs)
            print("Total Number of Docs is", self.total_doc_num)

            with open("data/terms.dict", 'rb') as f:
                terms = pkl.load(f)
            self.total_term_num = len(terms)
            print("Total Number of Terms is", self.total_term_num)

            with open('data/BSBI.dict', 'rb') as f:
                postings_dict, termsID = pkl.load(f)

            self.idf = {}

            ### Begin your code
            
            nums = self.total_term_num
            for i in range (nums):
                idf = math.log10(self.total_doc_num/postings_dict[i][1])
                self.idf[terms[i]] = idf
            print(self.idf)
            
            ### End your code
        except FileNotFoundError:
            print("doc_dict_file / term_dict_file Not Found!")

    def get_idf(self, term = None):
        """Return idf of return idf of a term, whether in or not in built dictionary.
        Args:
            term(str) : term to return its idf
        Return(float): 
            idf of the term
        """
        ### Begin your code
        
        if term in self.idf:
            return self.idf[term]
        else:
            return math.log10(self.total_doc_num)
        
        ### End your code
