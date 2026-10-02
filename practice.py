
import os

# =========================================================
# 1. YAHAN APNE VIDEO FOLDER KA PATH DAALO
# =========================================================
folder = r"C:\Users\abhin\Videos\classes\Python_Full_courses"


# =========================================================
# 2. VIDEO FILES FIND KARO
# =========================================================
video_extensions = (".mp4", ".mkv", ".avi", ".mov", ".webm")

files = [
    f for f in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, f))
    and f.lower().endswith(video_extensions)
]

# Filename ke according sorting
files.sort()


# =========================================================
# 3. NEW NAME BANAKAR PREVIEW DIKHAO
# =========================================================
rename_list = []

print("=" * 100)
print("                 FILE RENAME PREVIEW")
print("=" * 100)

for number, old_name in enumerate(files, start=1):

    # Extension alag karo
    name, extension = os.path.splitext(old_name)

    # Last 30 characters remove
    new_name_without_extension = name[:-30]

    # Starting me Lec-number add
    new_name = f"Lec-{number} {new_name_without_extension}{extension}"

    rename_list.append((old_name, new_name))

    print(f"\nOLD: {old_name}")
    print(f"NEW: {new_name}")


# =========================================================
# 4. CONFIRMATION
# =========================================================
print("\n" + "=" * 100)
print(f"TOTAL FILES: {len(rename_list)}")
print("=" * 100)

print("\n⚠️ Upar ki list ko carefully check karo.")
print("Agar sab kuch sahi hai to YES type karo.")
print("Kuch bhi galat lage to NO type karo.")

confirmation = input("\nRename karna hai? (YES/NO): ").strip().upper()


# =========================================================
# 5. RENAME ONLY AFTER YES
# =========================================================
if confirmation == "YES":

    print("\nRenaming files...\n")

    for old_name, new_name in rename_list:

        old_path = os.path.join(folder, old_name)
        new_path = os.path.join(folder, new_name)

        # Agar same naam ki file already exist karti hai
        if os.path.exists(new_path):
            print(f"⚠️ SKIPPED: {new_name} already exists.")
            continue

        os.rename(old_path, new_path)

        print(f"✅ {old_name}  -->  {new_name}")

    print("\n" + "=" * 100)
    print("✅ ALL POSSIBLE FILES HAVE BEEN RENAMED!")
    print("=" * 100)

else:

    print("\n❌ Rename cancelled. Koi file change nahi hui.")
