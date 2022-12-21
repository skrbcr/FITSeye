#ifndef __BASE_HPP
#define __BASE_HPP
#include <wx-3.2/wx/wxprec.h>
#ifndef WX_PRECOMP
    #include <wx-3.2/wx/wx.h>
#endif

namespace skrbcr {
class MyApp: public wxApp {
public:
    virtual bool OnInit();
};

class MyFrame: public wxFrame {
public:
    MyFrame(const wxChar *title, int xpos, int ypos, int width, int height);
    /* ~MyFrame(); */
};

}
#endif	// __BASE_HPP
