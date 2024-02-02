import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer


dbpedia_data = pd.read_csv('dbpedia_data.csv')


def search_name(name:str) -> pd.DataFrame:
    """
    Search for a name in the dbpedia_data DataFrame

    Args:
        name (str): The name to search for

    Returns:
        pd.DataFrame: A DataFrame containing the search results
    """
    results = dbpedia_data[dbpedia_data['name'].str.contains(name)]
    
    return results

def find_similar_people(index:int) -> None:
    """
    Find similar people to a person in the dbpedia_data DataFrame

    Args:
        index (int): The index of the person in the DataFrame

    Returns:
        None: Prints the similar people and their similarity scores
    """
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(dbpedia_data['text'])
    
    k = 11
    knn = NearestNeighbors(n_neighbors=k, metric='cosine')
    knn.fit(tfidf_matrix)
    
    input_index = index
    input_name = dbpedia_data.iloc[input_index]['name']
    distances, indices = knn.kneighbors(tfidf_matrix[input_index], n_neighbors=k+1)
    
    related_indices = indices[0][1:]
    
    related_names = dbpedia_data.iloc[related_indices]['name']
    similarity_scores = 1 - distances[0][1:]
    
    print(f"Similar people to {input_name}:")
    
    for name, score in zip(related_names, similarity_scores):
        print(f"{name}: {score:.4f}")
        
    return None


    
   




 
    