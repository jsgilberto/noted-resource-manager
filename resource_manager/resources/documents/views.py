from rest_framework.decorators import api_view
from resource_manager.resources.endpoints.utils import (
    Service
)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_update_delete_document(request, slug):
    """ Resource for getting a specific document or,
        updating a specific document or,
        deleting a specific document
    """

    if request.method == 'GET':
        s = Service(Service.DOCUMENTS, 'documents_get')
        response = s.make_request(request, path_params={"document_slug": slug})

    elif request.method in ['PUT', 'PATCH']:
        s = Service(Service.DOCUMENTS, 'documents_update')
        response = s.make_request(request, path_params={"document_slug": slug})
  
    elif request.method == 'DELETE':
        s = Service(Service.DOCUMENTS, 'documents_delete')
        response = s.make_request(request, path_params={"document_slug": slug})
    
    return response

@api_view(['GET', 'POST'])
def list_or_create_document(request):
    if request.method == 'GET':
        s = Service(Service.DOCUMENTS, 'documents_list')
        response = s.make_request(request)
    
    elif request.method == 'POST':
        s = Service(Service.DOCUMENTS, 'documents_create')
        response = s.make_request(request)
    
    return response