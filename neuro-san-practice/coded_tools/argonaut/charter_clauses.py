"""
CodedTool for Counsel.

Synthetic charter-party clause library for the Argonaut demonstration.
Replace this library with real charter-party document retrieval in production.
"""

from typing import Any, Dict

from neuro_san.interfaces.coded_tool import CodedTool


_CLAUSE_LIBRARY = {
    "time charter": {
        "war_risk_clause": (
            "Master may refuse an order into a zone reasonably judged dangerous; "
            "charterer bears resulting extra cost."
        ),
        "safe_port_warranty": (
            "Charterer warrants each ordered port or route is safe at the time of order."
        ),
        "ais_reporting": (
            "Continuous AIS reporting is required; any switch-off must be logged."
        ),
        "crew_rights": (
            "IBF/ITF high-risk-area bonus and applicable refusal rights may apply."
        ),
    },

    "voyage charter": {
        "war_risk_clause": (
            "Owner may decline an unsafe route; charterer bears increased insurance "
            "cost if the owner proceeds on charterer's instruction."
        ),
        "safe_port_warranty": (
            "Charterer warrants the discharge port is safe and remains so."
        ),
        "ais_reporting": (
            "AIS remains active except where flag-state or naval guidance requires "
            "otherwise; deviations must be logged."
        ),
        "crew_rights": (
            "Crew bonus and refusal rights depend on flag-state and applicable "
            "collective bargaining terms."
        ),
    },
}


_DEFAULT_CLAUSES = {
    "war_risk_clause": "No specific charter terms found.",
    "safe_port_warranty": "Not specified.",
    "ais_reporting": "Standard AIS reporting expected.",
    "crew_rights": "Applicable statutory and collective-bargaining protections apply.",
}


class CharterClauseLookup(CodedTool):
    """Return relevant charter-party clauses."""

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Dict[str, Any]:

        charter_type = str(
            args.get("charter_type", "")
        ).strip().lower()

        if charter_type in _CLAUSE_LIBRARY:
            source = "synthetic_charter_library"
            clauses = _CLAUSE_LIBRARY[charter_type]
        else:
            source = "default_unknown_charter"
            clauses = _DEFAULT_CLAUSES

        return {
            "charter_type": charter_type or "unspecified",
            "source": source,
            **clauses,
        }