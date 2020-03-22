# -*- coding: utf8 -*-
"""Search API module."""

import json
from flask import abort, request
from flask.views import MethodView
from sqlalchemy.exc import ProgrammingError

from explicates.core import search
from explicates.api.base import APIBase
from explicates.model.collection import Collection
from explicates.model.annotation import Annotation
from flask import abort, request, jsonify, make_response, url_for


class TagsAPI(APIBase, MethodView):
    """A tag is a label used to annotate an image"""

    # Common headers for all responses
    headers = {
        'Allow': 'GET,OPTIONS,HEAD'
    }

    def _filter_valid_params(self, data):
        """Return the valid search parameters."""
        valid_keys = ['collection', 'limit', 'order_by', 'offset', 'q']
        return {k: v for k, v in data.items() if k in valid_keys}

    def get(self):
        """Search Tags."""
        data = request.args.to_dict(flat=True)
        if request.data:
            data = json.loads(request.data.decode('utf8'))

        params = self._filter_valid_params(data)

        try:
            tags = self._suggests(**params)
        except (ValueError, ProgrammingError) as err:
            abort(400, err)

        ret = self._get_response_from_tags(tags)

        return ret

    def _suggests(self, **params):
        ret = [
            ['tag1', 'id1'],
            ['tag2', 'id2'],
        ]

        ret = search.suggest_tags(**params)

        return ret

    def _get_response_from_tags(self, tags):
        context = 'http://www.w3.org/ns/anno.jsonld'
        
        headers = {}
        status_code = 200

        out = {
            '@context': context,
            'first': {
                'id': '',
                'items': [
                    {
                        'body': {
                            'value': tag[0]
                        },
                        'id': tag[1]
                    }
                    for tag
                    in tags
                ],
                'startIndex': 0,
                "type": "AnnotationTag"
            },
            'total': len(tags),
        }
        response = jsonify(out)
        response.mimetype = 'application/ld+json; profile="{}"'.format(context)

        # Add Etags for HEAD and GET requests
        if request.method in ['HEAD', 'GET']:
            response.add_etag()

        # Add headers
        self._add_link_headers(response, out)
        common_headers = getattr(self, 'headers', {})
        response.headers.extend(common_headers)
        if headers:
            response.headers.extend(headers)

        response.status_code = status_code
        return response
