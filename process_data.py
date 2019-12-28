from flask import request
from flask_restful import Resource
from collections import Counter
import json


class Video(Resource):

    def post(self):
        input_data = request.get_json(force=True)
        if not input_data:
            return {'message': 'No input data provided'}, 400
        size = len(input_data)
        vid_array = []
        pid_vid = []
        return_data = []
        for i in range(size):
            split_data = input_data[i]['request'].split(";")
            vid_array.append(split_data[3].split("=") + split_data[5].split("="))  # Will return a list containing vid, video_id, pid, Publisher_id
        for x in vid_array:
            pid_vid.append(x[3] + " : " + x[1])  # Extracting Publisher_id and Video_id from the given data
        ids = Counter(pid_vid).keys()
        views = list(Counter(pid_vid).values())
        i = 0
        for id in ids:
            tmp_array = id.split(":")
            return_data.append({
                "publisher_id": tmp_array[0],
                "video_id": tmp_array[1],
                "number_of_views": views[i],
            })
            i = i + 1
        return return_data

