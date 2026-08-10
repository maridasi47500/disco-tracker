
mkdir templates 
python3 scaffold.py user username phone country_id:references email password
python3 scaffold.py userhasreviews user_id:references content reviewby
python3 scaffold.py discosong composer_artist title
python3 scaffold.py food name country_id:references
python3 scaffold.py dance name
python3 scaffold.py userhasdance dance_id:references user_id:references agility_level
python3 scaffold.py userhasfood user_id:references food_id:references
python3 scaffold.py artisthassong user_id:references discosong_id:references
python3 scaffold.py city name
python3 scaffold.py country name
python3 scaffold.py nightclub name city_id:references
python3 scaffold.py nightclubhassong nightclub_id:references discosong_id:references
python3 scaffold.py userhasnightclub user_id:references nightclub_id:references
python3 scaffold.py userdating user_id:references otheruser_id:references
