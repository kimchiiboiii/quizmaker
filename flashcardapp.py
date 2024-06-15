from dialogs import DeckSelectionDialog
import wx

class Flashcard:
    def __init__(self, question, answer, label):
        self.question = question
        self.answer = answer
        self.label = label

class FlashcardApp(wx.Frame):
    def __init__(self, parent, title):
        super(FlashcardApp, self).__init__(parent, title=title, size=(400, 300))

        self.flashcards = []
        self.current_card = 0

        self.question_label = wx.StaticText(self, label="")
        self.answer_label = wx.StaticText(self, label="")
        self.answer_label.Hide()

        self.next_button = wx.Button(self, label="Next")
        self.next_button.Bind(wx.EVT_BUTTON, self.on_next)

        self.show_button = wx.Button(self, label="Show Answer")
        self.show_button.Bind(wx.EVT_BUTTON, self.on_show)

        self.shuffle_button = wx.Button(self, label="Shuffle")
        self.shuffle_button.Bind(wx.EVT_BUTTON, self.shuffle_cards)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.question_label, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 15)
        sizer.Add(self.answer_label, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 30)
        
        buttons_grid = wx.FlexGridSizer(3, 90, 0)
        buttons_grid.Add(self.next_button, 0, 15)
        buttons_grid.Add(self.show_button, 0, 15)
        buttons_grid.Add(self.shuffle_button, 0, 15)

        sizer.Add(buttons_grid, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 60)
        self.SetSizer(sizer)
        self.Layout()
        self.select_deck()
        # self.load_flashcards("quiz.txt")

    
    def select_deck(self):
        deckSelect = DeckSelectionDialog(self)
        if deckSelect.ShowModal() == wx.ID_OK:
            selectedDeck = deckSelect.getSelectedDeck()
        deckSelect.Destroy()

        if selectedDeck: # Ensure selectedDeck is not None
            self.load_flashcards(selectedDeck)
    
    
    
    def load_flashcards(self, filename: str) -> None:
        
        # Reads flashcard data from a file, parses the content, and stores the flashcards in a list.
    
    
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        self.flashcards = []
        line_index = 0
        while line_index < len(lines):
            if lines[line_index].strip() == "": # Once we hit an empty line, skip one line then continue loop
                line_index += 1
                continue
            
            # Checks if text matches the correct format
            # Format: 3 lines with "Question: ", "Answer: ", and "Label: "
            # followed by a blank line. 
            try: 
                if line_index + 2 < len(lines) and \
                all(": " in lines[count] for count in range(line_index, line_index + 3)):
                    
                    questions, answer, label = [line.strip().split(": ")[1] for line in lines[line_index:line_index + 3]]
                    self.flashcards.append(Flashcard(questions, answer, label))
                    line_index += 3

            except IndexError as ie:
                print(f"line_index out of range {line_index + 1}: {str(ie)}")
                line_index += 1
            except ValueError as ve:
                print(f"Invalid flashcard format at line {line_index + 1}: {str(ve)}")
                line_index += 1
            except Exception as e:
                print(f"Unexpected error at line {line_index + 1}: {str(e)}")
                line_index += 1

        if self.flashcards:
            self.show_flashcard()
        else:
            print("No flashcards found in the file")


    def show_flashcard(self):
        flashcard = self.flashcards[self.current_card]
        self.question_label.SetLabel(flashcard.question)
        self.answer_label.SetLabel(flashcard.answer)

    def on_show(self, event):
        if self.answer_label.IsShown():
            self.answer_label.Hide()
        else:
            self.answer_label.Show()
        self.Layout()

    def on_next(self, event):
        self.current_card += 1
        if self.current_card >= len(self.flashcards):
            self.current_card = 0
        
        self.answer_label.Hide()
        self.show_flashcard()
        self.Layout()

    def shuffle_cards(self, event):
        import random
        random.shuffle(self.flashcards)
        self.current_card = 0
        self.show_flashcard()
        self.Layout()