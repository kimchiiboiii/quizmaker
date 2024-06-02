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
        self.next_button = wx.Button(self, label="Next")
        self.next_button.Bind(wx.EVT_BUTTON, self.on_next)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.question_label, 0, wx.ALL, 5)
        sizer.Add(self.answer_label, 0, wx.ALL, 5)
        sizer.Add(self.next_button, 0, wx.ALL, 5)

        self.SetSizer(sizer)
        self.Layout()

        self.load_flashcards("quiz.txt")

    def load_flashcards(self, filename):
        with open(filename, "r") as file:
            for line in file:
                question, answer, label = line.strip().split("\t")
                self.flashcards.append(Flashcard(question, answer, label))

        self.show_flashcard()

    def show_flashcard(self):
        print(f"Number of flashcards: {len(self.flashcards)}")
        print (f"Current card index: {self.current_card}")
        flashcard = self.flashcards[self.current_card]
        # self.question_label.SetLabel(flashcard.question)
        # self.answer_label.SetLabel(flashcard.answer)

    def on_next(self, event):
        self.current_card += 1
        if self.current_card >= len(self.flashcards):
            self.current_card = 0
        self.show_flashcard()

    def load_flashcards(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        self.flashcards = []
        i = 0
        while i < len(lines):
            if lines[i].strip() == "":
                i += 1
            # Check if there are at lesat 3 more lines andd they contain ": "
            elif i+2 < len(lines) and ": " in lines[i] and ": " in lines[i+1] and ": " in lines[i+2]:
                questions = lines[i].strip().split(": ")[1]
                answer = lines[i+1].strip().split(": ")[1]
                label = lines[i+2].strip().split(": ")[1]
                self.flashcards.append(Flashcard(questions, answer, label))
                i += 3

            else:
                # If the lines are not in the correct format, skip them
                i += 1

        if self.flashcards:
            self.show_flashcard()
        else:
            print("No flashcards found in the file")


    def show_flashcard(self):
        flashcard = self.flashcards[self.current_card]
        self.question_label.SetLabel(flashcard.question)
        self.answer_label.SetLabel(flashcard.answer)

    def on_next(self, event):
        self.current_card += 1
        if self.current_card >= len(self.flashcards):
            self.current_card = 0
        self.show_flashcard()


class MyDialog(wx.Dialog):
    
    # A custom dialog class for creating a new file.
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "New File", size=(300, 250))

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Create labels
        self.label1 = wx.StaticText(self, label="Question:")
        self.label2 = wx.StaticText(self, label="Answer:")
        self.label3 = wx.StaticText(self, label="Label 3")
        

        self.text1 = wx.TextCtrl(self, value="")
        self.text2 = wx.TextCtrl(self, value="")
        self.text3 = wx.TextCtrl(self, value="")

        self.sizer.Add(self.label1, 0, wx.ALL, 5)
        self.sizer.Add(self.text1, 0, wx.ALL, 5)
        self.sizer.Add(self.label2, 0, wx.ALL, 5)
        self.sizer.Add(self.text2, 0, wx.ALL, 5)
        self.sizer.Add(self.label3, 0, wx.ALL, 5)
        self.sizer.Add(self.text3, 0, wx.ALL, 5)

        # Create submit button
        self.submitButton = wx.Button(self, label="Submit")
        self.sizer.Add(self.submitButton, 0, wx.ALL, 5)
        
        # Bind the submit button to the event handler
        self.submitButton.Bind(wx.EVT_BUTTON, self.OnSubmit)
        
        self.SetSizer(self.sizer)

        

    def OnSubmit(self, event):
        # Get the values from the text fields
        question = self.text1.GetValue()
        answer = self.text2.GetValue()
        label = self.text3.GetValue()

        # Print the values to the console
        with open("quiz.txt", "a") as file:
            file.write("\n")
            file.write(f"Question: {question}\n")
            file.write(f"Answer: {answer}\n")
            file.write(f"Label: {label}\n")
            

        # Close the dialog
        self.Close()

class Test(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1080, 720))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        self.Centre()

        
        # Setting up the menu.
        filemenu = wx.Menu()
        editmenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_NEW, "&New", " Create a new file")
        filemenu.Append(wx.ID_OPEN, "&Open", " Open a file")
        filemenu.Append(wx.ID_SAVE, "&Save", " Save a file")
        filemenu.Append(wx.ID_SAVEAS, "&Save As", " Save a file with a different name")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")
        
        editmenu.Append(wx.ID_UNDO  , "Undo", "Undo last action")
        

        
        
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(editmenu, "&Edit")
        self.SetMenuBar(menuBar) # Adding the MenuBar to the Frame content.
        self.Show(True)

        # Add Load menu item
        load_item_id = wx.NewIdRef()
        filemenu.Append(load_item_id, "&Load", " Load a flashcard file")
        self.Bind(wx.EVT_MENU, self.OnLoad, id=load_item_id)

        # Set events.
        menuItem = wx.MenuItem(filemenu, wx.ID_ABOUT, "&About", " Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)
        menuItem2 = wx.MenuItem(filemenu, wx.ID_EXIT, "E&xit", " Terminate the program")
        self.Bind(wx.EVT_MENU, self.OnExit, menuItem2)
        menuItem3 = wx.MenuItem(filemenu, wx.ID_NEW, "&New", " Create a new file")
        self.Bind(wx.EVT_MENU, self.OnNew, menuItem3)
        


    def OnNew(self, event):
        dlg = MyDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
    
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "A quiz maker.", "About Quiz Maker", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True)

    def OnLoad(self, event):
        self.flashcard_app = FlashcardApp(None, "Flashcards")
        self.flashcard_app.Show(True)

def main():
    app = wx.App(False)
    frame = Test(None, title='Test')
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()



