# Séance 01 - Transcription

Vidéo source : `Guide complet _ Bien démarrer avec Cloud Code.mp4`

Modèle : `large-v3-turbo` | langue détectée : `fr` (1)

## Transcription horodatée

[00:00:00.050 - 00:00:29.930] Bonjour à tous et à toutes j'espère que vous allez bien donc on va parler sur cette séance de Claude Code qui va être notre outil principal tout au long de la formation ça va être très important de suivre cette séance là pourquoi parce qu'on va parler du coup d'installation on va voir comment bien l'utiliser on va se faire un petit exercice sur la création d'un site web et une étude de marché donc je vous invite à bien suivre vous allez voir c'est pas bien complexe même si

[00:00:29.930 - 00:00:59.810] si derrière vous n'avez jamais mis les mains dans un terminal au fur et à mesure de la formation vous allez avoir les compétences pour gérer n'importe quel projet sur Claude Code encore une fois mon objectif c'est de vous accompagner sur la création de projet donc sur par exemple un blog automatique vous allez très bien pouvoir ensuite revendre cette compétence là mais vous allez aussi très bien pouvoir vous adapter au marché donc si un client vous fait une demande

[00:00:59.810 - 00:01:23.370] sur un projet que vous avez pas réalisé sur cette formation là vous allez pouvoir le faire sans problème parce que vous avez compris du coup cet outil et vous avez compris comment suivre une bonne méthodologie pour arriver à votre objectif final donc on va voir un petit peu la différence entre ChatGPT du coup

[00:01:23.370 - 00:01:56.060] et Claude Code donc ChatGPT ça va être plus un chatbot où derrière je vais lui poser une question où il va nous donner du texte après ça va être à nous de copier-coller créer les fichiers et tout faire à la main en gros si je fais une demande à ChatGPT de me créer un site internet de freelance il va me donner un code HTML je vais devoir le copier créer un fichier directement dans bloc note et l'enregistrer sous en .html et ensuite je vais sélectionner où je souhaite le déposer

[00:01:56.060 - 00:02:14.630] par exemple sur un dossier que j'ai créé après je vais devoir cliquer dessus Claude Code ça va être vraiment différent comme on va le voir sur cette séance là il va vraiment agir sur notre ordinateur donc il va créer notre fichier directement dans le dossier et il va l'ouvrir aussi on va gagner vraiment beaucoup de temps

[00:02:14.630 - 00:02:31.020] maintenant ce que ça va changer pour toi c'est que si tu sais pas coder c'est pas grave parce que Claude Code code pour nous directement il faut pas avoir le syndrome de l'imposteur en se disant voilà je vais avoir des lignes de code je connais rien au code etc

[00:02:31.020 - 00:02:42.940] enfin j'ai pas les compétences pour au départ j'étais un petit peu comme ça en sachant que moi j'avais quand même un petit background de code derrière je faisais du Python du Java du HTML etc

[00:02:42.940 - 00:03:01.700] maintenant il faut savoir que j'écris plus du tout une ligne de code c'est vraiment Claude Code qui le fait pour moi il faut se mettre en tête que quand on utilise Claude Code c'est comme avoir un développeur à côté de moi H24 il a vraiment les compétences de tout faire et c'est ça qu'on va voir tout au long de la formation

[00:03:01.700 - 00:03:15.440] maintenant on va parler coût donc combien ça coûte ? on a la partie abonnement derrière on a 3 abos le pro à 20 euros par mois je vous le conseille pas du tout pourquoi ? parce que vous allez très vite limiter en termes de quota

[00:03:15.440 - 00:03:26.920] si vous bossez sur un projet de la formation vous allez voir que le quota va être vite dépassé que vous allez devoir attendre le lendemain pour que ça se remette à jour vous allez perdre du temps

[00:03:26.920 - 00:03:42.060] je vous conseille de foncer soit sur l'abonnement 5 fois ou soit sur l'abonnement x20 sachant que moi j'ai cet abonnement en 4 fois donc je paye à peu près 850 euros par mois mais derrière je suis rentable

[00:03:42.060 - 00:03:56.600] parce que si vous vendez un projet client par exemple automatisation de gestion d'avis Google avis et bien derrière vous vendez 2000 euros vous avez remboursé votre abonnement

[00:03:56.600 - 00:04:03.600] même si derrière cet abonnement a passé à 1500 euros par mois je le prendrai quand même parce que je sais que je vais être rentable

[00:04:03.600 - 00:04:16.920] n'hésitez pas je sais que ça peut paraître cher mais foncez c'est une opportune si peu chère qui peut nous permettre de réaliser énormément de choses

[00:04:16.920 - 00:04:27.100] on a aussi une autre partie donc API je pense que tout le monde en a entendu parler mais ça on va l'utiliser plus que sur des projets clients

[00:04:27.100 - 00:04:41.180] ou par exemple on va on va enfin un client nous demande un système de réponse automatique par mail et bien sur le système en question on va utiliser une clé API anthropique

[00:04:41.180 - 00:05:06.650] plateforme que derrière l'utilisateur envoie un email à notre système et bien la réponse qu'on va faire de manière automatique et bien écoutez par exemple 5 centimes

[00:05:06.650 - 00:05:30.230] 5 centimes là je serai à 8 dollars et 1 centime donc on va payer par exécution donc c'est ça la différence nous on va utiliser API key juste c'est ça qu'on va connecter au système

[00:05:30.230 - 00:05:42.900] on va voir comment installer cloud code installez vous bien on va prendre du temps on va faire étape par étape il faut savoir que moi je suis sur Mac

[00:05:42.900 - 00:05:50.060] donc si vous êtes sur Windows ça va être un petit peu différent mais une fois que vous aurez installé cloud code ça va être exactement la même chose

[00:05:50.060 - 00:05:56.080] donc vous inquiétez pas vous perdre tout au long de la formation

[00:05:56.080 - 00:06:03.810] donc sur Mac comment on va faire tout d'abord on va aller dans notre bureau nouveau dossier

[00:06:03.810 - 00:06:13.220] on va créer un dossier directement le renommé voilà ce que je vais faire ensuite c'est que je vais faire clic gauche

[00:06:13.220 - 00:06:23.340] nouveau terminal au dossier donc là comme on peut voir j'ai une session terminale connectée à mon dossier

[00:06:23.340 - 00:06:36.010] donc on peut passer à l'étape 2 qu'est-ce que je dois faire c'est que je dois installer Node.js

[00:06:36.010 - 00:06:52.490] donc pour installer Node.js sur ma barre de recherche Node.js une fois que c'est fait je mets GetNode.js

[00:06:52.490 - 00:07:36.340] juste ici et là j'installe tout est safe il n'y a pas de progressage et lui l'a installé la première fois

[00:07:36.340 - 00:07:41.850] je vais continuer accepter installer

[00:07:41.850 - 00:08:00.360] on passe l'installation l'installation est terminée donc je peux fermer la partie là mais tu n'es pas placé dans Corbeil

[00:08:00.360 - 00:08:08.180] cliquez sur conserver et on peut passer du coup à la prochaine étape qui est l'étape 3

[00:08:08.180 - 00:08:11.940] l'étape 3 c'est installer Cloud Code

[00:08:11.940 - 00:08:17.980] on sait que maintenant Node.js est là on a besoin d'une seule commande donc vous allez sur le support technique

[00:08:17.980 - 00:08:33.750] vous cliquez retourner du coup et vous faites entrer

[00:08:33.750 - 00:08:43.720] et Cloud Code ça prend un petit peu de temps

[00:08:43.720 - 00:08:46.650] ok c'est terminé

[00:08:46.650 - 00:08:48.650] maintenant on voit qu'on a trois packages installés

[00:08:48.650 - 00:08:53.210] Cloud Code a bien été installé

[00:08:53.210 - 00:08:55.210] on peut voir la version aussi qu'on a

[00:08:55.210 - 00:08:57.210] donc vous copiez cette commande là

[00:08:57.210 - 00:09:01.610] entrée, autre version

[00:09:01.610 - 00:09:06.420] donc c'est la dernière

[00:09:06.420 - 00:09:10.310] on peut passer à l'étape 4

[00:09:10.310 - 00:09:12.310] on va revenir rapidement sur la partie

[00:09:12.310 - 00:09:28.900] on arrive du coup sur l'interface officielle de Cloud

[00:09:28.900 - 00:09:31.450] donc si vous n'avez pas de compte

[00:09:31.450 - 00:09:33.450] vous en créez un avec votre adresse email

[00:09:33.450 - 00:09:35.700] et vous allez arriver du coup sur cette interface là

[00:09:35.700 - 00:09:42.200] donc vous allez cliquer sur le profil en bas à gauche

[00:09:42.200 - 00:09:55.240] les forfaits, simplement pas utile tout au long de la formation

[00:09:55.240 - 00:09:57.370] vous allez vous retrouver trop vite bloqué

[00:09:57.370 - 00:09:59.370] vous allez perdre du temps

[00:09:59.370 - 00:10:01.590] donc je vous conseille de partir directement sur l'abonnement Max

[00:10:01.590 - 00:10:03.910] l'abonnement Max

[00:10:03.910 - 00:10:16.630] qui est facturé avec 20%

[00:10:16.630 - 00:10:20.040] c'est Max qui s'offre à vous

[00:10:20.040 - 00:10:22.040] 20 fois plus d'utilisation pro

[00:10:22.040 - 00:10:28.710] et la version du coup je vous conseille celle-ci

[00:10:28.710 - 00:10:30.870] derrière vous allez être safe en terme de quota

[00:10:30.870 - 00:10:32.870] une fois que vous avez sélectionné votre forfait

[00:10:32.870 - 00:10:35.670] vous allez passer commande

[00:10:35.670 - 00:10:37.670] une fois que vous avez validé votre abonnement

[00:10:37.670 - 00:10:39.670] de manière automatique

[00:10:39.670 - 00:10:42.120] votre profil juste en bas va se mettre à jour

[00:10:42.120 - 00:10:46.040] l'abonnement que vous avez sélectionné

[00:10:46.040 - 00:10:48.620] ce qu'on va faire ensuite

[00:10:48.620 - 00:10:51.030] on va passer du coup à l'étape 5

[00:10:51.030 - 00:10:53.030] lancer Cloud Code

[00:10:53.030 - 00:10:55.030] pour lancer Cloud Code

[00:10:55.030 - 00:10:58.540] c'est pas compliqué

[00:10:58.540 - 00:11:20.820] relancer du coup

[00:11:20.820 - 00:11:25.030] moi personnellement je vais sur le dark mode

[00:11:25.030 - 00:11:27.030] parce que moi je me suis habitué à ça

[00:11:27.030 - 00:11:31.530] mais ça change pas grand chose si vous préférez le light mode

[00:11:31.530 - 00:11:34.650] entrez

[00:11:34.650 - 00:11:39.270] ensuite 3 options s'offrent

[00:11:39.270 - 00:11:41.750] on a la Cloud Hakune question

[00:11:41.750 - 00:11:43.750] avec abonnement

[00:11:43.750 - 00:11:45.750] on a la partie par API

[00:11:45.750 - 00:11:48.070] donc ça c'est ce qu'on a vu tout à l'heure

[00:11:48.070 - 00:11:50.460] payer par exécution

[00:11:50.460 - 00:11:58.700] ça va vous revenir très cher si vous utilisez l'option là

[00:11:58.700 - 00:12:01.880] on a une entrée

[00:12:01.880 - 00:12:03.880] et là ça nous redirige directement

[00:12:03.880 - 00:12:06.740] vers

[00:12:06.740 - 00:12:08.670] c'est

[00:12:08.670 - 00:12:12.390] Cloud Code

