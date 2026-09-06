"""
CodedTool for Broker.

Synthetic war-risk pricing model for the Argonaut demonstration.
"""

from typing import Any, Dict

from neuro_san.interfaces.coded_tool import CodedTool


_RATE_BY_THREAT_LEVEL = {
    "low": 0.001,
    "elevated": 0.009,
    "high": 0.018,
    "acute": 0.030,
    "unknown": 0.012,
}


class WarRiskPricing(CodedTool):
    """Calculate illustrative war-risk insurance premium."""

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Dict[str, Any]:

        corridor = str(
            args.get("corridor", "")
        ).strip().lower()

        threat_level = str(
            args.get("threat_level", "")
        ).strip().lower()

        vessel_class = str(
            args.get("vessel_class", "")
        ).strip().lower()

        if not corridor:
            raise ValueError("corridor is required")

        if not threat_level:
            raise ValueError("threat_level is required")

        if not vessel_class:
            raise ValueError("vessel_class is required")

        try:
            cargo_value = float(args["cargo_value_usd"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError("cargo_value_usd must be numeric") from exc

        if cargo_value <= 0:
            raise ValueError("cargo_value_usd must be greater than zero")

        rate = _RATE_BY_THREAT_LEVEL.get(
            threat_level,
            _RATE_BY_THREAT_LEVEL["unknown"],
        )

        premium = round(
            cargo_value * rate,
            2,
        )

        return {
            "corridor": corridor,
            "vessel_class": vessel_class,
            "threat_level": threat_level,
            "premium_rate_pct": round(rate * 100, 3),
            "transit_insurance_premium_usd": premium,
            "quote_status": "illustrative",
            "quote_validity_hours": 48,
        }