# pythonVideoGameSales

Pour lancer django : 
cd pythonVideoGameSales/videoGamesSalesSite
python manage.py runserver 8080
aller sur http://127.0.0.1:8080/videoGames pour avoir la page de formulaire

Pour lancer fastApi (sur la branche “lea”)
cd pythonVideoGameSales
uvicorn videoGamesSalesSite.wsgi:app --reload

La mise en place de fastApi ne fonctionne pas à cause d’une erreur de répertoire Static que l’on a pas su régler. Mais nous avons modifié le router et les views pour que cela puisse normalement fonctionner avec fastApi.

Architecture du projet : 
dans le dossier racine pythonVideoGameSales nous avons : 
- l’analyse des données dans analyseNotebook.ipynb
- l’entrainement et le clean des données dans index.ipynb
- video_games_sales.csv sont les données d’origines 

le dossier videoGameSalesSite : 
- dossier “templates” avec index.html correspondant à la page du formulaire et predict.html correspondant à la page du résultat
- dossier “videoGames” : 
    - dossier static pour le style
    - apiIA.py : fonction pour faire la prédiction grâce au model
    - forms.py : fichier gérant la création des différents champs du formulaire
    - model.json : le model exporté suite à l’entrainement de index.ipynb
    - urls.py : router 
    - views.py : les vues correspondant aux templates index et predict