[00:12:12.390 - 00:12:13.390] souhaite se connecter

[00:12:13.390 - 00:12:15.450] Cloud Chat

[00:12:15.450 - 00:12:19.460] accéder à vos informations

[00:12:19.460 - 00:12:23.250] distribuer à l'utilisation

[00:12:23.250 - 00:12:24.250] du forfait Cloud

[00:12:24.250 - 00:12:26.250] accéder à vos sessions

[00:12:26.250 - 00:12:27.250] Cloud Code

[00:12:27.250 - 00:12:28.250] utiliser et gérer vos connecteurs

[00:12:28.250 - 00:12:30.250] téléverser des fichiers

[00:12:30.250 - 00:12:33.270] cliquer sur autoriser

[00:12:33.270 - 00:12:42.060] connecter à mon abonnement

[00:12:42.060 - 00:12:51.700] entrer

[00:12:51.700 - 00:12:56.280] j'utilise comme de base

[00:12:56.280 - 00:12:57.280] et là

[00:12:57.280 - 00:12:59.540] vous êtes sur l'interface Cloud Code

[00:12:59.540 - 00:13:01.540] connecter directement

[00:13:01.540 - 00:13:03.600] à votre terminal

[00:13:03.600 - 00:13:05.600] donc tout est bien installé

[00:13:05.600 - 00:13:08.620] on peut passer du coup

[00:13:08.620 - 00:13:10.580] une étape

[00:13:10.580 - 00:13:15.140] Cloud Code marche de plusieurs façons

[00:13:15.140 - 00:13:18.350] on peut l'utiliser

[00:13:18.350 - 00:13:19.350] VS Code

[00:13:19.350 - 00:13:21.090] VS Code

[00:13:21.090 - 00:13:22.090] on peut l'utiliser sur le web

[00:13:22.090 - 00:13:23.150] donc sur le web

[00:13:23.150 - 00:13:24.180] c'est juste ici

[00:13:24.180 - 00:13:25.180] si vous allez

[00:13:25.180 - 00:13:26.630] sur l'interface

[00:13:26.630 - 00:13:30.230] sur code à gauche

[00:13:30.230 - 00:13:35.580] marche sur Cloud Code

[00:13:35.580 - 00:13:37.220] le problème

[00:13:37.220 - 00:13:38.220] c'est que vous êtes obligé

[00:13:38.220 - 00:13:39.220] de vous connecter avec Github

[00:13:39.220 - 00:13:41.960] si vous travaillez

[00:13:41.960 - 00:13:44.660] sur Cloud Web

[00:13:44.660 - 00:13:45.660] vous allez travailler

[00:13:45.660 - 00:13:47.660] sur des repos Github

[00:13:47.660 - 00:13:48.660] c'est un petit peu problématique

[00:13:48.660 - 00:13:50.700] en termes d'organisation

[00:13:50.700 - 00:13:51.700] donc je vous recommande pas

[00:13:51.700 - 00:13:52.700] cette partie

[00:13:52.700 - 00:13:54.720] je vous recommande par contre

[00:13:54.720 - 00:13:56.940] c'est intéressant

[00:13:56.940 - 00:13:57.940] si derrière

[00:13:57.940 - 00:14:01.020] le terminal

[00:14:01.020 - 00:14:02.590] mais si vous travaillez sur le terminal

[00:14:02.590 - 00:14:03.590] vous allez utiliser

[00:14:03.590 - 00:14:06.710] l'application desktop

[00:14:06.710 - 00:14:08.800] ou Cloud

[00:14:08.800 - 00:14:10.280] donc ça marche

[00:14:10.280 - 00:14:11.280] pareil que le terminal

[00:14:11.280 - 00:14:12.470] vous pouvez

[00:14:12.470 - 00:14:13.470] travailler directement

[00:14:13.470 - 00:14:14.470] avec un dossier

[00:14:14.470 - 00:14:17.420] donc pareil

[00:14:17.420 - 00:14:18.420] et là si on lui envoie un message

[00:14:18.420 - 00:14:19.420] derrière

[00:14:20.900 - 00:14:21.900] il va travailler à l'intérieur

[00:14:21.900 - 00:14:23.000] de ce dossier là

[00:14:23.000 - 00:14:24.000] donc il doit nous créer un site internet

[00:14:24.000 - 00:14:25.000] il le mettra à l'intérieur

[00:14:25.000 - 00:14:26.580] de ce dossier

[00:14:26.580 - 00:14:27.580] donc maintenant

[00:14:27.580 - 00:14:29.640] on va tout simplement

[00:14:29.640 - 00:14:31.600] lui demander

[00:14:31.600 - 00:14:34.490] de nous créer

[00:14:34.490 - 00:14:35.550] un petit site internet

[00:14:35.550 - 00:14:36.550] donc créer

[00:14:36.550 - 00:14:53.680] relativement simple

[00:14:53.680 - 00:14:54.680] le but

[00:14:54.680 - 00:14:56.860] c'est un petit peu

[00:14:56.860 - 00:14:59.590] à dire

[00:14:59.590 - 00:15:03.280] utiliser

[00:15:03.280 - 00:15:04.790] complètement

[00:15:04.790 - 00:15:05.790] consulter profil

[00:15:05.790 - 00:15:06.790] existant en mémoire

[00:15:06.790 - 00:15:07.790] donc là il va voir

[00:15:07.790 - 00:15:08.950] que derrière

[00:15:08.950 - 00:15:09.950] on a rien du tout

[00:15:09.950 - 00:15:20.460] sur le dossier

[00:15:20.460 - 00:15:22.260] on va créer un site

[00:15:22.260 - 00:15:23.260] en automatisation

[00:15:23.260 - 00:15:24.260] il y a

[00:15:24.260 - 00:15:25.260] je vais construire un site

[00:15:25.260 - 00:15:26.260] moderne responsive

[00:15:26.260 - 00:15:27.510] et complet

[00:15:27.510 - 00:15:28.510] on pourra lui donner

[00:15:28.510 - 00:15:29.510] un meilleur prompt

[00:15:29.510 - 00:15:30.800] pour qu'il améliore le design

[00:15:30.800 - 00:15:31.800] encore une fois

[00:15:31.800 - 00:15:32.800] le but c'est de faire

[00:15:32.800 - 00:15:33.800] quelque chose de très simple

[00:15:33.800 - 00:15:36.140] pour le moment

[00:15:36.140 - 00:15:37.140] comprendre un petit peu

[00:15:37.140 - 00:15:39.460] on va utiliser

[00:15:39.460 - 00:15:42.130] là le ton qui réfléchit

[00:15:42.130 - 00:15:43.350] très bien

[00:15:43.350 - 00:15:44.350] le faire travailler

[00:15:44.350 - 00:15:52.300] le dossier qu'on a créé

[00:15:52.300 - 00:15:53.300] au tout départ

[00:15:53.300 - 00:15:54.980] clic gauche

[00:15:54.980 - 00:15:57.390] nouveau terminale au dossier

[00:15:57.390 - 00:15:59.030] donc là

[00:15:59.030 - 00:16:09.700] hop ça nous ouvre

[00:16:09.700 - 00:16:11.090] et derrière

[00:16:11.090 - 00:16:12.090] on a encore une fois

[00:16:12.090 - 00:16:13.090] l'interface de code code

[00:16:13.090 - 00:16:14.090] qui est connecté

[00:16:14.090 - 00:16:15.090] du coup à notre dossier

[00:16:15.090 - 00:16:18.180] qu'on a créé tout à l'heure

[00:16:18.180 - 00:16:19.180] en parallèle

[00:16:19.180 - 00:16:20.210] du site internet

[00:16:20.210 - 00:16:21.210] qu'il est en train de nous créer

[00:16:21.210 - 00:16:23.210] on pourrait lui dire

[00:16:23.210 - 00:16:24.500] je suis

[00:16:24.500 - 00:16:25.560] freelance

[00:16:25.560 - 00:16:29.480] en automatisation

[00:16:29.480 - 00:16:31.120] il y a

[00:16:31.120 - 00:16:32.120] je souhaite

[00:16:32.120 - 00:16:34.180] faire

[00:16:34.180 - 00:16:39.980] pousser

[00:16:39.980 - 00:16:41.650] csv

[00:16:41.650 - 00:16:43.420] donc là

[00:16:43.420 - 00:16:44.420] on lance

[00:16:44.420 - 00:16:45.420] notre prompt

[00:16:45.420 - 00:16:47.060] et on peut voir

[00:16:47.060 - 00:16:48.060] qu'il est en train de réfléchir

[00:16:48.060 - 00:16:49.060] et qu'il travaille

[00:16:49.060 - 00:16:50.060] en parallèle

[00:16:50.060 - 00:16:51.060] de la création

[00:16:51.060 - 00:16:52.060] de notre site internet

[00:16:52.060 - 00:16:53.060] donc là on gagne déjà

[00:16:53.060 - 00:16:54.060] beaucoup de temps

[00:16:54.060 - 00:16:55.700] on fait deux choses

[00:16:55.700 - 00:16:56.700] en même temps

[00:16:56.700 - 00:16:57.700] ça ça va être important

[00:16:57.700 - 00:16:59.370] de comprendre

[00:16:59.370 - 00:17:00.370] cette partie là

[00:17:00.370 - 00:17:01.370] pourquoi

[00:17:01.370 - 00:17:02.400] parce que

[00:17:02.400 - 00:17:03.400] on va

[00:17:03.400 - 00:17:04.400] chaque fois

[00:17:04.400 - 00:17:05.400] sur chaque projet

[00:17:05.400 - 00:17:07.100] mettre en place

[00:17:07.100 - 00:17:09.100] une stratégie similaire

[00:17:09.100 - 00:17:10.650] pour qu'on puisse bull

[00:17:10.650 - 00:17:12.130] rapidement

[00:17:12.130 - 00:17:14.220] sur des projets réels

[00:17:14.220 - 00:17:15.220] par exemple

[00:17:15.220 - 00:17:16.220] avec un client

[00:17:16.220 - 00:17:17.220] travailler sur

[00:17:17.220 - 00:17:18.220] cinq interfaces différentes

[00:17:18.220 - 00:17:19.220] pour

[00:17:19.220 - 00:17:20.290] à la place

[00:17:20.290 - 00:17:21.290] de prendre trois jours

[00:17:21.290 - 00:17:22.700] prendre tout simplement

[00:17:22.700 - 00:17:23.700] cinq à six heures

[00:17:23.700 - 00:17:24.700] et du coup

[00:17:24.700 - 00:17:25.700] être plus rentable

[00:17:25.700 - 00:17:27.980] sur le mois

[00:17:27.980 - 00:17:30.070] donc là

[00:17:30.070 - 00:17:31.070] il a pratiquement fini

[00:17:31.070 - 00:17:33.070] l'index.html

[00:17:33.070 - 00:17:34.810] là

[00:17:34.810 - 00:17:36.810] il a réfléchi

[00:17:36.810 - 00:17:37.810] il nous a demandé

[00:17:37.810 - 00:17:39.810] des informations similaires

[00:17:39.810 - 00:17:49.870] donc France uniquement

[00:17:49.870 - 00:17:50.870] qui nous dit

[00:17:50.870 - 00:17:51.870] angle de l'étude

[00:17:51.870 - 00:17:52.870] tu veux analyser le marché

[00:17:52.870 - 00:17:53.870] de l'automatisation

[00:17:53.870 - 00:17:54.870] Thaï

[00:17:54.870 - 00:17:55.870] et France

[00:17:55.870 - 00:17:56.870] je veux tout analyser

[00:17:56.870 - 00:17:58.190] donc on va pas se prendre la tête

