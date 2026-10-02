from pathlib import Path

base = Path(r"C:\Users\abhin\Downloads\My all project\programming\python\100_Days_of_code")
base.mkdir(exist_ok=True)

quotes = [
    "Har din chhota sa step leke bada result pao.",
    "Consistency beats talent when talent does not work hard.",
    "Apne sapne ko roz ek chhota sa code dedo.",
    "Kal ka version aaj ke effort se banta hai.",
    "Code karo, seekho, aur agge badho.",
    "Ek line code bhi aaj ka progress hai.",
    "Dhairya rakho, practice hi perfection banati hai.",
    "Aaj ka mehnat kal ki confidence hai.",
]

for i in range(2, 101):
    text = (
        f"# Day {i} - 100 Days of Code Challenge\n"
        "# Yeh file aapki daily coding journey ka hissa hai.\n"
        f"# Motivation: {quotes[(i - 2) % len(quotes)]}\n"
        "# Chhoti chhoti steps bhi bade sapne banati hain.\n\n"
    )
    (base / f"Day_{i}.py").write_text(text, encoding="utf-8")

print(f"Created {100 - 1} files in {base}")
