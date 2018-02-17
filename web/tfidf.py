import math
from textblob import TextBlob as tb

def tf(word, blob):
    return (float)(blob.words.count(word)) / (float)(len(blob.words))

def n_containing(word, bloblist):
    return (float)(sum(1 for blob in bloblist if word in blob))

def idf(word, bloblist):
    return (float)(math.log(len(bloblist)) / (float)(1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return (float)((float)(tf(word, blob)) * (float)(idf(word, bloblist)))

answer1 = """When data is stored on disk based storage devices it is stored as blocks of data. These blocks are accessed in their
 entirety making them the atomic disk access operation. Disk blocks are structured in much the same way as linked lists both contain a 
 section for data a pointer to the location of the next node (or block) and both need not be stored contiguously. Due to the fact that a 
 number of records can only be sorted on one field we can state that searching on a field that isnt sorted requires a Linear Search which 
 requires N/2 block accesses (on average) where N is the number of blocks that the table spans. If that field is a non-key field (i.e. 
 doesn't contain unique entries) then the entire table space must be searched at N block accesses. Whereas with a sorted field a Binary 
 Search may be used this has log2 N block accesses. Also since the data is sorted given a non-key field the rest of the table doesnt need to 
 be searched for duplicate values once a higher value is found. Thus the performance increase is substantial.Indexing is a way of sorting a 
 number of records on multiple fields. Creating an index on a field in a table creates another data structure which holds the field value, 
 and pointer to the record it relates to. This index structure is then sorted allowing Binary Searches to be performed on it. The downside to 
 indexing is that these indexes require additional space on the disk since the indexes are stored together in a table using the MyISAM engine 
 this file can quickly reach the size limits of the underlying file system if many fields within the same table are indexed. When should it 
 be used? Given that creating an index requires additional disk space (277778 blocks extra from the above example) and that too many indexes 
 can cause issues arising from the file systems size limits careful thought must be used to select the correct fields to index. Since indexes 
 are only used to speed up the searching for a matching field within the records it stands to reason that indexing fields used only for 
 output would be simply a waste of disk space and processing time when doing an insert or delete operation and thus should be avoided. Also 
 given the nature of a binary search the cardinality or uniqueness of the data is important. Indexing on a field with a cardinality of 2 
 would split the data in half whereas a cardinality of 1000 would return approximately 1000 records. With such a low cardinality the 
 effectiveness is reduced to a linear sort and the query optimizer will avoid using the index if the cardinality is less than 30% of the 
 record number effectively making the index a waste of space."""

document1 = tb(answer1.lower())

document2 = tb("""Python, from the Greek word is a genus of
nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
recognised.[2] A member of this genus, P. reticulatus, is among the longest
snakes known.""")

document3 = tb("""The Colt Python is a .357 Magnum caliber revolver formerly
manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
in 1955, the same year as Smith & Wesson's M29 .44 Magnum. The now discontinued
Colt Python targeted the premium revolver market segment. Some firearm
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
Thompson, Renee Smeets and Martin Dougherty have described the Python as the
finest production revolver ever made.""")

bloblist = [document1, document2, document3]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:100]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 10)))
