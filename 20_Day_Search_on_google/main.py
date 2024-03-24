# from googlesearch import search
#
# def google_search(query, num_results=10):
#     try:
#         search_results = search(query, num_results=num_results)
#         return search_results
#     except Exception as e:
#         return [f"Search error: {e}"]
#
# if __name__ == "__main__":
#     query = input("Enter your Google search query: ")
#     num_results = int(input("Enter the number of results to fetch: "))
#
#     search_results = google_search(query, num_results)
#
#     if search_results:
#         print("Search Results:")
#         for i, result in enumerate(search_results, start=1):
#             if i <= num_results:
#                 print(f"{i}. {result}")
#             else:
#                 break
#     else:
#         print("No results found.")

from googlesearch import search
import os

def google_image_search(query, num_results=10):
    try:
        # Perform Google search
        search_results = search(query, num_results=num_results)

        # Filter out image URLs based on file extensions
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
        image_urls = [url for url in search_results if os.path.splitext(url)[1].lower() in image_extensions]

        return image_urls
    except Exception as e:
        print(f"Search error: {e}")
        return []

if __name__ == "__main__":
    query = input("Enter your Google image search query: ")
    num_results = int(input("Enter the number of image results to fetch: "))

    image_urls = google_image_search(query, num_results)

    if image_urls:
        print("Image Results:")
        for i, url in enumerate(image_urls, start=1):
            print(f"{i}. {url}")
    else:
        print("No image results found.")
