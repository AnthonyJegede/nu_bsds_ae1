#This is the import libraries section
#These are necessary super classes for the subclasses 
#and function work properly.
import concurrent.futures
from collections import Counter

# Store an example text (the main document)inside a variable, 
# in this case, we call it - "main_doc"
main_doc = "My name is Anthony and Anthony is studying computer science. ... (main document)"

# Now we use the spliter function to split the main_doc 
# into two parts or pagesfor simpliicity
def splitter(text, num_pages):
    page_size = len(text) // num_pages
    pages = []
    start_idx = 0
    for _ in range(num_pages - 1):
        end_idx = start_idx + page_size
        if end_idx >= len(text):
            # In the event that end_idx > the length of text.
            pages.append(text[start_idx:])
            return pages
        while end_idx < len(text) and text[end_idx] != ' ':
            end_idx += 1
        pages.append(text[start_idx:end_idx])
        start_idx = end_idx + 1 if end_idx < len(text) and text[end_idx] == ' ' else end_idx
    pages.append(text[start_idx:])
    return pages


# Next, we use the Mapper function to create our bag of words
# i.e calculating how frequently each word occur in the txt or corpus.
def mapper(page):
    words = page.split()
    return Counter(words)

# This function (reducer function), brings together the counted words from the fragmented 
# text (pages) and creates a kind of summarisation.
def reducer(results):
    final_count = Counter()
    for count in results:
        final_count.update(count)
    return final_count
#This is the main function that runs when the program starts.
# Here, all the major functions are called to perform their 
# tasks in order,
def main():
    num_pages = 5   
    pages = splitter(main_doc, num_pages)

    # Map 
    with concurrent.futures.ThreadPoolExecutor() as executor:
        mapped_results = executor.map(mapper, pages)

    # Store the returned value of the reducer funtion 
    reduced_result = reducer(mapped_results)

    # Printing the bag of words
    print("Bag of words:") # This is the label
    print(reduced_result) # This is the actual result

if __name__ == "__main__":
    main()
 # main function gets called here if true.
    
