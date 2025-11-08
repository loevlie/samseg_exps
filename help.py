#!/usr/bin/env python3
import sys
import re

# Read the file
input_file = sys.argv[1] if len(sys.argv) > 1 else 'samseg_commands.sh'
output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.sh', '_cleaned.sh')

with open(input_file, 'r') as f:
    content = f.read()

# Remove T2 file paths (everything between T1.nii.gz and the next space before a flag)
# Pattern: T1.nii.gz /path/to/T2.nii.gz -> T1.nii.gz
content = re.sub(r'(T1\.nii\.gz) /cluster/tufts/hugheslabkp/data_irb_required/KPSC_MRI_800_nifti/STUDY_\d+/T2\.nii\.gz', r'\1', content)

# Fix lesion-mask-pattern: 0 1 -> 0
content = re.sub(r'--lesion-mask-pattern 0 1', '--lesion-mask-pattern 0', content)

# Write the cleaned file
with open(output_file, 'w') as f:
    f.write(content)

print(f"Cleaned file saved to: {output_file}")
print("Changes made:")
print("  1. Removed T2 file paths from --input arguments")
print("  2. Changed '--lesion-mask-pattern 0 1' to '--lesion-mask-pattern 0'")