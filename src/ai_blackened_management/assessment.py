from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from .data import (
    AGE_RANGES,
    BRAIN_REGION_IMPACTS,
    BRAIN_SYSTEMS,
    FREQUENCIES,
    SEVERITIES,
    SYSTEM_IMPACTS,
    TRAUMA_BRAIN_REGIONS,
)


@dataclass
class Occurrence:
    trauma_type: str
    age_range: str
    frequency: str
    severity: str


@dataclass
class Assessment:
    gender: str
    experiences: List[Occurrence] = field(default_factory=list)

    def add_occurrence(
        self, trauma_type: str, age_range: str, frequency: str, severity: str
    ) -> None:
        if trauma_type not in TRAUMA_BRAIN_REGIONS:
            raise ValueError(f"Unknown trauma type: {trauma_type}")
        if age_range not in AGE_RANGES:
            raise ValueError(f"Invalid age range: {age_range}")
        if frequency not in FREQUENCIES:
            raise ValueError(f"Invalid frequency: {frequency}")
        if severity not in SEVERITIES:
            raise ValueError(f"Invalid severity: {severity}")

        self.experiences.append(
            Occurrence(
                trauma_type=trauma_type,
                age_range=age_range,
                frequency=frequency,
                severity=severity,
            )
        )

    def compute_scores(self) -> Dict[str, Dict[str, int]]:
        affected_regions: Dict[str, int] = {}
        for exp in self.experiences:
            regions = TRAUMA_BRAIN_REGIONS[exp.trauma_type][self.gender][exp.age_range]
            freq_score = FREQUENCIES.index(exp.frequency) + 1
            sev_score = SEVERITIES.index(exp.severity) + 1
            for region in regions:
                affected_regions.setdefault(region, 0)
                affected_regions[region] += freq_score * sev_score

        affected_systems: Dict[str, int] = {}
        for system, regions in BRAIN_SYSTEMS.items():
            score = sum(affected_regions.get(r, 0) for r in regions)
            if score:
                affected_systems[system] = score
        return {"regions": affected_regions, "systems": affected_systems}

    def generate_report(self) -> str:
        scores = self.compute_scores()
        affected_regions = scores["regions"]
        affected_systems = scores["systems"]

        lines: List[str] = []
        if affected_regions:
            lines.append("Brain Areas Impacted:")
            for region, score in sorted(
                affected_regions.items(), key=lambda x: x[1], reverse=True
            ):
                impact = BRAIN_REGION_IMPACTS.get(region, "No data available.")
                lines.append(
                    f"- {region.replace('_', ' ').title()} (score {score}): {impact}"
                )

        if affected_systems:
            lines.append("\nBrain Systems Impacted:")
            for system, score in sorted(
                affected_systems.items(), key=lambda x: x[1], reverse=True
            ):
                impact = SYSTEM_IMPACTS[system]
                lines.append(
                    f"- {system} (score {score}): {impact['simple_description']}"
                )

        if not lines:
            lines.append("No significant impacts identified.")

        return "\n".join(lines)
