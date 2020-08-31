import pytest

# Documentation https://dog.ceo/dog-api/documentation/


def test_get_list_all_breeds(api_client, get_expected_response):
    """
    List all breeds.
    """

    r = api_client.get(path="/breeds/list/all")
    actual_response = r.json()
    expected_response = get_expected_response("test_get_list_all_breeds")

    assert r.status_code == 200
    assert actual_response == expected_response


def test_get_breeds_random_image(
    api_client, get_expected_response, get_image_info
):
    """
    Display a single random image from all dogs collection.
    """

    r = api_client.get(path="/breeds/image/random")
    actual_response = r.json()
    image_url, image_format = get_image_info(actual_response)
    expected_response = get_expected_response("test_get_breeds_random_image")
    expected_response["message"] = image_url

    assert r.status_code == 200
    assert image_format == "JPEG"
    assert actual_response == expected_response


@pytest.mark.parametrize(
    "actual_images_count, expected_images_count",
    [(-1, 1), (0, 1), (1, 1), (2, 2), (50, 50), (51, 50), ("test", 1)],
)
def test_get_breeds_random_images(
    api_client,
    get_expected_response,
    get_image_info,
    actual_images_count,
    expected_images_count,
):
    """
    Display multiple random images from all dogs collection.
    """

    r = api_client.get(path=f"/breeds/image/random/{actual_images_count}")
    actual_response = r.json()
    images_list = actual_response["message"]
    response_images_count = len(images_list)

    for image in images_list[:5]:
        image_url, image_format = get_image_info(actual_response)
        assert image_format == "JPEG"

    expected_response = get_expected_response("test_get_breeds_random_images")
    expected_response["message"] = images_list

    assert r.status_code == 200
    assert response_images_count == expected_images_count
    assert actual_response == expected_response


@pytest.mark.parametrize(
    "breed_name_path, breed_name_image, response_file_name",
    [
        ("hound", "hound", "test_get_all_images_by_breed_hound"),
        (
            "terrier",
            "terrier-",
            "test_get_all_images_by_breed_terrier",
        ),
        (
            "terrier/fox",
            "terrier-fox",
            "test_get_all_images_by_breed_terrier_fox",
        ),
    ],
)
def test_get_all_images_by_breed_200(
    api_client,
    get_expected_response,
    get_image_info,
    breed_name_path,
    breed_name_image,
    response_file_name,
):
    """
    Returns an array of all the images from a breed, e.g. hound, or sub-breed,
    e.g. terrier-fox.
    """

    r = api_client.get(path=f"/breed/{breed_name_path}/images")
    actual_response = r.json()
    expected_response = get_expected_response(response_file_name)
    images_list = actual_response["message"]

    for image in images_list[:5]:
        image_url, image_format = get_image_info(actual_response)
        assert image_format == "JPEG"

    assert r.status_code == 200
    assert breed_name_image in image_url
    assert actual_response == expected_response


@pytest.mark.parametrize(
    "breed_name_path, response_file_name",
    [
        ("test", "test_get_all_images_by_breed_404"),
        ("terrier/test", "test_get_all_images_by_sub_breed_404"),
    ],
)
def test_get_all_images_by_breed_404(
    api_client, get_expected_response, breed_name_path, response_file_name
):
    """
    Returns 404 if breed or sub-breed doesn't exist.
    """

    r = api_client.get(path=f"/breed/{breed_name_path}/images")
    actual_response = r.json()
    expected_response = get_expected_response(response_file_name)

    assert r.status_code == 404
    assert actual_response == expected_response


@pytest.mark.parametrize(
    "breed_name_path, breed_name_image",
    [("hound", "hound"), ("terrier/fox", "terrier-fox")],
)
def test_get_random_image_by_breed(
    api_client,
    get_expected_response,
    get_image_info,
    breed_name_path,
    breed_name_image,
):
    """
    Returns a random dog image from a breed, e.g. hound, or sub-breed,
    e.g. terrier-fox.
    """

    r = api_client.get(path=f"/breed/{breed_name_path}/images/random")
    actual_response = r.json()
    image_url, image_format = get_image_info(actual_response)
    expected_response = get_expected_response("test_get_random_image_by_breed")
    expected_response["message"] = image_url

    assert r.status_code == 200
    assert image_format == "JPEG"
    assert breed_name_image in image_url
    assert actual_response == expected_response


@pytest.mark.parametrize(
    "actual_images_count, expected_images_count",
    [
        (-1, 10),
        (0, 1),
        (1, 1),
        (2, 2),
        (100, 100),
        ("test", 1),
    ],
)
@pytest.mark.parametrize(
    "breed_name_path, breed_name_image",
    [("terrier", "terrier"), ("terrier/fox", "terrier-fox")],
)
def test_get_random_multiple_images_by_breed(
    api_client,
    get_expected_response,
    get_image_info,
    breed_name_path,
    breed_name_image,
    actual_images_count,
    expected_images_count,
):
    """
    RReturn multiple random dog image from a breed, e.g. hound, or sub-breed,
    e.g. terrier-fox.
    """

    r = api_client.get(
        path=f"/breed/{breed_name_path}/images/random/{actual_images_count}"
    )
    actual_response = r.json()
    images_list = actual_response["message"]
    response_images_count = len(images_list)

    for image in images_list[:5]:
        image_url, image_format = get_image_info(actual_response)
        assert image_format == "JPEG"

    expected_response = get_expected_response(
        "test_get_random_multiple_images_by_breed"
    )
    expected_response["message"] = images_list

    assert r.status_code == 200
    assert response_images_count == expected_images_count
    assert actual_response == expected_response


@pytest.mark.parametrize(
    "breed_name_path, response_file_name",
    [
        ("hound", "test_get_list_all_sub_breeds_hound"),
        (
            "vizsla",
            "test_get_list_all_sub_breeds_vizsla",
        ),
    ],
)
def test_get_list_all_sub_breeds_200(
    api_client, get_expected_response, breed_name_path, response_file_name
):
    """
    Returns an array of all the sub-breeds from a breed.
    """

    r = api_client.get(path=f"/breed/{breed_name_path}/list")
    actual_response = r.json()
    expected_response = get_expected_response(response_file_name)

    assert r.status_code == 200
    assert actual_response == expected_response


def test_get_list_all_sub_breeds_404(api_client, get_expected_response):
    """
    Returns 404 if sub-breed doesn't exist.
    """
    r = api_client.get(path="/breed/test/list")
    actual_response = r.json()
    expected_response = get_expected_response(
        "test_get_list_all_sub_breeds_404"
    )

    assert r.status_code == 404
    assert actual_response == expected_response
