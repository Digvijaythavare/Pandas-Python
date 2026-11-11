
import pandas as pd
import random

products = [
    'Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch',
    'Camera', 'Printer', 'Monitor', 'Keyboard', 'Mouse',
    'Speaker', 'Router', 'External Hard Drive', 'USB Flash Drive', 'Webcam'
]

categories = [
    'Electronics', 'Accessories', 'Peripherals', 'Networking', 'Storage',
    'Audio', 'Video', 'Wearables', 'Computing', 'Mobile Devices'
]

data = []

for i in range(100):
    data.append({
        "Product_Id": f"p{i+1:03}",
        "Product_Name": random.choice(products),
        "Category": random.choice(categories),
        "Quantity": random.randint(1, 20),
        "Price": random.randint(50, 1500)
    })

df = pd.DataFrame(data)

file_path = "products_dataset.xlsx"

df.to_csv(file_path, index=False)

print(df)
print("\nDataset saved successfully!")
