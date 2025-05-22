import json
import os

class JsonlPipeline:
    def open_spider(self, spider):
        os.makedirs('output', exist_ok=True)
        self.file = open('output/python_qna.jsonl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
