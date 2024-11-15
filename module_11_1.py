import requests
import pandas as pd
from PIL import Image, ImageOps

# Чтение CSV и фильтрация URL
url_data = pd.read_csv("urls.csv")
filtered_urls = url_data.loc[url_data["url"] == "https://api.thecatapi.com/v1/images/search"]

if filtered_urls.empty:
    print("Нет данных для обработки.")
else:
    image_list = []
    for _, row in filtered_urls.iterrows():
        for _ in range(3):  # Три изображения на URL
            response = requests.get(row["url"])
            if response.status_code == 200:
                cat_image_url = response.json()[0]["url"]
                image_response = requests.get(cat_image_url)
                if image_response.status_code == 200:
                    file_name = f"random_cat_{len(image_list) + 1}.jpg"
                    with open(file_name, "wb") as file:
                        file.write(image_response.content)
                    image_list.append(file_name)
                    print(f"Скачано: {file_name}")
            else:
                print(f"Ошибка при запросе: {response.status_code}")

# Обработка изображений
def process_and_save_image(image_path, output_path, size=(300, 300)):
    try:
        ImageOps.invert(Image.open(image_path).resize(size).convert("RGB")).save(output_path)
        print(f"Сохранено: {output_path}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Применение обработки
for img, out in zip(image_list, [f"output{i + 1}.jpg" for i in range(3)]):
    process_and_save_image(img, out)
