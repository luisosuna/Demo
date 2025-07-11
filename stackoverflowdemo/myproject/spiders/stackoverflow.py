import scrapy
import requests
import html
from bs4 import BeautifulSoup

class StackoverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    allowed_domains = ["api.stackexchange.com"]
    start_urls = [
        "https://api.stackexchange.com/2.3/questions?order=desc&sort=votes&tagged=Python&site=stackoverflow&key=rl_7MDaPq5dVss5TykzTyAY4soTi&pagesize=100&key=rl_7MDaPq5dVss5TykzTyAY4soTi",
    ]

    def start_requests(self):
        # Make an API request to fetch questions
        for url in self.start_urls:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for question in data.get("items", []):
                    # Pass each question to the parse_answers method
                    yield scrapy.Request(
                        url=f"https://api.stackexchange.com/2.3/questions/{question['question_id']}/answers?order=desc&sort=votes&site=stackoverflow&key=rl_7MDaPq5dVss5TykzTyAY4soTi&pagesize=3",
                        callback=self.parse_answers,
                        meta={"question_data": question},
                    )

    def parse_answers(self, response):
        # Extract question data from the API response
        question_data = response.meta["question_data"]
        answers_data = response.json().get("items", [])

        # Extract answer IDs
        answers_ids = [answer["answer_id"] for answer in answers_data]

        # Make a request to fetch each answer's details
        for answer_id in answers_ids[:3]:
            yield scrapy.Request(
                url=f"https://api.stackexchange.com/2.3/answers/{answer_id}?order=desc&sort=votes&site=stackoverflow&filter=withbody&key=rl_7MDaPq5dVss5TykzTyAY4soTi",
                callback=self.collect_answers,
                meta={"question_data": question_data, "answer_id": answer_id},
            )

    def collect_answers(self, response):
        # Extract question data and answer ID from meta
        question_data = response.meta["question_data"]
        answer_id = response.meta["answer_id"]

        # Extract the answer details from the API response
        answer_data = response.json().get("items", [])[0]

        # Decode HTML entities in the answer body
        answer_data["body"] = html.unescape(answer_data["body"])
        # Use BeautifulSoup to clean the answer body
        soup = BeautifulSoup(answer_data["body"], "html.parser")
        answer_data["body"] = soup.get_text(separator="\n")
        # Clean the answer body further if needed
        answer_data["body"] = answer_data["body"].replace("\n", " ").strip()

        # Create the item with the question and answer details
        item = {
            "question": question_data["title"],
            "tags": question_data["tags"],
            "link": question_data["link"],
            "answer_count": question_data["answer_count"],
            "answers": {
                "id": answer_id,
                "body": answer_data["body"],
                "score": answer_data.get("score"), 
            },
        }
        yield item
