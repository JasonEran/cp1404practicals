# wiki.py
import wikipedia


def get_page_details():
    while True:
        # Prompt user for input
        search_term = input("Enter a page title or search phrase (or press Enter to quit): ").strip()

        # Check for blank input to exit
        if not search_term:
            print("Exiting program.")
            break

        try:
            # Get the page with autosuggest disabled to avoid unexpected suggestions
            page = wikipedia.page(search_term, auto_suggest=False)

            # Print page details
            print("\nPage Title:", page.title)
            print("Summary (first 200 characters):", wikipedia.summary(search_term, sentences=2)[:200] + "...")
            print("URL:", page.url)
            print("-" * 50)

        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation error (e.g., "Python" may refer to multiple topics)
            print(f"\nError: '{search_term}' is ambiguous. Possible options include:")
            for option in e.options[:5]:  # Limit to first 5 options for brevity
                print(f"- {option}")
            print("Please be more specific.")
            print("-" * 50)

        except wikipedia.exceptions.PageError:
            # Handle page not found error (e.g., "jcu" may not exist)
            print(f"\nError: No page found for '{search_term}'.")
            print("Please try a different title or search phrase.")
            print("-" * 50)

        except Exception as e:
            # Handle any other unexpected errors
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("-" * 50)


if __name__ == "__main__":
    get_page_details()