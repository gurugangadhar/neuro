"""
CodedTool for Helmsman.

Synthetic voyage economics used for the Argonaut demonstration.
"""

from typing import Any, Dict

from neuro_san.interfaces.coded_tool import CodedTool


_ROUTE_DELTAS = {
    ("bab-el-mandeb", "cape of good hope"): {
        "extra_nm": 4500,
        "extra_days": 11.0,
    },
    ("strait of hormuz", "cape of good hope"): {
        "extra_nm": 3800,
        "extra_days": 9.5,
    },
    ("suez canal", "cape of good hope"): {
        "extra_nm": 4900,
        "extra_days": 12.0,
    },
}

_DEFAULT_DELTA = {
    "extra_nm": 4000,
    "extra_days": 10.0,
}

_BUNKER_PRICE_USD_PER_MT = 620.0

_CONSUMPTION_MT_PER_DAY = {
    "vlcc": 70.0,
    "suezmax tanker": 55.0,
    "product tanker": 32.0,
    "container ship": 140.0,
    "bulk carrier": 28.0,
}

_DEFAULT_CONSUMPTION = 40.0
_CHARTER_DAY_RATE_USD = 45_000.0


class VoyageEconomics(CodedTool):
    """Calculate diversion cost and delay."""

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Dict[str, Any]:

        direct_route = str(
            args.get("direct_route", "")
        ).strip().lower()

        diversion_route = str(
            args.get("diversion_route", "")
        ).strip().lower()

        vessel_class = str(
            args.get("vessel_class", "")
        ).strip().lower()

        if not direct_route:
            raise ValueError("direct_route is required")

        if not diversion_route:
            raise ValueError("diversion_route is required")

        if not vessel_class:
            raise ValueError("vessel_class is required")

        delta = _ROUTE_DELTAS.get(
            (direct_route, diversion_route),
            _DEFAULT_DELTA,
        )

        consumption = _CONSUMPTION_MT_PER_DAY.get(
            vessel_class,
            _DEFAULT_CONSUMPTION,
        )

        extra_days = float(delta["extra_days"])

        fuel_cost = round(
            consumption
            * extra_days
            * _BUNKER_PRICE_USD_PER_MT,
            2,
        )

        charter_cost = round(
            extra_days * _CHARTER_DAY_RATE_USD,
            2,
        )

        total_cost = round(
            fuel_cost + charter_cost,
            2,
        )

        return {
            "direct_route": direct_route,
            "diversion_route": diversion_route,
            "extra_distance_nm": delta["extra_nm"],
            "extra_days": extra_days,
            "extra_fuel_cost_usd": fuel_cost,
            "extra_charter_hire_usd": charter_cost,
            "reroute_extra_cost_usd": total_cost,
            "assumptions": {
                "bunker_price_usd_per_mt": _BUNKER_PRICE_USD_PER_MT,
                "consumption_mt_per_day": consumption,
                "charter_hire_usd_per_day": _CHARTER_DAY_RATE_USD,
                "source": "illustrative synthetic assumptions",
            },
        }