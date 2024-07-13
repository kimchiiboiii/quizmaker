## Flashcard App (WIP)

Program is ran by running the quiz.py file. <br>
<br> App for creating and showing flashcards from a .txt file.

Project is made with wx.Python. <br>
- menu.py handles the toolbar in the main window. <br>
- quiz.py is the main/init file. <br>
- flashcardapp.py handles the functions and frames for the flashcard app. <br>
- dialogs.py contains the various dialogs used in menu.py and flashcardapp.py (DeckSelection and NewFile)


Flashcard deck must be a text file. <br>
The flashcard .txt file must follow this format:

Question: *"Your Question"* <br>
Answer: *"Your Answer"* <br>
Label: *"A tag that will be used to organize flashcards in the future."* <br>

### Instructions
Create new flashcards: <br>
File > New > Load Existing Deck - to add new flashcards to an already existing deck <br>
File > New > Create a New Deck - to create a new flashcard deck .txt file in the current directory <br>
<br>
Load and use flashcard deck: <br>
File > Load > Load Existing Deck - load a flashcard deck then display it
File > Load > Create a New Deck - **WIP** currently it just does the same thing as "File > New > Create a New Deck" will change soon.