[00:17:58.190 - 00:17:59.190] parce que là

[00:17:59.190 - 00:18:00.640] juste en phase exemple

[00:18:00.640 - 00:18:01.640] on pourrait très bien

[00:18:01.640 - 00:18:02.640] du coup améliorer cette partie là

[00:18:02.640 - 00:18:05.080] donc là

[00:18:05.080 - 00:18:06.400] c'est top

[00:18:06.400 - 00:18:09.320] en train de travailler en parallèle

[00:18:09.320 - 00:18:10.320] on pourrait aussi très bien

[00:18:10.320 - 00:18:11.320] je sais pas

[00:18:11.320 - 00:18:12.320] si vous avez une autre idée

[00:18:12.320 - 00:18:16.400] demander à Claude

[00:18:16.400 - 00:18:17.400] directement

[00:18:17.400 - 00:18:19.820] sur un nouveau terminal

[00:18:19.820 - 00:18:21.820] d'aller analyser

[00:18:21.820 - 00:18:23.620] LinkedIn

[00:18:23.620 - 00:18:24.620] qui sont intéressants

[00:18:24.620 - 00:18:25.620] dans votre niche

[00:18:25.620 - 00:18:29.560] dans une recherche

[00:18:29.560 - 00:18:31.560] sur tous les accents parallèles

[00:18:31.560 - 00:18:33.420] ok c'est top

[00:18:33.420 - 00:18:37.180] on va ouvrir

[00:18:37.180 - 00:18:38.180] le dossier juste ici

[00:18:38.180 - 00:18:39.180] on va voir

[00:18:39.180 - 00:18:41.940] s'il a terminé

[00:18:41.940 - 00:18:43.930] le coup

[00:18:43.930 - 00:18:44.930] il a créé trois fichiers

[00:18:44.930 - 00:18:46.790] une partie html

[00:18:46.790 - 00:18:48.940] une partie

[00:18:48.940 - 00:18:49.940] et là on peut voir

[00:18:49.940 - 00:18:51.970] qu'il a internet

[00:18:51.970 - 00:18:52.970] donc freelance

[00:18:52.970 - 00:18:53.970] automatisation

[00:18:53.970 - 00:18:54.970] il y a

[00:18:54.970 - 00:18:55.970] comme je vous ai dit

[00:18:55.970 - 00:18:56.970] au tout départ

[00:18:56.970 - 00:18:57.970] il ouvre automatiquement

[00:18:57.970 - 00:18:58.970] donc quand il a terminé

[00:18:58.970 - 00:18:59.970] ça qui est vraiment

[00:18:59.970 - 00:19:00.970] intéressant

[00:19:00.970 - 00:19:01.970] donc c'est vraiment un agent

[00:19:01.970 - 00:19:02.970] qui agit directement

[00:19:02.970 - 00:19:03.970] sur notre ordinateur

[00:19:03.970 - 00:19:05.970] je transforme vos processus

[00:19:05.970 - 00:19:07.970] avec l'intelligence artificielle

[00:19:07.970 - 00:19:08.970] quand on est vraiment

[00:19:08.970 - 00:19:09.970] sur un site

[00:19:09.970 - 00:19:12.180] tout simple

[00:19:12.180 - 00:19:13.250] il faut pousser

[00:19:13.250 - 00:19:14.250] mais c'est un bon départ

[00:19:14.250 - 00:19:16.700] on peut très bien

[00:19:16.700 - 00:19:17.890] tout simplement

[00:19:17.890 - 00:19:18.890] travailler

[00:19:18.890 - 00:19:19.890] enfin le retravailler

[00:19:19.890 - 00:19:20.890] donc là on pourrait

[00:19:20.890 - 00:19:22.080] lui dire

[00:19:22.080 - 00:19:23.460] sur le lien

[00:19:23.460 - 00:19:57.620] en question

[00:19:57.620 - 00:20:06.710] un tout simple

[00:20:06.710 - 00:20:08.580] entre temps

[00:20:08.580 - 00:20:24.260] la demande

[00:20:24.260 - 00:20:36.240] il y a deux agents

[00:20:36.240 - 00:20:37.240] qui ont terminé

[00:20:37.240 - 00:20:38.270] sur cinq

[00:20:38.270 - 00:20:40.270] donc si par exemple

[00:20:40.270 - 00:20:41.270] je fais flèche du bas

[00:20:41.270 - 00:20:43.370] là juste ici

[00:20:43.370 - 00:20:44.370] on voit qu'il y a trois

[00:20:44.370 - 00:20:45.370] local agents

[00:20:45.370 - 00:20:47.330] donc là ils sont en train

[00:20:47.330 - 00:20:48.810] comme on voit

[00:20:48.810 - 00:20:49.810] une ligne

[00:20:49.810 - 00:20:50.870] donc travailler

[00:20:50.870 - 00:20:51.870] et une fois

[00:20:51.870 - 00:20:52.870] qu'ils ont terminé

[00:20:52.870 - 00:20:53.900] leurs tâches

[00:20:53.900 - 00:20:54.900] eh bien CloudCode

[00:20:54.900 - 00:20:55.900] va nous mentionner

[00:20:55.900 - 00:20:56.900] que c'est bon

[00:20:56.900 - 00:20:57.900] le fichier csv est prêt

[00:20:57.900 - 00:21:00.470] et on va voir

[00:21:00.470 - 00:21:01.470] directement

[00:21:01.470 - 00:21:12.900] juste ici

[00:21:12.900 - 00:21:13.900] je suis en train

[00:21:13.900 - 00:21:14.900] d'écrire des lignes de code

[00:21:14.900 - 00:21:15.900] là je lui ai demandé

[00:21:15.900 - 00:21:17.190] de changer

[00:21:17.190 - 00:21:18.190] du coup la couleur

[00:21:18.190 - 00:21:24.860] ou l'util css

[00:21:24.860 - 00:21:50.780] vous allez voir

[00:21:50.780 - 00:21:51.780] au départ

[00:21:51.780 - 00:21:52.780] c'est un petit peu

[00:21:52.780 - 00:21:53.780] complexe

[00:21:53.780 - 00:21:54.780] vous n'avez pas l'habitude

[00:21:54.780 - 00:21:55.780] de travailler

[00:21:55.780 - 00:21:56.780] sur un terminal

[00:21:56.780 - 00:21:57.780] mais au fur et à mesure

[00:21:57.780 - 00:22:01.130] en fait ça va vous paraître

[00:22:01.130 - 00:22:02.130] très simple

[00:22:02.130 - 00:22:03.130] parce que mis à part

[00:22:03.130 - 00:22:04.130] faire des demandes

[00:22:04.130 - 00:22:05.130] à CloudCode

[00:22:05.130 - 00:22:06.130] vous n'avez pratiquement

[00:22:06.130 - 00:22:07.130] rien à faire

[00:22:07.130 - 00:22:08.130] le plus important

[00:22:08.130 - 00:22:09.130] c'est vraiment

[00:22:09.130 - 00:22:10.130] bien structurer

[00:22:10.130 - 00:22:11.130] votre projet

[00:22:11.130 - 00:22:12.130] avoir un bon système

[00:22:12.130 - 00:22:13.130] de prompting

[00:22:13.130 - 00:22:14.380] et comprendre

[00:22:14.380 - 00:22:15.380] la réflexion

[00:22:15.380 - 00:22:16.380] de CloudCode

[00:22:16.380 - 00:22:17.380] pour arriver à votre objectif

[00:22:17.380 - 00:22:18.380] le plus rapidement possible

[00:22:18.380 - 00:22:20.740] et c'est ce qu'on va voir

[00:22:20.740 - 00:22:21.740] tout au long

[00:22:21.740 - 00:22:26.220] de la formation

[00:22:26.220 - 00:22:28.440] donc là

[00:22:28.440 - 00:22:29.440] on va bientôt terminer

[00:22:29.440 - 00:22:34.470] parce que

[00:22:34.470 - 00:22:39.150] pour le light mode

[00:22:39.150 - 00:22:40.150] donc là il est en train

[00:22:40.150 - 00:22:41.150] d'ajouter un light mode

[00:22:41.150 - 00:22:42.150] top

[00:22:42.150 - 00:22:43.220] on peut voir

[00:22:43.220 - 00:22:44.220] que juste ici

[00:22:44.220 - 00:22:45.220] on a 3 agents

[00:22:45.220 - 00:22:46.310] qui ont terminé

[00:22:46.310 - 00:22:47.310] donc là c'est super

[00:22:47.310 - 00:22:48.310] on a fini

[00:22:48.310 - 00:22:50.720] enfin CloudCode

[00:22:50.720 - 00:22:51.720] a fini du coup

[00:22:51.720 - 00:22:52.780] le site internet

[00:22:52.780 - 00:22:53.780] il l'a bien remis

[00:22:53.780 - 00:22:55.650] en full blanc

[00:22:55.650 - 00:23:10.410] des itérations

[00:23:10.410 - 00:23:13.110] pour arriver à une version

[00:23:13.110 - 00:23:16.540] qui est

[00:23:16.540 - 00:23:17.540] je clique dessus

[00:23:17.540 - 00:23:19.380] ça va bien m'envoyer

[00:23:19.380 - 00:23:20.380] après je ne vais pas donner le bon lien

[00:23:20.380 - 00:23:21.380] mais vers Linkedin

[00:23:21.380 - 00:23:22.410] voilà le lien que j'ai mis

[00:23:22.410 - 00:23:23.410] vous pouvez très bien aussi

[00:23:23.410 - 00:23:27.140] envoyer un screen à CloudCode

[00:23:27.140 - 00:23:28.970] votre tête

[00:23:28.970 - 00:23:30.100] pour qu'il l'ajoute

[00:23:30.100 - 00:23:31.420] automatiquement

[00:23:31.420 - 00:23:39.810] maintenant

[00:23:39.810 - 00:23:41.220] comme vous l'avez vu

[00:23:41.220 - 00:23:42.220] c'est un dialogue

[00:23:42.220 - 00:23:43.220] ça ne va pas être un formulaire

[00:23:43.220 - 00:23:44.220] donc si je lui dis

[00:23:44.220 - 00:23:45.220] de créer un fichier HTML

[00:23:45.220 - 00:23:46.220] avec un titre mon site

[00:23:46.220 - 00:23:48.220] il va le faire directement

[00:23:48.220 - 00:23:50.120] il va créer des vrais fichiers

[00:23:50.120 - 00:23:51.120] on l'a vu aussi

[00:23:51.120 - 00:23:56.150] je l'ai créé

[00:23:56.150 - 00:24:12.960] usage

[00:24:12.960 - 00:24:14.470] extra usage

[00:24:14.470 - 00:24:22.140] utilisé 22%

[00:24:22.140 - 00:24:23.140] aujourd'hui

[00:24:23.140 - 00:24:24.140] donc ça va se réinitialiser

[00:24:24.140 - 00:24:25.140] dans 24 minutes

[00:24:25.140 - 00:24:27.140] et on a une partie

[00:24:27.140 - 00:24:28.140] qui se réinitialise

[00:24:28.140 - 00:24:30.140] tous les lundis à 11h

[00:24:30.140 - 00:24:32.140] donc là j'ai utilisé 30%

[00:24:32.140 - 00:24:33.140] donc je suis assez safe

[00:24:33.140 - 00:24:34.140] en termes de taille

[00:24:34.140 - 00:24:35.140] et là on a la partie

[00:24:35.140 - 00:24:36.140] usage supplémentaire

[00:24:36.140 - 00:24:38.680] ça c'est quand tout simplement

[00:24:38.680 - 00:24:40.190] j'ai trop utilisé

