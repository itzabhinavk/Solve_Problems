import os
import re

# ============================================================
# SAFE RECOVERY + CORRECT RENAME
# ============================================================
# Put this script in the SAME folder as your videos.
# It first shows the COMPLETE OLD -> NEW preview.
# NOTHING is renamed until you type YES.
# ============================================================

FOLDER = r"C:\Users\abhin\Videos\classes\Python_Full_courses"

# Current Lec number -> original lecture number
MAPPING = {1: 70, 2: 69, 3: 57, 4: 5, 5: 100, 6: 58, 7: 85, 8: 33, 9: 34, 10: 29, 11: 42, 12: 36, 13: 93, 14: 90, 15: 94, 16: 99, 17: 15, 18: 26, 19: 27, 20: 40, 21: 47, 22: 55, 23: 64, 24: 67, 25: 68, 26: 75, 27: 76, 28: 82, 29: 88, 30: 49, 31: 37, 32: 17, 33: 21, 34: 92, 35: 20, 36: 91, 37: 60, 38: 44, 39: 81, 40: 14, 41: 61, 42: 66, 43: 22, 44: 56, 45: 39, 46: 52, 47: 1, 48: 19, 49: 23, 50: 48, 51: 59, 52: 62, 53: 73, 54: 7, 55: 8, 56: 83, 57: 96, 58: 53, 59: 16, 60: 74, 61: 3, 62: 98, 63: 80, 64: 79, 65: 97, 66: 25, 67: 77, 68: 4, 69: 38, 70: 30, 71: 95, 72: 89, 73: 32, 74: 31, 75: 41, 76: 87, 77: 78, 78: 63, 79: 2, 80: 65, 81: 13, 82: 12, 83: 11, 84: 10, 85: 84, 86: 24, 87: 9, 88: 6, 89: 43, 90: 86, 91: 18, 92: 71, 93: 28, 94: 35, 95: 45, 96: 54, 97: 46, 98: 50, 99: 51, 100: 72}

VIDEO_EXTENSIONS = (".mp4", ".mkv", ".avi", ".mov", ".webm")


def natural_key(filename):
    return [
        int(x) if x.isdigit() else x.lower()
        for x in re.split(r"(\d+)", filename)
    ]


files = [
    f for f in os.listdir(FOLDER)
    if os.path.isfile(os.path.join(FOLDER, f))
    and f.lower().endswith(VIDEO_EXTENSIONS)
]

files.sort(key=natural_key)

rename_list = []

print("=" * 110)
print("              RECOVERY + CORRECT RENAME PREVIEW")
print("=" * 110)

for old_name in files:

    # Current files created by the previous script:
    # Lec-1 ..., Lec-2 ..., etc.
    m = re.match(r"^Lec-\s*(\d+)\s*(.*?)(\.[^.]+)$", old_name, re.I)

    if not m:
        print(f"\n⚠️ NOT RECOGNIZED: {old_name}")
        continue

    current_num = int(m.group(1))
    title = m.group(2).strip()
    extension = m.group(3)

    if current_num not in MAPPING:
        print(f"\n⚠️ NO MAPPING FOUND: {old_name}")
        continue

    actual_num = MAPPING[current_num]

    # Remove accidental old Lec number from title, if present.
    title = re.sub(
        r"^Lec[-\s]*\d+\s*",
        "",
        title,
        flags=re.I
    ).strip()

    # Zero-padding keeps Windows Explorer in correct order.
    new_name = f"Lec-{actual_num:03d} {title}{extension}"

    rename_list.append((old_name, new_name))

    print(f"\nOLD: {old_name}")
    print(f"NEW: {new_name}")


print("\n" + "=" * 110)
print(f"FILES READY: {len(rename_list)}")
print("=" * 110)

print("\n⚠️ IMPORTANT: Check the preview above.")
print("If everything looks correct, type exactly YES.")
print("Anything else cancels the operation.")

confirm = input("\nRename now? (YES/NO): ").strip().upper()

if confirm != "YES":
    print("\n❌ CANCELLED — no files were changed.")
    input("\nPress Enter to close...")
    raise SystemExit


# ------------------------------------------------------------
# Two-step temporary rename prevents collisions.
# Example: Lec-1 -> Lec-70 while Lec-70 already exists.
# ------------------------------------------------------------
print("\nStep 1/2: creating temporary names...")

temp_files = []

for index, (old_name, new_name) in enumerate(rename_list):

    old_path = os.path.join(FOLDER, old_name)

    _, ext = os.path.splitext(old_name)
    temp_name = f"__RENAME_TEMP_{index:04d}__{ext}"
    temp_path = os.path.join(FOLDER, temp_name)

    os.rename(old_path, temp_path)

    temp_files.append((temp_name, new_name))

print("Temporary rename complete.")

print("\nStep 2/2: applying final names...")

for temp_name, new_name in temp_files:

    temp_path = os.path.join(FOLDER, temp_name)
    new_path = os.path.join(FOLDER, new_name)

    if os.path.exists(new_path):
        print(f"⚠️ SKIPPED — destination already exists: {new_name}")
        continue

    os.rename(temp_path, new_path)

    print(f"✅ {new_name}")


print("\n" + "=" * 110)
print("✅ RECOVERY + CORRECT RENAME COMPLETE")
print("=" * 110)

input("\nPress Enter to close...")
