import wx
from app import MainFrame


if __name__ == "__main__":

    app = wx.App()
    MainFrame(title="Reddit", parent=None, id=-1)
    app.MainLoop()
