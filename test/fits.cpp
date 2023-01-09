#include <fitsio.h>
#include <iostream>
#include <gtest/gtest.h>
#include "../fitseye/fits.hpp"

using skrbcr::FITS;

/* Test for skrbcr::FITS class */

TEST(FITS, NORMAL) {
    FITS fits1;
    EXPECT_NO_THROW(fits1 = FITS("sample/WFPC2u5780205r_c0fx.fits", "sample/tmp.fits"));
    EXPECT_NO_THROW(fits1.close());
}
TEST(FITS, EXCEPTION) {
    EXPECT_ANY_THROW(FITS("sample/this_file_does_not_exist.fits", "sample/tmp.fits"));
}

class FITStest : public ::testing::Test {
protected:
    FITS fits1, fits2, fits3, fits4, fits5, fits6, fits7, fits8, fits9, fits10, fits11;
    virtual void SetUp() {
        fits1 = FITS("sample/DDTSUVDATA.fits", "sample/tmp1.fits");
        fits2 = FITS("sample/EUVEngc4151imgx.fits", "sample/tmp2.fits");
        fits3 = FITS("sample/FGSf64y0106m_a1f.fits", "sample/tmp3.fits");
        fits4 = FITS("sample/FOCx38i0101t_c0f.fits", "sample/tmp4.fits");
        fits5 = FITS("sample/FOSy19g0309t_c2f.fits", "sample/tmp5.fits");
        fits6 = FITS("sample/HRSz0yd020fm_c2f.fits", "sample/tmp6.fits");
        fits7 = FITS("sample/IUElwp25637mxlo.fits", "sample/tmp7.fits");
        fits8 = FITS("sample/NICMOSn4hk12010_mos.fits", "sample/tmp8.fits");
        fits9 = FITS("sample/UITfuv2582gc.fits", "sample/tmp9.fits");
        fits10 = FITS("sample/WFPC2ASSNu5780205bx.fits", "sample/tmp10.fits");
        fits11 = FITS("sample/WFPC2u5780205r_c0fx.fits", "sample/tmp11.fits");
    }
    virtual void TearDown() {
        fits1.close();
        fits2.close();
        fits3.close();
        fits4.close();
        fits5.close();
        fits6.close();
        fits7.close();
        fits8.close();
        fits9.close();
        fits10.close();
        fits11.close();
    }
};

TEST_F(FITStest, GETLENHDUS) {
    EXPECT_EQ(fits1.getLenHdus(), 2);
    EXPECT_EQ(fits2.getLenHdus(), 9);
    EXPECT_EQ(fits3.getLenHdus(), 2);
    EXPECT_EQ(fits4.getLenHdus(), 2);
    EXPECT_EQ(fits5.getLenHdus(), 2);
    EXPECT_EQ(fits6.getLenHdus(), 2);
    EXPECT_EQ(fits7.getLenHdus(), 2);
    EXPECT_EQ(fits8.getLenHdus(), 6);
    EXPECT_EQ(fits9.getLenHdus(), 1);
    EXPECT_EQ(fits10.getLenHdus(), 1);
    EXPECT_EQ(fits11.getLenHdus(), 2);
}
TEST_F(FITStest, HDUINDEX) {
    EXPECT_EQ(fits1.getHduIndex(), 1);
    EXPECT_NO_THROW(fits1.setHduIndex(2));
    EXPECT_EQ(fits1.getHduIndex(), 2);
    EXPECT_ANY_THROW(fits1.setHduIndex(3));
    EXPECT_EQ(fits1.getHduIndex(), 2);
    EXPECT_ANY_THROW(fits1.setHduIndex(0));
    EXPECT_EQ(fits1.getHduIndex(), 2);
}
TEST_F(FITStest, GETHDUTYPE) {
    EXPECT_EQ(fits1.getHduType(), IMAGE_HDU);
    fits1.setHduIndex(2);
    EXPECT_EQ(fits1.getHduType(), BINARY_TBL);
    fits3.setHduIndex(2);
    EXPECT_EQ(fits3.getHduType(), ASCII_TBL);
}
TEST_F(FITStest, GETIMGDIM) {
    EXPECT_EQ(fits1.getImgDim(), 6);
    fits1.setHduIndex(2);
    EXPECT_ANY_THROW(fits1.getImgDim());
    fits2.setHduIndex(2);
    EXPECT_EQ(fits2.getImgDim(), 2);
    fits2.setHduIndex(6);
    EXPECT_ANY_THROW(fits2.getImgDim());
    EXPECT_EQ(fits7.getImgDim(), 0);
    EXPECT_EQ(fits11.getImgDim(), 3);
}
TEST_F(FITStest, GETIMGSHAPE) {
    EXPECT_EQ(strcmp(fits1.getImgShape().c_str(), "0 x 3 x 4 x 1 x 1 x 1"), 0);
    fits1.setHduIndex(2);
    EXPECT_ANY_THROW(fits1.getImgShape());
    fits2.setHduIndex(2);
    EXPECT_EQ(strcmp(fits2.getImgShape().c_str(), "512 x 512"), 0);
    fits2.setHduIndex(3);
    EXPECT_EQ(strcmp(fits2.getImgShape().c_str(), "2048 x 300"), 0);
    fits2.setHduIndex(6);
    EXPECT_ANY_THROW(fits2.getImgShape().c_str());
    EXPECT_EQ(strcmp(fits7.getImgShape().c_str(), "0"), 0);
    EXPECT_EQ(strcmp(fits11.getImgShape().c_str(), "200 x 200 x 4"), 0);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
