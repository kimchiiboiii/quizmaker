import wx

# COMPLETE ------------------------------------------------------------------------------------
# TODO: Allow different card decks to be created and saved.
# Probably will need a new window to select the deck
# Will need a way to write to the correct deck file
# COMPLETE ------------------------------------------------------------------------------------

class NewFileDialogue(wx.Dialog):
    
    # A custom dialog class for creating a new file.
    def __init__(self, parent, selectedDeck):
        super().__init__(parent, title="New Flashcard")
        self.selectedDeck = selectedDeck # Get the selected deck from DeckSelectionDialogue
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

        # Write the values to the file
        try:
            with open(self.selectedDeck, "a") as file:
                file.write("\n")
                file.write(f"Question: {question}\n")
                file.write(f"Answer: {answer}\n")
                file.write(f"Label: {label}\n")
            wx.MessageBox("Flashcard created successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.MessageBox(f"An error occurred: {e}", "Error", wx.OK | wx.ICON_ERROR)
        
        # Clear the text fields
        self.text1.SetValue("")
        self.text2.SetValue("")
        self.text3.SetValue("")
        self.text1.SetFocus()
        # Close the dialog
        # self.Close()

class DeckSelectionDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Select or Create Deck")
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Option to select an existing deck
        self.loadButton = wx.Button(self, label="Load Existing Deck")
        self.sizer.Add(self.loadButton, 0, wx.ALL, 5)
        self.loadButton.Bind(wx.EVT_BUTTON, self.onLoadDeck)
        
        # Option to create a new deck
        self.createButton = wx.Button(self, label="Create New Deck")
        self.sizer.Add(self.createButton, 0, wx.ALL, 5)
        self.createButton.Bind(wx.EVT_BUTTON, self.onCreateDeck)
        
        self.SetSizer(self.sizer)
        self.selectedDeck = None

    def onLoadDeck(self, event):
        with wx.FileDialog(self, "Select deck file", wildcard="Text files (*.txt)|*.txt",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.selectedDeck = fileDialog.GetPath()
        self.EndModal(wx.ID_OK)

    def onCreateDeck(self, event):
        with wx.TextEntryDialog(self, "Enter name for new deck:", "Create New Deck") as textDialog:
            if textDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.selectedDeck = textDialog.GetValue() + ".txt"
            with open (self.selectedDeck, "a") as file: 
                pass  # Deck file is created if it doesn't exist and if it does exist, is just left open for appending
        
        newFileDialo = NewFileDialogue(self, self.selectedDeck)
        newFileDialo.ShowModal()
        # self.NewFileDialogue(self.selectedDeck)
        self.EndModal(wx.ID_OK)

    def getSelectedDeck(self):
        return self.selectedDeck