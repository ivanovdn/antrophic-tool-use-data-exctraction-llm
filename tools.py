tools = [
    {
        "name": "get_single_shipment_info",
        "description": "Retrieves information about single shipment from email. Returns the pickup zip, deliery zip, equipment type.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pickup_zip": {
                    "type": "string",
                    "description": "The ZIP of pickup point.",
                },
                "delivery_zip": {
                    "type": "string",
                    "description": "The ZIP of delivery point.",
                },
                "equipment_type": {
                    "type": "string",
                    "description": "The type of equipment for freight. For example 'Dry'",
                },
            },
            "required": ["pickup_zip", "delivery_zip", "equipment_type"],
        },
    },
    {
        "name": "get_multiple_shipment_info",
        "description": "Retrieves information about multiple shipments from email. Returns the pickup zip, deliery zip, equipment type.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pickup_zip": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": 'Array of ZIPs of pickup point, e.g. ["30401", "94632"].',
                },
                "delivery_zip": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": 'Array of ZIPs of delivery point, e.g. ["30401", "94632"].',
                },
                "equipment_type": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": 'Array of equipment types for freight, for example: ["Reefer", "Dry"]',
                },
            },
            "required": ["pickup_zip", "delivery_zip", "equipment_type"],
        },
    },
    {
        "name": "get_shipment_with_stops_info",
        "description": "Retrieves information about single shipment with stops from email. Returns the pickup zip, deliery zip, equipment type.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pickup_zip": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": 'Array of ZIPs of pickup point, e.g. ["30401", "94632"].',
                },
                "delivery_zip": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": 'Array of ZIPs of delivery point, e.g. ["30401", "94632"].',
                },
                "equipment_type": {
                    "type": "string",
                    "description": "The type of equipment for freight. For example 'Dry'",
                },
            },
            "required": ["pickup_zip", "delivery_zip", "equipment_type"],
        },
    },
]
