from db import DatabaseManager
from search import FilmSearcher
from interface import ConsoleInterface


#Main entry point of the application.
if __name__ == "__main__":
    # Initialize the database manager for connecting and interacting with the database.
    db_manager = DatabaseManager()

    # Create an instance of FilmSearcher for performing search operations.
    searcher = FilmSearcher(db_manager)

    # Create an instance of ConsoleInterface for interacting with the user.
    interface = ConsoleInterface(searcher)

    try:
        # Start the console interface for user interaction.
        interface.run()
    finally:
        # Ensure the database connection is closed properly when the program exits.
        db_manager.close()
