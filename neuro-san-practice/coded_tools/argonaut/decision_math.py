"""
Deterministic routing decision engine for Argonaut.

The LLM never calculates the recommendation.
This tool owns the numeric decision.
"""

from typing import Any, Dict

from neuro_san.interfaces.coded_tool import CodedTool


class DecisionMath(CodedTool):
    """Computes routing recommendation, confidence and break-even thresholds."""

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Dict[str, Any]:

        threat_probability_pct = float(
            args.get("threat_probability_pct", 0.0)
        )

        reroute_extra_cost_usd = float(
            args.get("reroute_extra_cost_usd", 0.0)
        )

        transit_insurance_premium_usd = float(
            args.get("transit_insurance_premium_usd", 0.0)
        )

        customer_penalty_usd = float(
            args.get("customer_penalty_usd", 0.0)
        )

        # Convert threat probability into a simple illustrative exposure multiplier.
        risk_multiplier = 1.0 + (threat_probability_pct / 100.0)

        cost_if_transit = round(
            transit_insurance_premium_usd * risk_multiplier,
            2,
        )

        cost_if_reroute = round(
            reroute_extra_cost_usd + customer_penalty_usd,
            2,
        )

        if cost_if_transit <= cost_if_reroute:
            recommendation = "TRANSIT"
        else:
            recommendation = "REROUTE"

        larger_cost = max(cost_if_transit, cost_if_reroute, 1.0)

        margin_usd = abs(
            cost_if_transit - cost_if_reroute
        )

        margin_pct = (
            margin_usd / larger_cost
        ) * 100.0

        confidence_pct = max(
            55.0,
            min(95.0, 50.0 + margin_pct),
        )

        # Break-even values.

        insurance_break_even = round(
            cost_if_reroute / risk_multiplier,
            2,
        )

        reroute_break_even = round(
            max(
                0.0,
                cost_if_transit - customer_penalty_usd,
            ),
            2,
        )

        penalty_break_even = round(
            max(
                0.0,
                cost_if_transit - reroute_extra_cost_usd,
            ),
            2,
        )

        return {
            "recommendation": recommendation,

            "cost_if_transit_usd": round(
                cost_if_transit,
                2,
            ),

            "cost_if_reroute_usd": round(
                cost_if_reroute,
                2,
            ),

            "margin_usd": round(
                margin_usd,
                2,
            ),

            "confidence_pct": round(
                confidence_pct,
                1,
            ),

            "risk_model": {
                "threat_probability_pct": round(
                    threat_probability_pct,
                    1,
                ),
                "risk_multiplier": round(
                    risk_multiplier,
                    3,
                ),
                "note": (
                    "Illustrative demo model: threat probability "
                    "adjusts transit insurance exposure."
                ),
            },

            "what_would_change_this": {
                "insurance_premium_break_even_usd": (
                    insurance_break_even
                ),
                "reroute_cost_break_even_usd": (
                    reroute_break_even
                ),
                "customer_penalty_break_even_usd": (
                    penalty_break_even
                ),
            },
        }
    