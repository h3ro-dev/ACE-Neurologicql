TRAUMA_BRAIN_REGIONS = {
    "emotional_abuse": {
        "male": {
            "0-2": ["amygdala", "prefrontal_cortex"],
            "3-5": ["hippocampus"],
        },
        "female": {
            "0-2": ["amygdala", "prefrontal_cortex"],
            "3-5": ["hippocampus"],
        },
    },
    "physical_abuse": {
        "male": {
            "0-2": ["sensory_cortex", "amygdala"],
            "3-5": ["cerebellum", "amygdala"],
        },
        "female": {
            "0-2": ["sensory_cortex", "amygdala"],
            "3-5": ["hippocampus", "amygdala"],
        },
    },
    "household_dysfunction": {
        "male": {
            "0-2": ["amygdala"],
            "3-5": ["hippocampus"],
        },
        "female": {
            "0-2": ["amygdala"],
            "3-5": ["hippocampus"],
        },
    },
}

BRAIN_REGION_IMPACTS = {
    "prefrontal_cortex": "Issues with decision-making and executive function.",
    "amygdala": "Heightened fear responses and anxiety.",
    "hippocampus": "Impaired memory formation.",
    "sensory_cortex": "Increased sensitivity to sensory input.",
    "cerebellum": "Problems with coordination and balance.",
}

BRAIN_SYSTEMS = {
    "Emotional Regulation System": [
        "amygdala",
        "prefrontal_cortex",
    ],
    "Memory System": ["hippocampus", "prefrontal_cortex"],
}

SYSTEM_IMPACTS = {
    "Emotional Regulation System": {
        "neurological_description": "Alterations in emotion regulation pathways.",
        "simple_description": "Strong emotions that are hard to control.",
        "superpowers": ["Heightened emotional awareness"],
        "kryptonites": ["Difficulty managing emotions"],
    },
    "Memory System": {
        "neurological_description": "Changes in memory formation areas.",
        "simple_description": "Challenging to remember things.",
        "superpowers": ["Creative thinking"],
        "kryptonites": ["Forgetfulness"],
    },
}

AGE_RANGES = ["0-2", "3-5"]
FREQUENCIES = ["Once", "Occasionally", "Frequently", "Constantly"]
SEVERITIES = ["Mild", "Moderate", "Severe", "Extreme"]
