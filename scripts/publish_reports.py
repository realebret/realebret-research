import re
import shutil
import json
from pathlib import Path
from datetime import datetime


ROOT = Path(".")
DRAFTS = ROOT / "Research" / "Drafts"
REPORTS = ROOT / "Research" / "Reports"
ARCHIVE = ROOT / "Research" / "Archive"

INDEX = ROOT / "Research" / "Publication-Index.md"
METADATA = ROOT / "Research" / "metadata.json"


def get_number(filename):
    match = re.match(r"(\d+)", filename)
    return int(match.group(1)) if match else None


def get_title(content):
    match = re.search(r"## (.+)", content)
    return match.group(1) if match else "Unknown"


def publish_file(file):

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()


    pub_date = re.search(
        r"Publication Date:\s*(\d{4}-\d{2}-\d{2})",
        content
    )

    if not pub_date:
        return


    date = datetime.strptime(
        pub_date.group(1),
        "%Y-%m-%d"
    )


    if date > datetime.now():
        print(
            f"Bekliyor: {file.name}"
        )
        return


    number = get_number(file.name)


    # Draft -> Published
    content = content.replace(
        "Status: Draft",
        "Status: Published"
    )

    content = content.replace(
        "Version: 0.1",
        "Version: 1.0"
    )

    content = re.sub(
        r"Last Updated: .*",
        f"Last Updated: {datetime.now().strftime('%Y-%m-%d')}",
        content
    )


    REPORTS.mkdir(
        exist_ok=True
    )


    target = REPORTS / file.name


    # Eski varsa archive
    if target.exists():

        archive_folder = (
            ARCHIVE /
            f"Report-{number:03d}"
        )

        archive_folder.mkdir(
            parents=True,
            exist_ok=True
        )


        old_versions = list(
            archive_folder.glob(
                "version-*.md"
            )
        )


        version = len(old_versions)+1


        shutil.move(
            target,
            archive_folder /
            f"version-{version:03d}.md"
        )


    shutil.move(
        file,
        target
    )


    with open(
        target,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)


    update_index(
        number,
        get_title(content),
        pub_date.group(1)
    )


    print(
        f"Yayınlandı: {file.name}"
    )



def update_index(number,title,date):

    if not INDEX.exists():
        return


    with open(
        INDEX,
        "r",
        encoding="utf-8"
    ) as f:
        data=f.read()


    row=f"| {number:03d} | {title} | {date} | Published |\n"


    if row not in data:

        data=data.replace(
            "|---|---|---|---|\n",
            "|---|---|---|---|\n"+row
        )


    data=re.sub(
        r"Last Updated: .*",
        f"Last Updated: {datetime.now().strftime('%Y-%m-%d')}",
        data
    )


    with open(
        INDEX,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(data)



def update_metadata():

    if not METADATA.exists():
        return


    with open(
        METADATA,
        "r",
        encoding="utf-8"
    ) as f:
        data=json.load(f)


    data["statistics"]["published"] = len(
        list(REPORTS.glob("*.md"))
    )

    data["statistics"]["drafts"] = len(
        list(DRAFTS.glob("*.md"))
    )


    data["last_updated"] = datetime.now().strftime(
        "%Y-%m-%d"
    )


    with open(
        METADATA,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            data,
            f,
            indent=2
        )



def main():

    print(
        "Realebret Research Publisher"
    )


    for file in sorted(
        DRAFTS.glob("*.md")
    ):

        publish_file(file)


    update_metadata()


    print(
        "Tamamlandı."
    )



if __name__=="__main__":
    main()
