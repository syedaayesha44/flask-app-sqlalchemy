# upload_images.py
from models import db, Image
from app import app

# Sample data: a list of dictionaries containing image paths and their corresponding Flipkart URLs
sample_images = [
    {'path': 'uploaded_images/image4.png', 'flipkart_url': 'https://www.flipkart.com/blue-dove-men-solid-casual-white-shirt/p/itm7aa2bbce9262f?pid=SHTHY9J7GKWKV7T9&lid=LSTSHTHY9J7GKWKV7T9CATLPX&marketplace=FLIPKART&q=clothes&store=clo%2Fash&srno=s_1_1&otracker=search&fm=Search&iid=en_K9ixFWpAEgbf-GvqIxOi_JCrVikaYkn6-an4h-ZiRrRDrezHIRCypqU7WuB8VpeO7Y_nwwPkcHGjdXDF2oMsFw%3D%3D&ppt=sp&ppn=sp&ssid=zxe8n6pagw0000001717330751384&qH=e7a80f49aaf2f65d'},
    {'path': 'uploaded_images/image5.png', 'flipkart_url': 'https://www.flipkart.com/samsung-108-cm-43-inch-full-hd-led-smart-tizen-tv-2023/p/itm1f514be8d5bad?pid=TVSGRS7GYVN3UZNZ&lid=LSTTVSGRS7GYVN3UZNZULGKSS&marketplace=FLIPKART&store=ckf%2Fczl&spotlightTagId=FkPickId_ckf%2Fczl&srno=b_1_2&otracker=browse&fm=Search&iid=d958d019-4447-4a48-859e-2ed07f0dded6.TVSGRS7GYVN3UZNZ.SEARCH&ppt=browse&ppn=browse&ssid=hixzsvqxog0000001717331117004'},
    {'path': 'uploaded_images/image6.png', 'flipkart_url': 'https://www.flipkart.com/np-toys-3-feet-sky-blue-imported-teddy-bear-91-cm-sky-blue-95/p/itm36daf0bca1322?pid=STFG9BD7SF8GTASN&lid=LSTSTFG9BD7SF8GTASN7Y5DKX&marketplace=FLIPKART&store=tng%2Fclb&srno=b_1_16&otracker=nmenu_sub_Baby%20%26%20Kids_0_Soft%20Toys&fm=Search&iid=af04efc2-7d63-487d-85b8-75ce0069cf65.STFG9BD7SF8GTASN.SEARCH&ppt=browse&ppn=browse&ssid=s0ds24u0qo0000001717331193589'}
]

# Create an app context before accessing the database
with app.app_context():
    # Create all tables (you should have db.create_all() somewhere in your app initialization code)
    db.create_all()
    
    # Add sample images to the database
    for image_data in sample_images:
        image = Image(path=image_data['path'], flipkart_url=image_data['flipkart_url'])
        db.session.add(image)
    
    # Commit the session to save the changes
    db.session.commit()

print("Sample images added to the database!")
