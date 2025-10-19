from exa_py import Exa

exa = Exa(api_key="b24dc454-6bd7-4bd7-9871-daff3f5f90fc")

query = input("search here: ")

response = exa.search(
    query, 
    num_results=5,
    type='keyword'
)

#print(response)

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()