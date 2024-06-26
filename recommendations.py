from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def get_recommendations(product_id, products):
    product_df = pd.DataFrame(products)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(product_df['description'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    idx = product_df.index[product_df['id'] == product_id].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5 recommendations
    product_indices = [i[0] for i in sim_scores]
    return product_df.iloc[product_indices].to_dict('records')

def collaborative_filtering_recommendations(user_id):
    # Placeholder function for collaborative filtering recommendations
    recommendations = [
        {'name': 'Recommended Product 1', 'description': 'Description of Recommended Product 1', 'category': 'Electronics', 'price': 99.99, 'image_url':'https://images.fonearena.com/blog/wp-content/uploads/2020/01/Falkon-Aerbook-MarQ-Flipkart-laptop.jpg', 'flipkart_url':'https://www.flipkart.com/hp-pavilion-intel-core-i5-12th-gen-1235u-16-gb-512-gb-ssd-windows-11-home-14-dv2014tu-thin-light-laptop/p/itmb4b81cd1f873f?pid=COMGEG3ZNYZDAYVJ&lid=LSTCOMGEG3ZNYZDAYVJNYHV3Q'},
        {'name': 'Recommended Product 2', 'description': 'Description of Recommended Product 2', 'category': 'Home Appliances', 'price': 149.99, 'image_url':'https://rukminim2.flixcart.com/image/850/1000/xif0q/mobile/m/e/8/-original-imagbwx4mqamdbzj.jpeg?q=90', 'flipkart_url':'https://www.flipkart.com/redmi-note-11s-horizon-blue-64-gb/p/itm35daefaf408cb'},
        {'name': 'Recommended Product 3', 'description': 'Description of Recommended Product 3', 'category': 'Electronics', 'price': 199.99, 'image_url':'https://rukminim1.flixcart.com/image/832/832/keq058w0-0/headphone/0/b/d/103-wireless-boat-original-imafvccxgjypzgew.jpeg?q=70', 'flipkart_url':'https://www.flipkart.com/boat-103-wireless-bluetooth-headset/p/itmde6941010d8f1'},
        {'name': 'Recommended Product 4', 'description': 'Description of Recommended Product 4', 'category': 'Clothing', 'price': 49.99, 'image_url':'https://rukminim1.flixcart.com/image/1664/1664/coffee-maker/m/e/d/black-decker-dcm90-dcm90-original-imadsgkgvgbcc4gw.jpeg?q=90', 'flipkart_url':'https://www.flipkart.com/black-decker-dcm90-12-cups-coffee-maker/p/itmdsfuzye9dzxd8'},
        {'name': 'Recommended Product 5', 'description': 'Description of Recommended Product 5', 'category': 'Books', 'price': 29.99, 'image_url':'https://rukminim1.flixcart.com/image/1664/1664/vacuum-cleaner/u/8/n/kent-cyclonic-original-imaeggcpdxdzdykw.jpeg?q=90', 'flipkart_url':'https://www.flipkart.com/kent-kc-t3520-dry-vacuum-cleaner/p/itmegyqfhzqeghnz'}
    ]
    return recommendations
# recommendations.py

# recommendations.py

def get_laptop_recommendations(product_id):
    # Sample recommendation data for laptops
    return [
       
        { 
         'name':'Acer Predator Neo (2023) Intel Core i7 13th Gen 13700HX',
            'description':'Killer Performance The Acer Predator Helios Neo 16 laptop has a 13th Gen Intel Core i7 HX processor that enables you with quick and hybrid performance.',
            'category':'Laptop',
            'Price':99990,
            'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/computer/x/r/d/-original-imagp7w2wgf5ense.jpeg?q=70',
            'flipkart_url':'http://dl.flipkart.com/dl/msi-crosshair-16-hx-intel-core-i7-14th-gen-14700hx-16-gb-1-tb-ssd-windows-11-home-8-gb-graphics-nvidia-geforce-rtx-4060-d14vfkg-206in-gaming-laptop/p/itm2d94b1514f15c?',
        },
            {
            'name':'HP Victus Intel Core i7 13th Gen',
            'description':'High Gaming Immersion Powered by an AMD Ryzen processor and a high-performing graphics card, the HP Victus 15 Gaming Laptop ensures an immersive gaming experience.',
            'category':'Laptop',
            'price':62990,
            'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/computer/8/i/j/-original-imagthcbgurdzwuc.jpeg?q=70&crop=false' ,
            'flipkart_url':'http://dl.flipkart.com/dl/hp-victus-amd-ryzen-5-hexa-core-5600h-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-15-fb0135ax-gaming-laptop/p/itm740ddb5e8081e?'
            },
            {
            'name':'HP OMEN Intel Core i5 13th Gen',
            'description':'Powerful Processor This HP OMEN 16 gaming laptop comes with the 13th Gen Intel Core i5-13420H processor for smooth performance.',
            'category':'Laptop',
            'price':89990,
            'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/computer/f/3/h/-original-imagsnzbnbnyuf9b.jpeg?q=70',
            'flipkart_url':'http://dl.flipkart.com/dl/hp-omen-intel-core-i5-13th-gen-13420h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-4050-16-wd0880tx-gaming-laptop/p/itmf78f7125cef63?'
        },
        {
            'name': 'SAMSUNG Galaxy Book4 Pro',
            'description':'Dynamic AMOLED Present your ideas on the impressive 35.56 cm (14) display. Bright, vibrant colours, seamless scrolling',
            'category': 'Laptop',
            'price':173990,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/computer/a/8/6/-original-imagy4ruvwzjhc8x.jpeg?q=70',
            'flipkart_url':'http://dl.flipkart.com/dl/samsung-galaxy-book4-pro-evo-intel-core-ultra-7-155h-32-gb-1-tb-ssd-windows-11-home-np960xgk-lg3in-thin-light-laptop/p/itmae1ee075d0c48?'
        },
    {
            'name':'Avita Liber E Intel Core i3 12th Gen 1215U',
            'description':'designed for smooth performance',
            'category':'Laptop',
            'price':25990,
            'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/computer/n/n/k/liber-e-thin-and-light-laptop-avita-original-imagzw3nchhpnaqz.jpeg?q=70',
            'flipkart_url':'http://dl.flipkart.com/dl/avita-liber-e-intel-core-i3-12th-gen-1215u-8-gb-512-gb-ssd-windows-11-home-am15a2int56f-chf-thin-light-laptop/p/itm7b5db66b53509'
    },
    {
            'name':'ASUS VivoBook Ultra K14',
            'description':'Stylish and Functional This laptop comes with standout colours and a colour-blocking Enter key to add a touch of style to your daily life',
            'category':'Laptop',
            'price':58800,
            'image_url':'https://rukminim2.flixcart.com/image/300/300/krayqa80/computer/l/o/d/na-thin-and-light-laptop-asus-original-imag54k7pc2tdath.jpeg?q=90',
            'flipkart_url':'http://dl.flipkart.com/dl/asus-vivobook-ultra-k14-2021-amd-ryzen-5-hexa-core-r5-5500u-8-gb-512-gb-ssd-windows-10-home-km413ua-eb503ts-thin-light-laptop/p/itm116d42a8cd657?'
        }



    ]

def get_smartphone_recommendations(product_id):
    # Sample recommendation data for smartphones
    return [
        {
            'name': 'SAMSUNG Galaxy F15',
            'description': '6 GB RAM | 128 GB ROM | Expandable Upto 1 TB , 16.51 cm (6.5 inch) Full HD+ Display',

            'category': 'Smartphone',
            'price': 144999,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/k/8/n/-original-imagymhwtgmdr3v2.jpeg?q=70',
            'flipkart_url': 'https://www.flipkart.com/samsung-galaxy-f15-5g-ash-black-128-gb/p/itm3886145398f59?pid=MOBGYBAVBQ86QKJT&lid=LSTMOBGYBAVBQ86QKJTGZ1L1V&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_203aae66-5c5f-4fa5-a03a-c13071d977b0_1_1BUWY8OBA8L9_MC.MOBGYBAVBQ86QKJT&ppt=pp&ppn=pp&ssid=352e3vve3k0000001717319744568&otracker=clp_pmu_v2_Latest%2BSamsung%2Bmobiles%2B_3_1.productCard.PMU_V2_SAMSUNG%2BGalaxy%2BF15%2B5G%2B%2528Ash%2BBlack%252C%2B128%2BGB%2529_samsung-mobile-store_MOBGYBAVBQ86QKJT_neo%2Fmerchandising_2&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Latest%2BSamsung%2Bmobiles%2B_LIST_productCard_cc_3_NA_view-all&cid=MOBGYBAVBQ86QKJT'
        },
        {
            'name': 'SAMSUNG Galaxy A14 ',
            'description': '5G (Black, 128 GB)  (6 GB RAM)',
            'category': 'Smartphone',
            'price': 15999,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/p/w/b/-original-imagmefcaj26vdhg.jpeg?q=70',
            'flipkart_url': 'https://www.flipkart.com/samsung-galaxy-a14-5g-black-128-gb/p/itm4e53e4bf801e1?pid=MOBGHT8UR4T25NGB&lid=LSTMOBGHT8UR4T25NGBLLYADS&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_203aae66-5c5f-4fa5-a03a-c13071d977b0_5_AYSX42C7U6_MC.MOBGHT8UR4T25NGB&ppt=pp&ppn=pp&ssid=352e3vve3k0000001717319744568&otracker=clp_pmu_v2_Samsung%2BMobile%2Bunder%2B%25E2%2582%25B920K_3_5.productCard.PMU_V2_SAMSUNG%2BGalaxy%2BA14%2B5G%2B%2528Black%252C%2B128%2BGB%2529_samsung-mobile-store_MOBGHT8UR4T25NGB_neo%2Fmerchandising_2&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Samsung%2BMobile%2Bunder%2B%25E2%2582%25B920K_LIST_productCard_cc_3_NA_view-all&cid=MOBGHT8UR4T25NGB'
        },
        # Add more smartphone recommendations as needed
        {
            'name': 'Motorola Edge 50 Fusion',
            'description': '50 MP Ultra Pixel OIS Camera with Sony - LYTIA 700C Senor',
            'category': 'Smartphone',
            'price':24999,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/5/t/j/edge-50-fusion-pb300002in-motorola-original-imahywzrfagkuyxx.jpeg?q=70',
            'flipkart_url': 'http://dl.flipkart.com/dl/motorola-edge-50-fusion-marshmallow-blue-256-gb/p/itmd2b59acc725cf?'
        },
        {
            'name': 'Apple iPhone 15 (blue,128gb)',
            'description': 'Dynamic Island bubbles up alerts and Live Activities — so you don’t miss them while you’re doing something else.',
            'category': 'Smartphone',
            'price': 64999,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/k/l/l/-original-imagtc5fz9spysyk.jpeg?q=70',
            'flipkart_url': 'http://dl.flipkart.com/dl/apple-iphone-15-blue-128-gb/p/itmbf14ef54f645d?'
        },
        {
            'name': 'POCO C65 (Pastel Green, 128 GB)  (4 GB RAM)',
            'description':'Large Display The POCO C65 smartphone comes with a large display and a fast 90 Hz refresh rate to deliver exceptional visuals. ',
            'category': 'Smartphone',
            'price': 6799,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/g/1/p/-original-imagy2v5kfnq97xn.jpeg?q=70',
            'flipkart_url': 'http://dl.flipkart.com/dl/poco-c65-pastel-green-128-gb/p/itm534cf85baf789?'

        }
        




    ]

def get_vacuum_cleaner_recommendations(product_id):
  
    return [
        {
            'name': 'Karcher WD 3 V 15/4/20',
            'description': 'A powerful and efficient vacuum cleaner ,3 filterarion layer',
            'category': 'Vacuum Cleaner',
            'price': 1499,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/vacuum-cleaner/c/t/d/-original-imagzjdp6zg37ywu.jpeg?q=70',
            'flipkart_url': 'https://www.flipkart.com/karcher-wd-3-v-15-4-20-wet-dry-vacuum-cleaner/p/itmb366df11e5d3d?pid=VCLGKGZY9MCEGSJY&lid=LSTVCLGKGZY9MCEGSJY6SVRN7&marketplace=FLIPKART&q=vaccum+cleaner&store=j9e%2Fabm%2Ful2&srno=s_1_1&otracker=search&otracker1=search&fm=neo%2Fmerchandising&iid=en_5aZ9FQa7-_pPhihh--_2aDr4AJwwVlDACTmx0oQy_6d_xP0GdZDqZJ2IZTWIVS3ZkoxTaSi3EtZtKPlwk3nYrPUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=pp&ppn=pp&ssid=5nrsbtq5dc0000001717327792306&qH=e64a90cec0cf961b'
        },

        {
            'name': 'KENT 116133-Vortex Wet & Dry Wet & Dry Vacuum Cleaner with Reusable Dust Bag',
            'description': 'A lightweight and easy-to-use vacuum cleaner',
            'category': 'Vacuum Cleaner',
            'price': 4399,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/vacuum-cleaner/q/r/d/116133-vortex-wet-dry-kent-original-imagtbf8uh6jm8js.jpeg?q=70',
            'flipkart_url': 'https://www.flipkart.com/kent-116133-vortex-wet-dry-vacuum-cleaner-reusable-dust-bag/p/itma8cde1924e69a?pid=VCLGTBF8EQXTAGFB&lid=LSTVCLGTBF8EQXTAGFBLBYJ5Y&marketplace=FLIPKART&q=vaccum+cleaner&store=j9e%2Fabm%2Ful2&srno=s_1_12&otracker=search&otracker1=search&fm=neo%2Fmerchandising&iid=en_5aZ9FQa7-_pPhihh--_2aDr4AJwwVlDACTmx0oQy_6f65eE8mcMswcugP7UCdSDINhC2bPFDGtX9bfIL5WVKqZ2-SIbIDZ6lLvgRS75Tj4w%3D&ppt=pp&ppn=pp&ssid=5nrsbtq5dc0000001717327792306&qH=e64a90cec0cf961b'
        },
        {
            'name': 'AGARO REGAL Lite Plus Hand Held Vacuum Cleaner, Handheld & Stick, 700W, Dry Vacuuming Hand-held Vacuum Cleaner  (Black)',
            'description': 'AGARO Regal Lite Plus vacuum cleaner is a 700 watts handheld vacuum cleaner which lets you utilize it conveniently and clean your home quickly. ',
            'category': 'Vacuum Cleaner',
            'price': 1899,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/vacuum-cleaner/n/l/2/regal-lite-plus-hand-held-vacuum-cleaner-handheld-stick-700w-dry-original-imahy4zyzsh8q9my.jpeg?q=70&crop=false',
            'flipkart_url': 'http://dl.flipkart.com/dl/agaro-regal-lite-plus-hand-held-vacuum-cleaner-handheld-stick-700w-dry-vacuuming-hand-held-cleaner/p/itm4f384a859990b?'
        },
        {
            'name': 'PHILIPS FC9352/01 (883935201280) Bagless Dry Vacuum Cleaner with Powerful Suction,Turbo Brush (Blue)',
            'description': 'PowerPro Compact bagless vacuum cleaner provides strong suction power for top cleaning results .',
            'category': 'Vacuum Cleaner',
            'price': 8999,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/vacuum-cleaner/l/e/t/-original-imahy8dcqjzah4ae.jpeg?q=70&crop=false',
            'flipkart_url': 'http://dl.flipkart.com/dl/philips-fc9352-01-883935201280-bagless-dry-vacuum-cleaner-powerful-suction-turbo-brush/p/itm0ea00c5be24c8?'
        },
        {
            'name': 'Eureka Forbes bold wet and dry vacuum cleaner ',
            'description': 'Wet and Dry Cleaning Is the surface you are trying to clean wet? If yes, you have nothing to worry as this vacuum cleaner can clean both wet and dry surfaces.',
            'category': 'Vacuum Cleaner',
            'price': 5999,
            'image_url': 'https://rukminim2.flixcart.com/image/312/312/xif0q/vacuum-cleaner/l/e/t/-original-imahy8dcqjzah4ae.jpeg?q=70&crop=false',
            'flipkart_url': 'http://dl.flipkart.com/dl/eureka-forbes-bold-wet-dry-vacuum-cleaner/p/itm5a1c0501fa6e0?'
        }
        # Add more vacuum cleaner recommendations as needed
      ]


def get_cloth(product_id):
    # Sample recommendation data for Clothes
    return [
     {
    'name':'Baby Boys & Baby Girls Casual T-shirt Shorts',
    'description':'kids clothing set pack of 3 Baby boy clothing set, Boys ke kapde, kids clothing set, children clothing wear, kids wear,1 year boy clothes',
    'category':'kids clothes',
    'price':454,
    'image_url':'https://rukminim2.flixcart.com/image/612/612/xif0q/kids-apparel-combo/z/o/z/3-4-years-ay-t28-mr-t28-af-t33-blmrwh-kidisland-original-imagnmhy9wfh3sdj.jpeg?q=70',
    'flipkart_url':'http://dl.flipkart.com/dl/kidisland-baby-boys-girls-casual-t-shirt-shorts/p/itm8a98db4085627?'
    },
    {
    'name':'Women Cotton Rayon Kurta Pant Set',
    'description':'Beautiful embroidered suit sets with priented pink dupatta ',
    'category':'Women cotton clothes',
    'price':671,
    'image_url':'https://rukminim2.flixcart.com/image/571/571/xif0q/ethnic-set/h/g/p/xl-b-265611-menwal-collection-original-imahyzdhm3cegamw.jpeg?q=70&crop=false',
    'flipkart_url':'https://dl.flipkart.com/dl/menwal-collection-women-kurta-pant-set/p/itmbf0561efded25?'
    },
    {
    'name':'Embroidered Bollywood Georgette Saree ',
    'description':'Elaborate Design,Adorned with an intricate embroidered pattern, this women’s Bollywood saree emanates grace and allure.',
    'category':'saree',
    'price':549,
    'image_url':'https://rukminim2.flixcart.com/image/3024/3024/xif0q/sari/j/n/h/free-r-kaju-red-rosyqueen-unstitched-original-imaghf9cxztuhebn.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/nerta-boutique-embroidered-bollywood-georgette-saree/p/itm272feea99d6e5?'
    },
    {
    'name':'Floral Print Georgette Stitched Flared/A-line Gown',
    'description':'The beautiful printed georgette gown with dupatta for women. Women can buy this gown set to wear for their upcoming functions, reception, occasions and daily life.',
    'category':'dress',
    'price':690,
    'image-url':'https://rukminim2.flixcart.com/image/569/569/xif0q/gown/v/e/e/na-l-full-sleeve-stitched-me-netra-qvazor-na-original-imagrptycyhaefkj.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/qvazor-flared-a-line-gown/p/itm4820341e071f3?'
    }
    ]
    
def get_jwell(product_id):
    # Sample recommendation data for Jewellery
    return [
    {
    'name':'Brass, Copper Gold-plated Gold Jewel Set ',
    'description':'Durable Brass Necklace Set, This set is crafted from extremely durable brass material, which means that it is ideal to withstand heavy usage, wear and tear, as well as can strongly hold on to the stone embellishments on the pieces.',
    'category':'Jewellery',
    'price':237,
    'image_url':'https://rukminim2.flixcart.com/image/1330/1330/xif0q/jewellery-set/b/q/v/na-na-1-matte-choker-101-a-rofarword-original-imahyz3y2hn55fyc.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/rofarword-brass-copper-gold-plated-gold-jewellery-set/p/itmfcf5090fc929d?'
    },
    {
    'name':'Brass Gold-plated Gold, Pink Jewel Set',
    'description':'Ideal for Party WearMake a statement at your next event with this perfect jewellery set from Brado Jewellery',
    'category':'jewellery',
    'price':179,
    'image_url':'https://rukminim2.flixcart.com/image/2000/2000/xif0q/jewellery-set/3/c/h/d-na-2-ats-jewellery-set-001-brado-jewellery-original-imagp8vutaty44zj.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/brado-jewellery-brass-gold-plated-gold-pink-set/p/itmf74491f3558cc?'
    },
    {
    'name':'Alloy Gold-plated Gold Jewel Set ',
    'description':'Necklace and 2 Earring set For Women & Girls made with Finest Copper Brass Quality and Gold Platting. Product become Long lasting',
    'category':'jewellery',
    'price':122,
    'image_url':'https://rukminim2.flixcart.com/image/991/991/xif0q/jewellery-set/c/m/i/na-plastic-1-red-ad-mj-diksha-collection-original-imagqmxwtwmgefzz.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/diksha-collection-alloy-gold-plated-gold-jewellery-set/p/itm2496a5be41f4b?'
},
{
'name':'Alloy Gold-plated Gold Jewel Set',
'description':'Shimmering FinishFeaturing an attractive gold-plated finish, the M Creation Gold-plated Jewellery Set exudes a radiant allure',
'category':'jewellery',
'price':279,
'image_url':'https://rukminim2.flixcart.com/image/1076/1076/xif0q/jewellery-set/r/l/d/na-na-1-mc-c-7-t-watch-m-creation-original-imahf4j4zrjvehft.jpeg?q=70&crop=false',
'flipkart_url':'http://dl.flipkart.com/dl/m-creation-alloy-gold-plated-gold-jewellery-set/p/itm8ea27ed06eaf0?'
}
    ]
def get_smartwatch(product_id):
    # Sample recommendation data for smartwatches
    return [
    {
    'name':'Fastrack Revoltt FS1 Pro',
    'description':'High-quality Display Boasting up to a 4.978 cm (1.96) Super AMOLED arched display, the Fastrack Revoltt FS1 Pro Smartwatch provides clear and vibrant visuals',
    'category':'smartwatches',
    'price':1799,
    'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/smartwatch/q/i/r/-original-imagu7kzfk3kuc9j.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/fastrack-revoltt-fs1-pro-world-s-first-1-96-super-amoled-highest-resolution-bt-calling-smartwatch/p/itm868a2831ed59a?'
    },
{
'name':'Boult Striker+ 1.39" HD, BT Calling, Zinc Alloy Frame, 150+ Watch Faces, SpO2 Tracking Smartwatch ',
'description':'Make heads turn while being on top of your game with the Ultimate Trailblazer, the Boult Striker+ smartwatch. Featuring a stunning 1.39-inch Round HD Screen with thin bezels and various strap options in Black, Blue, White, and Emerald, this watch is as stylish as it is functional',
'category':'smartwatch',
'price':1299,
'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/smartwatch/u/d/d/-original-imagqz55yfbxq6nk.jpeg?q=70&crop=false',
'flipkart_url':'http://dl.flipkart.com/dl/boult-striker-1-39-hd-bt-calling-zinc-alloy-frame-150-watch-faces-spo2-tracking-smartwatch/p/itm23cfbb96d1fbb?'
},
{
'name':'boAt Wave Flex Connect with 1.83" HD Display,Bluetooth Calling & Premium Metal Design Smartwatch',
'description':'The boAt Wave Flex Connect is the next companion for your fitness transformation and is here to make life easy',
'category':'smartwatch',
'price':1399,
'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/smartwatch/y/q/q/-original-imagxp8tzzwyhkzr.jpeg?q=70&crop=false',
'flipkart_url':'http://dl.flipkart.com/dl/boat-wave-flex-connect-1-83-hd-display-bluetooth-calling-premium-metal-design-smartwatch/p/itm58a6e023a791e?'
},
{
'name':'Fire-Boltt Epic Plus with1.83" 2.5D Curved Glass,SPO2, Heart Rate tracking, Touchscreen Smartwatch ',
'description':'High-grade Display Featuring an up to 4.648 cm (1.83) full touch HD display with a high-resolution of up to 240x286p and 2.5D curved glass,',
'category':'smartwatch',
'price':999,
'image':'https://rukminim2.flixcart.com/image/312/312/xif0q/smartwatch/w/a/s/-original-imagxp8tahhvghys.jpeg?q=70&crop=false',
'flipkart_url':'http://dl.flipkart.com/dl/fire-boltt-epic-plus-with1-83-2-5d-curved-glass-spo2-heart-rate-tracking-touchscreen-smartwatch/p/itm681ecd1fc9d01?'
}
]
def get_book(product_id):
    # Sample recommendation data for books
    return [
    {
    'name':'ACE QUANT A Complete Guide On Quantitative Aptitude For Banking & Insurance Examinations',
    'description':'Quantitative Aptitude Book for Bank and Insurance Exams: ADDA 247 is launching a complete and comprehensive Book on "Quantitative Aptitude',
    'category':'Books',
    'price':309,
    'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/regionalbooks/m/o/s/-original-imagsn7gsqjyp5ja.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/ace-quant-complete-guide-quantitative-aptitude-banking-insurance-examinations/p/itm93b47f602f5f5?'
    },
    {
    'name':'CSSC Reasoning 7200 TCS MCQ Chapter Wise 6th Edition Hindi Medium',
    'description':'all latest TCS questions are asked in SSC exams. This book is updated till Feb 2024.',
    'category':'books',
    'price':489,
    'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/book/i/e/8/ssc-english-7200-tcs-mcq-chapter-wise-with-detailed-explanation-original-imagxwz8vjsekhdh.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/ssc-reasoning-7200-tcs-mcq-chapter-wise-6th-hindi-medium/p/itm4f50815661f0d?'
    },
    {
    'name':'Bharat Ka Sanvidhan - The Constitution Of India',
    'description':'r Babasaheb Ambedkar, the famous book “The Constitution of India” explains the supreme law of India',
    'category':'Books',
    'price':498,
    'image_url':'https://rukminim2.flixcart.com/image/312/312/kg9qbgw0/regionalbooks/2/f/m/bharat-ka-sanvidhan-the-constitution-of-india-original-hindi-original-imafwjggfsmpqfpu.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/bharat-ka-sanvidhan-constitution-india-hindi/p/itm5b20b72effc6c?'
    },
    {
    'name':'BRAHMASTRA Complete Maths Multicolored Formula Book Second Edition BILINGUAL',
    'description':'BRAHMASTRA Complete Maths Formula Book” is a comprehensive guide that has been designed to help students acquainted with the latest pattern and difficulty level of the exam',
    'category':'Books',
    'price':205,
    'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/regionalbooks/f/s/2/-original-imahffz6yzhyqvfq.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/brahmastra-complete-maths-multicolored-formula-book-second-bilingual/p/itmd6d06bf7fa4b5?',
    },
    {
    'name':'Oswaal ICSE Question Bank Class 9 Commercial Studies | Chapterwise | Topicwise | Solved Papers | For 2025 Exams',
    'description':': We have got you covered with the latest and 100% updated curriculum •Crisp Revision with Topic-wise Revision Notes & Smart Mind Maps: Study smart, not hard! •Extensive Practice with 500+ Questions & Self',
    'category':'Books',
    'price':299,
    'image_url':'https://rukminim2.flixcart.com/image/312/312/xif0q/book/q/z/k/oswaal-icse-question-bank-class-9-english-paper-2-chapterwise-original-imagyr6cypkhudrg.jpeg?q=70&crop=false',
    'flipkart_url':'http://dl.flipkart.com/dl/oswaal-icse-question-bank-class-9-commercial-studies-chapterwise-topicwise-solved-papers-2025-exams/p/itm82ac1203c3bc8?'
    }
    ]
def get_headfon(product_id):
    return[
        
    ]