[00:24:40.190 - 00:24:41.800] bonnement

[00:24:41.800 - 00:24:42.800] j'utilise par API

[00:24:42.800 - 00:24:45.020] mais ça vous n'allez pas avoir besoin

[00:24:45.020 - 00:24:47.080] parce que je travaille

[00:24:47.080 - 00:24:48.080] avec beaucoup de clients

[00:24:48.080 - 00:24:49.080] et du coup je suis obligé parfois

[00:24:49.080 - 00:24:50.560] de travailler

[00:24:50.560 - 00:24:52.390] donc voilà

[00:24:52.390 - 00:24:58.550] voir comment bien lui parler

[00:24:58.550 - 00:24:59.550] donc comme vous l'avez vu

[00:24:59.550 - 00:25:00.550] là je suis allé sur des promes

[00:25:00.550 - 00:25:01.550] basiques

[00:25:01.550 - 00:25:03.100] donc la règle numéro 1

[00:25:03.100 - 00:25:04.100] c'est être vraiment précis

[00:25:04.100 - 00:25:05.100] donc fais moi un site

[00:25:05.100 - 00:25:06.100] ça ne va pas être top

[00:25:06.100 - 00:25:07.100] il ne va pas comprendre

[00:25:07.100 - 00:25:08.100] il va te faire un site basique

[00:25:08.100 - 00:25:09.100] on ne sait même pas

[00:25:09.100 - 00:25:10.100] sur quel secteur d'activité

[00:25:10.100 - 00:25:11.100] il va aller etc

[00:25:11.100 - 00:25:12.100] donc c'est là où derrière

[00:25:12.100 - 00:25:13.100] il va quand même nous poser

[00:25:13.100 - 00:25:14.100] des questions par la suite

[00:25:14.100 - 00:25:17.300] pour le souhaiter réellement

[00:25:17.300 - 00:25:19.850] c'est pour ça qu'il faut être vraiment précis

[00:25:19.850 - 00:25:20.850] créez moi un site vitrine

[00:25:20.850 - 00:25:21.850] pour un plombier à Lyon

[00:25:21.850 - 00:25:22.850] là on lui donne l'information

[00:25:22.850 - 00:25:25.740] à un plombier

[00:25:25.740 - 00:25:26.740] et que c'est à Lyon

[00:25:26.740 - 00:25:28.770] il nous faut une page d'accueil

[00:25:28.770 - 00:25:29.770] avec un héros

[00:25:29.770 - 00:25:30.770] service avec 4 cartes

[00:25:30.770 - 00:25:31.770] formulaire de contact

[00:25:31.770 - 00:25:32.770] là il va vraiment nous créer

[00:25:32.770 - 00:25:33.770] ce qu'on lui a demandé

[00:25:33.770 - 00:25:36.060] ensuite la règle numéro 2

[00:25:36.060 - 00:25:37.060] c'est de lui donner du contexte

[00:25:37.060 - 00:25:38.060] on va lui dire

[00:25:38.060 - 00:25:39.890] pour qui

[00:25:39.890 - 00:25:40.890] pourquoi

[00:25:40.890 - 00:25:41.890] quel style

[00:25:41.890 - 00:25:43.890] plus il sait mieux c'est

[00:25:43.890 - 00:25:44.890] c'est pas

[00:25:44.890 - 00:25:46.820] ça va servir à rien

[00:25:46.820 - 00:25:47.820] de créer un prompt

[00:25:47.820 - 00:25:48.820] de 600 euros

[00:25:48.820 - 00:25:49.820] là il va se perdre

[00:25:49.820 - 00:25:50.820] il va commencer à halluciner

[00:25:50.820 - 00:25:51.820] il va sortir

[00:25:51.820 - 00:25:53.300] votre demande

[00:25:53.300 - 00:25:54.300] et réaliser quelque chose

[00:25:54.300 - 00:25:55.300] qui n'a rien à voir

[00:25:55.300 - 00:25:56.300] donc c'est pour ça qu'il va

[00:25:56.300 - 00:25:57.300] bien falloir

[00:25:57.300 - 00:25:58.300] structurer notre prompt

[00:25:58.300 - 00:26:01.060] ce qu'on va voir au fur et à mesure

[00:26:01.060 - 00:26:02.060] de la formation

[00:26:02.060 - 00:26:03.670] par exemple

[00:26:03.670 - 00:26:04.670] s'il a derrière

[00:26:04.670 - 00:26:06.310] de créer un script

[00:26:06.310 - 00:26:07.310] d'une part

[00:26:07.310 - 00:26:08.310] on lui donne l'information script

[00:26:08.310 - 00:26:11.140] qu'on peut faire

[00:26:11.140 - 00:26:12.140] ensuite

[00:26:12.140 - 00:26:13.140] qu'il scrappe les restaurants

[00:26:13.140 - 00:26:14.140] donc là

[00:26:14.140 - 00:26:15.200] il va savoir que c'est les restaurants

[00:26:15.200 - 00:26:16.200] c'est pas les plombiers

[00:26:16.200 - 00:26:17.200] c'est pas les avocats etc

[00:26:17.200 - 00:26:18.200] et de Lyon

[00:26:18.200 - 00:26:20.200] donc on lui donne le secteur géographique

[00:26:20.200 - 00:26:24.280] c'est seulement des leads de Lyon

[00:26:24.280 - 00:26:26.280] récupérés seulement sur Google Maps

[00:26:26.280 - 00:26:27.280] donc là il a toutes les informations

[00:26:27.280 - 00:26:28.280] de ce qu'il doit faire

[00:26:28.280 - 00:26:29.410] et ensuite

[00:26:29.410 - 00:26:31.950] ce qu'on lui demande comme résultat

[00:26:31.950 - 00:26:34.400] c'est qu'on veut les noms

[00:26:34.400 - 00:26:36.330] l'adresse

[00:26:36.330 - 00:26:37.330] les téléphones

[00:26:37.330 - 00:26:40.330] et la note qu'il a sur Google Maps

[00:26:40.330 - 00:26:44.090] une fois qu'il a toutes ces informations là

[00:26:44.090 - 00:26:45.250] il nous font un CSV

[00:26:45.250 - 00:26:46.250] qu'on va utiliser

[00:26:46.250 - 00:26:48.540] pour le mettre sur Google Sheet

[00:26:48.540 - 00:26:50.080] voilà la partie

[00:26:50.080 - 00:26:51.080] avec beaucoup de contexte

[00:26:51.080 - 00:26:52.080] un prompt tout simple

[00:26:52.080 - 00:26:53.080] court

[00:26:53.080 - 00:26:54.400] derrière

[00:26:54.400 - 00:26:55.400] on est sûr qu'il va pas se tromper

[00:26:55.400 - 00:26:56.400] et la règle numéro 3

[00:26:56.400 - 00:26:57.400] sur des gros projets

[00:26:57.400 - 00:26:59.400] ça va être d'itérer

[00:26:59.400 - 00:27:00.780] on lui donne une instruction

[00:27:00.780 - 00:27:02.200] juste ici

[00:27:02.200 - 00:27:04.580] on regarde les résultats

[00:27:04.580 - 00:27:06.570] si ça nous plait pas

[00:27:06.570 - 00:27:07.570] change ça

[00:27:07.570 - 00:27:08.570] ajoute ça

[00:27:08.570 - 00:27:09.570] enlève ça

[00:27:09.570 - 00:27:10.570] tu re-regarde

[00:27:10.570 - 00:27:11.570] et quand c'est bon

[00:27:11.570 - 00:27:12.570] on peut passer

[00:27:12.570 - 00:27:13.570] à la prochaine phase

[00:27:13.570 - 00:27:15.660] donc là on va parler

[00:27:15.660 - 00:27:18.960] par la suite

[00:27:18.960 - 00:27:20.060] fichiers MD

[00:27:20.060 - 00:27:21.060] tout d'abord on va voir

[00:27:21.060 - 00:27:22.660] un petit peu

[00:27:22.660 - 00:27:23.660] les résultats

[00:27:23.660 - 00:27:41.590] donc ça

[00:27:41.590 - 00:27:43.420] par défaut

[00:27:43.420 - 00:27:45.840] on peut voir juste ici en bas

[00:27:45.840 - 00:27:46.870] height effort

[00:27:46.870 - 00:27:51.650] on peut très bien réduire

[00:27:51.650 - 00:27:53.640] si j'ai plus de token

[00:27:53.640 - 00:27:55.640] on peut partir en medium effort

[00:27:55.640 - 00:27:56.640] en low effort

[00:27:56.640 - 00:27:58.790] moi je pars directement

[00:27:58.790 - 00:28:01.300] sur le plus puissant

[00:28:01.300 - 00:28:02.300] donc max effort

[00:28:02.300 - 00:28:04.680] je vous conseille de faire de même

[00:28:04.680 - 00:28:05.680] ok sur entrée

[00:28:05.680 - 00:28:07.190] si derrière

[00:28:07.190 - 00:28:09.800] vous voulez changer de modèle

[00:28:09.800 - 00:28:12.120] sonner 4.6

[00:28:12.120 - 00:28:13.150] avec un million de contexte

[00:28:13.150 - 00:28:14.150] ou sonner directement

[00:28:14.150 - 00:28:15.150] celui-ci

[00:28:15.150 - 00:28:16.600] je crois que celui-ci

[00:28:16.600 - 00:28:18.600] il a 5 millions de contexte

[00:28:18.600 - 00:28:20.020] lui il a 1 million de contexte

[00:28:20.020 - 00:28:21.020] le contexte c'est quoi ?

[00:28:21.020 - 00:28:23.300] c'est la mémoire de code code

[00:28:23.300 - 00:28:25.300] si derrière

[00:28:25.300 - 00:28:26.330] je sais pas

[00:28:26.330 - 00:28:27.330] on travaille avec lui

[00:28:27.330 - 00:28:28.330] pendant une heure

[00:28:28.330 - 00:28:31.730] ça va pas se reset

[00:28:31.730 - 00:28:32.730] du coup

[00:28:32.730 - 00:28:33.730] on va pouvoir travailler

[00:28:33.730 - 00:28:34.980] avec lui bon temps

[00:28:34.980 - 00:28:35.980] avec beaucoup de contexte

[00:28:35.980 - 00:28:36.980] et il va comprendre constamment

[00:28:36.980 - 00:28:37.980] les axes d'amélioration

[00:28:37.980 - 00:28:38.980] qu'on souhaite

[00:28:38.980 - 00:28:40.980] plus souvent on a juste

[00:28:40.980 - 00:28:41.980] un million de contexte

[00:28:41.980 - 00:28:42.980] c'est déjà énorme

[00:28:42.980 - 00:28:45.290] on peut voir juste à droite

[00:28:45.290 - 00:28:46.290] par contre il est toujours

[00:28:46.290 - 00:28:47.290] en train de travailler

[00:28:47.290 - 00:28:50.250] au niveau de l'étude de marché

[00:28:50.250 - 00:28:51.250] donc maintenant

[00:28:51.250 - 00:28:53.370] ce qu'on va faire

[00:28:53.370 - 00:28:55.010] c'est qu'on va sectionner

[00:28:55.010 - 00:28:56.010] on va parler de la partie

[00:28:56.010 - 00:28:57.230] MD

[00:28:57.230 - 00:28:58.230] donc le fichier MD

[00:28:58.230 - 00:28:59.230] c'est un fichier texte

[00:28:59.230 - 00:29:00.230] que tu mets dans ton projet

[00:29:00.230 - 00:29:01.230] donc notre projet

[00:29:01.230 - 00:29:02.230] c'est notre dossier

[00:29:02.230 - 00:29:03.230] juste ici

