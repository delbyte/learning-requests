import requests

def get_image_metadata(image_key):
    url = f"https://a.mapillary.com/v3/images/{image_key}"
    params = {
        'client_id': 'YOUR_MAPILLARY_CLIENT_ID'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        metadata = response.json()
        return metadata
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    image_key = 'YOUR_IMAGE_KEY'
    metadata = get_image_metadata(image_key)
    if metadata:
        print("Image Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()

