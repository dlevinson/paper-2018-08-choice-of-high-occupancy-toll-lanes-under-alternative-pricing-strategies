# Choice of High Occupancy/Toll Lanes Under Alternative Pricing Strategies

## Contribution

This paper develops a lane-choice model for comparing dynamic HOT-lane pricing strategies. MnPASS evidence shows that a toll can initially signal downstream congestion and increase demand before its deterrent effect dominates, and demonstrates how incorporating general-purpose-lane density can better align price with the value of the managed lane.

Paper ID: paper-2018-08

This is a **public derived-model package**. The original paper folder supplied one shareable workbook, `elasticity_points_2_offset_2.xlsx`, with aggregate model/elasticity calculations and formulas. I did not find raw MnPASS/MnDOT/Metropolitan Council trip tables in the package, and they are intentionally outside this public archive boundary.

## Contents

- `paper/ChoiceofHOT-Published.pdf` - published TRR paper.
- `data/derived_model_workbook/elasticity_points_2_offset_2.xlsx` - original Excel workbook with formulas.
- `data/derived_model_workbook/elasticity_points_2_offset_2_formulas.csv` - formula-text export of the primary model sheet.
- `data/derived_model_workbook/elasticity_points_2_offset_2_values.csv` - value export of the primary model sheet.
- `metadata/WORKBOOK_SHEETS.csv` - worksheet inventory, dimensions, and formula counts.
- `metadata/SOURCE_FILE_DECISIONS.csv` - archive-boundary decisions.
- `metadata/PACKAGE_FILE_MANIFEST.csv` - generated file listing.
- `LICENSE` - operative repository license boundary for author-created package materials.

## Archive decision

Public release is limited to the author-created derived workbook package and supporting documentation. The repository should not claim to provide raw transaction, trip-table, transponder, loop-detector, corridor-demand, travel-time, or agency operating data.

## License and provenance boundary

The root `LICENSE` applies CC BY 4.0 only to rights-cleared author-created repository documentation, package metadata, source-decision notes, data dictionaries, manifests, and the derived HOT-lane pricing model workbook/formula/value exports to the extent controlled by the paper authors or repository maintainers.

The publication PDF retains its publisher, repository, or manuscript terms. Raw MnPASS, MnDOT, Metropolitan Council, transponder, loop-detector, trip-table, corridor-demand, travel-time, traffic-operations, public-agency/source data, vendor/runtime/file-format structures, and other externally controlled materials are not relicensed.

The recovered-project supplement includes an MIT-licensed archive verification script; no full simulation runtime is included.

Last reviewed: 2026-09-11 Australia/Sydney.

## Recovered completed-project archive

[The documented project supplement](completed_project/README.md) adds the June 2013 Task 2 report and `MnPassNewPricingAlgorithm.xlsx`, with original bytes, CSV/formula exports, citations, rights notes and checksums. This pricing workbook is project context; its exact relationship to the final 2018 calibration is not established.

[The private input companion](https://github.com/dlevinson/mnpass-pricing-project-restricted-inputs) preserves the recovered I-394 operating-data files and a tracked Task 7 working report. The public repository contains no raw operating records or subscriber/transponder microdata.

Run `python3 completed_project/scripts/verify_archive.py` to verify the supplement. `metadata/REPOSITORY_CHECKSUMS.csv` covers the complete repository except the checksum file itself. See the supplement's README and SOURCE_MANIFEST for provenance and exclusions.