[00:29:03.230 - 00:29:05.380] et ensuite

[00:29:05.380 - 00:29:06.380] cloud code

[00:29:06.380 - 00:29:07.380] lit automatiquement chaque session

[00:29:07.380 - 00:29:08.380] et du coup

[00:29:08.380 - 00:29:09.380] il va savoir

[00:29:09.380 - 00:29:12.270] ce que je fais actuellement

[00:29:12.270 - 00:29:14.270] et comment je veux bosser

[00:29:14.270 - 00:29:15.620] plus besoin de répéter

[00:29:15.620 - 00:29:16.620] constamment le code

[00:29:16.620 - 00:29:18.650] donc si

[00:29:18.650 - 00:29:25.340] il va le faire

[00:29:25.340 - 00:29:26.340] ensuite on va l'ouvrir

[00:29:26.340 - 00:29:27.340] fais moi

[00:29:27.340 - 00:29:51.960] il fait chier

[00:29:51.960 - 00:29:52.960] il a trouvé un pattern

[00:29:52.960 - 00:29:53.960] donc le pattern

[00:29:53.960 - 00:30:05.840] c'est notre site

[00:30:05.840 - 00:30:06.840] il a déjà créé leur ennemi

[00:30:06.840 - 00:30:08.840] donc on va pouvoir très bien

[00:30:08.840 - 00:30:09.940] l'ouvrir

[00:30:09.940 - 00:30:10.940] comme on peut voir

[00:30:10.940 - 00:30:11.940] derrière

[00:30:11.940 - 00:30:13.000] il est juste ici

[00:30:13.000 - 00:30:14.000] dans notre dossier

[00:30:14.000 - 00:30:15.000] donc il l'a créé directement

[00:30:15.000 - 00:30:16.000] encore une fois

[00:30:16.000 - 00:30:17.000] dans notre dossier

[00:30:17.000 - 00:30:18.000] si je fais clic droit

[00:30:18.000 - 00:30:19.130] clic gauche pardon

[00:30:19.130 - 00:30:20.130] ouvrir

[00:30:20.130 - 00:30:21.510] avec

[00:30:21.510 - 00:30:22.510] text edit

[00:30:22.510 - 00:30:24.950] on peut voir

[00:30:24.950 - 00:30:25.950] que derrière

[00:30:25.950 - 00:30:26.950] Baptistefort

[00:30:26.950 - 00:30:28.020] site freelance

[00:30:28.020 - 00:30:29.020] automatisation

[00:30:29.020 - 00:30:30.020] il y a

[00:30:30.020 - 00:30:31.020] site vitrine personnelle

[00:30:31.020 - 00:30:32.020] et freelance en automatisation

[00:30:32.020 - 00:30:33.020] il y a

[00:30:33.020 - 00:30:34.020] donc là on voit la structure

[00:30:34.020 - 00:30:35.020] du projet

[00:30:35.020 - 00:30:37.110] donc index.html

[00:30:37.110 - 00:30:38.110] style sss

[00:30:38.110 - 00:30:39.110] effet etc

[00:30:39.110 - 00:30:40.110] le style

[00:30:40.110 - 00:30:41.850] design

[00:30:41.850 - 00:30:42.850] le script js

[00:30:42.850 - 00:30:43.850] pour les animations

[00:30:43.850 - 00:30:45.140] du coup

[00:30:45.140 - 00:30:46.140] le redmi ce fichier là

[00:30:46.140 - 00:30:48.510] des sections

[00:30:48.510 - 00:30:52.010] pour le service

[00:30:52.010 - 00:30:53.010] la méthode

[00:30:53.010 - 00:30:54.010] le cas client

[00:30:54.010 - 00:30:55.010] les témoignages

[00:30:55.010 - 00:30:56.010] à propos

[00:30:56.010 - 00:30:57.010] et la partie contact

[00:30:57.010 - 00:30:59.010] stack html css

[00:30:59.010 - 00:31:00.420] donc utiliser

[00:31:00.420 - 00:31:02.780] la police d'écriture

[00:31:02.780 - 00:31:03.780] les icônes

[00:31:03.780 - 00:31:04.780] les fonctionnalités

[00:31:04.780 - 00:31:05.780] la personnalisation

[00:31:05.780 - 00:31:06.780] les informations

[00:31:06.780 - 00:31:07.780] à mettre à jour

[00:31:07.780 - 00:31:08.780] email remplacer

[00:31:08.780 - 00:31:09.780] contact

[00:31:09.780 - 00:31:10.780] Baptistefort

[00:31:10.780 - 00:31:11.780] dans index

[00:31:11.780 - 00:31:12.780] donc voilà

[00:31:12.780 - 00:31:14.320] là

[00:31:14.320 - 00:31:15.320] l'objectif d'avoir

[00:31:15.320 - 00:31:16.320] ce redmi là

[00:31:16.320 - 00:31:17.540] c'est que si derrière

[00:31:17.540 - 00:31:18.540] je quitte cette session

[00:31:18.540 - 00:31:19.540] et que je la relance

[00:31:19.540 - 00:31:20.540] par la suite

[00:31:20.540 - 00:31:21.610] je vais lui dire

[00:31:21.610 - 00:31:22.610] de lire le redmi

[00:31:22.610 - 00:31:23.610] donc on va le faire

[00:31:23.610 - 00:31:28.060] terminer

[00:31:28.060 - 00:31:31.340] réouvrir du coup

[00:31:31.340 - 00:31:32.340] une nouvelle session

[00:31:32.340 - 00:31:34.620] comme on a fait tout à l'heure

[00:31:34.620 - 00:31:35.620] clic gauche

[00:31:35.620 - 00:31:37.740] nouveau terminal

[00:31:37.740 - 00:31:38.740] au dossier

[00:31:38.740 - 00:31:41.770] on tape la commande cloud

[00:31:41.770 - 00:31:42.830] pour activer cloud code

[00:31:42.830 - 00:31:45.370] et ensuite

[00:31:45.370 - 00:31:46.370] il y a deux solutions

[00:31:46.370 - 00:31:47.370] soit je lui dis

[00:31:47.370 - 00:31:53.390] je peux très bien

[00:31:53.390 - 00:31:58.100] faire ça

[00:31:58.100 - 00:31:59.100] le fichier

[00:31:59.100 - 00:32:05.670] il va le lire automatiquement

[00:32:05.670 - 00:32:06.670] le redmi d'un site

[00:32:06.670 - 00:32:07.670] vitine finance

[00:32:07.670 - 00:32:08.670] pour Baptistefort

[00:32:08.670 - 00:32:09.670] donc moi

[00:32:09.670 - 00:32:10.670] spécialise en automatisation

[00:32:10.670 - 00:32:11.670] il y a

[00:32:11.670 - 00:32:12.670] projet

[00:32:12.670 - 00:32:13.670] site statique

[00:32:13.670 - 00:32:14.670] html

[00:32:14.670 - 00:32:15.670] donc il a bien compris

[00:32:15.670 - 00:32:16.670] le code qu'on avait

[00:32:16.670 - 00:32:18.540] 4 fichiers

[00:32:18.540 - 00:32:19.540] 7 sections

[00:32:19.540 - 00:32:21.270] etc

[00:32:21.270 - 00:32:22.270] chose à finaliser

[00:32:22.270 - 00:32:23.270] selon le redmi

[00:32:23.270 - 00:32:24.270] remplacer l'email

[00:32:24.270 - 00:32:25.270] donc là

[00:32:25.270 - 00:32:26.270] c'est superbe

[00:32:26.270 - 00:32:27.980] il a bien compris

[00:32:27.980 - 00:32:28.980] le lien twitter

[00:32:28.980 - 00:32:29.980] remplacer les témoignages

[00:32:29.980 - 00:32:30.980] par des vrais avis

[00:32:30.980 - 00:32:31.980] connecter le formulaire

[00:32:31.980 - 00:32:32.980] de contact

[00:32:32.980 - 00:32:33.980] France prix

[00:32:33.980 - 00:32:34.980] aux autres

[00:32:34.980 - 00:32:37.190] on pourrait très bien

[00:32:37.190 - 00:32:38.190] lui dire

[00:32:38.190 - 00:32:39.190] remplace

[00:32:39.190 - 00:32:40.190] l'adresse

[00:32:40.190 - 00:32:41.580] email

[00:32:41.580 - 00:32:42.580] par

[00:32:42.580 - 00:32:45.590] arrobase

[00:32:45.590 - 00:33:04.350] là on a terminé aussi

[00:33:04.350 - 00:33:06.350] notre étude de marché

[00:33:06.350 - 00:33:08.350] avec 13 fichiers csv

[00:33:08.350 - 00:33:09.350] 41

[00:33:09.350 - 00:33:10.350] codes de données

[00:33:10.350 - 00:33:11.350] structurés

[00:33:11.350 - 00:33:13.150] donc là

[00:33:13.150 - 00:33:14.150] ce qui va être relou

[00:33:14.150 - 00:33:15.150] c'est que si on a 14

[00:33:15.150 - 00:33:16.150] fichiers csv

[00:33:16.150 - 00:33:17.150] ça va être compliqué

[00:33:17.150 - 00:33:18.150] donc là

[00:33:18.150 - 00:33:19.150] ce qu'on va lui dire

[00:33:19.150 - 00:33:20.570] tout simplement

[00:33:20.570 - 00:33:26.950] un seul csv

[00:33:26.950 - 00:33:28.910] exporté

[00:33:28.910 - 00:33:30.140] directement

[00:33:30.140 - 00:33:31.140] donc les deux

[00:33:31.140 - 00:33:41.060] occurrences

[00:33:41.060 - 00:33:42.060] dans html

[00:33:42.060 - 00:33:43.060] ont été mises à jour

[00:33:43.060 - 00:33:44.060] donc là on peut voir

[00:33:44.060 - 00:33:45.060] qu'il a fini aussi

[00:33:45.060 - 00:33:46.060] l'autre tâche

[00:33:46.060 - 00:33:47.800] qu'on lui a demandé

[00:33:47.800 - 00:33:49.250] la tâche

[00:33:49.250 - 00:33:52.420] j'ai l'adresse email

[00:33:52.420 - 00:33:55.890] mon dossier

[00:33:55.890 - 00:33:57.180] Claude

[00:33:57.180 - 00:33:58.180] clique sur index

[00:33:58.180 - 00:33:59.180] .html

[00:33:59.180 - 00:34:09.330] email

[00:34:09.330 - 00:34:25.340] donc là il a bien

[00:34:25.340 - 00:34:26.340] mis à jour

[00:34:26.340 - 00:34:27.340] baptiste

[00:34:27.340 - 00:34:28.340] arrobasevisionia.io

[00:34:28.340 - 00:34:29.340] vous pouvez vraiment

[00:34:29.340 - 00:34:30.340] modifier tout ce que

[00:34:30.340 - 00:34:31.340] vous souhaitez

[00:34:31.340 - 00:34:33.230] on peut changer la couleur

[00:34:33.230 - 00:34:34.230] comme on l'a vu tout à l'heure

[00:34:34.230 - 00:34:35.230] on peut changer

[00:34:35.230 - 00:34:37.230] la taille des boutons

[00:34:37.230 - 00:34:39.230] on peut changer le texte

[00:34:39.230 - 00:34:40.900] on peut lui demander

[00:34:40.900 - 00:34:41.900] de créer une nouvelle page

[00:34:41.900 - 00:34:42.900] donc là

[00:34:42.900 - 00:34:43.900] ça va être vraiment

[00:34:43.900 - 00:34:44.900] un site basique

[00:34:44.900 - 00:34:45.900] pas très poussé

[00:34:45.900 - 00:34:47.640] on n'a pas utilisé

