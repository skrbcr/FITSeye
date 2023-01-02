#include "base.hpp"

IMPLEMENT_APP(skrbcr::MyApp);
DECLARE_APP(skrbcr::MyApp);

namespace skrbcr {
bool MyApp::OnInit() {
    wxFrame *frame = new TopFrame();
    frame->Show(true);
    SetTopWindow(frame);
    return true;
}

MyFrame::MyFrame(const wxChar *title, int xpos, int ypos, int width, int height) : wxFrame((wxFrame*)NULL, -1, title, wxPoint(xpos, ypos), wxSize(width, height)) {
}
MyFrame::MyFrame(const wxChar *title, int width, int height) : wxFrame((wxFrame*)NULL, -1, title, wxDefaultPosition, wxSize(width, height)) {
}

TopFrame::TopFrame(): wxFrame(nullptr, -1, STRSOFTNAME, wxDefaultPosition, wxSize(800, 300)) {
    // Menubar
    pMenubar = new wxMenuBar();
    pMenuFile = new wxMenu();
    pMenuFile->Append(wxID_OPEN, _T("&Open FITS File..."), _T("Open FITS File with new window"));
    pMenuFile->Append(wxID_SAVE, _T("&Save FITS File"), _T("Overwrite FITS file"));
    pMenuFile->Append(wxID_SAVEAS, _T("Save FITS File &As..."), _T("Save FITS file with a different file name"));
    pMenuFile->AppendSeparator();
    pMenuFile->Append(wxID_EXIT, _T("&Quit"));
    pMenubar->Append(pMenuFile, _T("&File"));
    pMenuHelp = new wxMenu();
    pMenuHelp->Append(wxID_HELP_CONTENTS, _T("&Help"), _T("Show Help"));
    pMenuHelp->Append(wxID_ABOUT, _T("&About"));
    pMenubar->Append(pMenuHelp, _T("&Help"));
    SetMenuBar(pMenubar);
    CreateStatusBar(2);
    /* SetStatusText(wxT("Ready"), 0); */
}

}
