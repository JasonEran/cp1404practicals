# wiki.py
import wikipedia


def get_page_details():
    """Retrieve page details from Wikipedia"""
    while True:
        # Prompt user for input
        search_term = input("Enter page title: ").strip()

        # Check for blank input to exit
        if not search_term:
            print("Thank you.")
            break

        try:
            # Get the page with autosuggest disabled to avoid unexpected suggestions
            page = wikipedia.page(search_term, auto_suggest=False)

            # Print page details: title, full summary, and URL
            print(page.title)
            print(wikipedia.summary(search_term))
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation error (e.g., "python")
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)  # Print the list of options as shown in sample

        except wikipedia.exceptions.PageError:
            # Handle page not found error (e.g., "jcu")
            print(f'Page id "{search_term}" does not match any pages. Try another id!')

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    get_page_details()