/* -*- c -*- */
/*****************************************************************************/
/*  LibreDWG - free implementation of the DWG file format                    */
/*                                                                           */
/*  Copyright (C) 2018 Free Software Foundation, Inc.                        */
/*                                                                           */
/*  This library is free software, licensed under the terms of the GNU       */
/*  General Public License as published by the Free Software Foundation,     */
/*  either version 3 of the License, or (at your option) any later version.  */
/*  You should have received a copy of the GNU General Public License        */
/*  along with this program.  If not, see <http://www.gnu.org/licenses/>.    */
/*****************************************************************************/

/*
 * auxheader.spec: DWG file header specification
 * written by Reini Urban
 */

#include "spec.h"

  SINCE(R_2000) {
    IF_ENCODE_FROM_EARLIER {
      BITCODE_RS tmpunknown[] = {5, 0x893, 5, 0x893, 0, 1, 0, 0, 0, 0};
      FIELD_VALUE(aux_intro[0]) = 0xff;
      FIELD_VALUE(aux_intro[1]) = 0x77;
      FIELD_VALUE(aux_intro[2]) = 0x01;
      FIELD_VALUE(minus_1) = -1;
      FIELD_VALUE(dwg_version) = dwg->header.dwg_version;
      FIELD_VALUE(maint_version) = dwg->header.maint_version;
      memcpy(FIELD_VALUE(unknown),tmpunknown,sizeof(tmpunknown));
      FIELD_VALUE(TDCREATE_JULIAN_DAY)   = dwg->header_vars.TDCREATE_JULIAN_DAY;
      FIELD_VALUE(TDCREATE_MILLISECONDS) = dwg->header_vars.TDCREATE_MILLISECONDS;
      FIELD_VALUE(TDUPDATE_JULIAN_DAY)   = dwg->header_vars.TDUPDATE_JULIAN_DAY;
      FIELD_VALUE(TDUPDATE_MILLISECONDS) = dwg->header_vars.TDUPDATE_MILLISECONDS;
    }
  }

  for (i=0; i<3; i++) {
    FIELD_RC(aux_intro[i]); /* ff 77 01 */
  }
  FIELD_RS(dwg_version); /* AC1010 = 17 ... AC1032 = 33 */
  FIELD_RS(maint_version);
  FIELD_RL(num_saves);
  FIELD_RL(minus_1);
  FIELD_RS(num_saves_1);
  FIELD_RS(num_saves_2);
  FIELD_RL(zero);
  FIELD_RS(dwg_version_1);
  FIELD_RS(maint_version_1);
  FIELD_RS(dwg_version_2);
  FIELD_RS(maint_version_2);
  for (i=0; i<10; i++) {
    FIELD_RS(unknown[i]); /* 5 0x893 5 0x893 0 1 0 0 0 0 */
  }
  FIELD_BL(TDCREATE_JULIAN_DAY);
  FIELD_BL(TDCREATE_MILLISECONDS);
  FIELD_BL(TDUPDATE_JULIAN_DAY);
  FIELD_BL(TDUPDATE_MILLISECONDS);
  FIELD_RL(HANDSEED);
  FIELD_RL(plot_stamp);
  FIELD_RS(zero_1);
  FIELD_RS(num_saves_3);
  FIELD_RL(zero_2);
  FIELD_RL(zero_3);
  FIELD_RL(zero_4);
  FIELD_RL(num_saves_4);
  FIELD_RL(zero_5);
  FIELD_RL(zero_6);
  FIELD_RL(zero_7);

  SINCE(R_2018) {
    for (i = 0; i < 3; i++) {
      FIELD_RS(zero_18[i]);
    }
  }


