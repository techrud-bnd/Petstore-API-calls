import random
import petstore_api
from petstore_api.rest import ApiException

# Configure the api client host
configuration = petstore_api.Configuration(
    host="https://petstore.swagger.io/v2"
)

with petstore_api.ApiClient(configuration) as api_client:
    pet_api = petstore_api.PetApi(api_client)

# Unique ID
    stored_pet_id = random.randint(100000, 999999)

# POST /pet - Create pet
    print("--- POST /pet ---")
    new_pet = petstore_api.Pet(
        id=stored_pet_id,
        name="Callie",
        photo_urls=["http://example.com/photo.jpg"],
        status="available"
    )

    try:
        post_response = pet_api.add_pet(body=new_pet)
        print(f"Successfully sent POST /pet.")
        print(f"Stored Pet ID: {stored_pet_id}\n")
        print(f"Response: {post_response}\n")
    except ApiException as e:
        print(f"Exception during POST /pet: {e}\n")
        exit(1)

# PUT /pet - Update pet
    print("--- PUT /pet ---")
    updated_pet = petstore_api.Pet(
        id=stored_pet_id,
        name="Callie the Pooch",
        photo_urls=["http://example.com/photo.jpg"],
        status="sold"
    )

    try:
        put_response = pet_api.update_pet(body=updated_pet)
        print(f"Successfully updated pet.")
        print(f"Stored Pet ID: {stored_pet_id}\n")
        print(f"Response: {put_response}\n")
    except ApiException as e:
        print(f"Exception during PUT /pet: {e}\n")

# GET /pet/{petId} - Fetch pet by ID
    print(f"--- GET /pet/{stored_pet_id} ---")
    try:
        get_response = pet_api.get_pet_by_id(pet_id=stored_pet_id)
        print("Successfully retrieved pet details.\n")
        print(f"Response: {get_response}\n")
    except ApiException as e:
        print(f"Exception during GET /pet/{stored_pet_id}: {e}\n")
