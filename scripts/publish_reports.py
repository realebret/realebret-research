from pathlib import Path
from datetime import datetime
import re
import json
import shutil


DRAFTS_DIR = Path("Research/Drafts")
REPORTS_DIR = Path("Research/Reports")
ARCHIVE_DIR = Path("Research/Archive")

INDEX_FILE = Path("Research/Publication-Index.md")
CHANGELOG_FILE = Path("CHANGELOG.md")
METADATA_FILE = Path("Research/metadata.json")


# ==========================
# HELPERS
# ==========================


def get_report_number(filename):

    match = re.search(r"^(\d+)", filename)

    return int(match.group(1)) if match else None



def get_title(content):

    match = re.search(
        r"## (.+)",
        content
    )

    if match:
        return match.group(1).strip()

    return "Unknown"



def get_version_number(folder):

    versions = list(
        folder.glob("version-*.md")
    )

    if not versions:
        return 1

    numbers = []

    for file in versions:

        match = re.search(
            r"version-(\d+)",
            file.name
        )

        if match:
            numbers.append(
                int(match.group(1))
            )

    return max(numbers) + 1



# ==========================
# UPDATE REPORT STATUS
# ==========================


def publish_content(content):

    content = content.replace(
        "Status: Draft",
        "Status: Published"
    )

    content = content.replace(
        "Version: 0.1",
        "Version: 1.0"
    )


    today = datetime.now().strftime(
        "%Y-%m-%d"
    )


    content = re.sub(
        r"Last Updated: .*",
        f"Last Updated: {today}",
        content
    )


    return content



# ==========================
# ARCHIVE
# ==========================


def archive_old(report_file, number):

    folder = (
        ARCHIVE_DIR /
        f"Report-{number:03d}"
    )

    folder.mkdir(
        parents=True,
        exist_ok=True
    )


    version = get_version_number(folder)


    destination = (
        folder /
        f"version-{version:03d}.md"
    )


    shutil.move(
        str(report_file),
        str(destination)
    )



# ==========================
# INDEX UPDATE
# ==========================


def update_index(number, title, date):

    if not INDEX_FILE.exists():

        INDEX_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        INDEX_FILE.write_text(
            "# Realebret Research — Publication Index\n\n"
            "| Report | Title | Date | Status |\n"
            "|---|---|---|---|\n",
            encoding="utf-8"
        )


    content = INDEX_FILE.read_text(
        encoding="utf-8"
    )


    row = (
        f"| {number:03d} | "
        f"{title} | "
        f"{date} | Published |\n"
    )


    if f"| {number:03d} |" not in content:

        content += row


    INDEX_FILE.write_text(
        content,
        encoding="utf-8"
    )



# ==========================
# CHANGELOG
# ==========================


def update_changelog(number, title, date):

    if not CHANGELOG_FILE.exists():

        CHANGELOG_FILE.write_text(
            "# Changelog\n",
            encoding="utf-8"
        )


    content = CHANGELOG_FILE.read_text(
        encoding="utf-8"
    )


    if f"Research Report {number:03d}" in content:
        return


    entry = f"""

## {date}

### Added

- Research Report {number:03d} — {title}

"""


    CHANGELOG_FILE.write_text(
        content + entry,
        encoding="utf-8"
    )



# ==========================
# METADATA
# ==========================


def update_metadata():

    if not METADATA_FILE.exists():
        return


    data = json.loads(
        METADATA_FILE.read_text(
            encoding="utf-8"
        )
    )


    published = len(
        list(REPORTS_DIR.glob("*.md"))
    )


    drafts = len(
        list(DRAFTS_DIR.glob("*.md"))
    )


    data["statistics"]["published"] = published

    data["statistics"]["drafts"] = drafts


    data["last_updated"] = (
        datetime.now()
        .strftime("%Y-%m-%d")
    )


    METADATA_FILE.write_text(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )



# ==========================
# MAIN
# ==========================


def main():

    print(
        "Realebret Research Publisher Started"
    )


    published_reports = []


    for draft in sorted(
        DRAFTS_DIR.glob("*.md")
    ):

        content = draft.read_text(
            encoding="utf-8"
        )


        date_match = re.search(
            r"Publication Date:\s*(\d{4}-\d{2}-\d{2})",
            content
        )


        if not date_match:
            continue


        publication_date = datetime.strptime(
            date_match.group(1),
            "%Y-%m-%d"
        )


        if publication_date > datetime.now():
            continue



        number = get_report_number(
            draft.name
        )


        title = get_title(
            content
        )


        destination = (
            REPORTS_DIR /
            draft.name
        )


        if destination.exists():

            archive_old(
                destination,
                number
            )


        new_content = publish_content(
            content
        )


        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        shutil.move(
            str(draft),
            str(destination)
        )


        destination.write_text(
            new_content,
            encoding="utf-8"
        )


        date = publication_date.strftime(
            "%Y-%m-%d"
        )


        update_index(
            number,
            title,
            date
        )


        update_changelog(
            number,
            title,
            date
        )


        published_reports.append(
            number
        )


        print(
            f"Published Report {number:03d}"
        )



    update_metadata()


    print(
        f"Completed: {len(published_reports)} reports published."
    )



if __name__ == "__main__":
    main()
