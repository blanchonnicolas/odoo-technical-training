# Odoo 17.0 - Technical Training

The Technical Training of Odoo 17.0 is available on the
[Tutorial](https://www.odoo.com/documentation/master/developer/howtos/rdtraining.html)

<a name="readme-top"></a>

-->
[Contributor](https://github.com/blanchonnicolas)
[Forks](https://github.com/odoo/technical-training)
[issues](https://github.com/odoo/technical-training/issues)
[Linkedin](https://www.linkedin.com/in/nicolas-blanchon)



<h3 align="center">Odoo Technical Training by Nicolas Blanchon</h3>

</div>

<!-- ABOUT THE PROJECT -->
## Development Introduction project

Project started at Odoo Experience 2023,  SmartClass "Introductipon to Development"

The project follows guidelines from [official tutorial](https://www.odoo.com/documentation/master/developer/howtos/rdtraining.html)

All development has been performed using Jupyter Web interface accessible through [odoo_sh](https://www.odoo.sh)

### New Odoo Module Project Structure 

The structure of the project follows standard rules from Odoo (New Module creation)

```
new_module
├── README.md
├── __init__.py
├── __manifest__.py
├── models
│   ├── __init__.py
│   ├── __businessobject1__.py
│   ├── __businessobject2__.py
├── views
│   ├── views.xml
│   ├── forms.xml
│   ├── data.csv
│   ├── data.xml
│   ├── menu.xml
├── security
│   ├── model_security_rules.csv
```

Summary in bullet points: 
 * Each subfolder is a module
 * Each package of module should contain dedicated __init__.py
 * Main package of module is using business oriented name, visible in app store Odoo
 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

Development of ths module has been performed following 16 chapters from [official tutorial](https://www.odoo.com/documentation/master/developer/howtos/rdtraining.html).

This rely on Odoo ORM layer, that mapp Business Objects with PostGreSQL database.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Project Notes

[Chapter_4](https://www.odoo.com/documentation/master/developer/tutorials/getting_started/04_basicmodel.html#chapter-4-models-and-basic-fields) : Création du modèle estate_property
1. Création du modèle relationnel
2. Customisation des champs du modèle 
3. Vérification des champs du modèle 
Note: Warning dûe à l'allocation des droits ma,nquante

[Chapter_5](https://www.odoo.com/documentation/master/developer/tutorials/getting_started/05_securityintro.html#chapter-5-security-a-brief-introduction) :  Ajout de la sécurité pour accéder à la donnée (par groupes d'utilisateurs)
1. La configuration de la sécurité pour les modèles est chargée à partir de fichiers = Il est donc primordiale de savoir comment charger un fichier
2. Création du fichier détaillant les groupes ayant accès aux données
3. Ce fichier est déclarée en tant que data, dans le  manifest.py et sera donc chargée par l'application

[Chapter_6](https://www.odoo.com/documentation/master/developer/tutorials/getting_started/06_firstui.html#chapter-6-finally-some-ui-to-play-with)
: Création de l'IHM
1. Définir une action (Afficher Views Tree ou Form ; déclarée dans le fichier action XML)
2. Créer des Menus dans la vue par défaut (Le Menu sera liée à l'action, qui elle-même est liée au modèle)
3. Ajuster fields, attributes and views : Ajout des propriétés DefaultValue ou Date++
4. Champs reservé : Active : Ce champ est recommandé pour activer, désactiver certaines entrées de la DB, sans avoir à les supprimer (Permet de Faciliter le filtrage / affichage des informations ; Actions Archive ou Unarchive pré-utilisable, lors de la selection d'une entrée via l'IHM)

[Chapter_7](https://www.odoo.com/documentation/master/developer/tutorials/getting_started/07_basicviews.html#list) : Définition des vues basiques
1. Vues en Listes (=Tree view) : Permet l'affichage du tableau
2. Vues de chaque entrées (=Form) : Permet l'affichage de chaque entrée
3. Vues de Recherche (=Filter or GroupBy) : Permet des filtres pré-préparés pour l'utilisateur

[Chapter_8](https://www.odoo.com/documentation/master/developer/tutorials/getting_started/08_relations.html#chapter-8-relations-between-models) : Relations entre les modèles
1. Many2One relation : Permet de faire le lien avec un autre objet
2. Many2Many relation : Utilisation des tags
3. One2Many : Inverse du Many2One - Permet l'accès à des informations via un autre modèle

[Chapter_9](https://www.odoo.com/documentation/master/developer/tutorials/getting_started/09_compute_onchange.html#chapter-9-computed-fields-and-onchanges): Champs pré-calculés:
1. Champ calculé : Création d'un fonction pour faire la somme des surfaces ; Création d'une fonction pour récuperer la valeur maximum d'un autre modèle
2. Fonction inversé : Possibilité de mettre à jour un champ pré-calculé (Attention à sauvegarder l'entrée pour que la mise à jour soit enregistrée)

[Chapter_10](https://www.odoo.com/documentation/master/developer/tutorials/getting_started/10_actions.html#object-type): Actions (Workflow automatique)
1. Types d'actions : Ajout des boutons dans la view, trigger des méthodes (Business logic et conditions d'affectations)
2. Liens entre Actions et Bouton : Non exploré

[Chapter_11](https://www.odoo.com/documentation/master/developer/tutorials/getting_started/11_constraints.html#chapter-11-constraints): Contraintes (SQL et Vérifications codées en Python)
1. SQL : Vérification sur Float, gestion des valeurs uniques
2. Python : Limitation des valeurs de champs, Comparaison et contraintes sur l'utilisation des objets business

[Chapter_12](https://www.odoo.com/documentation/master/developer/tutorials/getting_started/12_sprinkles.html#chapter-12-add-the-sprinkles): Customisation des vues
1. Views : Liste des propriétés accessible directement depuis le model "Propertiy_type"
2. Widgets : Ajout d'un widget dans la form view, représentant un wokflow de statut de la propriété
3. List Order : Trier l'affichager des objets, en fonction de l'id, du nom, de la valeur d'un champ
4. Attributes et Options: Attributes seem not to be working with Odoo 17. Also, "editable" option in tree view seems to not respond. decoration-bf is not responding.
5. Stat buttons : NOT performed


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Blanchon Nicolas - [Linkedin](https://www.linkedin.com/in/nicolas-blanchon)

Project Link: [odoo_technical_training](https://www.odoo.sh/project/blanchonnicolas-odoo-technical-training2/branches/master)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

/