[00:34:47.640 - 00:34:48.640] un bon système de prompting

[00:34:48.640 - 00:34:49.640] ça on verra un petit peu plus

[00:34:49.640 - 00:34:50.640] par la suite

[00:34:50.640 - 00:34:52.860] et puis

[00:34:52.860 - 00:34:55.260] on peut voir déjà

[00:34:55.260 - 00:34:56.260] un petit peu

[00:34:56.260 - 00:34:57.260] juste en 30 minutes

[00:34:57.260 - 00:34:58.260] la puissance de cloud code

[00:34:58.260 - 00:34:59.260] sur ce que vous pouvez faire

[00:34:59.260 - 00:35:00.260] assez rapidement

[00:35:00.260 - 00:35:03.540] on peut vous apporter

[00:35:03.540 - 00:35:04.540] de la plus-value

[00:35:04.540 - 00:35:07.620] donc CSV

[00:35:07.620 - 00:35:10.520] déjà on a

[00:35:10.520 - 00:35:11.520] un site web

[00:35:11.520 - 00:35:12.810] plutôt qualitatif

[00:35:12.810 - 00:35:14.810] ça reste quand même simple

[00:35:14.810 - 00:35:16.900] avec des liens cliquables

[00:35:16.900 - 00:35:17.900] on a une partie

[00:35:17.900 - 00:35:18.900] étude de marché

[00:35:18.900 - 00:35:20.900] qui a été terminée

[00:35:20.900 - 00:35:21.960] on pourrait très bien

[00:35:21.960 - 00:35:22.960] ensuite

[00:35:22.960 - 00:35:24.730] créer une nouvelle session

[00:35:24.730 - 00:35:26.620] et lui dire

[00:35:26.620 - 00:35:30.660] travailler maintenant

[00:35:30.660 - 00:35:31.660] sur

[00:35:31.660 - 00:35:33.700] une stratégie de prospection

[00:35:33.700 - 00:35:34.820] ou une stratégie

[00:35:34.820 - 00:35:38.740] de récupération

[00:35:38.740 - 00:35:39.740] de leads

[00:35:39.740 - 00:35:40.740] automatique

[00:35:40.740 - 00:35:43.700] on va pas aller trop

[00:35:43.700 - 00:35:45.080] dans le complexe

[00:35:45.080 - 00:35:46.080] sur cette première séance

[00:35:46.080 - 00:35:47.080] là

[00:35:47.080 - 00:35:48.080] j'ai pas envie

[00:35:48.080 - 00:35:49.080] de vous perdre

[00:35:49.080 - 00:35:50.080] mais le but

[00:35:50.080 - 00:35:52.040] c'est vraiment voilà

[00:35:52.040 - 00:35:53.040] de s'entraîner un petit peu

[00:35:53.040 - 00:35:54.040] aussi de votre côté

[00:35:54.040 - 00:35:55.040] donc créer votre propre

[00:35:55.040 - 00:35:56.040] site internet

[00:35:56.040 - 00:35:57.040] même si vous allez pas

[00:35:57.040 - 00:35:58.040] forcément l'utiliser

[00:35:58.040 - 00:36:00.040] aussi créer votre étude

[00:36:00.040 - 00:36:01.040] de marché

[00:36:01.040 - 00:36:02.040] de faire des petits tests

[00:36:02.040 - 00:36:03.040] si vous avez une idée

[00:36:03.040 - 00:36:04.070] en tête

[00:36:04.070 - 00:36:05.070] que ce soit

[00:36:05.070 - 00:36:06.070] par exemple

[00:36:06.070 - 00:36:07.070] un petit dashboard

[00:36:07.070 - 00:36:09.100] pour suivre vos leads

[00:36:09.100 - 00:36:10.100] vous pouvez le faire

[00:36:10.100 - 00:36:11.100] vraiment prendre du temps

[00:36:11.100 - 00:36:12.100] à comprendre

[00:36:12.100 - 00:36:15.800] cloud code

[00:36:15.800 - 00:36:16.800] comprendre comment l'utiliser

[00:36:16.800 - 00:36:18.800] à tester aussi

[00:36:18.800 - 00:36:19.800] les commandes

[00:36:19.800 - 00:36:21.220] ça sera que bénéfique

[00:36:21.220 - 00:36:22.220] par la suite

[00:36:22.220 - 00:36:23.660] quand on va rentrer

[00:36:23.660 - 00:36:25.300] plus dans le dur

[00:36:25.300 - 00:36:26.300] pour vous parler un petit peu

[00:36:26.300 - 00:36:27.300] commandes

[00:36:27.300 - 00:36:28.300] c'est pour ça que moi

[00:36:28.300 - 00:36:30.230] je préfère du codex

[00:36:30.230 - 00:36:31.230] c'est qu'on a des fonctionnalités

[00:36:31.230 - 00:36:33.230] qui sont extrêmement puissantes

[00:36:33.230 - 00:36:34.230] quand je vous dis puissantes

[00:36:34.230 - 00:36:35.230] c'est que derrière

[00:36:35.230 - 00:36:36.680] vous allez pouvoir

[00:36:36.680 - 00:36:37.680] faire des choses

[00:36:37.680 - 00:36:40.060] qui sont stratosphériques

[00:36:40.060 - 00:36:44.360] business du long terme

[00:36:44.360 - 00:36:45.620] par exemple

[00:36:45.620 - 00:36:47.620] la commande chrome

[00:36:47.620 - 00:36:48.620] qui est en bêta actuellement

[00:36:48.620 - 00:36:49.620] qui vient de sortir

[00:36:49.620 - 00:36:50.650] vous allez avoir

[00:36:50.650 - 00:36:51.650] cloud code

[00:36:51.650 - 00:36:52.650] qui va contrôler

[00:36:52.650 - 00:36:53.650] votre ordinateur

[00:36:53.650 - 00:36:56.860] donc que dire de faire

[00:36:56.860 - 00:36:58.140] vraiment tout

[00:36:58.140 - 00:36:59.340] ça c'est assez intéressant

[00:36:59.340 - 00:37:00.340] on a aussi

[00:37:00.340 - 00:37:01.340] la partie

[00:37:01.340 - 00:37:02.820] slash

[00:37:02.820 - 00:37:03.820] remote control

[00:37:03.820 - 00:37:07.470] donc si vous avez un lien ici

[00:37:07.470 - 00:37:08.470] vous allez vous l'envoyer

[00:37:08.470 - 00:37:09.470] directement

[00:37:09.470 - 00:37:11.720] au téléphone

[00:37:11.720 - 00:37:12.720] et vous allez ouvrir

[00:37:12.720 - 00:37:14.740] ce lien

[00:37:14.740 - 00:37:16.740] en question

[00:37:16.740 - 00:37:17.740] sur votre téléphone

[00:37:17.740 - 00:37:18.740] et vous allez écrire

[00:37:18.740 - 00:37:19.740] un message

[00:37:19.740 - 00:37:21.630] et pouvoir travailler

[00:37:21.630 - 00:37:22.630] sur votre téléphone

[00:37:22.630 - 00:37:23.630] directement

[00:37:24.400 - 00:37:25.400] en full remote

[00:37:25.400 - 00:37:32.260] ça peut vous faire gagner

[00:37:32.260 - 00:37:33.260] beaucoup de temps

[00:37:33.260 - 00:37:34.260] si vous êtes en déplacement

[00:37:34.260 - 00:37:36.350] ça peut être intéressant

[00:37:36.350 - 00:37:37.350] on a aussi

[00:37:37.350 - 00:37:38.350] une commande

[00:37:38.350 - 00:37:39.350] qu'on va beaucoup utiliser

[00:37:39.350 - 00:37:40.350] c'est la partie MCP

[00:37:40.350 - 00:37:42.350] ou derrière

[00:37:42.350 - 00:37:44.610] faire des tests utilisateurs

[00:37:44.610 - 00:37:47.180] c'est incroyable

[00:37:47.180 - 00:37:48.180] cette commande aussi

[00:37:48.180 - 00:37:49.180] vient de sortir

[00:37:49.180 - 00:37:50.180] il n'y a pas si longtemps

[00:37:50.180 - 00:37:52.540] pour vous donner un ordre d'idée

[00:37:52.540 - 00:37:53.540] il y a 3-4 mois

[00:37:55.110 - 00:37:57.110] je faisais mes tests utilisateurs

[00:37:57.110 - 00:37:58.110] moi-même

[00:37:58.110 - 00:37:59.110] donc je perdais beaucoup de temps

[00:37:59.110 - 00:38:00.110] dans le sens où

[00:38:00.110 - 00:38:01.110] si je faisais un chatbot

[00:38:01.110 - 00:38:03.110] SAV pour un client

[00:38:03.110 - 00:38:04.110] je vais moi-même

[00:38:04.110 - 00:38:05.110] créer des conversations

[00:38:05.110 - 00:38:06.400] du coup

[00:38:06.400 - 00:38:07.400] pour une conversation

[00:38:07.400 - 00:38:10.030] pour un IA

[00:38:10.030 - 00:38:12.950] complète 5 minutes

[00:38:12.950 - 00:38:14.400] là

[00:38:14.400 - 00:38:15.400] avec cette commande là

[00:38:15.400 - 00:38:16.400] je vais pouvoir

[00:38:16.400 - 00:38:17.400] lui demander

[00:38:17.400 - 00:38:18.400] de contrôler mon ordinateur

[00:38:18.400 - 00:38:19.400] de me créer

[00:38:19.400 - 00:38:20.400] à peu près

[00:38:20.400 - 00:38:22.400] 20 ou 30 pages

[00:38:22.400 - 00:38:23.530] Chrome

[00:38:23.530 - 00:38:24.530] pour faire des tests

[00:38:24.530 - 00:38:27.220] faire ces tests là

[00:38:27.220 - 00:38:28.220] et du coup

[00:38:28.220 - 00:38:29.320] à la fin

[00:38:29.320 - 00:38:30.320] on va lui demander

[00:38:30.320 - 00:38:31.540] de créer un rapport

[00:38:31.540 - 00:38:32.540] on va voir les résultats

[00:38:32.540 - 00:38:33.580] et on va lui demander

[00:38:33.580 - 00:38:34.580] d'ajuster du coup

[00:38:34.580 - 00:38:37.400] et ça

[00:38:37.400 - 00:38:38.400] c'est un gamme temps

[00:38:38.400 - 00:38:39.400] assez incroyable

[00:38:39.400 - 00:38:40.940] encore une fois

[00:38:40.940 - 00:38:41.940] mon objectif personnel

[00:38:41.940 - 00:38:42.940] tout au long

[00:38:42.940 - 00:38:43.940] de cette formation

[00:38:43.940 - 00:38:45.940] c'est d'une part

[00:38:45.940 - 00:38:46.940] vous donner accès

[00:38:46.940 - 00:38:48.390] à des workflows

[00:38:48.390 - 00:38:49.740] très intéressants

[00:38:49.740 - 00:38:50.740] pour la revendre

[00:38:50.740 - 00:38:51.740] par exemple

[00:38:51.740 - 00:38:52.740] des blogs automatiques

[00:38:52.740 - 00:38:54.190] pour facturer

[00:38:54.190 - 00:38:55.190] à 3500 euros

[00:38:55.190 - 00:38:56.320] peu importe

[00:38:56.320 - 00:38:57.320] ça dépend

[00:38:57.320 - 00:38:58.320] le client

[00:38:58.320 - 00:38:59.320] que vous avez

[00:38:59.320 - 00:39:00.320] mais aussi

[00:39:00.320 - 00:39:01.320] avoir

[00:39:01.320 - 00:39:02.320] à la fin

