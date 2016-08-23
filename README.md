# Youtube Search API #
## Requirements Installation

    pip install --upgrade google-api-python-client

## Usage ##
    from youtube import Youtube
    youtube = Youtube()
    results = youtube.search('keyword')

## Settings ##

    11. developer_key = "<your developer key>'
    ...
    13.  self.max_results = <result per page>
    ---
    17. self.max_page = <number of pages>

----------


### TODO ###
- example project (flask or django)
- other search parameters (e.g. category, published date)
