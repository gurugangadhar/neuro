"""
CodedTool for Ledger.

Synthetic customer-contract library for the Argonaut demonstration.
"""

from typing import Any, Dict

from neuro_san.interfaces.coded_tool import CodedTool


_CONTRACT_LIBRARY = {
    "default": {
        "cargo_description": "mixed cargo",
        "cargo_value_usd": 42_000_000.0,
        "delivery_deadline_note": (
            "Fixed delivery window with a per-day late penalty."
        ),
        "late_penalty_usd_per_day": 100_000.0,
        "perishable": False,
    },
}


class CustomerContractLookup(CodedTool):
    """Look up customer contract terms and calculate delay penalty."""

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Dict[str, Any]:

        customer_ref = str(
            args.get("customer_ref", "")
        ).strip().lower()

        if not customer_ref:
            raise ValueError("customer_ref is required")

        try:
            delay_days = float(args["delay_days"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError("delay_days must be numeric") from exc

        if delay_days < 0:
            raise ValueError("delay_days cannot be negative")

        contract = _CONTRACT_LIBRARY.get(
            customer_ref,
            _CONTRACT_LIBRARY["default"],
        )

        penalty = round(
            contract["late_penalty_usd_per_day"] * delay_days,
            2,
        )

        sly_data["customer_contract_terms"] = contract

        return {
            "customer_ref": customer_ref,
            "cargo_value_usd": contract["cargo_value_usd"],
            "delay_days": delay_days,
            "customer_penalty_usd": penalty,
            "penalty_per_day_usd": contract["late_penalty_usd_per_day"],
            "perishable": contract["perishable"],
            "note": contract["delivery_deadline_note"],
        }