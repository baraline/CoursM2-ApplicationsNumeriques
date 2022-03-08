Bienvenu sur le git du cours de Data Mining avancé pour les M2 2022. Vous trouverez ici les slides des cours, les sujets de TD et quelques exemples de codes pour les algorithmes que nous présenterons en cours.

## Au programme
Dans les précédentes parties du cours, vous avez étudié des sous familles du data mining avec notamment les approches de Text Mining et Pattern mining. Dans ce cours, nous allons voir comment ces deux approches peuvent être utilisées sur des applications continues plutôt que discrète. Plus spécifiquement, nous étudierons deux algorithmes de classification supervisés des séries temporelles, que sont Bag-of-SFA Symbols (BOSS) et Shapelet Transform.

## Instruction pour le TP
1. Télécharger cette archive sur votre machine locale :
    - Soit avec le zip sur la page git du projet, et ensuite extraction du zip
    - Soit avec un git clone https://github.com/baraline/CoursM2-ApplicationsNumeriques.git
    
Si vous utilisez un IDE python (ex: Spyder inclut dans Anaconda) pas besoin des étapes 2,3,4. Mais dans ce cas créer un nouveau projet sur le répertoire `CoursM2-ApplicationsNumeriques`.
2. Lancer une console python (via Anaconda ou votre installation de Python locale)
3. Naviguer vers le dossier `CoursM2-ApplicationsNumeriques` sur votre disque
4. Lancer la commande  `python setup.py install`
5. Si vous rencontrez une erreur d'installation, me prévenir.
6. Le sujet du TP est disponible dans le fichier `m2tpdm/README.md`

## Contributions
Si vous souhaitez contribuer à améliorer cette page ou que vous avez des questions sur une partie du contenu, merci d'utiliser le système de tickets (issues) de ce Git.

## Contact
Pour tout autres demandes, vous pouvez me contacter à l'adresse : antoine.guillaume@worldline.com

## Pour aller plus loin 

Quelques algorithmes de l'état de l'art (2022) pour la classification des séries temporelles pour les curieux:

- Random Convolution KErnel Transform (ROCKET) 
- Hive Cote 2.0 et ses composant
- InceptionTime (Deep Learning)

Plus généralement, le site https://timeseriesclassification.com/ regroupe les dernières nouveautés de beaucoup de chercheurs influent du domaine, ainsi qu'une archive de datasets accessible via les APIs de la librairie Sktime en Python et tsml en Java.


