import requests

# try:
    #  url = "https://the-trivia-api.com/api/questions"
    #  r = requests.get(url)
    # print("HTML:\n", r.text)
# except:
    # print("Invalid URL or some error occured while making the GET request to the specified URL")

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=multiple")
question_data = response.json()["results"]