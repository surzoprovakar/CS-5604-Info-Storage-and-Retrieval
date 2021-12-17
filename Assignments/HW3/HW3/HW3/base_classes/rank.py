from collections import Counter
from collections import OrderedDict

class Rank:
    def score(self, query_dict, score_type, idf, params):
        
        """ Call this function to score and rank documents for some queries, 
            with a specified scoring function.
        Args:
            query_dict (dict) :  Mapping of Query-url-Document.
            score_type (str) : "baseline"  "cosine" "window" "extra"
            idf (dict) : term-idf dictionary
            params(dict) : parames for scorer
        Return 
            query_rankings (dict) : a mapping of queries to rankings
        """
        if score_type == "baseline": scorer = BaselineScorer(idf)
        elif score_type == "cosine": scorer = CosineSimilarityScorer(idf, query_dict, params)
        elif score_type == "window": scorer = SmallestWindowScorer(idf, query_dict, params)
        else: print("Wrong score type!")

        # loop through urls for query, getting scores
        query_rankings = {}
        for query in query_dict.keys():
            doc_and_scores = {}
            # rank the urls based on scores
            ### Begin your code
            
            for doc in query_dict[query].values():
                doc_and_scores[doc] = scorer.get_sim_score(query, doc)
                
            sorted_doc_and_scores = sorted(doc_and_scores.items(), key=lambda i: -i[1])
            query_rankings[query] = [j for j, _ in sorted_doc_and_scores]

            ### End your code
        
        return query_rankings
    
    def rank_with_score(self, input_dict):
        
        """ Call this function to accept dictionary with an ordered ranking of queries. 
        You will need to implement this function for the learning-to-rank ipython notebook. 
        Note that this function will likely replicate code from the score function above.
        Args:
            input_dict (dict) :  Mapping of Query-url-score.
        Return 
            query_rankings (dict) : An ordered dictionary of Query->url->score (ordering done for each query)
        
        """
        # loop through urls for query, getting scores
        query_rankings = {}
        for query in input_dict.keys():
            url_and_scores = {}
            # sort the urls based on scores
            ### Begin your code
            
            inputdict = input_dict[query].items();
            ordered_query = OrderedDict(sorted([(k,v) for k,v in inputdict], key=lambda i : -i[1]))
            query_rankings[query] = ordered_query

            ### End your code
        return query_rankings
    
    def write_ranking_to_file(self, query_rankings, ranked_result_file):
        with open(ranked_result_file, "w", encoding="utf-8") as f:
            for query in query_rankings.keys():
                f.write("query: "+ query.__str__() + "\n")
                for res in query_rankings[query]:
                
                    url_string = "  url: " + res.url + "\n" + \
                                "    title: " + res.title + "\n" +\
                                "    debug: " + "\n" 
                    
                    f.write(url_string)
                    
        print("Write ranking result to " + ranked_result_file + " sucessfully!")     
 
