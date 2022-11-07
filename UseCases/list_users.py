from flask import Response
from .authentication import is_authenticated
import json


def list_all_users(request):
    return Response(
        response=json.dumps({
            "text": "Listing Users",
        }),
        status="200",
        content_type="application/json"
    )
