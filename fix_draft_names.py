from pathlib import Path

drafts = {
11:"Advanced-Materials-and-Nanotechnology",
12:"Graphene-and-Two-Dimensional-Materials-Research",
13:"Smart-Materials-and-Self-Healing-Technologies",
14:"Future-Battery-Technologies-and-Energy-Storage",
15:"Renewable-Energy-Technologies-Landscape",
16:"Nuclear-Fusion-Energy-Research-Overview",
17:"Advanced-Nuclear-Technologies-Beyond-Fusion",
18:"Semiconductor-Technology-and-Chip-Manufacturing",
19:"AI-Hardware-and-Next-Generation-Computing-Systems",
20:"Neuromorphic-Computing-and-Brain-Inspired-Systems",
21:"Future-Internet-and-Digital-Infrastructure",
22:"6G-Networks-and-Future-Communication-Systems",
23:"Cloud-Computing-Edge-AI-and-Distributed-Intelligence",
24:"Digital-Twins-and-Industrial-Simulation-Technologies",
25:"Robotics-and-Autonomous-Systems-Landscape",
26:"Humanoid-Robots-and-General-Purpose-Robotics",
27:"Industrial-Automation-and-Smart-Manufacturing",
28:"Autonomous-Vehicles-and-Transportation-Technologies",
29:"Drone-Technologies-and-Autonomous-Aviation",
30:"AI-Agents-and-Autonomous-Software-Systems",
31:"Space-Technology-and-Exploration-Landscape",
32:"Satellite-Technologies-and-Space-Infrastructure",
33:"Lunar-Economy-and-Moon-Exploration-Technologies",
34:"Mars-Exploration-and-Planetary-Science-Technologies",
35:"Advanced-Space-Propulsion-Systems",
36:"Astrobiology-and-Search-for-Extraterrestrial-Life",
37:"Climate-Technologies-and-Earth-System-Science",
38:"Carbon-Capture-and-Geoengineering-Technologies",
39:"Artificial-General-Intelligence-Research-Landscape",
40:"AI-for-Scientific-Discovery-The-Automated-Scientist-Era",
41:"Quantum-Biology-and-Quantum-Effects-in-Life-Sciences",
42:"Artificial-Life-and-Synthetic-Organisms",
43:"Machine-Consciousness-and-Cognitive-Architectures",
44:"Post-Quantum-Cryptography-and-Future-Cybersecurity",
45:"Advanced-Simulation-and-Digital-Reality-Technologies",
46:"Human-Enhancement-and-Human-Machine-Integration",
47:"Future-Education-Technologies-and-AI-Learning-Systems",
48:"Future-Cities-and-Intelligent-Civilization-Infrastructure",
49:"Technology-Forecast-2030-2050-Global-Transformation-Scenarios",
50:"Future-Civilization-Science-Technology-and-Humanity-Beyond-2050"
}


folder = Path("Research/Drafts")


for number, title in drafts.items():

    old = folder / f"{number}-Research-Report-Draft.md"
    new = folder / f"{number:03d}-{title}.md"

    if old.exists():
        old.rename(new)
        print(f"Renamed: {old.name} -> {new.name}")

    else:
        print(f"Missing: {old.name}")
