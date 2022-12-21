#include "base.hpp"

IMPLEMENT_APP(skrbcr::MyApp);
DECLARE_APP(skrbcr::MyApp);

namespace skrbcr {
bool MyApp::OnInit() {
    wxFrame *frame = new MyFrame(wxT(""), 100, 100, 400, 300);
    frame->Show(true);
    SetTopWindow(frame);
    return true;
}

MyFrame::MyFrame(const wxChar *title, int xpos, int ypos, int width, int height) : wxFrame((wxFrame*)NULL, -1, title, wxPoint(xpos, ypos), wxSize(width, height)) {
    // Statusbar
    CreateStatusBar(3);
    SetStatusText(wxT("Ready"), 0);
}

}