[00:39:02.320 - 00:39:03.320] une compréhension globale

[00:39:03.320 - 00:39:04.320] de tous ces outils là

[00:39:04.320 - 00:39:05.320] qui sont en train

[00:39:05.320 - 00:39:06.320] de révolutionner le monde

[00:39:06.320 - 00:39:07.580] donc vous allez pouvoir

[00:39:07.580 - 00:39:08.580] très bien vous adapter

[00:39:08.580 - 00:39:09.580] aux demandes clients

[00:39:09.580 - 00:39:10.580] c'est ça

[00:39:10.580 - 00:39:11.580] qui est le plus important

[00:39:11.580 - 00:39:17.890] dans le marché

[00:39:17.890 - 00:39:18.890] par exemple

[00:39:18.890 - 00:39:24.180] B2P d'entreprise

[00:39:24.180 - 00:39:25.180] et bien vous allez pouvoir

[00:39:25.180 - 00:39:26.180] avoir aussi des solutions

[00:39:26.180 - 00:39:27.180] qui vous sont demandées

[00:39:27.180 - 00:39:29.180] sur mesure

[00:39:29.180 - 00:39:30.180] et c'est à vous

[00:39:30.180 - 00:39:31.180] après

[00:39:31.180 - 00:39:32.180] de mettre ça en place

[00:39:32.180 - 00:39:33.300] donc

[00:39:33.300 - 00:39:34.300] à la fin de la formation

[00:39:34.300 - 00:39:35.300] si vous me suivez bien tout

[00:39:35.300 - 00:39:36.300] vous allez avoir les capacités

[00:39:36.300 - 00:39:37.300] ça j'ai pas de doute

[00:39:37.300 - 00:39:38.300] et puis

[00:39:38.300 - 00:39:39.750] faut pas oublier

[00:39:39.750 - 00:39:41.390] que voilà

[00:39:41.390 - 00:39:42.390] je suis disponible sur Slack

[00:39:42.390 - 00:39:43.740] vous pouvez me des demandes

[00:39:43.740 - 00:39:44.740] des messages

[00:39:44.740 - 00:39:45.740] pour que derrière

[00:39:45.740 - 00:39:46.740] si vous vous bloquez

[00:39:46.740 - 00:39:48.740] je puisse vous aider

[00:39:48.740 - 00:39:49.740] il n'y a pas de problème

[00:39:49.740 - 00:39:53.080] donc là on voit

[00:39:53.080 - 00:39:54.690] qu'il est travaillé

[00:39:54.690 - 00:39:55.780] ça fait quand même assez longtemps

[00:39:55.780 - 00:39:58.380] donc là il est en train de vérifier

[00:39:58.380 - 00:40:03.130] il est terminé

[00:40:03.130 - 00:40:06.610] on voit qu'il a 387 lignes

[00:40:06.610 - 00:40:09.700] il y a 16 sections dans le fichier

[00:40:09.700 - 00:40:10.860] donc c'est top

[00:40:10.860 - 00:40:11.860] l'étude de marché

[00:40:11.860 - 00:40:12.860] quand même assez détaillée

[00:40:12.860 - 00:40:15.300] maintenant on va aller sur

[00:40:15.300 - 00:40:38.220] le vierge

[00:40:38.220 - 00:40:41.020] portée

[00:40:41.020 - 00:40:46.980] le marché

[00:40:46.980 - 00:41:02.890] est assez longue

[00:41:02.890 - 00:41:03.890] assez longue

[00:41:03.890 - 00:41:05.460] pardon

[00:41:05.460 - 00:41:08.190] pratiquement

[00:41:08.190 - 00:41:10.440] illisible

[00:41:10.440 - 00:41:11.440] on voit qu'il y a le TGM moyen

[00:41:11.440 - 00:41:12.440] il a fait des recherches sur internet

[00:41:12.440 - 00:41:13.440] c'est top

[00:41:13.440 - 00:41:14.440] on pourrait lui demander

[00:41:14.440 - 00:41:15.440] de rajouter les sources

[00:41:15.440 - 00:41:19.000] mais les sources

[00:41:19.000 - 00:41:20.000] donc c'est top

[00:41:20.000 - 00:41:23.050] pour l'eau à lire

[00:41:23.050 - 00:41:24.270] donc nous on se demandait

[00:41:24.270 - 00:41:27.670] faire

[00:41:27.670 - 00:41:29.410] améliore

[00:41:29.410 - 00:41:47.780] un CSV

[00:41:47.780 - 00:41:49.100] on va travailler

[00:41:49.100 - 00:41:50.100] un fichier Excel directement

[00:41:50.100 - 00:41:52.700] puisse avoir quand même

[00:41:52.700 - 00:41:53.700] une étude de marché

[00:41:53.700 - 00:41:58.510] l'étude de marché

[00:41:58.510 - 00:42:02.490] on peut plus

[00:42:02.490 - 00:42:08.060] le travail

[00:42:08.060 - 00:42:09.060] d'internet

[00:42:09.060 - 00:42:10.060] là l'objectif c'est vraiment

[00:42:10.060 - 00:42:11.060] de vous montrer

[00:42:11.060 - 00:42:12.060] qu'on peut travailler

[00:42:12.060 - 00:42:14.770] sur le même projet

[00:42:14.770 - 00:42:15.770] mais sur une problématique

[00:42:15.770 - 00:42:16.770] qui est différente

[00:42:16.770 - 00:42:18.770] pour gagner du temps

[00:42:18.770 - 00:42:19.770] si derrière

[00:42:19.770 - 00:42:20.770] j'aurais attendu

[00:42:20.770 - 00:42:21.960] de finir mon site internet

[00:42:21.960 - 00:42:23.960] j'aurais perdu du temps

[00:42:23.960 - 00:42:24.960] le but c'est pas ça

[00:42:24.960 - 00:42:25.960] en fait le marché

[00:42:25.960 - 00:42:26.960] est tellement grand

[00:42:26.960 - 00:42:33.700] il y a plusieurs contrats

[00:42:33.700 - 00:42:38.060] le but c'est

[00:42:38.060 - 00:42:41.620] de ne pas la qualité

[00:42:41.620 - 00:42:42.620] l'organisation

[00:42:42.620 - 00:42:43.620] là

[00:42:43.620 - 00:42:44.620] sur un projet

[00:42:44.620 - 00:42:46.220] j'ai deux terminal

[00:42:46.220 - 00:42:49.060] des terminal différents

[00:42:49.060 - 00:42:50.380] par projet

[00:42:50.380 - 00:42:51.500] mais

[00:42:51.500 - 00:42:52.500] si j'avais

[00:42:52.500 - 00:42:54.850] un client

[00:42:54.850 - 00:42:55.850] par exemple

[00:42:55.850 - 00:43:02.030] qui demande une automatisation

[00:43:02.030 - 00:43:03.030] SAV

[00:43:03.030 - 00:43:05.020] donc ce que j'aurais fait

[00:43:05.020 - 00:43:06.020] c'est que j'aurais ouvert

[00:43:06.020 - 00:43:07.020] un terminal

[00:43:07.020 - 00:43:08.020] juste ici

[00:43:08.020 - 00:43:14.110] directement

[00:43:14.110 - 00:43:16.260] du coup

[00:43:16.260 - 00:43:20.820] au dossier client 1

[00:43:20.820 - 00:43:21.820] je leur ai dit

[00:43:21.820 - 00:43:25.310] travail

[00:43:25.310 - 00:43:26.310] travail sur

[00:43:26.310 - 00:43:33.230] une base de données

[00:43:33.230 - 00:43:36.640] une base de données

[00:43:36.640 - 00:43:37.640] Supabase

[00:43:37.640 - 00:43:40.210] voilà

[00:43:40.210 - 00:43:41.210] je leur ai donné une première mission

[00:43:41.210 - 00:43:42.210] pour aller plus vite

[00:43:42.210 - 00:43:44.070] ensuite

[00:43:44.070 - 00:43:45.070] j'aurais ouvert

[00:43:45.070 - 00:43:46.550] le terminal

[00:43:46.550 - 00:43:58.730] j'aurais très bien pu lui dire

[00:43:58.730 - 00:43:59.730] en HTML

[00:43:59.730 - 00:44:04.440] et après voilà

[00:44:04.440 - 00:44:05.440] au fur et à mesure

[00:44:05.440 - 00:44:06.440] avoir plusieurs onglets

[00:44:06.440 - 00:44:08.440] qui travaillent en même temps

[00:44:08.440 - 00:44:09.890] pour ne pas perdre du temps

[00:44:09.890 - 00:44:10.890] donc là hop

[00:44:10.890 - 00:44:11.890] premier projet

[00:44:11.890 - 00:44:12.890] deuxième projet

[00:44:12.890 - 00:44:13.890] etc

[00:44:13.890 - 00:44:14.890] jusqu'à temps que

[00:44:14.890 - 00:44:15.890] malheureusement

[00:44:15.890 - 00:44:18.810] on va avoir d'autres onglets

[00:44:18.810 - 00:44:19.810] parce que sinon

[00:44:19.810 - 00:44:20.810] vous allez vite vous perdre

[00:44:20.810 - 00:44:21.810] mais c'est vraiment

[00:44:21.810 - 00:44:22.810] essayer d'optimiser

[00:44:22.810 - 00:44:23.810] un maximum son temps

[00:44:23.810 - 00:44:24.840] pour

[00:44:24.840 - 00:44:26.220] simplement

[00:44:26.220 - 00:44:27.220] délivrer le plus vite

[00:44:27.220 - 00:44:28.540] et passer

[00:44:28.540 - 00:44:29.670] rapidement

[00:44:29.670 - 00:44:30.670] autre chose

[00:44:30.670 - 00:44:31.860] donc ça on le verra aussi

[00:44:31.860 - 00:44:32.860] par la suite

[00:44:32.860 - 00:44:40.170] du fichier Excel

[00:44:40.170 - 00:44:49.170] vraiment

[00:44:49.170 - 00:44:50.170] amusez-vous

[00:44:50.170 - 00:44:52.170] à créer n'importe quoi

[00:44:52.170 - 00:44:54.520] prenez du temps

[00:44:54.520 - 00:44:55.520] ça va être important

[00:44:55.520 - 00:44:56.520] ne vous précipitez pas

[00:44:56.520 - 00:44:57.520] à passer directement

[00:44:57.520 - 00:44:59.520] sur la séance 2

[00:44:59.520 - 00:45:00.520] faites vous plaisir

[00:45:00.520 - 00:45:01.520] découvrez l'outil

[00:45:01.520 - 00:45:02.520] si vous ne l'avez jamais

[00:45:02.520 - 00:45:03.520] découvert

[00:45:03.520 - 00:45:07.160] créez tout et n'importe quoi

[00:45:07.160 - 00:45:09.120] comprenez la puissance

[00:45:09.120 - 00:45:11.250] qui peut vous apporter

[00:45:11.250 - 00:45:13.250] faites des petits jeux

[00:45:13.250 - 00:45:14.340] demandez de créer

[00:45:14.340 - 00:45:18.140] snake.io

[00:45:18.140 - 00:45:19.870] vraiment

[00:45:19.870 - 00:45:20.870] prenez votre temps

[00:45:20.870 - 00:45:21.870] ça va être très important

[00:45:21.870 - 00:45:23.870] si vous n'avez jamais baigné

[00:45:23.870 - 00:45:26.030] si vous n'avez jamais travaillé

[00:45:26.030 - 00:45:27.030] avec Cloud Code

[00:45:27.030 - 00:45:28.160] pour que par la suite

[00:45:28.160 - 00:45:30.160] tout au long de la formation

[00:45:30.160 - 00:45:31.160] ça paraît bien plus simple

