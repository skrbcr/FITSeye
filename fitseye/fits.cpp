#include "fits.hpp"
#include <algorithm>
#include <fitsio.h>
#include <iostream>
#include <longnam.h>
#include <string>

namespace skrbcr {
FITS::FITS() {
}
FITS::FITS(string_view inFilename, string_view tmpFilename) {
    strInFilename = inFilename;
    strTmpFilename = tmpFilename;
    fits_open_file(&pInFile, strInFilename.c_str(), READONLY, &status);
    checkError();
    fits_get_hdu_num(pInFile, &nHdu);
    checkError();
    fits_create_file(&pFile, strTmpFilename.c_str(), &status);
    checkError();
    for (int i = 1; status == 0; ++i) {
        if (fits_movabs_hdu(pInFile, i, nullptr, &status) == 0) {
            fits_copy_hdu(pInFile, pFile, 0, &status);
        }
    }
    fits_close_file(pInFile, &status);
    if (status == END_OF_FILE) {
        status = 0;
    }
    checkError();
    fits_get_num_hdus(pFile, &nLenHdus, &status);
    checkError();
    fits_movabs_hdu(pFile, nHdu, &nTypeHdu, &status);
}
void FITS::close() noexcept {
    fits_delete_file(pFile, &status);
}
int FITS::getLenHdus() const noexcept {
    return nLenHdus;
}
int FITS::getHduIndex() const noexcept {
    return nHdu;
}
void FITS::setHduIndex(const int i) {
    fits_movabs_hdu(pFile, i, &nTypeHdu, &status);
    checkError();
    nHdu = i;
}
int FITS::getHduType() const noexcept {
    return nTypeHdu;
}
int FITS::getImgDim() {
    int ndim;
    fits_get_img_dim(pFile, &ndim, &status);
    checkError();
    return ndim;
}
string FITS::getImgShape() {
    int ndim = getImgDim();
    if (ndim != 0) {
        vector<long> nsize(ndim);
        fits_get_img_size(pFile, ndim, &(nsize[0]), &status);
        string res = std::to_string(nsize[0]);
        std::for_each(nsize.begin() + 1, nsize.end(), [&res](const long s) {
            res += " x " + std::to_string(s);
        });
        checkError();
        return res;
    }
    else {
        return "0";
    }
}
void FITS::checkError() const {
    if (status > 0) {
        throw status;
    }
}
}
