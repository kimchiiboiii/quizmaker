import wx
import wx.aui
from flashcardapp import FlashcardApp
from dialogs import NewFileDialogue, DeckSelectionDialog

class Frame1(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 720))

class Frame2(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(540, 720))


class MenuFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1080, 720))
        # frame1 = Frame1(self, "Frame 1")
        # frame2 = Frame2(self, "Frame 2")
        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.mgr = wx.aui.AuiManager(self)
        self.CreateStatusBar()
        self.Centre()
        self.createPane()

        
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
        deckSelect = DeckSelectionDialog(self)
        selectedDeck = (deckSelect.getSelectedDeck() if 
                        deckSelect.ShowModal() == wx.ID_OK else None)  
        deckSelect.Destroy()
        
        if not selectedDeck: # If user does not select a deck, simply return.
            return
        nfdialogue = NewFileDialogue(self, selectedDeck)
        nfdialogue.ShowModal()
        nfdialogue.Destroy()
    
    def OnAbout(self, event):
        nfdialogue = wx.MessageDialog(self, "A quiz maker.", "About Quiz Maker", wx.OK)
        nfdialogue.ShowModal()
        nfdialogue.Destroy()

    def OnExit(self, event):
        self.Close(True)

    def OnLoad(self, event):
        self.flashcard_app = FlashcardApp(None, "Flashcards")
        self.flashcard_app.SetPosition(wx.Point(900, 400))
        self.flashcard_app.Show(True)

    def createPane(self):
        text1 = wx.TextCtrl(self)
        self.mgr.AddPane(text1, wx.aui.AuiPaneInfo().Bottom().BestSize(
            wx.Size(200, 200)))
        self.mgr.Update()