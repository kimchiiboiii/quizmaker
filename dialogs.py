import wx

class NewFileDialogue(wx.Dialog):
    
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