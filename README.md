# Groel

A full description of the scripts can be found in
[Macromolecular assembly structures by comparative modeling and electron microscopy](http://salilab.org/pdf/Lasker_MethodsMolBiol_2011.pdf)

## Steps
Modeling of the bacterial molecular chaperone GroEL
1. Template identification: `$IMP/tools/imppy.sh python scripts/script1_build_profile.py`
1. Template(s) selection by sequence: `$IMP/tools/imppy.sh python scripts/script2_compare_templates.py`
1. Density map segmentation: `$IMP/tools/imppy.sh python scripts/script3_density_segmentation.py`
1. Template selection by fitting to a density map: `$IMP/tools/imppy.sh python scripts/script4_score_templates_by_cc.py`
1. Template alignment: `$IMP/tools/imppy.sh python scripts/script5_template_alignment.py`
1. Model building and assessment: `$IMP/tools/imppy.sh python scripts/script6_model_building_and_assessment.py` and `$IMP/tools/imppy.sh python scripts/script7_pairwise_rmsd.py`
1. Multiple fitting into a density map: `$IMP/tools/imppy.sh python scripts/script8_split_density.py` and `$IMP/tools/imppy.sh python scripts/script9_symmetric_multiple_fitting.py`

## Info

_Author(s)_: Keren Lasker

_Version_: 1.0


_License_: \[LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Testable_: No.

_Parallelizeable_: No

_Publications_:
 - Keren Lasker, Javier A. Velazquez-Muriel, Benjamin M. Webb, Zheng Yang, Thomas E. Ferrin, Andrej Sali, [Macromolecular assembly structures by comparative modeling and electron microscopy](http://salilab.org/pdf/Lasker_MethodsMolBiol_2011.pdf), Methods in Molecular Biology, 2011.