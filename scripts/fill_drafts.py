from pathlib import Path
import re
from datetime import datetime


SOURCE = Path("Research/deepseek_research.md")
DRAFTS = Path("Research/Drafts")


def find_sections(text):

    pattern = r"#(\d{3})(.*?)(?=\n#\d{3}|$)"

    return re.findall(
        pattern,
        text,
        re.S
    )


def main():

    if not SOURCE.exists():
        print("deepseek_research.md bulunamadı")
        return


    content = SOURCE.read_text(
        encoding="utf-8"
    )


    sections = find_sections(content)


    if not sections:
        print("Numaralı içerik bulunamadı")
        return


    today = datetime.now().strftime("%Y-%m-%d")


    for number, body in sections:

        number = int(number)


        files = list(
            DRAFTS.glob(
                f"{number:03d}-*.md"
            )
        )


        if not files:
            print(
                f"{number:03d} dosyası bulunamadı"
            )
            continue


        draft_file = files[0]


        title = draft_file.stem


        new_content = f"""# Research Report {number:03d}

## {title.replace(f'{number:03d}-','').replace('-',' ')}

Publication Date: 2026-08-10

Status: Draft

Version: 0.1

Evidence Level: Under Review

Last Updated: {today}


## Research Content


{body.strip()}


## References

"""


        draft_file.write_text(
            new_content,
            encoding="utf-8"
        )


        print(
            f"✓ {draft_file.name} dolduruldu"
        )


if __name__ == "__main__":
    main()
