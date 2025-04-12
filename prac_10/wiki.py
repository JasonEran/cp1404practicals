import wikipedia


def get_page_details():
    while True:
        search_term = input("Enter a Wikipedia page title or search phrase (or press Enter to quit): ").strip()

        # Check if the input is empty to exit
        if not search_term:
            print("Exiting program.")
            break

        # Get page, disable automatic suggestions
        page = wikipedia.page(search_term, autosuggest=False)

        print("\nPage Details:")
        print(f"Title: {page.title}")
        print(f"Summary: {wikipedia.summary(search_term, sentences=2)[:200]}...")
        print(f"URL: {page.url}\n")


if __name__ == "__main__":
    get_page_details()