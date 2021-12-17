import nbimporter
import os
from HW1 import BSBIIndex, CompressedPostings

print("Testing BSBIIndex.")
BSBI_instance = BSBIIndex(data_dir='hw1dataraw', output_dir = 'index_dir', )
print("Building BSBIIndex ...")
BSBI_instance.index()
print("Done. Begin test cases ...")
for i in range(1, 9):
    with open('dev_queries/query.' + str(i)) as q:
        query = q.read()
        my_results = [os.path.normpath(path) for path in BSBI_instance.retrieve(query)]
        #print(my_results)
        with open('dev_output/' + str(i) + '.out') as o:
            reference_results = [os.path.normpath(x.strip()) for x in o.readlines()]
            assert not set(my_results)-set(reference_results), "Results DO NOT match for query: "+query.strip()
        print("Results match for query:", query.strip())
print("BSBIIndex test done.") 


print("Testing Compressed BSBIIndex.")
BSBI_instance_compressed = BSBIIndex(data_dir='hw1dataraw', output_dir='index_dir_compressed', postings_encoding=CompressedPostings)
print("Building BSBIIndex compressed...")
BSBI_instance_compressed.index()
print("Done. Begin test cases ...")
for i in range(1, 9):
    with open('dev_queries/query.' + str(i)) as q:
        query = q.read()
        my_results = [os.path.normpath(path) for path in BSBI_instance_compressed.retrieve(query)]
        with open('dev_output/' + str(i) + '.out') as o:
            reference_results = [os.path.normpath(x.strip()) for x in o.readlines()]
            assert not set(my_results)-set(reference_results), "Results DO NOT match for query: "+query.strip()
        print("Results match for query:", query.strip())
print("Compressed BSBIIndex test done.") 
