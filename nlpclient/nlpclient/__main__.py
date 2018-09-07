
import client


def main():
    with client.NERClient('127.0.0.1', 9090) as nlp_client:
        extracted_entities = nlp_client.entities("ENG",
                                         "Hello there from over here.  Do you listen to the Beatles? the Beatles net worth exceeds 1 billion dollars")
        for entity in extracted_entities:
            print(entity)


if __name__ == "__main__":
    main()