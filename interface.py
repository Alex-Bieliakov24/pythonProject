class ConsoleInterface:
    """
    A class to manage the console-based user interface for the film search system.

    Provides methods for displaying search results, handling user input, and
    executing corresponding search functionalities.
    """

    def __init__(self, searcher):
        """
        Initializes the ConsoleInterface with a searcher object.

        Parameters:
            searcher: An instance of a searcher class that provides search functionalities.
        """
        self.searcher = searcher

    def display_results(self, results):
        """
        Displays the search results in the console.

        Parameters:
            results: A list of tuples containing the search results.

        Behavior:
            - If results are found, each result is printed on a new line.
            - If no results are found, a message "Nothing found." is displayed.
        """
        if results:
            for row in results:
                print(row)
        else:
            print("Nothing found.")

    def run(self):
        """
        Runs the main interactive console loop for the film search system.

        Behavior:
            - Displays a menu with available commands.
            - Handles user input for different operations:
                1. Search by keyword.
                2. Search by genre and year.
                3. Display the top 10 popular queries.
                4. Exit the program.
            - Executes the corresponding search methods and displays results.
            - Handles any exceptions during the execution and prints an error message.
        """
        print("Welcome to the Film Search System!")
        while True:
            # Display the menu
            print("\nAvailable commands:")
            print("1. Search by keyword")
            print("2. Search by genre and year")
            print("3. Top popular queries")
            print("4. Exit")
            choice = input("Enter the command number: ")

            try:
                if choice == "1":
                    # Search by keyword
                    keyword = input("Enter a keyword to search: ")
                    results = self.searcher.search_by_keyword(keyword)
                    self.display_results(results)
                elif choice == "2":
                    # Search by genre and year
                    genre = input("Enter the genre: ")
                    year = input("Enter the year: ")
                    results = self.searcher.search_by_genre_and_year(genre, year)
                    self.display_results(results)
                elif choice == "3":
                    # Display top queries
                    print("Top 10 popular queries:")
                    results = self.searcher.get_top_queries()
                    self.display_results(results)
                elif choice == "4":
                    # Exit the program
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    # Invalid input
                    print("Invalid input. Please try again.")
            except Exception as e:
                # Handle exceptions and print the error message
                print(f"An error occurred: {e}")
