"""
CodedTool for Sentinel.

Synthetic maritime threat intelligence for the Argonaut demonstration.
"""

from typing import Any, Dict

from neuro_san.interfaces.coded_tool import CodedTool


_CORRIDOR_STATUS = {
    "bab-el-mandeb": {
        "threat_level": "elevated",
        "threat_probability_pct": 31.0,
        "days_since_last_incident": 9,
        "jwc_listed": True,
        "note": (
            "Three vessel incidents reported in this corridor in the last "
            "nine days; two involved vessels linked to the same flag state "
            "as this voyage."
        ),
    },

    "strait of hormuz": {
        "threat_level": "acute",
        "threat_probability_pct": 54.0,
        "days_since_last_incident": 2,
        "jwc_listed": True,
        "note": (
            "GPS jamming and AIS spoofing have recently been reported."
        ),
    },

    "suez canal": {
        "threat_level": "low",
        "threat_probability_pct": 4.0,
        "days_since_last_incident": 210,
        "jwc_listed": False,
        "note": (
            "No recent incidents are recorded in the synthetic dataset."
        ),
    },
}


class ZoneThreatLookup(CodedTool):
    """Look up synthetic threat intelligence for a corridor."""

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Dict[str, Any]:

        corridor = str(
            args.get("corridor", "")
        ).strip().lower()

        if not corridor:
            raise ValueError(
                "corridor is required; do not call zone_threat_lookup "
                "with empty arguments"
            )

        # First try an exact corridor match.
        status = _CORRIDOR_STATUS.get(corridor)

        # Support realistic route descriptions while preserving
        # the deterministic corridor dataset.
        if status is None:
            if (
                "bab-el-mandeb" in corridor
                or "bab-el-mandem" in corridor
            ):
                corridor = "bab-el-mandeb"
                status = _CORRIDOR_STATUS.get(corridor)

            elif "strait of hormuz" in corridor:
                corridor = "strait of hormuz"
                status = _CORRIDOR_STATUS.get(corridor)

            elif "suez canal" in corridor:
                corridor = "suez canal"
                status = _CORRIDOR_STATUS.get(corridor)

        # No matching corridor.
        if status is None:
            return {
                "corridor": corridor,
                "threat_level": "unknown",
                "threat_probability_pct": None,
                "days_since_last_incident": None,
                "jwc_listed_area": None,
                "note": "No corridor data is available.",
                "data_age_warning": "Threat data unavailable.",
                "data_status": "unavailable",
            }

        age = status["days_since_last_incident"]

        return {
            "corridor": corridor,
            "threat_level": status["threat_level"],
            "threat_probability_pct": status["threat_probability_pct"],
            "days_since_last_incident": age,
            "jwc_listed_area": status["jwc_listed"],
            "note": status["note"],
            "data_age_warning": f"Incident data is {age} days old.",
            "data_status": "synthetic_demo_data",
        }