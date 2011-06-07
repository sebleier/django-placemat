
from hashlib import sha1 as sha
import json
import os
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template.loaders.filesystem import Loader

try:
    import json
except ImportError:
    from django.utils import simplejson as json

def json_view(func):
    def wrap(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        data = json.dumps(response)
        return HttpResponse(data, mimetype='application/json')
    return wrap


loader = Loader()
@json_view
def template_with_hash(request, path):
    template_path = os.path.join('fragments', path)
    content = loader.load_template_source(template_path)
    digest = sha(content[0]).hexdigest()
    return {
        'hash': digest,
        'template': content[0],
    }



