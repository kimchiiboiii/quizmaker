import wx
from menu import MenuFrame

def main():
    app = wx.App(False)
    frame = MenuFrame(None, title='Test')
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()


# COMPLETE ------------------------------------------------------------------------------------
# TODO: Trouble with selecting and loading decks.
# Both New and Load are opening to the Select or Create Deck dialog.
# You also cannot create new decks...
# When you try in the New tab, you go through the motions but it doesn't save it
# When you try in Load, it says "No such file or directory:" because the function only reads.
# COMPLETE ------------------------------------------------------------------------------------

