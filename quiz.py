import wx
from flashcardapp import FlashcardApp
from menu import MenuFrame

def main():
    app = wx.App(False)
    frame = Test(None, title='Test')
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()



