import os
from src.build_killi.run01_get_hemisphere_shifts import get_hemisphere_shifts

if __name__ == '__main__':
    root = "E:\\Nick\\Cole Trapnell's Lab Dropbox\\Nick Lammers\\Nick\\killi_tracker\\"
    side1_name = "20250311_LCP1-NLSMSC_side1"
    side2_name = "20250311_LCP1-NLSMSC_side2"
    interval = 25

    get_hemisphere_shifts(root=root, side1_name=side1_name, side2_name=side2_name, interval=interval)

