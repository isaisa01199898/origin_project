from serpapi import GoogleSearch
import urllib.request
params = {
    "engine": "google_images",  # ← Google画像検索を指定
    "q": "吉田松陰",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "api_key": "ad05af9e948cb95d6f4e2cf9082e6568a9a98682cc2374e6d218848cfaf46b0f"
}

search = GoogleSearch(params)
results = search.get_dict()

images_results = results.get("images_results", [])

if images_results:
    first_img = images_results[0]
    first_img_url = first_img.get("original")
    print(first_img_url)
    if first_img_url:
        print(first_img_url)
        safe_url = urllib.parse.quote(first_img_url, safe=':/?=&')
        save_path = r"C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/ground_v5.0.png"
        urllib.request.urlretrieve(safe_url, save_path)
        print("画像保存完了:", save_path)
    else:
        print("eee")
else:
    print("iie")





