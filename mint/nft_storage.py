import time
import nft_storage
from nft_storage.api import nft_storage_api
from nft_storage.model.error_response import ErrorResponse
from nft_storage.model.upload_response import UploadResponse
from nft_storage.model.unauthorized_error_response import UnauthorizedErrorResponse
from nft_storage.model.forbidden_error_response import ForbiddenErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.nft.storage
# See configuration.py for a list of all supported configuration parameters.
configuration = nft_storage.Configuration(
    host = "https://api.nft.storage"
)