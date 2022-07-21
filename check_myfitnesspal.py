# from curses import window
import requests
import json
import pyodbc 
from bs4 import BeautifulSoup
import openpyxl
import array as arr
import pandas as pd

class Nutrition:
    def __init__(self, key, name, link, isverified): 
        self.key = key 
        self.name = name 
        self.link = link
        self.isverified = isverified
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, ensure_ascii=False, indent=4)
    key = str;
    name = str;
    link = str;
    isverified = bool;
    unit = str;
    unitId = str;
    calories = str;
    sodium = str;
    toalFat = str;
    potassium = str;
    saturated = str;
    totalCarbs = str;
    polyunsaturated = str;
    dietaryFiber = str;
    monounsaturated = str;
    sugars = str;
    trans = str;
    protein = str;
    cholesterol = str;
    vitaminA = str;
    calcium = str;
    vitaminC = str;
    iron = str;
    
def GetNutritionsList():
    url = "https://www.myfitnesspal.com/food/calorie-chart-nutrition-facts"
    nutritions = [];
    
    #cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
    #                      "Server=DESKTOP-ESDPF32;"
    #                      "Database=9Health;"
    #                      "Trusted_Connection=yes;")
    
    # cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
    #                       "Server=DESKTOP-ESDPF32;"
    #                       "Database=9Health;"
    #                       'UID=SA;'
    #                       'PWD=1Lik39Health!;'
    #                       "Trusted_Connection=no;")


    # cursor = cnxn.cursor()
    #cursor.execute('SELECT distinct NameENG FROM IngredientTrans1 where NameENG is not null')
    #cursor.execute('SELECT distinct NameENG FROM IngredientTrans1 where NameENG is not null and NameENG not in (select [key] from myfitnesspal_temp2)')
    # cursor.execute('SELECT NameEn FROM ConvertView220714 where NameEn is not null and NameEn not in (select [key] from myfitnesspal_temp1)')
    # cursor.execute('SELECT NameEn FROM ConvertView220714 where NameEn is not null and NameEn not in (select [key] from keepTrackMFP_temp1)')
    # result_set = cursor.fetchall()
    # print(type(result_set))

    path = "C:/Users/9Health/OneDrive/9Health (1)/70_Server/60_Database/FixNameEn_220720.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    #cell_obj = sheet_obj.cell(row = 65, column = 1)
    cell_obj = sheet_obj['A']
    result_set = []
    # Control iteration cell
    start_cell = 60
    for x in range(start_cell,len(cell_obj)):
    # for x in range(len(cell_obj)):
        result_set.append(cell_obj[x].value)
        tuple_set = zip(result_set)

    for row in tuple_set:
        payload = json.dumps({
          "utf8": "✓",
           "authenticity_token": "l2Rb4FU3PKiXURFfqU5ZLg5Agld1eHAdbf8ab4l6TXRQzmaB7i3jZZpB0DF+BeTZJdqGwEfoReaI4aOtp9o5tg==",
          "meal": "",
          "date": "2022-02-20",
          "search": row[0]
        })
        headers = {
          'Cookie': 'ajs_anonymous_id=%22325993de-4896-4735-aeb8-9ea6f742a82d%22; _gcl_au=1.1.1874794306.1644721395; __pdst=67368d9dbda24962899744eead098911; _tq_id.TV-8127903627-1.20a0=a602ccdd5aeca68a.1644721397.0.1644805030..; _pin_unauth=dWlkPVpUVTJOR0l4WldZdE4ySXpOQzAwTmpJMkxXRTVaamd0WkdVd01UbG1NMlk1TUdWag; _ga=GA1.2.189157224.1644721397; _gid=GA1.2.1556697643.1644721397; CCPABannerShown=1; amplitude_id_2746a27a28431837e776d192ed6db604myfitnesspal.com=eyJkZXZpY2VJZCI6IjdhMzZkZmRmLWRkYTEtNGY4MS04ZDk3LTk0NjgyOGUwZDk0M1IiLCJ1c2VySWQiOiI5Nzg3MTMyMjY4MTMyNSIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0NDgwNTAyMzMzNSwibGFzdEV2ZW50VGltZSI6MTY0NDgwNTAyOTYwNiwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjF9; last_login_date=2022-02-13; p=xO3U4F3dTY7JTFC23LspgrG7; remember_me=v1%3A156409154%3Ac59be126456a6d07a6fa420979d3deda; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..GptxqpPJEjAj8LxG.4DY1MHAJ7C5IcdwBQEjM_TwST69YZ2B6AkojmzIp33R2jqH9C1ZVOqt9zYGQyyRVfezTAJ769cSkpgRXLGKYmXd64Jt8223c8l0J0RGOIzfXYCUDEUXqEgD4_JeoF_j_r-OZpMrRvS137wg3bdprMgHYPetRR5-YpdMbJulbL0YqJkFclfLVNTwh5OvpROPhstfMevHmnW088dwcM77mZBJMWBXZXn39W8bPYfNeVdHkVZMbQJuJqJfqMz-36jLMuwZBZq4qTM0x_Q9Oh8WaRIva0sK53RuNnhiDj32IiYZ-bCPMvodh5Kvza5zVu250wP1x0n8N7wFzAZmHBpDMFxRXonwu8Zfn9_COUMATy2iaIx778v5iyNjhiyeSC6HFPKhkfkbHYcom_B7smQWH1XjwTmoUX1s2HMaanls0RXSUB2CMBiu3wUHnp_T1gesGmCMAgA295RcVn8HXXTOpwMX0jYPT-cG9UCwm73ER5I7M69o_7GjBNPTiMzhm2M-Pov0Hi2BOvGfV744Tcn4S_VcI5cKh6lfn7VB818wFKeKVuxwiOBtso9t5w12yz7WUemB4o5wpfD9FdUseCj3xL-coBJcJODGyBpqEdpkRQsItFbNn540K--2Tiz0SlDCw-ImbG2OGebTRpL1LXFlzCPC81DvY-dc1rOO328rKP0z3K5Ceaewhz8a_vGQ0lqbh3PzGqAhwWPPT96PLerhD_d8O5pJALdUbS8U6NM6QdW7fdb8I00K9BO8NZ0YQpPMo09ZpD_D7ThbMyEzUXaL9zr16Rg91A9dSHRcGAWIsiZ3m_lG_ZQhLkzSaDsPLNRHQr6hDEvgj5fJ37rf4Y3XeLwEAT3ktjmpFTNnwema7VsmJA-yoBDEJh9iePH2cVB55H_G3JW3z2zbCmmiW4cxFf_ojAh5NZlHhTCpsW6dgtrpfQfUQ1DC4QMyFMlNe0dgqsPH5yReWOMpL6Ha65ug4_VtJzrxXE_Mj2Q.NjY_O_OlnwVnlOQlyRku7g; known_user=156409154; mobile_seo_test_guid=336dfd8c-eff6-9dbc-561f-709c56156dbe; split-id=50a65014-b0e8-4e82-ba84-6585ec1405d7; _mfp_session=NWQwUjUwMGlUNkdjSlFGZ1drSUtsdERMTTFaQldCcS8rVWNsMTNDSTROUXJmM2RNUWgzWjJCVGcwUWdJaHdueXViMGcwVjZLZFZod0hVeXcvcEdQVlhOcFNzVFRQcFpoc3hSeTFic2RmUmRtSytvdk9EMVdtOUQrcm9LZUVNOTR2clA5YTcxN3o1NHVCajBNdVhQSlVCenNkVUNuYkN0K1dLVVA1VUViTmF1NzhFbW9VdDF5a0hoc3BYd28vSzBraHc3VUIzNkdPekQ1em1GWk92NHZNa09oRE1BWVV5U2NDZzJ1d2tCU3d3bmN6WWhoY1V4UFlSS0E3ZUlNSmhLVkcwY1dhNzkwTE80MDZOcHMxckVxSDI0YnQ5LzJZeXVRbnZQT3dwdUowaFg0RmtkeVU1K0xkTjZuUVVNTi90RS93WWV4dmk3Y3RMMmVIY0VMNTBpdlZEZmx1blg4RWNxYlJ0cmxlYzEwQ0xiaEZ0enRoLzlhbTRIN0JueGxhdEg0TVJEd2w3cmsyaEFsc3VUK2g0cEFzZz09LS1leERnb0dKMEZIU3BNdWp4L2M0cndnPT0%3D--c8f4a298b5f7323dc0a2a158326c436dcdb4f6b3; __Host-next-auth.csrf-token=f144cdf55b50c752cadbabe32f863e857ea6967b0e5683489f3734dd127a6974%7C20469f6688397d837b92bc199bb724b1da09164b4a330f8a09654c5c7ab07d6c; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.myfitnesspal.com%2Faccount%2Flogin%3FcallbackUrl%3Dhttps%253A%252F%252Fwww.myfitnesspal.com%2Fen%2Faccount%2Flogin; session_event_session_start_website_97871322681325=true; _dc_gtm_UA-273418-97=1; _dc_gtm_UA-273418-116=1; _gat_UA-273418-116=1; _gat=1; _mfp_session=amc3NVhIYnVOQnBjdTZHZmhZdHNCRHFpU1BFVzcxRlkybUJhZFZKWjVJMVI5Q2E3amF5QjFReTlMa2c1NkpYcjlMMWRDaVpPOU5yV210SHBUYmNHVEVmYUJqaDhQYkdndDgrWXFXWTFsOWErcDBNTGQ2QUtkWFdVWHhDR0dTOTVub0Q5Qmp1M3pvTTRTVlNlNGN1K1c1aVA2ZUdjRjNxeC9zZ01zVkZraFBJWHBzWUN1cEVqdkFuS2RqOXM4UncxUVJEdFRGNHhzNXFESDlPbGEwU2IySzRWb3VyUFpDYlVJTzFXMHBIWU0rREdrRmgrQXVvL1kwcXFmNjZmb1VzOU9PckUrRHhqaXRxakpDY2R4WXBsTkJuRTliVGU4dDAyclkvbWgwWDNxdXJ2Ylp5WEd1NDFOUGFHL2g3Ykw3M3h4VDR5OFh4QmlOdVMzOW1qTVBCc3JXNjU3WW1XUVZ1QXEyVE9rSkdQL2tGYld3ZndscWpjQ0JwQ2YwUUVvYUt2UG92RXA1TGZnS2t5VkNDbTZhOFo0UT09LS1ZbEY5L0RuY1lVTWFxVXZiMnR1cWhnPT0%3D--2790a12f9fb09020c2892c87e5518cba387ac43f; known_user=156409154; last_login_date=2022-02-20; session_event_session_start_website_97871322681325=true',
          'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload);
        soup = BeautifulSoup(response.text, 'html.parser');
        elements = soup.select("#matching > .matched-food > .search-title-container");

        nutri_temps = []
        for row2 in elements[:15]:
            item = row2.find('a', class_='search');
            name = item.getText();
            link = item['href'];
            isverified = row2.find('div', class_='verified') != None;
            nutri_temps.append(Nutrition(row[0], name, link, isverified))
            my_dict = Nutrition(row[0], name, link, isverified).__dict__
            df = pd.DataFrame(my_dict, index=[0])
            df2 =  df.append(my_dict)
            # df['x'] = x
            print(df2)
            print("=" * 200)
            print(df.to_markdown())
            # print(df2)
        
        nutritions.extend(nutri_temps)
        nutritions = []

    #     if(len(elements) == 0):
    #         continue;
    #     nutri_temps = [];
    #     for row2 in elements[:15]:
    #         item = row2.find('a', class_='search');
    #         name = item.getText();
    #         link = item['href'];
    #         isverified = row2.find('div', class_='verified') != None;
    #         if(name.lower() == row[0].lower() and isverified is True):
    #             nutri_temps.append(Nutrition(row[0], name, link, isverified))
    #             break
    #         #elif (name.lower() == row[0].lower() and isverified is False):
    #         #    nutri_temps.append(Nutrition(row[0], name, link, False))
    #         #    break

    #     if(len(nutri_temps) == 0 and len(elements) > 0):
    #         for row3 in elements[:5]:
    #             item = row3.find('a', class_='search')
    #             name = item.getText()
    #             link = item['href']
    #             if (name.lower() == row[0].lower()):
    #                 nutri_temps.append(Nutrition(row[0], name, link, False))
    #                 break
    #         #elem = elements[0].find('a', class_='search');
    #         #nutri_temps.append(Nutrition(row[0], elem.getText(), elem['href'], False));



    #     nutritions.extend(nutri_temps);

    #     if(len(nutritions) >= 1):
    #         print(len(nutritions));
    #         for nuti in nutritions:
    #             #cursor.execute("INSERT INTO myfitnesspal_temp1([key],name,link,isverified) VALUES (?,?,?,?)", (nuti.key, nuti.name, nuti.link, nuti.isverified));

    #             cursor.execute("INSERT INTO keepTrackMFP_temp1([key],name,link,isverified) VALUES (?,?,?,?)", (nuti.key, nuti.name, nuti.link, nuti.isverified));
    #             cursor.execute("COMMIT");
    #             nutritions = [];
        
    # cursor.close();
    # cnxn.close();

def GetNutritionsDetailList():
    nutritions = [];
    baseUrl = "https://www.myfitnesspal.com";
    nutritions = [];
    
    #cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
    #                      "Server=DESKTOP-ESDPF32;"
    #                      "Database=try9Health;"
    #                      "Trusted_Connection=yes;")
    
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=DESKTOP-ESDPF32;"
                          "Database=9Health;"
                          'UID=SA;'
                          'PWD=1Lik39Health!;'
                          "Trusted_Connection=no;")

    cursor = cnxn.cursor()
    #cursor.execute('SELECT * FROM myfitnesspal_temp1 where [key] not in (select [key] FROM tryIngredientNutrient)');
    cursor.execute('SELECT * FROM keepTrackMFP_temp1 where [key] not in (select [key] FROM tryIngredientNutrient)');
    # cursor.execute('SELECT * FROM ConvertView220714 where [NameEn] not in (select [key] FROM tryIngredientNutrient)');
    # cursor.execute('SELECT * FROM myfitnesspal_temp1');
    # cursor.execute('SELECT * FROM ConvertView220714 where [NameEn] not in (select [key] FROM myfitnesspal_temp1)');

    result_set = cursor.fetchall()
    
    for row in result_set:
        # Get key, name, link, is_verified
        nution = Nutrition(row[0], row[1], row[2], row[3]);
        url = baseUrl + nution.link;
        payload={}
        #headers = {
        #  'Cookie': '_mfp_session=eFJVTVpCQ3l4UGNyYXVnVHpkTWR1Q3pTRGtLUDRjY1FOQzFmaWEwcDJuaExxekpMS3dzcVJCZmE0ZGVXUFlpeXpFNnRwR0tXTVZPQWw0Mmgyb01RYzQ4ZkhxRkRXallCaS9kc012K1lLK1RJeW1CZE5KRE9UdnY0NDcvUUFSY3BSZlJaVFVGK1p5eXNBcW81dXR2ZDhGSXhLYWpybFZXbG1ISEk5Vk91UkZ6YmNsbUQvakIyZVBmVG51MzZ3ZGRBYnZIOWhTWXk0ZUNSQ0tzY0ZSdFBjUT09LS1yYjhDdy81Z3hxaFNtRlg2c3NtMEl3PT0%3D--19d8eb7122ec3a7e518e041f11933c0197875340; known_user=156409154; last_login_date=2022-02-20'
        #}

        headers = {
          'Cookie': '_mfp_session=bGQxTXpzMUtlZGJMbUtZVG02QWZVZlNTNUp4OFYzL2R2TFV6S3VoNzZVOXkyZGY0TlBkTzQ2U2l5QXl5VVdmeVN5TDFkVHJPMUVYUVg4cm12WTRNNDRlaHBNMnkwRVRuUjB6dWZHeE9TOHFlcHI2T2l3ZGxrKzcwdDhuZmFXSlRhR2VKSFdkQWZ4YnQxempWbHp5M2E4VE95VTJXZ0x3OVBQS3FlODEzVFdzRUZMNVYwQkg5ci9TVnJ6ODdMODZxVEFUVEFVd1BsZXAvTEtkVGxsVWl5aXVtcWo3VVBFc0VYTDBDQ3RDcDVzaWFsTThrWWNXbEl0b2tWRW1DWjJOdTgzRGtmaWRHTHlJdGE4TXdqKy85TU1NTGthSWhtQzg0L0VnVTE0SmpBaVFGTVFLd1VlVkt1MzAyU3J5Mkd2elU1Vmk5WWh1Vis4UGRrUG9RK3VFQStyWElUbUNkWkJnaWpNVk1MOGlLblI0cTF6ZCtRYityVkNMaVRTVmoxMGw1K2FOcWVaZnIwWXVycjJPSjdRZVNqUT09LS1lMUJIOG91eFF4QjZmOEN4UFd5bEt3PT0=--fdf45da0a1bc3703a78bfc07b71d03a25dcfa143; known_user=156409154; last_login_date=2022-06-28'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser');
        
        #unit
        unitElements = soup.select("#nutrition-facts-form > .fieldset > .field > #food_entry_weight_id");
        for row2 in unitElements[:5]:
            item = row2.find('option', {'selected': True});
            if(item != None):
                nution.unit = item.getText();
                nution.unitId = item['value'];
                break;
                
        #ingredient
        ingredientElements = soup.select("#nutrition_info > #nutrition-facts");
        
        
        tables = [
            [
                [td.get_text(strip=True) for td in tr.findAll('td')] 
                for tr in table.findAll('tr')
            ] 
            for table in ingredientElements[0].findAll('tbody')
        ];
        
        for cols in tables:
            nution.calories = cols[0][1];
            nution.sodium = cols[0][3];
            nution.toalFat = cols[1][1];
            nution.potassium = cols[1][3];
            nution.saturated = cols[2][1];
            nution.totalCarbs = cols[2][3];
            nution.polyunsaturated = cols[3][1];
            nution.dietaryFiber = cols[3][3];
            nution.monounsaturated = cols[4][1];
            nution.sugars = cols[4][3];
            nution.trans = cols[5][1];
            nution.protein = cols[5][3];
            nution.cholesterol = cols[6][1];
            nution.vitaminA = cols[7][1];
            nution.calcium = cols[7][3];
            nution.vitaminC = cols[8][1];
            nution.iron = cols[8][3];
           	
        nutritions.append(nution);
        if(len(nutritions) >= 1):
            print(len(nutritions));
            for nuti in nutritions:
                cursor.execute("INSERT INTO tryIngredientNutrient([key],name,link,isverified,unit,unitId,calories,sodium,toalFat,potassium,saturated,totalCarbs,polyunsaturated,dietaryFiber,monounsaturated,sugars,trans,protein,cholesterol,vitaminA,calcium,vitaminC,iron) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
                               (nuti.key, nuti.name, nuti.link, nuti.isverified,nuti.unit,nuti.unitId,nuti.calories,nuti.sodium,nuti.toalFat,nuti.potassium,nuti.saturated,nuti.totalCarbs,nuti.polyunsaturated,nuti.dietaryFiber,nuti.monounsaturated,nuti.sugars,nuti.trans,nuti.protein,nuti.cholesterol,nuti.vitaminA,nuti.calcium,nuti.vitaminC,nuti.iron));
                cursor.execute("COMMIT");
                nutritions = [];
        
    cursor.close();
    cnxn.close();

if __name__ == "__main__":
    GetNutritionsList();
     #GetNutritionsDetailList();
     





