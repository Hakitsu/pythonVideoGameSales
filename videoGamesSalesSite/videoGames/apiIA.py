import xgboost as xgb
import pandas as pd

df_train = pd.read_csv(r'C:\xampp\php\www\pythonProject\df_train.csv')

def prediction(data):
    with open(r'C:\xampp\php\www\pythonProject\model.json') as mon_fichier:
        model_xgb= xgb.XGBRegressor()
        # model = json.load(mon_fichier)
        model_xgb.load_model(r'C:\xampp\php\www\pythonProject\model.json')
        print (data)
        modal_table = ['year', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales', 
                        #plateform
                        'platform_2600', 'platform_3DO', 'platform_3DS',
                        'platform_DC', 'platform_DS', 'platform_GB', 'platform_GBA',
                        'platform_GC', 'platform_GEN', 'platform_GG', 'platform_N64',
                        'platform_NES', 'platform_NG', 'platform_PC', 'platform_PCFX',
                        'platform_PS', 'platform_PS2', 'platform_PS3', 'platform_PS4',
                        'platform_PSP', 'platform_PSV', 'platform_SAT', 'platform_SCD',
                        'platform_SNES', 'platform_TG16', 'platform_WS', 'platform_Wii',
                        'platform_WiiU', 'platform_X360', 'platform_XB', 'platform_XOne',
                        #genre
                        'genre_Action', 'genre_Adventure', 'genre_Fighting', 'genre_Misc',
                        'genre_Platform', 'genre_Puzzle', 'genre_Racing', 'genre_Role-Playing',
                        'genre_Shooter', 'genre_Simulation', 'genre_Sports', 'genre_Strategy',
                        #publisher
                        'publisher_505 Games', 'publisher_5pb',
                        'publisher_Alchemist', 'publisher_Atari', 'publisher_Atlus',
                        'publisher_Acclaim Entertainment', 'publisher_Activision',
                        'publisher_Capcom', 'publisher_Codemasters',
                        'publisher_Banpresto', 'publisher_Bethesda Softworks',
                        'publisher_DTP Entertainment', 'publisher_Deep Silver',
                        'publisher_Crave Entertainment', 'publisher_D3Publisher',
                        'publisher_Eidos Interactive', 'publisher_Electronic Arts',
                        'publisher_Destineer', 'publisher_Disney Interactive Studios',
                        'publisher_GT Interactive', 'publisher_Hudson Soft',
                        'publisher_Empire Interactive', 'publisher_Focus Home Interactive',
                        'publisher_Infogrames', 'publisher_Kadokawa Shoten',
                        'publisher_Idea Factory', 'publisher_Ignition Entertainment',
                        'publisher_MTV Games', 'publisher_Majesco Entertainment',
                        'publisher_Konami Digital Entertainment', 'publisher_LucasArts',
                        'publisher_Midway Games', 'publisher_Namco Bandai Games',
                        'publisher_Marvelous Interactive', 'publisher_Microsoft Game Studios',
                        'publisher_Other', 'publisher_Rising Star Games', 'publisher_Sega',
                        'publisher_Nintendo', 'publisher_Nippon Ichi Software',
                        'publisher_SquareSoft', 'publisher_THQ',
                        'publisher_Sony Computer Entertainment', 'publisher_Square Enix',
                        'publisher_Ubisoft', 'publisher_Virgin Interactive',
                        'publisher_Take-Two Interactive', 'publisher_Tecmo Koei',
                        'publisher_Warner Bros. Interactive Entertainment',
                        'publisher_Vivendi Games',
                        'publisher_Zoo Digital Publishing'
                    ]
        
        list_data = []

        for col in modal_table:
            list_data.append(0)

        df = pd.DataFrame([list_data],columns=df_train.columns)
        print(df)
        print('-------------------------------------')
        for element in data:
            if element == 'genre':
                df.loc[0,"genre_"+data[element]] = 1

            elif element == 'platform':
                df.loc[0,"platform_"+data[element]] = 1

            elif element == 'publisher':
                df.loc[0,"publisher_"+data[element]] = 1

            else:
                df.loc[0,element] = int(data[element])

        print(df)
        return model_xgb.predict(df)