# -*- coding: utf-8 -*-
from apiclient.discovery import build

from itertools import islice


class Youtube(object):
    def __init__(self):
        service_name = "youtube"
        api_version = "v3"
        developer_key = ""

        self.max_results = 50

        self.youtube = build(service_name, api_version, developerKey=developer_key)

        self.max_page = 3

        self.chunk = lambda ulist, step:  map(lambda i: ulist[i:i+step],  xrange(0, len(ulist), step))
        
    def _search(self, next_page_token, keyword, **options):
        all_results = []
        page_count = 0
        while next_page_token:
            page_count += 1
            # first time
            if next_page_token == True:
                results = self.youtube.search().list(type="video", part="id,snippet", maxResults=self.max_results,
                                                q=keyword).execute()
            else:
                results = self.youtube.search().list(type="video", part="id,snippet", maxResults=self.max_results,
                                                q=keyword, pageToken=next_page_token).execute()

            for items in results['items']:
                video_id = items['id']['videoId']
                if not video_id in all_results:
                    all_results.append(video_id)
            
            try:
                next_page_token = results['nextPageToken']
            except KeyError:
                return all_results

            if self.max_page <= page_count:
                return all_results

    def get_details(self, youtube_id_lists):
        data = {}
        try:
            youtube_id_lists = self.chunk(youtube_id_lists, self.max_results)
            for youtube_ids in youtube_id_lists:

                youtube_ids = ','.join(youtube_ids)
                results = self.youtube.videos().list(part='contentDetails,snippet', id=youtube_ids).execute()
                if not results.get('items'):
                    return []

                for detail in results['items']:
                    tags = detail['snippet'].get('tags') or []
                    
                    data[detail['id']] = {
                        'tags': tags,
                        'duration': detail['contentDetails']['duration'],
                        'title': detail['snippet']['title'],
                        'description': detail['snippet']['description'],
                    }
            return data
        except Exception as e:
            print e
            return False

    def search(self, keyword):
        result_video_ids = self._search(True, keyword)

        return self.get_details(result_video_ids)