[00:45:31.160 - 00:45:32.160] que ce soit Codex

[00:45:32.160 - 00:45:33.160] que ce soit Cowork

[00:45:33.160 - 00:45:34.450] que ce soit N8N

[00:45:34.450 - 00:45:36.450] parce que les projets

[00:45:36.450 - 00:45:38.900] vont être de plus en plus durs

[00:45:38.900 - 00:45:39.900] et le but

[00:45:39.900 - 00:45:40.900] c'est pas que vous vous retrouviez

[00:45:40.900 - 00:45:41.900] bloqué

[00:45:41.900 - 00:45:42.900] parce que vous n'avez pas compris

[00:45:42.900 - 00:45:44.120] quelque chose

[00:45:44.120 - 00:45:45.120] vraiment

[00:45:45.120 - 00:45:46.120] testez tout

[00:45:46.120 - 00:45:47.120] tout

[00:45:47.120 - 00:45:48.180] tout

[00:45:48.180 - 00:45:49.180] créez un bel projet

[00:45:49.180 - 00:45:50.540] encore une fois

[00:45:50.540 - 00:46:03.190] je vais vous donner un petit conseil aussi

[00:46:03.190 - 00:46:05.480] n'ayez pas le syndrome

[00:46:05.480 - 00:46:06.480] de l'imposteur

[00:46:06.480 - 00:46:07.480] je sais que c'est pas simple

[00:46:07.480 - 00:46:09.150] souvent quand on se lance

[00:46:09.150 - 00:46:11.150] dans un nouveau domaine

[00:46:11.150 - 00:46:12.150] on peut se dire

[00:46:12.150 - 00:46:13.150] ouais mais j'ai pas les compétences

[00:46:13.150 - 00:46:14.150] aptes

[00:46:14.150 - 00:46:15.150] pour travailler

[00:46:15.150 - 00:46:16.150] à l'intérieur

[00:46:16.150 - 00:46:18.150] de ce domaine là

[00:46:18.150 - 00:46:19.150] j'étais comme vous au départ

[00:46:19.150 - 00:46:20.310] et au fur et à mesure

[00:46:20.310 - 00:46:21.310] quand vous allez avoir

[00:46:21.310 - 00:46:23.140] vous promets que vos clients

[00:46:23.140 - 00:46:24.140] vont être satisfait

[00:46:24.140 - 00:46:25.140] eh bien

[00:46:25.140 - 00:46:26.780] là

[00:46:26.780 - 00:46:27.980] va disparaître

[00:46:27.980 - 00:46:28.980] croyez vraiment en vous

[00:46:28.980 - 00:46:30.520] je suis certain

[00:46:30.520 - 00:46:31.520] que derrière

[00:46:31.520 - 00:46:32.810] si vous suivez bien

[00:46:32.810 - 00:46:33.810] la formation

[00:46:33.810 - 00:46:34.810] vous allez avoir

[00:46:34.810 - 00:46:35.810] toutes les compétences adéquates

[00:46:35.810 - 00:46:37.970] pour proposer quelque chose

[00:46:37.970 - 00:46:40.320] de qualitatif

[00:46:40.320 - 00:46:41.320] à n'importe quel client

[00:46:41.320 - 00:46:43.380] c'est juste qu'il faut bien suivre

[00:46:43.380 - 00:46:44.380] beaucoup travailler

[00:46:44.380 - 00:46:47.180] et prendre son temps aussi

[00:46:47.180 - 00:46:49.180] c'est pas grave si

[00:46:49.180 - 00:46:51.180] derrière vous bloquez sur une module

[00:46:51.180 - 00:46:53.310] encore une fois vous me contactez

[00:46:53.310 - 00:46:55.310] et puis derrière j'essaierai

[00:46:55.310 - 00:47:00.540] sur la partie en question

[00:47:00.540 - 00:47:02.770] donc là comme on peut voir

[00:47:02.770 - 00:47:06.220] il a terminé notre étude de marché

[00:47:06.220 - 00:47:08.220] on va pouvoir l'importer

[00:47:08.220 - 00:47:09.220] pour voir la différence

[00:47:09.220 - 00:47:15.220] entre la v1 et la v2

[00:47:15.220 - 00:47:16.950] il y a le cheat

[00:47:16.950 - 00:47:20.610] importer

[00:47:20.610 - 00:47:22.280] tout à l'heure

[00:47:22.280 - 00:47:23.280] étude de marché

[00:47:23.280 - 00:47:24.280] on récupère

[00:47:24.280 - 00:47:34.080] le feuille de calcul

[00:47:34.080 - 00:47:38.470] et là on peut voir

[00:47:38.470 - 00:47:39.470] que c'est bien différent

[00:47:39.470 - 00:47:41.470] la qualité est assez

[00:47:41.470 - 00:47:44.140] plutôt pas mal

[00:47:44.140 - 00:47:46.740] petite synthèse

[00:47:46.740 - 00:47:48.470] on a une partie globale

[00:47:48.470 - 00:47:54.980] en France

[00:47:54.980 - 00:47:59.050] c'est

[00:47:59.050 - 00:48:02.200] 2,6 milliards

[00:48:02.200 - 00:48:03.580] on peut voir qu'il y a une projection

[00:48:03.580 - 00:48:04.580] du coût de 2026

[00:48:04.580 - 00:48:05.780] nous on en 2026

[00:48:05.780 - 00:48:06.870] 4,6 milliards

[00:48:06.870 - 00:48:07.900] donc ça fait

[00:48:07.900 - 00:48:10.260] une belle hausse

[00:48:10.260 - 00:48:12.640] on a les sources juste ici

[00:48:12.640 - 00:48:14.640] les segments technologiques

[00:48:14.640 - 00:48:15.640] et taille croissante

[00:48:15.640 - 00:48:17.640] donc là vraiment

[00:48:17.640 - 00:48:18.640] on a de quoi faire

[00:48:18.640 - 00:48:20.470] pour bien comprendre

[00:48:20.470 - 00:48:22.470] le marché en question

[00:48:22.470 - 00:48:23.470] donc ça a pas pris beaucoup de temps

[00:48:23.470 - 00:48:24.470] comme vous voyez

[00:48:24.470 - 00:48:26.700] c'est ça qui est vraiment intéressant

[00:48:26.700 - 00:48:28.780] avoir un système

[00:48:28.780 - 00:48:29.780] qui est capable

[00:48:29.780 - 00:48:30.780] de nous proposer quelque chose

[00:48:30.780 - 00:48:31.780] de qualitatif

[00:48:31.780 - 00:48:32.780] en peu de temps

[00:48:32.780 - 00:48:35.200] c'est assez incroyable

[00:48:35.200 - 00:48:38.700] et ça peut être très important

[00:48:38.700 - 00:48:39.700] très intéressant

[00:48:39.700 - 00:48:41.950] sur tous les projets

[00:48:41.950 - 00:48:42.950] qu'on va voir ensemble

[00:48:42.950 - 00:48:43.950] et sur les projets aussi que vous avez

[00:48:43.950 - 00:48:46.300] vous allez délivrer

[00:48:46.300 - 00:48:47.300] liste détaillé par secteur

[00:48:47.300 - 00:48:49.810] donc la finance assurance

[00:48:49.810 - 00:48:50.810] maturité

[00:48:50.810 - 00:48:51.810] il y a 8 sur 10

[00:48:51.810 - 00:48:53.030] collectivité locale

[00:48:53.030 - 00:48:54.800] voilà

[00:48:54.800 - 00:48:59.060] ça peut être tout ça

[00:48:59.060 - 00:49:00.060] par la suite

[00:49:00.060 - 00:49:05.580] quand vous avez créé votre propre

[00:49:05.580 - 00:49:06.580] de marché

[00:49:06.580 - 00:49:07.580] et comprendre sur quoi

[00:49:07.580 - 00:49:08.580] vous voulez vous positionner

[00:49:08.580 - 00:49:12.430] on peut faire

[00:49:12.430 - 00:49:13.430] et à quoi ça sert

[00:49:13.430 - 00:49:14.430] d'itérer constamment

[00:49:14.430 - 00:49:15.430] d'autres demandes

[00:49:15.430 - 00:49:16.430] pour avoir quelque chose

[00:49:16.430 - 00:49:18.590] qui est de plus en plus

[00:49:18.590 - 00:49:26.790] pour revenir du coup

[00:49:26.790 - 00:49:27.790] un petit peu

[00:49:27.790 - 00:49:28.790] sur le support technique

[00:49:28.790 - 00:49:30.690] on peut voir

[00:49:30.690 - 00:49:31.690] qu'on a aussi

[00:49:31.690 - 00:49:32.690] des commandes

[00:49:32.690 - 00:49:33.690] essentiel

[00:49:33.690 - 00:49:34.690] donc il y en a pas 50

[00:49:34.690 - 00:49:36.070] mais voilà

[00:49:36.070 - 00:49:39.290] que tu vas utiliser du coup

[00:49:39.290 - 00:49:40.290] tous les jours

[00:49:40.290 - 00:49:41.290] la partie help

[00:49:41.290 - 00:49:42.290] clear

[00:49:42.290 - 00:49:43.290] cost

[00:49:43.290 - 00:49:46.980] compact

[00:49:46.980 - 00:49:47.980] compressé quand la conversation

[00:49:47.980 - 00:49:48.980] est trop longue

[00:49:48.980 - 00:49:49.980] si là je retourne ici

[00:49:49.980 - 00:50:04.460] je fais générer un cloud md

[00:50:04.460 - 00:50:05.460] ça on l'a vu

[00:50:05.460 - 00:50:08.860] on peut voir qu'il peut gérer les fichiers

[00:50:08.860 - 00:50:10.960] donc tu parles français

[00:50:10.960 - 00:50:11.960] lire le fichier index.html

[00:50:11.960 - 00:50:12.960] modifier le titre

[00:50:12.960 - 00:50:13.960] il va le faire

[00:50:13.960 - 00:50:15.960] on peut lancer des commandes du coup

[00:50:15.960 - 00:50:17.060] qu'on a vu

[00:50:17.060 - 00:50:19.780] on peut voir aussi

[00:50:19.780 - 00:50:20.780] qu'il y a des limites

[00:50:20.780 - 00:50:21.780] parfois il peut se tromper

[00:50:21.780 - 00:50:22.780] c'est pour ça qu'il faut bien

[00:50:22.780 - 00:50:23.780] analyser

[00:50:23.780 - 00:50:26.380] fait

[00:50:26.380 - 00:50:28.860] qu'il voit aussi

[00:50:28.860 - 00:50:33.730] la meilleure astuce

[00:50:33.730 - 00:50:34.730] c'est

[00:50:34.730 - 00:50:36.940] des petites étapes

[00:50:36.940 - 00:50:37.940] pour avoir vraiment

[00:50:37.940 - 00:50:39.940] un résultat qui est parfait

[00:50:39.940 - 00:50:41.810] donc là je vous ai mis

[00:50:41.810 - 00:50:42.810] une petite liste d'exemples

[00:50:42.810 - 00:50:51.780] que vous pouvez

[00:50:51.780 - 00:50:52.780] on se retrouve tout de suite

[00:50:52.780 - 00:50:53.780] pour l'étape 2 du coup

[00:50:53.780 - 00:50:56.260] qui va parler de codex

[00:50:56.260 - 00:50:58.260] qui est un outil similaire

[00:50:58.260 - 00:50:59.540] du coup à code code

[00:50:59.540 - 00:51:00.540] et on va voir comment

[00:51:00.540 - 00:51:01.540] utiliser les deux

[00:51:01.540 - 00:51:03.540] pour gagner en efficacité

