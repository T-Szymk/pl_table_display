import bs4, requests


#url = "http://www.livefootball.com/football/england/premier-league/live/"
url = "http://www.livefootball.com/football/intl/club-friendlies/live/"
html_output_file_name = "live_results.html"

# get web page html
url_get_result = requests.get(url)
try:
	url_get_result.raise_for_status()
except Exception as e:
	print(f'There was an issue with the get: {e}')
	exit()

# write html to file
with open(html_output_file_name, 'wb') as file:
	for byte_chunk in url_get_result.iter_content(100000):
		file.write(byte_chunk)

# create bs4 object for parsing
soup = bs4.BeautifulSoup( open(html_output_file_name), 'html.parser')
tag = soup.select('div[id="sdLr"]') # returns full table with all data

if tag:
	print(tag[0].get_text())