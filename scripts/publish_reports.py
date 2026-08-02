from pathlib import Path


DRAFT_DIR = Path("Research/Drafts")


reports = [
    "004-Biotechnology-and-Synthetic-Biology-Landscape",
    "005-Genomics-and-Gene-Editing-Technologies",
    "006-Computational-Biology-and-Bioinformatics-Revolution",
    "007-AI-Driven-Drug-Discovery-and-Protein-Engineering",
    "008-Precision-Medicine-and-Future-Healthcare-Technologies",
    "009-Longevity-Research-and-Aging-Science",
    "010-Neuroscience-and-Brain-Computer-Interfaces",
    "011-Advanced-Materials-and-Nanotechnology",
    "012-Graphene-and-Two-Dimensional-Materials",
    "013-Smart-Materials-and-Self-Healing-Technologies",
    "014-Future-Battery-Technologies-and-Energy-Storage",
    "015-Renewable-Energy-Technologies",
    "016-Nuclear-Fusion-Energy-Research",
    "017-Advanced-Nuclear-Technologies",
    "018-Semiconductor-Technology-and-Chip-Manufacturing",
    "019-AI-Hardware-and-Next-Generation-Computing",
    "020-Neuromorphic-Computing-and-Brain-Inspired-Systems",
    "021-Future-Internet-and-Digital-Infrastructure",
    "022-6G-Networks-and-Future-Communication-Systems",
    "023-Cloud-Computing-and-Edge-AI",
    "024-Digital-Twins-and-Industrial-Simulation",
    "025-Robotics-and-Autonomous-Systems",
    "026-Humanoid-Robots-and-General-Purpose-Robotics",
    "027-Industrial-Automation-and-Smart-Manufacturing",
    "028-Autonomous-Vehicles-and-Transportation-Technologies",
    "029-Drone-Technologies-and-Autonomous-Aviation",
    "030-AI-Agents-and-Autonomous-Software-Systems",
    "031-Space-Technology-and-Exploration",
    "032-Satellite-Technologies-and-Space-Infrastructure",
    "033-Lunar-Economy-and-Moon-Exploration",
    "034-Mars-Exploration-and-Planetary-Science",
    "035-Advanced-Space-Propulsion-Systems",
    "036-Astrobiology-and-Search-for-Extraterrestrial-Life",
    "037-Climate-Technologies-and-Earth-System-Science",
    "038-Carbon-Capture-and-Geoengineering-Technologies",
    "039-Artificial-General-Intelligence-Research-Landscape",
    "040-AI-for-Scientific-Discovery-Automated-Scientist-Era",
    "041-Quantum-Biology-and-Quantum-Life-Effects",
    "042-Artificial-Life-and-Synthetic-Organisms",
    "043-Machine-Consciousness-and-Cognitive-Architectures",
    "044-Post-Quantum-Cryptography-and-Future-Cybersecurity",
    "045-Advanced-Simulation-and-Digital-Reality-Technologies",
    "046-Human-Enhancement-and-Human-Machine-Integration",
    "047-Future-Education-Technologies-and-AI-Learning-Systems",
    "048-Future-Cities-and-Intelligent-Civilization-Infrastructure",
    "049-Technology-Forecast-2030-2050-Global-Scenarios",
    "050-Future-Civilization-Science-Technology-and-Humanity-Beyond-2050"
]


template = """# Research Report {number}
## {title}

**Publication Date:** YYYY-MM-DD  
**Last Updated:** YYYY-MM-DD  
**Status:** Draft  
**Version:** 0.1  
**Research Category:** Under Review  
**Evidence Level:** Under Review

---

# Abstract

"""


def create_files():

    DRAFT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    for report in reports:

        number = report[:3]

        title = report[4:].replace("-", " ")


        file = DRAFT_DIR / f"{report}.md"


        if file.exists():
            print(f"Exists: {file.name}")
            continue


        file.write_text(
            template.format(
                number=number,
                title=title
            ),
            encoding="utf-8"
        )


        print(f"Created: {file.name}")


if __name__ == "__main__":
    create_files()
