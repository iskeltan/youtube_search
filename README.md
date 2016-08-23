# Youtube Search API #
## Requirements Installation

    pip install --r requirements.txt

## Usage ##
    from youtube import Youtube
    youtube = Youtube()
    results = youtube.search('keyword')

## Flask
    cd example_project/
    python example.py

## Settings ##

    11. developer_key = "<your developer key>'
    ...
    13.  self.max_results = <result per page>
    ---
    17. self.max_page = <number of pages>

----------


### TODO ###
- other search parameters (e.g. category, published date)
