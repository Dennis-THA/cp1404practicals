import wikipedia


def main():
    prompt = input(">>> ")
    while prompt != "":
        page = wikipedia.page(prompt, auto_suggest=False)
        print(page.title)
        print(page.url)
        try:
            page_summary = wikipedia.summary(prompt)
            print(page_summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)

        prompt = input(">>> ")
    print("Goodbye!")


main()
