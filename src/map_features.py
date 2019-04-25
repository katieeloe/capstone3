import json
import pandas as pd
import numpy as np
from multi_key_dict import multi_key_dict


def dummify_features(recipes_json):

    ingredient_dict = multi_key_dict()

    # Baking
    ingredient_dict['active yeast', 'bread machine yeast', 'dry yeast', 'instant yeast', 'nutritional yeast',
                    'yeast'] = 'yeast'
    ingredient_dict['baking powder', 'cream of tartar'] = 'baking_powder'
    ingredient_dict['baking soda', 'bicarbonate of soda'] = 'baking_soda'
    ingredient_dict['alcohol free vanilla flavor', 'bourbon vanilla extract', 'colher de de essência de baunilha'] = 'vanilla_extract'
    ingredient_dict['food coloring','food colourings','food dye', 'green food color','green food coloring',
                    'red food coloring','yellow food color','yellow food coloring', 'achiote'] = 'food_coloring'
    ingredient_dict['vanilla','vanilla extract','vanilla bean','vanilla bean paste','vanilla paste','vanilla pod'] = 'vanilla'
    ingredient_dict['coconut', 'flake coconut', 'unsweetened coconut flakes', 'unsweetened dried coconut',
                    'unsweetened shredded coconut', 'sweetened coconut','sweetened coconut flakes',
                    'sweetened shredded coconut','coconut extract'] = 'coconut'

    # Misc
    ingredient_dict['all-bran cereal', 'cereal', 'corn flakes', 'cornflakes', 'crisp rice cereal', 'rice chex',
                    'rice krispies cereal'] = 'cereal'
    ingredient_dict['chex snack mix'] = 'chex'
    ingredient_dict['granola'] = 'granola'
    ingredient_dict['angostura bitters', 'bitters', 'orange bitters'] = 'bitters'
    ingredient_dict['blackberry jam','pineapple jam','strawberry jam','strawberry preserves','raspberry jam',
                    'cherry jam','apricot jam','apricot preserves','apple jelly', 'jam','jelly', 'grape jelly',
                    'orange marmalade'] = 'fruit_preserve'
    ingredient_dict['champagne vinegar', 'malt vinegar','unseasoned rice wine vinegar','vinegar','white vinegar',
                    'white wine vinegar','white distilled vinegar','wine vinegar','red wine vinegar',
                    'sherry vinegar','rice vinegar','rice wine vinegar','seasoned rice vinegar',
                    'apple cider vinegar', 'cider vinegar'] = 'vinegar'
    ingredient_dict['condensed cream of mushroom soup', 'cream of chicken soup', 'cheddar cheese soup',
                    'cheese soup'] = 'cream_soup'
    ingredient_dict['fried onions'] = 'fried_onion'
    ingredient_dict['ice', 'ice cubes'] = 'ice'
    ingredient_dict['water','ice water'] ='water'
    ingredient_dict['liquid smoke'] = 'liquid_smoke'
    ingredient_dict['mac & cheese', 'macaroni'] = 'mac&cheese'
    ingredient_dict['maple extract','maple flavoring','maple syrup'] = 'maple'
    ingredient_dict['maraschino cherries','maraschino liqueur','grenadine'] = 'maraschino'
    ingredient_dict['microwave popcorn', 'popcorn','popped corn',
                    'sacos de pipoca de microondas ou 9 xícaras de de pipoca pronta'] = 'popcorn'
    ingredient_dict['mid-sized skewers', 'wooden skewers'] = 'skewer'
    ingredient_dict['vanilla powder','vanilla protein powder','soy protein','soy protein powder'] = 'protein_powder'
    ingredient_dict['polenta'] = 'polenta'
    ingredient_dict['brine'] = 'brine'

    # Fruits
    ingredient_dict['dried apricots','dried cherries','dried cranberries','dried fruit',
                    'sweetened dried cranberries','raisins','golden raisins'] = 'dried_fruit'
    ingredient_dict['whole berry cranberry sauce','whole cranberry sauce'] = 'cranberry_sauce'
    ingredient_dict['peach','peaches', 'peach nectar','peach schnapps'] = 'peach'
    ingredient_dict['rhubarb'] = 'rhubarb'
    ingredient_dict['pineapple','pineapple chunks','pineapple in juice','pineapple juice'] = 'pineapple'
    ingredient_dict['pomegranate arils','pomegranate juice','pomegranate seeds','pomegranates',
                    'seeds of pomegranate'] = 'pomegranate'
    ingredient_dict['mango','mangoes','mangos', 'mango chutney','mango puree'] = 'mango'
    ingredient_dict['lemon peel', 'lemon zest', 'orange peel','orange zest', 'lime peel', 'lime zest',
                    'finely grated lime zest'] = 'citrus_zest'
    ingredient_dict['juice of lemon', 'lemon', 'lemon juice', 'lemons', 'meyer lemon juice','lemon curd','lemon extract'] = 'lemon'
    ingredient_dict['juice of lime', 'lime','lime juice', 'lime wedge','lime wedges','limes'] = 'lime'
    ingredient_dict['juice of orange', 'mandarin orange segments','mandarin oranges','mandarins', 'orange',
                    'oranges','navel oranges','nectarines', 'orange juice','orange juice concentrate',
                    'tangerine juice', 'orange extract','clementines', 'blood orange','blood orange juice'] = 'orange'
    ingredient_dict['guava juice'] = 'guava_juice'
    ingredient_dict['grapefruit','grapefruit juice'] = 'grapefruit'
    ingredient_dict['grapes', 'red grapes','white grape juice'] = 'grapes'
    ingredient_dict['watermelon'] = 'watermelon'
    ingredient_dict['plums'] = 'plum'
    ingredient_dict['currants', 'currant']   = 'currant'
    ingredient_dict['date','dates', 'medjool dates'] = 'date'
    ingredient_dict['figs', 'fig', 'fresh figs'] = 'fig'
    ingredient_dict['cherries','cherry','sweet cherries','cherry juice','cherry pie filling'] = 'cherry'
    ingredient_dict['berries', 'blackberries', 'blueberries', 'cranberries', 'mixed berries', 'strawberries',
                    'strawberry','raspberries','raspberry', 'freeze-dried strawberries'] = 'berry'
    ingredient_dict['banana','bananas','plantain','plantains'] = 'banana'
    ingredient_dict['apple', 'apples', 'fuji apple', 'gala apples', 'granny smith apples',
                    'golden delicious apple','mcintosh apple','tart apple','tart apples','apple butter',
                    'apple cider', 'apple juice','applesauce', 'unsweetened applesauce'] = 'apple'
    ingredient_dict['bartlett pears', 'pear','pears'] = 'pear'
    ingredient_dict['musk melon','cantaloupe'] = 'melon'

    # Meat
    ingredient_dict['93% lean ground turkey meat', 'ground turkey', 'lean ground turkey','ground beef',
                    'ground beef chuck','ground bison','hamburger meat', 'lean beef', 'lean ground beef',
                    'ground lamb','ground pork','meatballs','ground chicken'] = 'ground_meat'
    ingredient_dict['breakfast sausage', 'bulk sausage', 'ground sausage', 'italian turkey sausage',
                    'italian sausage', 'linguiça and/or presunto', 'polish sausage','pork sausage',
                    'pork sausages','sausage','sausage links','sausages','spanish chorizo','smoked sausage',
                    'turkey sausage','andouille sausage', 'andouille sausages','chicken sausage',
                    'chicken sausage links','chorizo','franks'] = 'sausage'
    ingredient_dict['bone in chicken thighs', 'bone-in skin-on chicken thighs', 'chicken','chicken breast','chicken breasts',
                    'chicken drumsticks and thighs','chicken meat','chicken pieces', 'chicken strips',
                    'chicken tenderloins','chicken tenders','chicken thigh','chicken thighs','chicken wings',
                    'chickens','cooked chicken','cooked chicken breast','cooked chicken breasts', 'roasted chicken',
                    'rotisserie chicken','skinless boneless chicken breast','shredded chicken',
                    'skinless boneless chicken breast halves','skinless boneless chicken breasts',
                    'skinless boneless chicken thighs'] = 'chicken'
    ingredient_dict['beef','beef brisket', 'beef chuck roast', 'beef shoulder roast', 'beef steak',
                    'beef stew meat', 'beef tenderloin', 'chuck roast', 'porterhouse steak','rib roast',
                    'rib-eye','rib-eye steak','ribeye steaks','ribs','roast beef','round steak', 'short ribs',
                    'steak', 'steaks','skirt steak'] = 'beef'
    ingredient_dict['boneless pork loin roast','boneless pork shoulder','boston butt', 'cooked pork',
                    'lean pork tenderloin', 'pork','pork belly','pork butt','pork chops','pork loin',
                    'pork loin chops','pork ribs','pork shoulder','pork sirloin tip roast','pork tenderloin',
                    'pork tenderloins','roast pork','roasted pork'] = 'pork'
    ingredient_dict['turkey','roast turkey breast'] = 'turkey'
    ingredient_dict['lamb','lamb stew meat'] = 'lamb'
    ingredient_dict['duck','duck breast'] = 'duck'
    ingredient_dict['bacon','bacon bits','bacon rashers','bacon strips', 'cooked bacon','cooked bacon strips',
                    'thick-cut bacon','pan-fried bacon','turkey bacon'] = 'bacon'
    ingredient_dict['canadian bacon', 'cooked ham', 'deli ham', 'diced ham', 'ham','ham bone','ham steak'] = 'ham'
    ingredient_dict['mortadella', 'pancetta','pepperoni','prosciutto', 'salami'] = 'cured_meat'

    # Seafood
    ingredient_dict['tilapia','tilapia fillets','cod','cod filets','cod fillets','halibut','catfish fillets',
                    'squid','skate wings'] = 'mild_fish'
    ingredient_dict['swordfish','red snapper fillets'] = 'medium_fish'
    ingredient_dict['ahi tuna', 'ahi tuna steak', 'fresh tuna','salmon','salmon fillet','salmon fillets'] = 'strong_fish'
    ingredient_dict['raw shrimp','shrimp','prawns','canned crabmeat', 'crab meat','crabmeat', 'imitation crab meat',
                    'lump crab meat','lobster'] = 'crustacean'
    ingredient_dict['light tuna', 'tuna','water-packed tuna','anchovies', 'anchovies in olive oil', 'anchovy',
                    'anchovy fillets'] = 'canned_fish'
    ingredient_dict['fish'] = 'fish'
    ingredient_dict['clam juice'] = 'clam_juice'
    ingredient_dict['smoked salmon'] = 'smoked_salmon'


    # Herbs & Spices
    ingredient_dict['cumin','cumin powder','cumin seeds', 'ground cumin','ground cumin seed', 'whole cumin'] = 'cumin'
    ingredient_dict['curry leaves', 'curry powder', 'curry paste', 'red curry paste'] = 'curry'
    ingredient_dict['coarse salt', 'coarse sea salt', 'fleur de sel', 'kosher salt','salt','sea salt',
                    'sea-salt','table salt','seasoned salt','seasoning salt','uma pitada de sal'] = 'salt'
    ingredient_dict['cloves ground', 'ground cloves'] = 'clove'
    ingredient_dict['cilantro','cilantro leaves', 'fresh cilantro','fresh cilantro leaves'] = 'cilantro'
    ingredient_dict['celery salt','celery seed'] = 'ground_celery'

    ingredient_dict['caraway seeds'] = 'caraway'
    ingredient_dict['cardamom pods','cardamon','carom seeds', 'ground cardamom'] = 'cardamom'
    ingredient_dict['black pepper', 'black peppercorns', 'ground pepper', 'peppercorn','peppercorns','pepper',
                    'white pepper','whole peppercorns'] = 'black_pepper'
    ingredient_dict['black mustard seeds', 'dry mustard', 'ground mustard', 'mustard powder','mustard seeds',
                    'yellow mustard seed','yellow mustard seeds'] = 'ground_mustard'
    ingredient_dict['bay leaf','bay leaves', 'dried bay leaf'] = 'bay_leaf'
    ingredient_dict['basil','basil leaves'] = 'basil'
    ingredient_dict['allspice'] = 'allspice'
    ingredient_dict['black sesame seeds', 'sesame','sesame seed','sesame seeds','white sesame seeds'] = 'sesame'
    ingredient_dict['cinnamon','cinnamon stick','cinnamon sticks', 'ground cinnamon'] = 'cinnamon'
    ingredient_dict['star anise'] = 'star_anise'
    ingredient_dict['oregano','oregano leaves'] = 'oregano'
    ingredient_dict['tamari'] = 'tamari'
    ingredient_dict['tahini'] = 'tahini'
    ingredient_dict['poppy seed','poppy seeds'] = 'poppy seed'
    ingredient_dict['smoked paprika','paprika'] = 'paprika'
    ingredient_dict['saffron'] = 'saffron'
    ingredient_dict['lavender'] = 'lavender'
    ingredient_dict['lemon pepper seasoning'] = 'lemon_pepper'
    ingredient_dict['italian seasoning'] = 'italian_seasoning'
    ingredient_dict['herbes de provence'] = 'herbes_de_provence'
    ingredient_dict['ground turmeric', 'turmeric','turmeric powder'] = 'turmeric'
    ingredient_dict['ground all spice','ground allspice', 'whole allspice'] = 'allspice'
    ingredient_dict['ground ginger'] = 'ground_ginger'
    ingredient_dict['ground hazelnuts', 'hazelnuts'] = 'hazelnut'
    ingredient_dict['fennel seed', 'fennel seeds'] = 'fennel'
    ingredient_dict['fenugreek leaves','fenugreek seeds'] = 'fenugreek'
    ingredient_dict['dried basil'] = 'basil'
    ingredient_dict['dried chives'] = 'dried_chives'
    ingredient_dict['dried cilantro'] = 'dried_cilantro'
    ingredient_dict['dried garlic', 'garlic flakes','garlic granules','garlic powder', 'granulated garlic',
                    'garlic salt'] = 'ground_garlic'
    ingredient_dict['dried marjoram'] = 'dried_marjoram'
    ingredient_dict['dried onion', 'onion flakes','onion powder'] = 'dried_onion'
    ingredient_dict['dried parsley'] = 'dried_parsley'
    ingredient_dict['dried porcini mushrooms'] = 'dried_mushroom'
    ingredient_dict['dried rosemary'] = 'dried_rosemary'
    ingredient_dict['dried tarragon'] = 'dried_tarragon'
    ingredient_dict['dried thyme'] = 'dried_thyme'
    ingredient_dict['coriander','coriander powder','coriander seeds', 'ground coriander', 'whole coriander seeds'] = 'coriander'
    ingredient_dict['crystallized ginger'] = 'crystallized_ginger'
    ingredient_dict['ground nutmeg', 'nutmeg'] = 'nutmeg'
    ingredient_dict['kefir'] = 'kefir'
    ingredient_dict['hing'] = 'hing'
    ingredient_dict['harissa'] = 'harissa'
    ingredient_dict['garam masala'] = 'garam_masala'
    ingredient_dict['cajun seasoning'] = 'cajun seasoning'
    ingredient_dict['dill seed', 'dried dill','dried dill weed'] = 'dill'

    # Chilies
    ingredient_dict['anaheim chiles','poblano chile','poblano pepper','poblano peppers','green chiles','green chili',
                    'green chilies','green chilis','green chillies','chile peppers', 'chiles', 'chili', 'chilies',
                    'chillies', 'chili peppers','thai chili','thai chili pepper','thai chilis','canned green chiles'] = 'mild_chile'
    ingredient_dict['serrano chili pepper','jalapeno','jalapeno chiles','jalapeno pepper','jalapeno peppers',
                    'jalapenos'] = 'hot_chile'
    ingredient_dict['chile flakes','chili flakes','chilli flakes','chilli powder','chili powder','chile powder',
                    'chipotle','chipotle chili powder','crushed red pepper','dried chile pepper',
                    'ground chipotle chile pepper','red pepper','red pepper flake','red pepper flakes','red chili',
                    'red chili powder','cayenne','cayenne pepper','ground cayenne pepper','ancho chile',
                    'ancho chile powder', 'ancho chili powder', 'ground ancho chile'] = 'ground_chile'
    ingredient_dict['chile garlic sauce','chili oil','sweet chili sauce'] = 'chile_sauce'
    ingredient_dict['canned chipotle in adobo','chipotle chilies in adobo','chipotle in adobo',
                    'chipotle pepper in adobo','chipotle peppers','chipotle peppers in adobo',
                    'chipotle chile in adobo'] = 'chipotle_adobo'

    # Sweetners
    ingredient_dict['erythritol', 'liquid stevia', 'truvia','stevia','stevia extract','swerve sweetener',
                    'sukrin sweetener'] = 'erythritol'
    ingredient_dict['date palm sugar'] = 'date_sugar'
    ingredient_dict['corn syrup', 'golden syrup'] = 'corn_syrup'
    ingredient_dict['confectioners sugar',"confectioners' sugar", 'icing sugar', 'powdered sugar'] = 'powdered_sugar'
    ingredient_dict['coconut palm sugar','coconut sugar', 'gula melaka'] = 'coconut_sugar'
    ingredient_dict['cinnamon sugar'] = 'cinnamon_sugar'
    ingredient_dict['cane sugar', 'granulated sugar','natural cane sugar','raw sugar','sugar','sugar cubes',
                    'turbinado sugar','white sugar','xícara de de açúcar','simple syrup'] = 'sugar'
    ingredient_dict['brown sugar', 'dark brown sugar', 'demerara sugar', 'golden brown sugar', 'jaggery',
                    'light brown sugar'] = 'brown_sugar'
    ingredient_dict['agave', 'agave nectar', 'agave syrup'] = 'agave'
    ingredient_dict['black treacle', 'molasses', 'light muscovado sugar'] = 'molasses'
    ingredient_dict['clear honey', 'honey', 'raw honey'] = 'honey'

    # Veggies
    ingredient_dict['edamame'] = 'edamame'
    ingredient_dict['eggplant','eggplants'] = 'eggplant'
    ingredient_dict['fennel bulb', 'fennel bulbs'] = 'fennel_bulb'
    ingredient_dict['fire roasted canned tomatoes', 'fire roasted tomatoes', 'fire-roasted tomatoes'] = 'fire_roasted_tomato'
    ingredient_dict['green peas', 'pea pods','peas','petite peas','snow peas','sugar snap peas'] = 'pea'
    ingredient_dict['green tomatoes', 'tomatillos'] = 'green_tomato'
    ingredient_dict['jicama'] = 'jicama'
    ingredient_dict['leek','leeks'] = 'leek'
    ingredient_dict['lemon lime soda','squirt'] = 'citrus_soda'
    ingredient_dict['lemongrass'] = 'lemongrass'
    ingredient_dict['lima beans'] = 'lima_bean'
    ingredient_dict['sprouts'] = 'sprouts'
    ingredient_dict['radicchio'] = 'radicchio'
    ingredient_dict['spaghetti squash'] = 'spaghetti_squash'
    ingredient_dict['turnip', 'turnips'] = 'turnip'
    ingredient_dict['radishes'] = 'radish'
    ingredient_dict['okra'] = 'okra'
    ingredient_dict['rutabaga','rutabagas'] = 'rutabaga'
    ingredient_dict['sweet potato','sweet potatoes'] = 'sweet_potato'
    ingredient_dict['red onion','red onions'] = 'red_onion'
    ingredient_dict['shallot','shallots'] = 'shallot'
    ingredient_dict['oil packed sun dried tomatoes','sun-dried tomatoes','sundried tomatoes'] = 'sun_dried_tomato'
    ingredient_dict['onion','onions','sweet onion','sweet onions','vidalia onion','vidalia onions','white onion','white onions','yellow onion','yellow onions'] = 'onion'
    ingredient_dict['zucchini','zucchini noodles','zucchinis'] = 'zucchini'
    ingredient_dict['parsnips'] = 'parsnip'
    ingredient_dict['roasted red pepper','roasted red peppers'] = 'roasted_red_pepper'
    ingredient_dict['acorn squash'] = 'acorn_squash'
    ingredient_dict['canned corn','cobs corn','corn','corn kernels','ear of corn','ears corn','ears of corn',
                    'fresh corn','fresh corn kernels', 'frozen corn','whole kernel corn'] =  'corn'
    ingredient_dict['cabbage', 'green cabbage', 'napa cabbage','purple cabbage','red cabbage','savoy cabbage'] = 'cabbage'
    ingredient_dict['butternut squash'] = 'butternut_squash'
    ingredient_dict['broccoli carrot cauliflower mix', 'mixed veggies', 'root vegetables','vegetable','veggie mix'] = 'mixed_vege'
    ingredient_dict['broccoli','broccoli florets','broccoli rabe','broccolini'] = 'broccoli'
    ingredient_dict['bok choy'] = 'bok_choy'
    ingredient_dict['cos lettuce','boston lettuce', 'boston lettuce leaves', 'butter lettuce', 'iceberg lettuce',
                    'iceburg lettuce', 'hearts of romaine', 'lettuce','lettuce leaf','romaine lettuce','romaine lettuce leaves','salad greens','salad mix', 'spring mix'] = 'lettuce'
    ingredient_dict['black eyed peas', 'canned black eyed peas'] = 'black_eyed_pea'
    ingredient_dict['beet', 'beetroot','beets', 'canned beets'] = 'beet'
    ingredient_dict['beet greens'] = 'beet_greens'
    ingredient_dict['bell pepper', 'green bell pepper','green bell peppers', 'green peppers','orange bell pepper','red bell pepper','red bell peppers','yellow bell pepper','peppers'] = 'bell_pepper'
    ingredient_dict['bean sprouts'] = 'bean_sprouts'
    ingredient_dict['baby bella mushrooms', 'button mushrooms', 'crimini mushrooms', 'fresh mushrooms',
                    'mushroom','mushrooms', 'mixed mushrooms','portabella mushrooms','shiitake mushrooms',
                    'white mushrooms'] = 'mushroom'
    ingredient_dict['baby carrots', 'carrot','carrots'] = 'carrot'
    ingredient_dict['baby corn', 'baby corns'] = 'baby_corn'
    ingredient_dict['baby peas'] = 'peas'
    ingredient_dict['baby potatoes','creamer potatoes','fingerling potatoes','gold potatoes','new potatoes',
                    'potato','potatoes','red potato','red potatoes','russet potato','russet potatoes',
                    'white potatoes','yukon gold potatoes','tater tots','hash brown potatoes','hashbrowns','french fries'] = 'potato'
    ingredient_dict['baby spinach','baby spinach leaves', 'frozen spinach','spinach','spinach leaves'] = 'spinach'
    ingredient_dict['artichoke','artichoke bottoms','artichoke hearts','artichokes', 'frozen artichoke hearts',
                    'marinated artichoke'] = 'artichoke'
    ingredient_dict['arugula', 'baby arugula'] = 'arugula'
    ingredient_dict['asparagus','asparagus spears'] = 'asparagus'
    ingredient_dict['avocado','avocados', 'haas avocados'] = 'avocado'
    ingredient_dict['fresh dill', 'dill'] = 'fresh_dill'
    ingredient_dict['fresh ginger','fresh ginger root', 'ginger'] = 'ginger'
    ingredient_dict['fresh green beans', 'green beans', 'haricots verts'] = 'green_bean'
    ingredient_dict['fresh herbs'] = 'freshh_herbs'
    ingredient_dict['fresh mint','fresh mint leaves', 'mint', 'mint leaves'] = 'fresh_mint'
    ingredient_dict['fresh rosemary','fresh rosemary leaves', 'rosemary','rosemary leaves'] = 'rosemary'
    ingredient_dict['fresh sage','fresh sage leaves', 'ground sage', 'sage','sage leaves'] = 'sage'
    ingredient_dict['fresh tarragon', 'tarragon'] = 'tarragon'
    ingredient_dict['fresh thyme','fresh thyme leaves','thyme','thyme leaves','thyme sprigs'] = 'thyme'
    ingredient_dict['fresh basil','fresh basil leaves','fresh bay leaves', 'lemon basil'] = 'fresh_basil'
    ingredient_dict['fresh coriander','fresh coriander leaves'] = 'fresh_coriander'
    ingredient_dict['flat leaf parsley','flat leaf parsley leaves','flat-leaf parsley','fresh flat leaf parsley',
                    'fresh parsley', 'fresh parsley leaves', 'parsley','parsley leaves'] = 'parsley'
    ingredient_dict['cucumber', 'cucumbers', 'english cucumber'] = 'cucumber'
    ingredient_dict['coleslaw mix'] = 'coleslaw_mix'
    ingredient_dict['collard greens', 'greens', 'mustard greens', 'leafy greens', 'turnip greens','swiss chard',
                    'water spinach','watercress'] = 'greens'
    ingredient_dict['chive','chives', 'green onion','green onions', 'scallion','scallion greens','scallions',
                    'spring onions','tokyo negi'] = 'chive'
    ingredient_dict['cherry tomato','cherry tomatoes', 'grape tomatoes', 'plum tomato','plum tomatoes'] = 'sweet_tomato'
    ingredient_dict['celery','celery stalk','celery stalks','celery stick','celery leaves','celery root'] = 'celery'
    ingredient_dict['cauliflower','cauliflower florets','cauliflowerets'] = 'cauliflower'
    ingredient_dict['canned diced tomatoes', 'canned tomatoes', 'heirloom tomato', 'roma tomato','roma tomatoes',
                    'stewed tomatoes','tomatoes','tomatos', 'tomato', 'tomaoes','vine ripened tomatoes'] = 'tomato'
    ingredient_dict['capers'] = 'caper'
    ingredient_dict['kiwi','kiwis'] = 'kiwi'
    ingredient_dict['kale', 'lacinato kale'] = 'kale'
    ingredient_dict['horseradish'] = 'horseradish'
    ingredient_dict['green grams'] = 'mung_bean'
    ingredient_dict['ginger garlic paste','ginger paste','ginger-garlic paste'] = 'ginger_paste'
    ingredient_dict['garlic','garlic clove','garlic cloves', 'garlics', 'roasted garlic','whole garlic',
                    'whole garlic clove'] = 'garlic'
    ingredient_dict['bamboo shoots'] = 'bamboo_shoot'
    ingredient_dict['brussels sprouts']  = 'brussels_sprouts'
    ingredient_dict['galangal'] = 'galangal'
    ingredient_dict['creamed corn'] = 'creamed_corn'
    ingredient_dict['delicata squash', 'squash','summer squash','winter squash','yellow squash',
                    'yellow summer squash'] = 'squash'
    ingredient_dict['guacamole'] = 'guacamole'
    ingredient_dict['hominy'] = 'hominy'
    ingredient_dict['edible flowers','squash blossoms'] = 'edible_flowers'
    ingredient_dict['pepperoncini','pickled jalapenos','pickled ginger','pimentos'] = 'pickled_veg'
    ingredient_dict['dill pickle chips', 'dill pickles','pickle','pickles','dill pickle juice'] = 'dill_pickle'
    ingredient_dict['dill pickle relish','pickle relish','sweet pickle relish'] = 'pickle_relish'
    ingredient_dict['canned pumpkin', 'canned pumpkin puree','solid pack pumpkin','pumpkin','pumpkin pie mix',
                    'pumpkin puree'] = 'pumpkin'
    ingredient_dict['black olives', 'greek olives', 'green olives', 'kalamata olives', 'oil cured black olives',
                    'olives','pimento stuffed olives'] = 'olive'

    # Thickening Agents / Grains / Flours
    ingredient_dict['agar'] = 'agar'
    ingredient_dict['sorghum flour', 'teff flour','semolina flour', 'quinoa flakes','quinoa flour','soy flour',
                    'spelt','spelt flour'] = 'flour_sub'
    ingredient_dict['millet','millet flour'] = 'millet'
    ingredient_dict['corn flour'] = 'corn_flour'
    ingredient_dict['coconut flour'] = 'coconut_flour'
    ingredient_dict['bread flour'] = 'bread_flour'
    ingredient_dict['buckwheat flour'] = 'buckwheat_flour'
    ingredient_dict['brown rice flour', 'rice flour','sweet rice flour'] = 'rice_flour'
    ingredient_dict['besan flour', 'kadalai maavu'] = 'gram_flour'
    ingredient_dict['arrowroot','arrowroot powder'] = 'arrowroot'
    ingredient_dict['almond flour', 'almond meal', 'almond meal flour', 'blanched almond flour', 'ground almonds'] = 'almond_flour'
    ingredient_dict['alfredo pasta sauce', 'alfredo sauce'] = 'alfredo'
    ingredient_dict['all purpose flour', 'flour', 'unbleached all purpose flour','unbleached flour','plain flour',
                    'self-raising flour','white flour','white whole wheat flour','whole wheat flour',
                    'whole wheat white flour'] = 'ap_flour'
    ingredient_dict['corn meal', 'cornmeal', 'fine cornmeal', 'ground cornmeal', 'yellow cornmeal',] = 'cornmeal'
    ingredient_dict['corn starch', 'cornstarch'] = 'corn_starch'
    ingredient_dict['amaranth grain'] = 'amaranth_grain'
    ingredient_dict['brown rice', 'cooked brown rice']    = 'brown_rice'
    ingredient_dict['grain blend'] = 'grain_blend'
    ingredient_dict['quick cooking grits', 'oatmeal'] = 'hot_cereal'
    ingredient_dict['old fashioned oats','old fashioned rolled oats','old-fashioned oats','oats','quick cooking oats',
                    'rolled oats','steel cut oats'] = 'oats'
    ingredient_dict['tapioca','tapioca flour','tapioca starch','quick cooking tapioca'] = 'tapioca'
    ingredient_dict['whole wheat pastry flour','pastry flour','cake flour'] = 'pastry_flour'
    ingredient_dict['pearl barley','quick cooking barley'] = 'barley'
    ingredient_dict['potato starch','potato starch flour'] = 'potato_flour'
    ingredient_dict['oat bran','oat flour'] = 'oat_flour'
    ingredient_dict['wheat berries','wheat bran','wheat germ','vital wheat gluten'] = 'wheat'
    ingredient_dict['cooked couscous', 'dry couscous'] = 'couscous'
    ingredient_dict['cooked quinoa','quinoa'] = 'quinoa'
    ingredient_dict['arborio rice','risotto rice'] = 'arborio_rice'
    ingredient_dict['basmati rice'] = 'basmati_rice'
    ingredient_dict['cooked rice', 'cooked white rice', 'instant white rice', 'rice','white rice',
                    'ready-to-serve asian fried rice'] = 'rice'
    ingredient_dict['corn bread mix'] = 'corn_bread_mix'

    # Nuts & Seeds
    ingredient_dict['flax meal','flax seed','flaxmeal','ground flaxseed'] = 'flax'
    ingredient_dict['hemp seeds'] = 'hemp_seed'
    ingredient_dict['sunflower seeds'] = 'sunflower_seed'
    ingredient_dict['pine nuts'] = 'pine_nut'
    ingredient_dict['unsalted pistachios','pistachios'] = 'pistachio'
    ingredient_dict['raw pumpkin seeds','roasted pumpkin seeds','pepitas'] = 'pumpkin_seed'
    ingredient_dict['pecan','pecan pieces','pecans'] = 'pecan'
    ingredient_dict['almond', 'almonds','slivered almonds','almond extract'] = 'almond'
    ingredient_dict['dry roasted peanuts', 'peanut','peanuts','roasted peanuts','unsalted peanuts'] = 'peanut'
    ingredient_dict['creamy peanut butter', 'crunchy peanut butter', 'peanut butter','powdered peanut butter',
                    'smooth peanut butter'] = 'peanut_butter'
    ingredient_dict['cashews', 'roasted cashews','salted cashews','salted roasted cashews','raw cashews'] = 'cashew'
    ingredient_dict['almond butter', 'nut butter'] = 'almond_butter'
    ingredient_dict['chia seed','chia seeds'] = 'chia_seed'
    ingredient_dict['walnuts'] = 'walnut'

    # Beverages
    ingredient_dict['tequila'] = 'tequila'
    ingredient_dict['tea'] = 'tea'
    ingredient_dict['sake'] = 'sake'
    ingredient_dict['rose water'] = 'rose_water'
    ingredient_dict['vodka'] = 'vodka'
    ingredient_dict['whiskey'] = 'whiskey'
    ingredient_dict['matcha tea'] = 'matcha'
    ingredient_dict['lemonade'] = 'lemonade'
    ingredient_dict['kahlua'] = 'kahlua'
    ingredient_dict['gin'] = 'gin'
    ingredient_dict['fernet-branca'] = 'fernet'
    ingredient_dict['dessert wine'] = 'dessert_wine'
    ingredient_dict['dark rum','rum','rum extract','spiced rum'] = 'rum'
    ingredient_dict['crème de cacao'] = 'crème_de_cacao'
    ingredient_dict['club soda','seltzer water'] = 'club_soda'
    ingredient_dict['chardonnay', 'dry white wine', 'wine', 'white wine'] = 'white_wine'
    ingredient_dict['champagne', 'sparkling wine'] = 'sparkling_wine'
    ingredient_dict['bourbon'] = 'bourbon'
    ingredient_dict['brandy'] = 'brandy'
    ingredient_dict['beer', 'dark beer', 'guinness', 'lager', 'rye beer'] = 'beer'
    ingredient_dict['coca cola', 'coke', 'cola flavored carbonated beverage', 'diet soda', 'dr. pepper'] = 'cola'
    ingredient_dict['dry sherry'] = 'sherry'
    ingredient_dict['dry cider', 'stella artois cidre'] = 'cider'
    ingredient_dict['cabernet sauvignon', 'dry red wine', 'pinot noir', 'red wine'] = 'red_wine'
    ingredient_dict['amaretto'] = 'amaretto'
    ingredient_dict['espresso powder', 'instant espresso','instant espresso powder'] = 'espresso_powder'
    ingredient_dict['decaf coffee'] = 'decaf_coffee'
    ingredient_dict['coffee','coffee beans', 'strong coffee'] = 'coffee'
    ingredient_dict['coffee extract'] = 'coffee_extract'
    ingredient_dict['instant coffee','instant coffee granules'] = 'instant_coffee'
    ingredient_dict['ginger beer'] = 'ginger_beer'
    ingredient_dict['cointreau'] = 'cointreau'
    ingredient_dict['eggnog'] = 'eggnog'
    ingredient_dict['irish cream'] = 'irish_cream'

    # Dessert
    ingredient_dict['white chocolate','white chocolate chips'] = 'white_chocolate'
    ingredient_dict['toffee bar','toffee bits'] = 'toffee'
    ingredient_dict['peanut butter candies','peanut butter candy','peanut butter chips','pb cups','snickers'] = 'candy'
    ingredient_dict['mint extract','peppermint baking chips','peppermint extract','andes mints',
                    'crème de menthe baking chips'] = 'mint'
    ingredient_dict['marshmallow cream','marshmallow creme','marshmallow fluff','marshmallow peeps',
                    'marshmallows'] = 'marshmallow'
    ingredient_dict['lemon cake mix','spice cake mix','vanilla cake mix','white cake mix','yellow cake mix'] = 'cake_mix'
    ingredient_dict['jelly beans'] = 'jelly_beans'
    ingredient_dict['hot chocolate mix'] = 'hot_choc'
    ingredient_dict['graham cracker crumbs','graham cracker crust','graham cracker sheets','graham crackers'] = 'graham_cracker'
    ingredient_dict['ginger snap crumbs','ginger snaps','gingerbread','gingersnap crumbs'] = 'gingerbread'
    ingredient_dict['fat free cool whip', 'lightly sweetened whipped cream', 'whipped cream','whipped topping',
                    'nonfat cool whip'] = 'whipped_cream'
    ingredient_dict['dark chocolate','dark chocolate bar','dark chocolate candy bars', 'dark chocolate chips'] = "dark_chocolate"
    ingredient_dict['cream cheese frosting', 'cream cheese icing', 'icing'] = 'frosting'
    ingredient_dict['chocolate chip cookie', 'chocolate cookie crust', 'chocolate wafer cookies', 'cookie',
                    'cookie crumbs','cookie mix','cookies', 'ladyfingers','nilla wafers','oreo cookies','oreos',
                    'shortbread cookies','vanilla wafer cookies','vanilla wafers', 'scones'] = 'cookie'
    ingredient_dict['chocolate hazelnut spread', 'nutella'] = 'nutella'
    ingredient_dict['chocolate ice cream sauce', 'chocolate syrup', 'fudge ice cream topping','fudge topping',
                    'hot fudge sauce'] = 'chocolate_sauce'
    ingredient_dict['caramel','caramel sauce','caramel topping','caramels', 'dulce de leche'] = 'caramel'
    ingredient_dict['candy cane','candy canes'] = 'candy_cane'
    ingredient_dict['candy coating','candy melting wafers','candy melts'] = 'candymelt'
    ingredient_dict['baking chocolate', 'bittersweet chocolate', 'chocolate', 'cocoa', 'dutch process cocoa',
                    'dutch processed cocoa', 'german chocolate'] = 'chocolate'
    ingredient_dict['baking cocoa', 'cacao powder', 'cocoa powder', 'dutch processed cocoa powder',
                    'dutch process cocoa powder', 'unsweetened baking cocoa','unsweetened cocoa',
                    'unsweetened cocoa powder'] = 'cocoa_powder'
    ingredient_dict['allergy friendly chocolate chips', 'bittersweet chocolate chips', 'cacao nibs',
                    'chocolate chips', 'milk chocolate chips','semi sweet chocolate chips',
                    'semi sweet chocolate morsels','semi-sweet chocolate','semi-sweet chocolate baking chips',
                    'semisweet chocolate','semisweet chocolate chips','unsweetened chocolate'] = 'chocolate_chips'
    ingredient_dict['chocolate shavings', 'chocolate sprinkles','sprinkles','rainbow sprinkles'] = 'sprinkles'
    ingredient_dict['brownie mix'] = 'brownie_mix'
    ingredient_dict['angel food cake', 'lb cake', 'pound cake'] = 'sponge_cake'
    ingredient_dict['butterscotch chips'] = 'butterscotch_chips'
    ingredient_dict['butterfingers'] = 'butterfingers'
    ingredient_dict['gelatin'] = 'gelatin'
    ingredient_dict['ice cream', 'vanilla ice cream','sherbet'] = 'ice_cream'
    ingredient_dict['instant chocolate pudding mix', 'instant lemon pudding mix','instant vanilla pudding mix',
                    'lemon pie filling','lemon pudding mix', 'vanilla pudding mix'] = 'pudding'
    ingredient_dict["m & m's para decorar",'m&m candies','mini m&m', 'mnm minis'] = 'm&m'

    # Cheese
    ingredient_dict['romano cheese','pecorino romano cheese','parmesan cheese','swiss cheese','asiago cheese',
                    'parmigiano reggiano','pecorino','parmesan','sharp cheddar','extra sharp cheddar cheese',
                    'white cheddar cheese','sharp cheddar cheese'] = 'hard_cheese'
    ingredient_dict['provolone cheese','provolone','gouda','gouda cheese','gruyere','gruyere cheese','halloumi cheese'] = 'semi_hard_cheese'
    ingredient_dict['mozzarella','mozzarella cheese','part skim mozzarella','part-skim mozzarella',
                    'part-skim mozzarella cheese','skim milk mozzarella cheese','havarti cheese',
                    'pepperjack cheese','fontina cheese'] = 'semi_soft_cheese'
    ingredient_dict['ricotta','ricotta salata','feta','feta cheese','low fat ricotta cheese',
                    'skim milk ricotta cheese','part skim ricotta cheese','ricotta cheese','skim milk ricotta',
                    'cotija cheese','goat cheese','buffalo mozzarella', 'fresh mozzarella','fresh mozzarella ball',
                    'fresh mozzarella cheese','mascarpone','mascarpone cheese'] = 'soft_cheese'
    ingredient_dict['bleu cheese', 'blue cheese', 'blue cheese crumbles', 'gorgonzola','gorgonzola cheese'] = 'blue_cheese'
    ingredient_dict['processed american cheese','nacho cheese sauce','queso dip'] = 'processed_cheese'
    ingredient_dict['cheese','italian cheese blend','jack cheese','mexican cheese','monterey jack cheese',
                    'low fat cheese','shredded mexican cheese blend','shredded mozzarella',
                    'shredded mozzarella cheese','shredded cheddar','shredded cheddar cheese','shredded cheese',
                    'reduced fat shredded cheddar cheese','cheddar cheese','colby and monterey jack cheese',
                    'colby jack cheese'] = 'cheese'

    # Dairy
    ingredient_dict['low fat sour cream', 'mexican crema', 'sour cream','crème fraîche'] = 'sour_cream'
    ingredient_dict['cream', 'double cream', 'heavy cream','heavy whipping cream','half & half','half and half',
                    'half n half','half n half cream', 'whipping cream'] = 'cream'
    ingredient_dict['cream cheese', 'cream cheese block', 'light cream cheese', 'neufchatel cheese'] = 'cream_cheese'
    ingredient_dict['chocolate milk'] = 'chocolate_milk'
    ingredient_dict['buttermilk'] = 'buttermilk'
    ingredient_dict['evaporated milk', 'milk powder','skim evaporated milk','nonfat milk powder','skim milk powder'] = 'evaporated_milk'
    ingredient_dict['fat-free cottage cheese'] = 'cottage_cheese'
    ingredient_dict['fat-free milk', 'milk', 'low fat milk', 'whole milk','skimmed milk','nonfat milk'] = 'milk'
    ingredient_dict['full fat plain yogurt', 'low fat plain yogurt', 'low fat yogurt', 'low-fat yogurt',
                    'natural yogurt','plain yogurt','vanilla yogurt','yoghurt','yogourt','yogurt'] = 'yogurt'
    ingredient_dict['0% fat greek yogurt', 'greek yogurt', 'low fat greek yogurt', 'lowfat greek yoghurt',
                    'skim vanilla greek yogurt','plain greek yogurt','nonfat greek yogurt',
                    'non-fat greek yogurt'] = 'greek_yogurt'
    ingredient_dict['a 4 colheres de de leite condensado', 'condensed milk','sweetened condensed milk'] = 'condensed_milk'
    ingredient_dict['egg', 'eggs', 'whole egg','whole eggs'] = 'egg'
    ingredient_dict['egg white','egg white powder','egg whites'] = 'egg_white'
    ingredient_dict['egg yolk','egg yolks'] = 'egg_yolk'
    ingredient_dict['hard cooked eggs','hard-boiled eggs','hardboiled egg','hardboiled eggs'] = 'hard_boiled_egg'

    # Oils and Fats
    ingredient_dict['grape seed oil', 'grapeseed oil'] = 'grape_seed_oil'
    ingredient_dict['dark sesame oil', 'sesame oil'] = 'sesame_oil'
    ingredient_dict['coconut oil','coconut butter'] = 'coconut_oil'
    ingredient_dict['canola oil', 'cooking oil', 'oil','peanut oil','vegetable oil','palm oil','rapeseed oil',
                    'walnut oil'] = 'light_oil'
    ingredient_dict['avocado oil'] = 'avocado_oil'
    ingredient_dict['bacon fat', 'lard'] = 'animal_fat'
    ingredient_dict['butter', 'light butter', 'margarine', 'salted butter','unsalted butter','ghee'] = 'butter'
    ingredient_dict['butter flavored shortening', 'shortening','solid vegetable shortening','vegetable shortening'] = 'shortening'
    ingredient_dict['extra virgin olive oil','extra-virgin olive oil', 'light olive oil', 'olive oil'] = 'olive_oil'


    # Beans
    ingredient_dict['canned pinto beans', 'pinto beans'] = 'pinto_bean'
    ingredient_dict['canned kidney beans', 'canned red kidney beans', 'chili beans', 'dried kidney beans',
                    'kidney beans', 'red kidney beans'] = 'kidney_bean'
    ingredient_dict['canned garbanzo beans'] = 'garbanzo_bean'
    ingredient_dict['canned great northern beans', 'great northern beans'] = 'great_northern_bean'
    ingredient_dict['canned cannellini beans','canned white beans', 'canned white cannellini beans',
                    'cannellini beans', 'white beans'] = 'cannellini_beans'
    ingredient_dict['canned chickpeas', 'chickpeas'] = 'chickpeas'
    ingredient_dict['black beans', 'canned black beans', 'cooked black beans', 'refried beans'] = 'black_bean'
    ingredient_dict['mat beans'] = 'mat_bean'
    ingredient_dict['canned lentils', 'cooked red lentils', 'dried lentils', 'lentils','red lentils'] = 'lentil'

    # Breads & Pastas
    ingredient_dict['burger bun', 'hamburger buns', 'sandwich bun','sandwich buns','sandwich rolls',
                    'slider buns','sub buns','sub roll','sub rolls','whole wheat buns', 'poppyseed roll'] = 'bun'
    ingredient_dict['bread', 'multi grain bread','wholemeal bread', 'white sandwich bread','white bread',
                    'sourdough bread','pita','pita breads','wheat flatbreads','naan','naan bread','texas toast',
                    'hawaiian bread','pizza crust','pizza dough'] = 'bread'
    ingredient_dict['bread crumbs', 'breadcrumb', 'breadcrumbs', 'dry bread crumbs', 'dry breadcrumbs', 'italian seasoned bread crumbs', 'panko','panko bread crumbs','panko breadcrumbs','seasoned bread crumbs'] = 'breadcrumb'
    ingredient_dict['bread dough'] = 'bread_dough'
    ingredient_dict['blintzes -)', 'pancake mix'] = 'pancake'
    ingredient_dict['biscuits', 'buttermilk biscuits'] = 'biscuits'
    ingredient_dict['bagels'] = 'bagel'
    ingredient_dict['baguette','baguettes'] = 'baguette'
    ingredient_dict['brioche','brioche buns'] = 'brioche'
    ingredient_dict['ciabatta loaf','ciabatta rolls'] = 'ciabatta'
    ingredient_dict['crescent roll dough','crescent rolls', 'croissants', 'refrigerated crescent dinner rolls'] = 'croissant'
    ingredient_dict['crostini', 'croutons'] = 'croutons'
    ingredient_dict['filo dough','filo pastry', 'puff pastry','puff pastry dough','puff pastry sheets',
                    'puff pastry shells','shortcrust pastry','pastry dough','pie crust','pie shell','pie shells',
                    'refrigerated pie crust','refrigerated pie crusts'] = 'pastry_dough'
    ingredient_dict['english muffins'] = 'english_muffin'
    ingredient_dict['egg noodles'] = 'egg_noodles'
    ingredient_dict['crackers', 'cracker', 'ritz crackers','saltine crackers','saltines','pita chips',
                    'pretzels'] = 'crackers'
    ingredient_dict['angel hair', 'big shells', 'cavatappi pasta', 'cooked penne pasta', 'ditalini pasta',
                    'elbow macaroni','fettuccine','fettuccini', 'fusilli', 'linguine', 'lasagna noodles',
                    'long pasta', 'orzo','orzo pasta','pasta','pasta shells','penne','penne pasta','rigatoni',
                    'shells','ziti', 'whole wheat spaghetti','spaghetti','spaghetti noodles','spaghetti pasta',
                    'refrigerated spinach tortellini','noodles','rice noodles','soba noodles'] = 'pasta'
    ingredient_dict['flour tortillas', 'taco shells','tacos','whole wheat tortillas','tortillas',
                    'tortilla chips','corn tortillas','corn chips', 'corn tortilla chips'] = 'tortilla'
    ingredient_dict['gnocchi'] = 'gnocchi'

    # Alternatives
    ingredient_dict['soy buttery spread', 'vegan margarine'] = 'df_butter'
    ingredient_dict['quorn mince'] = 'meat_sub'
    ingredient_dict['egg replacer', 'ener-g egg replacer', 'chia eggs'] = 'egg_replacement'
    ingredient_dict['dairy free cheese', 'vegan cheese','marzipan'] = 'df_cheese'
    ingredient_dict['dairy free milk', 'non-dairy milk', 'unsweetened soy milk'] = 'df_milk'
    ingredient_dict['almond milk'] = 'almond_milk'
    ingredient_dict['extra firm tofu', 'tofu','tempeh','seitan'] = 'tofu'
    ingredient_dict['vegan chocolate chips'] = 'df_choc_chip'
    ingredient_dict['gf chocolate cake mix'] = 'gf_cake_mix'
    ingredient_dict['gluten free all purpose flour','gluten-free flour'] = 'gf_flour'
    ingredient_dict['dairy-free chocolate chips'] = 'df_choc_chips'

    # Stock
    ingredient_dict['chicken bouillon','chicken bouillon cube','chicken bouillon cubes','chicken broth',
                    'chicken stock','fat free chicken broth','low sodium chicken broth','low sodium chicken stock',
                    'low-salt chicken broth', 'stock','turkey stock', 'reduced sodium chicken broth'] = "chicken_stock"
    ingredient_dict['vegetable broth','vegetable stock'] = 'vege_stock'
    ingredient_dict['beef broth', 'beef consomme', 'beef stock', 'canned beef broth', 'low sodium beef broth'] = 'beef_stock'

    # Sauces
    ingredient_dict['ranch','ranch dressing','ranch dressing mix','ranch mix','ranch salad dressing',
                    'ranch salad dressing mix'] = 'ranch'
    ingredient_dict['ketchup'] = 'ketchup'
    ingredient_dict['hot sauce', 'sriracha','sriracha hot sauce','sriracha sauce','tabasco','tabasco sauce',
                    'pepper sauce','sambal oelek','buffalo sauce','buffalo wing sauce','chili paste',
                    'chili sauce'] = 'hot_sauce'
    ingredient_dict['hoisin sauce'] = 'hoisin'
    ingredient_dict['canned tomato sauce', 'marinara sauce','pasta sauce','pizza sauce','spaghetti sauce',
                    'tomato puree','tomato sauce', 'tomato juice','tomato paste'] = 'tomato_sauce'
    ingredient_dict['caesar dressing'] = 'caesar_dressing'
    ingredient_dict['browning sauce'] = 'browning_sauce'
    ingredient_dict['barbecue sauce', 'bbq sauce'] = 'bbq_sauce'
    ingredient_dict['basil pesto', 'pesto'] = 'pesto'
    ingredient_dict['adobo sauce'] = 'adobo'
    ingredient_dict['worcestershire sauce'] = 'worcestershire'
    ingredient_dict['tzatziki sauce'] = 'tzatziki'
    ingredient_dict['balsamic glaze','balsamic vinegar'] = 'balsamic'
    ingredient_dict['italian dressing','italian salad dressing mix'] = 'italian_dressing'
    ingredient_dict['fat free mayo', 'fat-free mayonnaise', 'low fat mayonnaise', 'mayo','mayonnaise',
                    'light mayonnaise', 'reduced fat mayo'] = 'mayo'
    ingredient_dict['dijon mustard', 'grainy mustard', 'mustard', 'spicy brown mustard','whole-grain mustard',
                    'yellow mustard'] = 'mustard'
    ingredient_dict['hummus'] = 'hummus'

    ingredient_dict['tomato ketchup'] = 'ketchup'
    ingredient_dict['pico de gallo','salsa'] = 'salsa'
    ingredient_dict['enchilada sauce', 'red enchilada sauce'] = 'enchilada_sauce'

    # Asian
    ingredient_dict['canned water chestnuts','water chestnuts'] = 'water_chestnut'
    ingredient_dict['dashi'] = 'dashi'
    ingredient_dict['fish sauce', 'oyster sauce'] = 'fish_sauce'
    ingredient_dict['mirin','shaoxing wine'] = 'mirin'
    ingredient_dict['miso soybean paste', 'yellow miso'] = 'miso'
    ingredient_dict['kombu'] = 'seaweed'
    ingredient_dict['wasabi paste'] = 'wasabi'
    ingredient_dict['won ton wrappers','wonton wrappers'] = 'wonton'
    ingredient_dict['tamarind'] = 'tamarind'
    ingredient_dict['light soy sauce','low sodium soy sauce','kecap manis','reduced sodium soy sauce','soy sauce',
                    'coconut aminos'] = 'soy_sauce'
    ingredient_dict['garlic oil'] = 'garlic_oil'
    ingredient_dict['coconut milk','coconut water','canned coconut milk','light coconut milk',
                    'unsweetened coconut milk'] = 'coconut_milk'

    remove_set = set(['as required', 'bake your own', 'condiments', 'cutters', 'each', 'enough', 'feeds', 'garnish',
                  'ground', 'guar gum', 'i swear', 'juice', 'just over', 'mason jars', 'mix', 'mixed peel',
                  'mixed spice', 'moist', 'meat','optional','see post above','saucepan','slow cooker','time',
                  'to','toppings','veined','salt & pepper','salt and pepper','omelette','nuts','seeds','wrap',
                  'xanthan gum','rub', 'taco seasoning','taco seasoning mix','steak seasoning','spice rub',
                  'seasoning','seasoning blend','seasoning mix','pumpkin pie spice','pumpkin spice mix',
                  'old bay seasoning','queso quesadilla','to 4 suman sa ibus','slit','steak sauce',
                  'apple pie spice','chicken seasoning', 'creole seasoning','fruit','salad dressing',
                  'slaw dressing'])

    feature_dict = dict([('dairy free', 'dairy_free'), ('fodmap friendly', 'fodmap_friendly'), ('gluten free', 'gluten_free'),
                         ('ketogenic', 'keto'), ('lacto ovo vegetarian', 'vegetarian'), ('paleolithic', 'paleo'),
                         ('pescatarian', 'pescatarian'), ('primal', 'primal'), ('vegan', 'vegan'), ('whole 30', 'whole_30'),
                         ('american', 'american'), ('asian', 'asian'), ('british', 'british'), ('caribbean', 'caribbean'),
                         ('central american', 'central_american'), ('chines', 'chinese'), ('english', 'english'),
                         ('european','european'),('french', 'french'), ('german', 'german'), ('greek', 'greek'),
                         ('indian', 'indian'), ('italian', 'italian'),('jewish', 'jewish'), ('mediterranean', 'mediterranean'),
                         ('mexican', 'mexican'), ('middl eastern', 'middle_eastern'),('scottish', 'scottish'),
                         ('southern', 'southern'), ('spanish', 'spanish'),('vietnames', 'vietnamese'), ('antipasti', 'appetizer'),
                         ('antipasto', 'appetizer'),('appetizer', 'appetizer'), ('batter', 'batter'), ('bread', 'bread'),
                         ('breakfast', 'breakfast'),('brunch', 'breakfast'), ('condiment', 'condiment'), ('dessert', 'dessert'),
                         ('dinner', 'dinner'), ('dip', 'dip'), ("hor d'oeuvre", 'appetizer'), ('lunch', 'lunch'),
                         ('main course', 'main_dish'),('main dish', 'main_dish'), ('morning meal', 'breakfast'),('salad', 'salad'),
                         ('sauce', 'condiment'),('side dish', 'side_dish'), ('snack', 'snack'),('soup', 'soup'),
                         ('spread', 'spread'), ('starter', 'appetizer'), ('african', 'african'), ('cajun', 'cajun'), ('creol', 'cajun'),
                         ('south american', 'south_american'), ('latin american', 'latin_american'), ('irish', 'irish'), ('thai', 'thai'),
                         ('bbq', 'bbq'), ('barbecu', 'bbq'), ('japanes', 'japenese'), ('scandinavian', 'eastern_european'),
                         ('nordic', 'eastern_european'), ('beverage', 'beverage'), ('drink', 'beverage'), ('frosting', 'dessert'),
                         ('icing', 'dessert'), ('crust', 'bread')])

    categorical_feat = []
    unbucketed_ingredients = []
    for recipe in recipes_json:
        feats = []

        for ingredient in recipe['extendedIngredients']:
            if ingredient['name'].lower() in remove_set:
                continue
            elif ingredient_dict.get(ingredient['name'].lower()) == None:
                unbucketed_ingredients.append(ingredient['name'].lower())
            else:
                feats.append(ingredient_dict.get(ingredient['name'].lower()))
        for diet in recipe['diets']:
            feats.append(feature_dict.get(diet.lower()))
        for dt in recipe['dishTypes']:
            feats.append(feature_dict.get(dt.lower()))
        for cuisine in recipe['cuisines']:
            feats.append(feature_dict.get(cuisine.lower()))
        categorical_feat.append(feats)

    return categorical_feat, unbucketed_ingredients
