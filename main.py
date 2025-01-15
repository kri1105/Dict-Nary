import requests

class Dictnary:
    base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def __init__(self):
        pass
    
    def get_json(self, word):
        """FETCHES THE DATA AND CONVERTS TO JSON FROM THE API
        """
        try:
            response = requests.get(self.base_url + word)
            data = response.json()
            return data
        except Exception as err:
            return None

    def get_meaning(self, data):
        """RETURNS THE MEANING OF THE WORD
        """
        if data:
            try:
                print(f"Word: {data[0]['word']}")
                for meaning in data[0]['meanings']:
                    part_of_speech = meaning['partOfSpeech']
                    print(f"\nPart of Speech: {part_of_speech}")
                    for definition in meaning['definitions']:
                        print(f" - Definition: {definition['definition']}")
                        if 'example' in definition:
                            print(f"   Example: {definition['example']}")
            except (KeyError, IndexError):
                print("Unexpected data format received from the API.")
        else:
            print("No definition found for the word.")

    def run(self):
        """RUNS THE APP, DISPLAYS THE MEANING OF THE WORD
        """
        while True:
            word = input("Enter the word('exit':to exit):").strip()
            if word.lower() == "exit":
                print("Bbyee !!")
                break
            data = self.get_json(word)  
            self.get_meaning(data)      

if __name__ == '__main__':
    app = Dictnary()
    app.run()