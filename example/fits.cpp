#include <iostream>
#include "../fitseye/fits.hpp"

using std::cout;
using std::endl;
/* using std::cerr; */
using skrbcr::FITS;

int main() {
    FITS fits;
    try {
        fits = FITS("sample/WFPC2u5780205r_c0fx.fits", "tmp1.fits");
        /* FITS fits1 = FITS("~/seminar/a.fits", "./tmp1.fits"); */
        /* FITS fits2 = FITS(); */
        int lenHdus = fits.getLenHdus();
        cout << lenHdus << endl;
        fits.setHduIndex(5);
    }
    catch (int& e) {
        fits_report_error(stdout, e);
        fits.close();
    }
    return 0;
}
