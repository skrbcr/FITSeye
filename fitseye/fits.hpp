#ifndef __FITS_HPP
#define __FITS_HPP

#include <string>
#include <string_view>
#include <exception>
#include <fitsio.h>

namespace skrbcr {
using std::string;
using std::string_view;
class FITS {
private:
    fitsfile *pInFile = nullptr;    // input fits file
    fitsfile *pFile = nullptr;   // temporary fits file
    string strInFilename = "";      // filename of input
    string strTmpFilename = "";     // filename of temporary
    int status = 0;                 // error status
    int nLenHdus = 0;               // length of hdus
    int nHdu = 0;                   // index of hdu
    int nTypeHdu = 0;               // type of hdu

public:
    // File routines
    FITS();
    FITS(string_view inFilename, string_view tmpFilename);
    void close() noexcept;
    // HDU routines
    int getLenHdus() const noexcept;
    int getHduIndex() const noexcept;
    void setHduIndex(const int i);
    int getHduType() const noexcept;
    // image hdu routines
    int getImgType() const;
    int getImgDim() const;
    // table hdu routines
    long getTabNumRows() const;
    int getTabNumCols() const;
    int getTabColNum() const;
    int getTabColType() const;
    void tabSelectRows(string_view expression);
    void getTabCols() const;
    void getTabSelCols() const;
    // header routines
    void getHduHeader(string_view records);

private:
    void checkError();
};
}

#endif  // __FITS_HPP
