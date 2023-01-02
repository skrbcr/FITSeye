#ifndef __BASE_HPP
#define __BASE_HPP
#include <string>
#include "global.hpp"
#include "fits.hpp"

using std::string;

namespace skrbcr {
class MyApp: public wxApp {
public:
    virtual bool OnInit();
};

// test class and will be deleted
class MyFrame: public wxFrame {
public:
    MyFrame(const wxChar *title, int xpos, int ypos, int width, int height);
    MyFrame(const wxChar *title, int width, int height);
    /* ~MyFrame(); */
};

class TopFrame: public wxFrame {
private:
    string strFilename = "";
    FITS fits = FITS();

    wxMenuBar *pMenubar;
    wxMenu *pMenuFile;
    wxMenu *pMenuHelp;

public:
    TopFrame();

    /* DECLARE_EVENT_TABLE() */
};

}
#endif	// __BASE_HPP
