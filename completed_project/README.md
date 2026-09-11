# MnPASS modeling and pricing project: recovered report and pricing workbook

Recovered completed-project archive, prepared 2026-09-11. Visibility: **public**.

The completed-project recovery adds Andrew Owen, Michael Janson and David Levinson's June 2013 *MnPASS Modeling and Pricing Algorithm Enhancement Task 2 Report: Lane Choice Model Development* and the original `MnPassNewPricingAlgorithm.xlsx`.

The workbook is a 61-row, 8-column illustrative pricing calculation. It retains named parameters including `quarter=4`, `kmax=50`, `pmax=8` and `factor=0.1`, with density (`K_h`), price in quarters (`P_h`) and price in dollars. Formula-address and cached-value exports preserve the original calculation without recalculating it. The recovered file's exact link to the final 2018 calibration is not established; it is labelled as project context.

The existing 2018 paper/elasticity package remains the paper-specific archive. Five recovered I-394 operating-data files and a tracked Task 7 working report are preserved in [the private project input archive](https://github.com/dlevinson/mnpass-pricing-project-restricted-inputs). Those files are not subscriber/transponder microdata and are not represented as a complete calibrated Aimsun project. No executable simulation was recovered in this selected set. The final project report is separately identified by [MnDOT handle 20.500.14153/mndot.3012](https://hdl.handle.net/20.500.14153/mndot.3012).

## Files and verification

`originals/` preserves selected source bytes and informative source-folder names. `metadata/SOURCE_MANIFEST.csv` records every archived original, its relative completed-project path, source and stored hashes, and storage method. `metadata/SOURCE_DECISIONS.csv` records included, excluded and deduplicated candidates. `metadata/CHECKSUMS.csv` covers all repository files except itself and Git internals.

Run `python3 scripts/verify_archive.py` from this directory. It checks file lengths, SHA-256 checksums, original-copy identity and any gzip restoration. Integrity verification does not reproduce historical study results. For a release asset, supply its download directory as the optional argument.

Where present, `exports/` contains readable cached-value CSV sidecars; `metadata/EXPORTS.csv` gives exact worksheet dimensions and conversion limitations. Sidecars omit layout, charts and Excel execution semantics; originals remain the source of record. Legacy XLS dates may remain Excel serial values. Stata missing values export as blank and category codes remain numeric. Formula exports are explicit formula text, not runnable CSV formulas. Spreadsheet originals require compatible Excel/LibreOffice; Stata files/logs require Stata or a compatible reader. GIS files require GIS software.

## Rights and completeness

See `LICENSE` and `RIGHTS.md` before reuse. Reports, agency inputs and third-party source tables retain their original terms. The archive is the selected recovered report/data component described above; missing computational dependencies and excluded records are documented. Original completed-project folders were left unchanged. No additional publication action is required for this selected archive; the stated gaps remain limits on full study reproduction.
