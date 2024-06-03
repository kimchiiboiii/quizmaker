import wx
from flashcardapp import FlashcardApp
from dialogs import NewFileDialogue

class MenuFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1080, 720))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        self.Centre()

        
        # Setting up the menu.
        filemenu = wx.Menu()
        editmenu = wx.Menu()
        load_item_id = wx.NewIdRef()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_NEW, "&New", " Create a new file")
        filemenu.Append(wx.ID_OPEN, "&Open", " Open a file")
        filemenu.Append(wx.ID_SAVE, "&Save", " Save a file")
        filemenu.Append(load_item_id, "&Load", " Load a flashcard file")
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

        # Set events.
        menuItem = wx.MenuItem(filemenu, wx.ID_ABOUT, "&About", " Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)
        menuItem2 = wx.MenuItem(filemenu, wx.ID_EXIT, "E&xit", " Terminate the program")
        self.Bind(wx.EVT_MENU, self.OnExit, menuItem2)
        menuItem3 = wx.MenuItem(filemenu, wx.ID_NEW, "&New", " Create a new file")
        self.Bind(wx.EVT_MENU, self.OnNew, menuItem3)
        self.Bind(wx.EVT_MENU, self.OnLoad, id=load_item_id)
        


    def OnNew(self, event):
        dlg = NewFileDialogue(self)
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