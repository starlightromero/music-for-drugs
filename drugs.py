"""Import webdriver and sleep."""
from selenium import webdriver
from time import sleep


class YoutubeBot:
    """Bot which accesses YouTube playlists."""

    def __init__(self):
        """Initilize YoutubeBot."""

    def weed(self):
        """Access weed playlist."""
        print(
            "{:-^80}\n".format(
                "We appologize. Weed is currently unavailable."
            ).upper()
        )

    def mushrooms(self):
        """Access mushrooms playlist."""
        self.driver = webdriver.Chrome()
        self.driver.get(
            "https://www.youtube.com/playlist?list=PLhaBYjOdLf6VYXiFsmPYJR4yvR30LbIbB"
        )

    def acid(self):
        """Access acid playlist."""
        self.driver = webdriver.Chrome()
        self.driver.get(
            "https://www.youtube.com/playlist?list=PLhaBYjOdLf6UMD3z8ekHUk9Hmigtj8ix7"
        )
        sleep(2)

    def ecstasy(self):
        """Access ecstasy playlist."""
        self.driver = webdriver.Chrome()
        self.driver.get(
            "https://www.youtube.com/playlist?list=PLhaBYjOdLf6UHZA7h2drxHNOA9fxe5sTH"
        )

    def coke(self):
        """Access coke playlist."""
        self.driver = webdriver.Chrome()
        self.driver.get(
            "https://www.youtube.com/playlist?list=PLhaBYjOdLf6XU1AI2MJY-jgWJCyZd4BTd"
        )

    def speed(self):
        """Access speed playlist."""
        print(
            "{:-^80}\n".format(
                "We appologize. Speed is currently unavailable."
            ).upper()
        )

    def play(self):
        """Play YouTube playlist."""
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@aria-label='Shuffle play']"
        ).click()


class Display:
    """User interface methods."""

    def get_user_input(self):
        """Get user input."""
        print("{:-^80}".format("What is your drug of choice?").upper())
        print("1: Weed")
        print("2: Mushrooms")
        print("3: Acid")
        print("4: Ecstasy")
        print("5: Coke")
        print("6: Speed")
        print("q: Quit")
        return input("Your selection: ")

    @staticmethod
    def wait():
        """Print after a user selction has been made."""
        print(
            "{:-^80}\n".format(
                "Please wait while your drug is administered"
            ).upper()
        )
        sleep(1)

    @staticmethod
    def unavailable():
        """Print for unavailable user input."""
        print(
            "{:-^80}\n".format(
                "The drug you picked is still under experimental research."
            ).upper()
        )

    @staticmethod
    def farewell():
        """Print for exiting the user interface."""
        print(
            "{:-^80}\n".format(
                "Thank you for choosing us as your drug provider."
            ).upper()
        )

    def listen_for_input(self):
        """Process user input."""
        waiting_for_input = True
        while waiting_for_input:
            user_input = self.get_user_input()
            self.wait()
            bot = YoutubeBot()
            if user_input == "1":
                bot.weed()
            elif user_input == "2":
                bot.mushrooms()
                bot.play()
            elif user_input == "3":
                bot.acid()
                bot.play()
            elif user_input == "4":
                bot.ecstasy()
                bot.play()
            elif user_input == "5":
                bot.coke()
                bot.play()
            elif user_input == "6":
                bot.speed()
            elif user_input == "q":
                print(
                    "{:-^80}\n".format(
                        "No drugs have been administered."
                    ).upper()
                )
                waiting_for_input = False
            else:
                self.unavailable()
        else:
            self.farewell()


display = Display()
display.listen_for_input()
