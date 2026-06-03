from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "support-technique-seance-01.html"
INDEX_OUT = ROOT / "index.html"

DOCS = {
    "overview": "https://code.claude.com/docs/en/overview",
    "setup": "https://code.claude.com/docs/en/getting-started",
    "cli": "https://code.claude.com/docs/en/cli-usage",
    "memory": "https://code.claude.com/docs/en/memory",
    "settings": "https://code.claude.com/docs/en/settings",
    "security": "https://code.claude.com/docs/en/security",
    "workflows": "https://code.claude.com/docs/en/common-workflows",
    "troubleshooting": "https://code.claude.com/docs/en/troubleshooting",
    "ide": "https://code.claude.com/docs/en/ide-integrations",
    "mcp": "https://code.claude.com/docs/en/mcp",
    "github": "https://code.claude.com/docs/en/github-actions",
    "sdk": "https://code.claude.com/docs/en/agent-sdk/overview",
    "hooks": "https://code.claude.com/docs/en/hooks",
    "node": "https://nodejs.org/en/download",
    "npm": "https://docs.npmjs.com/",
    "plans": "https://support.claude.com/en/articles/11049762-choose-a-claude-plan",
    "pro": "https://support.claude.com/en/articles/8325606-what-is-the-pro-plan",
    "pro_max": "https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan",
    "first_day": "https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code",
}

SCREENS = [
    "01-overview-top.png",
    "02-overview-actions.png",
    "03-getting-started-top.png",
    "04-getting-started-install.png",
    "05-getting-started-windows.png",
    "06-cli-top.png",
    "07-cli-table.png",
    "08-memory-top.png",
    "09-memory-table.png",
    "10-settings-top.png",
    "11-settings-json.png",
    "12-security-top.png",
    "13-security-permissions.png",
    "14-common-workflows-top.png",
    "15-common-workflows-example.png",
    "16-troubleshooting-top.png",
    "17-troubleshooting-search.png",
    "18-ide-setup-top.png",
    "19-mcp-top.png",
    "20-github-actions-top.png",
    "21-sdk-top.png",
    "22-hooks-top.png",
]

INTERFACE_SCREENS = [
    "terminal-start.png",
    "install-node-npm.png",
    "install-claude-command.png",
    "first-prompt.png",
    "cli-help.png",
    "permissions-modes.png",
    "pricing-plans.png",
    "usage-limits.png",
    "desktop-code-tab.png",
    "desktop-terminal-pane.png",
    "memory-claude-md.png",
    "troubleshooting.png",
    "project-folder.png",
    "auth-login.png",
    "plan-mode.png",
    "diff-approval.png",
    "file-created.png",
    "git-status.png",
    "npm-test.png",
    "update-doctor.png",
    "desktop-files-preview.png",
    "desktop-permissions.png",
    "desktop-usage.png",
    "windows-terminal.png",
    "api-vs-subscription.png",
    "api-key-warning.png",
    "source-docs.png",
    "prompt-constraints.png",
    "checklist-test.png",
    "clear-compact.png",
    "error-copy.png",
    "delivery-summary.png",
]

INTERFACE_META = {
    "terminal-start.png": ("Terminal Claude Code", "Claude Code lancé dans le bon dossier de travail."),
    "install-node-npm.png": ("Terminal Node et npm", "Vérification des pré-requis avant l’installation."),
    "install-claude-command.png": ("Commande d’installation", "Installation de Claude Code avec npm."),
    "first-prompt.png": ("Premier prompt Claude Code", "Demande courte avec un résultat facile à vérifier."),
    "cli-help.png": ("Aide CLI Claude Code", "Repères utiles pour retrouver les commandes."),
    "permissions-modes.png": ("Modes de permission", "Choix du niveau de contrôle avant les actions."),
    "pricing-plans.png": ("Plans Claude", "Repère visuel pour Pro, Max 5x et Max 20x."),
    "usage-limits.png": ("Limites d’usage", "Comprendre pourquoi une session peut être ralentie ou bloquée."),
    "desktop-code-tab.png": ("Claude Code Desktop", "Vue pédagogique du Code tab dans Claude Desktop."),
    "desktop-terminal-pane.png": ("Terminal intégré Desktop", "Terminal et session Claude dans le même espace."),
    "memory-claude-md.png": ("Mémoire CLAUDE.md", "Règles de projet que Claude Code peut relire."),
    "troubleshooting.png": ("Diagnostic Claude Code", "Vérifier le chemin, Node, npm et la version de Claude Code."),
    "project-folder.png": ("Dossier projet", "Arborescence propre avant de lancer Claude Code."),
    "auth-login.png": ("Connexion Claude Code", "Connexion au compte Claude utilisé pour Pro ou Max."),
    "plan-mode.png": ("Plan mode", "Demander un plan avant de modifier les fichiers."),
    "diff-approval.png": ("Diff à valider", "Relire une modification avant de l’accepter."),
    "file-created.png": ("Fichiers créés", "Preuve concrète que la demande a produit un résultat."),
    "git-status.png": ("Git status", "Vérifier les fichiers modifiés avant publication."),
    "npm-test.png": ("Tests et build", "Lire le résultat d’une commande de vérification."),
    "update-doctor.png": ("Doctor et update", "Diagnostiquer avant de modifier l’installation."),
    "desktop-files-preview.png": ("Desktop fichiers et aperçu", "Voir les fichiers, la demande et l’aperçu dans Desktop."),
    "desktop-permissions.png": ("Permissions Desktop", "Accepter ou refuser une action en comprenant le geste."),
    "desktop-usage.png": ("Usage Desktop", "Suivre les limites du plan et les crédits disponibles."),
    "windows-terminal.png": ("Terminal Windows", "Identifier PowerShell, CMD, Git Bash ou WSL."),
    "api-vs-subscription.png": ("Abonnement ou API", "Différence entre usage personnel et usage automatisé."),
    "api-key-warning.png": ("Clé API privée", "Rappel visuel : une clé API ne se publie jamais."),
    "source-docs.png": ("Sources officielles", "Docs Claude Code, Help Center et Node.js."),
    "prompt-constraints.png": ("Prompt avec contraintes", "Contexte, sortie attendue et règles de travail."),
    "checklist-test.png": ("Checklist de test", "Points concrets avant de dire que c’est terminé."),
    "clear-compact.png": ("Commandes de session", "Nettoyer ou compacter une session longue."),
    "error-copy.png": ("Erreur exacte", "Copier le message d’erreur avant de demander de l’aide."),
    "delivery-summary.png": ("Résumé de livraison", "Finir avec fichiers, vérification et prochaine action."),
}

CHAPTERS = [
    (
        "Avant de lancer",
        "Tu prépares le terrain avant d’écrire la première commande.",
        "Théorie",
        "blue",
        [
            ("Tu pars d’un dossier propre", "Un dossier propre évite les erreurs dès le début. Claude Code travaille dans le dossier où tu le lances. Si ce dossier est mélangé avec d’autres projets, il peut lire ou modifier des éléments qui n’ont rien à faire là.", "Crée un dossier nommé `formation-s1-claude-code`. Mets-le sur le bureau pour le retrouver facilement.", "Le dossier est vide, visible, et tu sais l’ouvrir sans chercher."),
            ("Tu comprends le rôle de Claude Code", "Claude Code n’est pas seulement une fenêtre de discussion. C’est un assistant qui peut lire ton projet, créer des fichiers, lancer des commandes et corriger un résultat. C’est pour ça qu’il doit être utilisé avec méthode.", "Explique à voix haute la différence entre “répondre à une question” et “agir dans un dossier”.", "Tu sais pourquoi cet outil sert dans une formation orientée projet."),
            ("Tu gardes le contrôle", "L’élève ne doit jamais se dire que Claude Code décide à sa place. Tu choisis le résultat attendu. Claude Code propose, produit, corrige. Toi, tu relis et tu valides.", "Avant chaque exercice, écris une phrase : `À la fin, je veux obtenir...`", "Tu sais ce que tu vas vérifier avant de lancer l’outil."),
            ("Tu acceptes de commencer petit", "Le premier objectif n’est pas de livrer un gros site. Le premier objectif est de réussir une boucle simple : demander, obtenir, ouvrir, vérifier, corriger.", "Choisis un mini-test : une page HTML, un fichier README, ou une checklist.", "Tu as un exercice court, pas un projet flou."),
            ("Tu lis le support comme une marche guidée", "Ce support n’est pas une retranscription. C’est une méthode pour refaire la séance et comprendre quoi faire à chaque étape.", "Garde le support ouvert à côté de ton terminal.", "Tu peux suivre sans retourner dans la vidéo toutes les deux minutes."),
            ("Tu sais ce que tu vas apprendre", "À la fin, tu dois savoir installer Claude Code, le lancer dans un dossier, lui donner une demande claire et vérifier le résultat.", "Note ces quatre verbes : installer, lancer, demander, vérifier.", "Tu as une grille mentale simple pour toute la suite."),
        ],
    ),
    (
        "ChatGPT ou Claude Code",
        "Tu sais quand utiliser un chatbot et quand utiliser un agent dans ton dossier.",
        "Comparaison",
        "violet",
        [
            ("ChatGPT aide à réfléchir", "ChatGPT est pratique pour expliquer une idée, reformuler un texte ou préparer un plan. Mais il ne travaille pas directement dans ton dossier local.", "Utilise ChatGPT pour préparer une idée si tu en as besoin.", "Tu ne confonds pas réflexion et exécution."),
            ("Claude Code aide à produire", "Claude Code devient utile quand tu veux créer ou modifier de vrais fichiers. Il peut lire le contexte du projet et agir dedans.", "Demande une page simple à Claude Code dans ton dossier test.", "Tu vois un fichier apparaître dans le dossier."),
            ("Tu ne copies-colles pas tout à la main", "Avec un chatbot classique, tu récupères souvent du code puis tu dois créer les fichiers toi-même. Claude Code réduit ce travail manuel.", "Compare mentalement les étapes : copier, créer, coller, enregistrer, ouvrir.", "Tu comprends le gain de temps concret."),
            ("Tu dois plus vérifier", "Plus l’outil peut agir, plus ta vérification compte. Il faut regarder ce qui a été créé, pas seulement lire la réponse dans le terminal.", "Demande toujours un résumé des fichiers modifiés.", "Tu sais ce qui a changé."),
            ("Tu choisis selon la tâche", "Si tu veux juste comprendre une notion, un chatbot suffit. Si tu veux produire une page, un script, une arborescence ou un audit, Claude Code est plus adapté.", "Classe tes demandes en deux colonnes : réfléchir ou produire.", "Tu sais quel outil ouvrir."),
            ("Tu construis un réflexe professionnel", "Un professionnel ne lance pas l’outil au hasard. Il choisit l’outil selon le résultat attendu.", "Avant de lancer Claude Code, demande-toi : `Quel fichier doit exister à la fin ?`", "Ta demande devient plus claire."),
        ],
    ),
    (
        "Budget et accès",
        "Tu comprends la différence entre abonnement, quota et API.",
        "Théorie",
        "blue",
        [
            ("Quel plan choisir ?", "Question simple : est-ce que tu vas juste tester, ou est-ce que tu vas travailler plusieurs heures sur de vrais projets ? Le Help Center Claude indique Pro à 20 $/mois aux États-Unis, information vérifiée le 3 juin 2026. Le prix peut varier selon la région et les taxes.", "Compare ton besoin réel avant de payer : test, formation complète, ou projets clients. Avant achat, ouvre toujours la page officielle.", "Tu sais pourquoi Pro peut suffire au début, mais pas toujours pendant une grosse session."),
            ("Pourquoi Max 5x existe ?", "Le Help Center liste Max 5x à 100 $/mois. L’idée est d’avoir plus de capacité par session que Pro. Pour un élève qui suit toute la formation et travaille souvent, c’est le plan à regarder si les limites deviennent un blocage.", "Note dans quel cas tu bloques : une fois de temps en temps, ou souvent au milieu d’un projet.", "Tu ne changes pas de plan par peur, tu changes parce que ton usage le justifie."),
            ("Pourquoi Max 20x existe ?", "Le Help Center liste Max 20x à 200 $/mois. Il vise un usage plus intensif. Si tu fais beaucoup de Claude Code, plusieurs projets, des longues sessions et du travail client, il peut éviter des coupures.", "Demande-toi : est-ce que je perds du temps à cause des limites, ou est-ce que je n’utilise pas encore assez l’outil ?", "Tu relies le prix au temps gagné, pas à une envie vague."),
            ("Que se passe-t-il si tu touches la limite ?", "Les limites Pro et Max sont partagées entre Claude et Claude Code. Donc si tu utilises beaucoup Claude dans le chat et Claude Code dans le terminal, tout compte dans la même capacité.", "Si tu touches la limite : attends le reset, réduis les demandes, active des crédits si besoin, ou passe à un plan plus adapté.", "Tu comprends que ce n’est pas un bug : c’est une limite d’usage."),
            ("L’API, c’est encore autre chose", "L’API sert quand un système client appelle Claude automatiquement. Exemple : un assistant email, un chatbot ou une automatisation. Ce n’est pas ton abonnement personnel.", "Garde cette phrase : abonnement = toi qui travailles ; API = un système qui appelle Claude.", "Tu peux expliquer la différence à un client sans jargon."),
            ("Une clé API reste privée", "Une clé API peut coûter de l’argent si quelqu’un l’utilise. Tu ne la mets jamais dans un support, une capture ou GitHub.", "Si une clé a été montrée, tu la révoques et tu en recrées une.", "Tu sais protéger tes accès avant de faire un projet client."),
        ],
    ),
    (
        "Installation",
        "Tu installes Claude Code proprement sur ta machine.",
        "Pratique",
        "cyan",
        [
            ("Tu installes Node.js", "Claude Code s’installe avec npm. npm arrive avec Node.js. Si Node.js n’est pas installé, la commande d’installation ne pourra pas fonctionner.", "Installe Node.js depuis le site officiel, de préférence en version LTS.", "La commande `node -v` affiche une version."),
            ("Tu vérifies npm", "npm est l’outil qui va installer Claude Code. Avant d’aller plus loin, tu vérifies qu’il répond.", "Lance `npm -v` dans le terminal.", "Une version s’affiche sans erreur."),
            ("Tu installes Claude Code", "La commande d’installation ajoute Claude Code à ton environnement. Tu dois la lancer dans un terminal propre.", "Lance `npm install -g @anthropic-ai/claude-code`.", "L’installation se termine sans erreur bloquante."),
            ("Tu n’utilises pas sudo sans comprendre", "Sur beaucoup de machines, utiliser sudo avec npm peut créer des problèmes de droits. La documentation officielle prévient ce point.", "Si tu vois une erreur de permission, lis la doc avant de forcer.", "Tu corriges proprement au lieu de bricoler."),
            ("Tu lances Claude Code dans le dossier", "Le dossier courant est important. Tu dois lancer `claude` depuis le dossier du projet.", "Va dans `formation-s1-claude-code` puis lance `claude`.", "Claude Code démarre dans le bon contexte."),
            ("Tu connectes ton compte", "Au premier lancement, Claude Code te demande de t’authentifier. C’est normal.", "Suis le lien de connexion puis reviens au terminal.", "La session est connectée."),
            ("Tu vérifies l’installation", "Un diagnostic évite de chercher longtemps si quelque chose semble étrange.", "Lance `claude doctor` si l’outil ne se comporte pas comme prévu.", "Tu sais si ton installation est correcte."),
            ("Tu notes les commandes", "Un élève oublie vite une commande vue une seule fois. Le support doit donc te faire garder une trace.", "Crée une note `commandes-s1.md` avec les commandes utiles.", "Tu peux refaire l’installation plus tard."),
        ],
    ),
    (
        "Windows",
        "Tu sais quoi faire si tu n’es pas sur Mac.",
        "Pratique",
        "cyan",
        [
            ("Tu ne copies pas les gestes Mac", "Windows peut demander WSL ou Git Bash selon la configuration. Tu dois suivre la route adaptée à ta machine.", "Lis la partie Windows de la documentation officielle.", "Tu évites les commandes qui ne correspondent pas à ton terminal."),
            ("Tu choisis un terminal principal", "Une erreur fréquente consiste à installer dans un terminal puis lancer dans un autre. Ça rend le diagnostic plus dur.", "Choisis WSL ou Git Bash, puis garde ce choix pendant la séance.", "Tes commandes restent cohérentes."),
            ("Tu vérifies le chemin du dossier", "Sur Windows aussi, Claude Code agit dans le dossier courant.", "Affiche le chemin du terminal avant de lancer `claude`.", "Tu sais où les fichiers seront créés."),
            ("Tu notes ton cas", "Chaque machine peut avoir une petite différence. Ce n’est pas grave si tu gardes une trace.", "Écris : système, terminal utilisé, commandes qui marchent.", "Tu peux reprendre sans repartir à zéro."),
            ("Tu demandes de l’aide avec l’erreur exacte", "Une erreur copiée exactement est plus utile qu’une explication approximative.", "Copie l’erreur complète avant de demander une solution.", "La correction est plus rapide."),
            ("Tu gardes le même objectif", "Mac ou Windows, le but reste identique : lancer Claude Code dans un dossier propre et vérifier le résultat.", "Refais le même mini-exercice que les élèves Mac.", "Tout le monde arrive au même niveau."),
        ],
    ),
    (
        "Claude Code Desktop",
        "Tu comprends la différence entre l’interface terminal et l’interface Desktop.",
        "Interface",
        "violet",
        [
            ("C’est quoi le Code tab ?", "Claude Desktop possède un onglet Code. Il permet d’utiliser Claude Code dans une interface graphique au lieu de tout faire dans le terminal.", "Regarde l’interface Desktop comme un espace de travail : sessions, chat, fichiers, terminal, aperçu.", "Tu sais que Desktop n’est pas un autre outil magique, c’est une autre surface pour Claude Code."),
            ("Pourquoi Desktop peut aider un élève ?", "Si le terminal te stresse, Desktop peut rendre le flux plus visuel. Tu vois les sessions, les fichiers, les panneaux et parfois l’aperçu de l’app.", "Utilise Desktop si tu veux mieux voir ce qui se passe.", "Tu comprends que le principe reste le même : dossier, demande, vérification."),
            ("Le terminal intégré", "Dans Desktop, le terminal peut être intégré à la session. Il travaille dans le même dossier que Claude.", "Ouvre le terminal intégré quand tu dois lancer `npm test`, `git status` ou une commande simple.", "Tu ne changes pas d’outil sans comprendre le dossier actif."),
            ("Les modes de permission", "Desktop met en avant les modes comme Ask permissions, Plan mode ou Auto accept edits. Pour un débutant, Ask permissions ou Plan mode sont plus rassurants.", "Commence avec un mode où Claude explique ou demande avant d’agir.", "Tu vois les actions avant de les accepter."),
            ("L’aperçu de l’app", "Desktop peut ouvrir un aperçu de page ou d’application. Pour les supports HTML et les sites, c’est très utile.", "Quand Claude crée une page, ouvre l’aperçu avant de dire que c’est terminé.", "Tu vérifies comme un utilisateur, pas seulement comme un technicien."),
            ("Terminal ou Desktop ?", "Question à te poser : est-ce que je veux aller vite dans le terminal, ou mieux visualiser le projet dans Desktop ? Les deux peuvent être utiles.", "Choisis la surface qui t’aide à mieux contrôler le travail.", "Tu sais expliquer pourquoi tu utilises l’un ou l’autre."),
        ],
    ),
    (
        "Premier exercice",
        "Tu fais une petite production pour comprendre la boucle de travail.",
        "Pratique",
        "cyan",
        [
            ("Tu demandes une page simple", "Le premier exercice doit être court. Tu veux voir le cycle complet, pas construire un grand projet.", "Demande : `Crée une page HTML simple pour un freelance IA.`", "Un fichier HTML est créé."),
            ("Tu demandes où est le fichier", "Un élève doit toujours savoir où se trouve le résultat.", "Ajoute : `À la fin, liste les fichiers créés.`", "Tu sais ouvrir le bon fichier."),
            ("Tu ouvres la page", "Le résultat doit être visible. Ne valide pas seulement parce que Claude Code dit que c’est terminé.", "Ouvre le fichier dans le navigateur.", "Tu vois la page."),
            ("Tu corriges une chose à la fois", "Si tu demandes dix corrections à la fois, tu ne sais plus ce qui a changé.", "Demande une seule correction : titre, couleur, section, texte.", "La page progresse sans devenir confuse."),
            ("Tu demandes une checklist", "Claude Code peut t’aider à tester. C’est utile pour apprendre à livrer proprement.", "Demande une checklist de vérification en 8 points.", "Tu sais quoi regarder."),
            ("Tu fais un résumé final", "À la fin, tu dois pouvoir expliquer ce qui a été fait.", "Demande : `Résume les fichiers créés et les prochaines actions.`", "Tu peux fermer la session proprement."),
        ],
    ),
    (
        "Bien écrire à Claude Code",
        "Tu apprends à donner une demande claire sans parler comme un robot.",
        "Méthode",
        "violet",
        [
            ("Tu donnes le contexte", "Claude Code doit savoir pour qui il travaille. Un support élève, une page client et un script interne ne se rédigent pas pareil.", "Commence par : `Je crée un support pour des élèves débutants.`", "Le ton devient plus adapté."),
            ("Tu donnes la sortie attendue", "Un bon prompt dit ce qui doit exister à la fin. Sinon, l’outil invente une forme.", "Précise : fichier HTML, README, tableau, checklist, script.", "Le résultat est plus simple à vérifier."),
            ("Tu donnes les contraintes", "Les contraintes protègent la qualité. Elles évitent les pages trop génériques.", "Indique le ton, les couleurs, les fichiers à ne pas toucher.", "Le rendu respecte mieux le cadre."),
            ("Tu demandes un plan avant le gros travail", "Pour un gros support, l’élève doit voir la structure avant la production.", "Demande : `Propose le plan avant de créer le fichier.`", "Tu peux corriger la direction."),
            ("Tu demandes une correction précise", "Une correction précise donne un meilleur résultat qu’une phrase vague.", "Dis : `Rends les phrases plus courtes dans la section installation.`", "La modification est ciblée."),
            ("Tu demandes une vérification", "Claude Code peut relire son travail avec une consigne précise.", "Demande : `Vérifie les liens, les titres et la version mobile.`", "Tu réduis les oublis."),
        ],
    ),
    (
        "Fichiers et sécurité",
        "Tu apprends à garder ton projet lisible et sûr.",
        "Vigilance",
        "orange",
        [
            ("Tu sépares les projets", "Ne mélange pas formation, client et tests. Un agent qui lit trop de choses peut se tromper de contexte.", "Un dossier par projet, avec un nom clair.", "Tu réduis les erreurs."),
            ("Tu nommes les fichiers clairement", "Un fichier doit expliquer son rôle par son nom.", "Utilise `support-technique-seance-01.html` plutôt que `new-final-ok.html`.", "Tu retrouves vite le bon fichier."),
            ("Tu ne mets pas les secrets dans GitHub", "Un mot de passe, une clé API ou un token ne doit jamais être publié.", "Utilise des fichiers privés et vérifie avant de commit.", "Tes accès restent protégés."),
            ("Tu demandes avant de supprimer", "Si Claude Code propose de nettoyer, il doit expliquer ce qu’il veut enlever.", "Demande : `Liste ce que tu veux supprimer avant action.`", "Tu évites une perte de fichiers."),
            ("Tu gardes une note projet", "Une note simple aide les élèves à reprendre après une pause.", "Crée un `README.md` ou une note de livraison.", "Le projet devient compréhensible."),
            ("Tu vérifies les fichiers touchés", "Après une action, il faut savoir ce qui a changé.", "Demande un résumé des fichiers modifiés.", "Tu ne travailles pas à l’aveugle."),
        ],
    ),
    (
        "Commandes utiles",
        "Tu gardes les commandes courtes à portée de main.",
        "Pratique",
        "cyan",
        [
            ("Tu lances l’outil", "La commande `claude` lance une session interactive dans le dossier courant.", "Lance `claude` dans ton dossier test.", "Claude Code démarre."),
            ("Tu diagnostiques", "La commande `claude doctor` aide à vérifier l’installation.", "Lance-la si quelque chose ne répond pas normalement.", "Tu as un diagnostic."),
            ("Tu mets à jour", "Claude Code évolue. Une mise à jour peut corriger un problème.", "Utilise `claude update` quand tu n’es pas en livraison urgente.", "L’outil est à jour."),
            ("Tu utilises l’aide", "Tu n’as pas besoin de tout retenir. Tu dois savoir retrouver.", "Utilise `/help` dans la session.", "Tu vois les commandes disponibles."),
            ("Tu repars proprement", "Quand une conversation devient confuse, mieux vaut parfois repartir avec un contexte propre.", "Utilise `/clear` si la session est trop polluée.", "Tu retrouves une discussion lisible."),
            ("Tu compacts si c’est long", "Sur un projet long, le contexte peut devenir lourd. `/compact` aide à garder l’essentiel.", "Utilise-le après une grosse étape.", "La session reste exploitable."),
        ],
    ),
    (
        "CLAUDE.md",
        "Tu donnes une mémoire claire au projet.",
        "Méthode",
        "violet",
        [
            ("Tu crées un briefing permanent", "CLAUDE.md explique à Claude Code les règles du projet. C’est utile quand le travail dure plus d’une session.", "Crée un fichier `CLAUDE.md` dans les projets sérieux.", "Claude Code retrouve le cadre."),
            ("Tu écris des règles concrètes", "Une règle vague n’aide pas. Une règle précise guide vraiment.", "Écris : `Phrases courtes. Français simple. Ne pas modifier les vidéos.`", "Les sorties sont plus stables."),
            ("Tu notes les commandes du projet", "Si un projet a des commandes de test ou de génération, mets-les dans CLAUDE.md.", "Ajoute les commandes utiles avec une courte explication.", "L’agent peut les retrouver."),
            ("Tu sépares personnel et projet", "Tes préférences globales ne sont pas toujours les règles du projet.", "Mets les règles du projet dans le dossier projet.", "Le cadre reste propre."),
            ("Tu relis la mémoire", "Une mémoire ancienne peut créer des erreurs. Elle doit suivre le projet.", "Relis CLAUDE.md avant une nouvelle phase.", "Tu évites les consignes dépassées."),
            ("Tu l’utilises comme un professeur", "Pour les élèves, CLAUDE.md peut servir de consigne permanente : ton simple, étapes claires, vérification finale.", "Ajoute une section `Règles pédagogiques`.", "Le support reste orienté apprenant."),
        ],
    ),
    (
        "Résoudre les problèmes",
        "Tu sais quoi faire quand une commande ne marche pas.",
        "Vigilance",
        "orange",
        [
            ("Tu copies l’erreur exacte", "Une erreur exacte est plus utile qu’un résumé approximatif.", "Copie le message complet dans une note.", "Tu peux demander une aide précise."),
            ("Tu regardes le dossier courant", "Beaucoup de problèmes viennent du mauvais dossier.", "Vérifie le chemin avant de relancer.", "Tu sais où tu travailles."),
            ("Tu vérifies Node et npm", "Si l’installation bloque, commence par les bases.", "Lance `node -v` puis `npm -v`.", "Tu sais si l’environnement répond."),
            ("Tu ne forces pas au hasard", "Lancer des commandes au hasard peut créer plus de problèmes.", "Demande une explication avant une commande sensible.", "Tu gardes une machine propre."),
            ("Tu réduis la demande", "Si Claude Code part dans tous les sens, réduis le problème.", "Demande une seule correction.", "Tu reprends le contrôle."),
            ("Tu utilises la documentation", "La documentation Claude Code est la source de référence. Le support t’aide, mais la doc confirme.", "Ouvre la page de dépannage si besoin.", "Tu vérifies avec la source officielle."),
        ],
    ),
    (
        "Livrer proprement",
        "Tu penses déjà comme quelqu’un qui va rendre un travail.",
        "Validation",
        "green",
        [
            ("Tu expliques ce qui a été fait", "Un bon livrable n’est pas juste un fichier. C’est un fichier avec une explication simple.", "Ajoute une note : objectif, fichiers, lancement.", "La personne comprend le résultat."),
            ("Tu listes les limites", "Dire les limites évite les malentendus.", "Ajoute : ce qui marche, ce qui reste à tester, ce qui est hors périmètre.", "La livraison est plus professionnelle."),
            ("Tu donnes une checklist de test", "Une checklist aide l’élève ou le client à tester sans se perdre.", "Demande une checklist claire à Claude Code.", "Les retours sont plus précis."),
            ("Tu gardes l’humain au centre", "L’IA aide à produire, mais la validation reste humaine.", "Relis les textes et ouvre les pages.", "Tu valides vraiment."),
            ("Tu proposes la suite", "Une livraison propre peut ouvrir une amélioration sans forcer.", "Liste trois prochaines actions possibles.", "Le projet peut continuer."),
            ("Tu ranges avant de finir", "Un dossier rangé est plus facile à reprendre.", "Demande une proposition de rangement avant fermeture.", "Tu termines proprement."),
        ],
    ),
    (
        "Récapitulatif",
        "Tu repars avec une méthode utilisable dans les prochaines séances.",
        "Validation",
        "green",
        [
            ("Tu sais installer", "Tu sais que Node.js et npm sont nécessaires avant Claude Code.", "Refais les commandes de vérification.", "Tu peux contrôler l’environnement."),
            ("Tu sais lancer", "Tu sais que Claude Code se lance dans un dossier précis.", "Lance `claude` depuis ton dossier test.", "La session est au bon endroit."),
            ("Tu sais demander", "Tu sais écrire un prompt avec contexte, sortie et contraintes.", "Prépare une demande courte et claire.", "L’outil comprend mieux."),
            ("Tu sais vérifier", "Tu sais ouvrir le résultat et demander une correction.", "Teste le fichier créé.", "Tu ne valides pas à l’aveugle."),
            ("Tu sais sécuriser", "Tu sais ne pas publier de secrets et demander avant suppression.", "Vérifie les fichiers avant de partager.", "Le projet reste sûr."),
            ("Tu es prêt pour Codex", "La séance suivante comparera Codex et Claude Code. Tu arrives avec les bases.", "Note ce que tu veux comparer.", "Tu suis la suite plus facilement."),
        ],
    ),
]


def e(text: str) -> str:
    return escape(text, quote=True)


def screen(index: int, alt: str, caption: str) -> str:
    file_name = SCREENS[index % len(SCREENS)]
    src = f"assets/claude-code-screens/{file_name}"
    return f"""
      <figure class="group overflow-hidden border-2 border-slate-950 bg-white shadow-[8px_8px_0_#111827]">
        <img class="h-full min-h-[260px] w-full object-cover transition duration-300 group-hover:scale-[1.025]" src="{src}" alt="{e(alt)}" loading="lazy">
        <figcaption class="border-t-2 border-slate-950 bg-white px-4 py-3 text-sm font-semibold text-slate-700">{e(caption)}</figcaption>
      </figure>
    """


def visual_for(item: dict[str, str], index: int) -> str:
    text = f"{item['chapter']} {item['title']} {item['story']} {item['action']} {item['check']} {item['tag']}".lower()
    if "clé api" in text or "secret" in text:
        name = "api-key-warning.png"
    elif "api" in text:
        name = "api-vs-subscription.png"
    elif "max 20" in text or "max 5" in text or "prix" in text or "payer" in text or "achat" in text:
        name = "pricing-plans.png"
    elif "limite" in text or "quota" in text or "usage" in text or "reset" in text or "crédit" in text:
        name = "usage-limits.png"
    elif "windows" in text or "powershell" in text or "wsl" in text or "git bash" in text:
        name = "windows-terminal.png"
    elif "desktop" in text or "code tab" in text or "aperçu" in text:
        if "permission" in text:
            name = "desktop-permissions.png"
        elif "usage" in text or "limite" in text:
            name = "desktop-usage.png"
        elif "terminal" in text:
            name = "desktop-terminal-pane.png"
        else:
            name = "desktop-files-preview.png"
    elif "connect" in text or "authent" in text or "compte" in text or "/login" in text:
        name = "auth-login.png"
    elif "node" in text or "npm -v" in text:
        name = "install-node-npm.png"
    elif "install" in text or "npm install" in text:
        name = "install-claude-command.png"
    elif "doctor" in text or "update" in text or "diagnostic" in text:
        name = "update-doctor.png"
    elif "git" in text:
        name = "git-status.png"
    elif "test" in text or "build" in text or "checklist" in text:
        name = "checklist-test.png" if "checklist" in text else "npm-test.png"
    elif "plan mode" in text or "propose le plan" in text or "plan avant" in text:
        name = "plan-mode.png"
    elif "permission" in text or "sécurité" in text or "bypass" in text:
        name = "permissions-modes.png"
    elif "diff" in text or "accepter" in text or "valider" in text:
        name = "diff-approval.png"
    elif "claude.md" in text or "mémoire" in text:
        name = "memory-claude-md.png"
    elif "fichier" in text and ("créé" in text or "existe" in text or "ouvrir" in text):
        name = "file-created.png"
    elif "dossier" in text or "chemin" in text or "lancer" in text or "terminal" in text:
        name = "project-folder.png" if "propre" in text or "chemin" in text else "terminal-start.png"
    elif "dépannage" in text or "erreur" in text or "bloque" in text or "permission denied" in text:
        name = "error-copy.png" if "copie" in text or "exact" in text else "troubleshooting.png"
    elif "prompt" in text or "contrainte" in text or "contexte" in text:
        name = "prompt-constraints.png"
    elif "exercice" in text or "demande une page" in text:
        name = "first-prompt.png"
    elif "cli" in text or "help" in text:
        name = "cli-help.png"
    elif "clear" in text or "compact" in text or "conversation" in text:
        name = "clear-compact.png"
    elif "résumé" in text or "livrer" in text or "livraison" in text or "terminé" in text or "final" in text:
        name = "delivery-summary.png"
    elif "documentation" in text or "source officielle" in text or "liens" in text:
        name = "source-docs.png"
    else:
        name = INTERFACE_SCREENS[index % len(INTERFACE_SCREENS)]
    alt, caption = INTERFACE_META.get(name, ("Interface Claude Code", "Interface Claude Code adaptée à cette section."))
    src = f"assets/claude-code-interface/{name}"
    return f"""
      <figure class="group overflow-hidden border-2 border-slate-950 bg-white shadow-[8px_8px_0_#111827]">
        <img class="aspect-[16/10] w-full bg-white object-contain transition duration-300 group-hover:scale-[1.015]" src="{src}" alt="{e(alt)}" loading="lazy">
        <figcaption class="border-t-2 border-slate-950 bg-white px-4 py-3 text-sm font-semibold text-slate-700">{e(caption)}</figcaption>
      </figure>
    """


def question_for(item: dict[str, str]) -> str:
    text = f"{item['chapter']} {item['title']} {item['story']} {item['tag']}".lower()
    if "prix" in text or "plan" in text or "quota" in text or "limite" in text:
        return "Est-ce que ce plan répond à mon usage réel, ou est-ce que je paie trop tôt ?"
    if "installation" in text or "node" in text or "npm" in text:
        return "Quelle preuve simple me montre que l’installation marche vraiment ?"
    if "desktop" in text or "interface" in text:
        return "Qu’est-ce que cette interface me permet de mieux contrôler ?"
    if "sécurité" in text or "clé" in text or "secret" in text:
        return "Qu’est-ce que je dois protéger avant de publier ou partager ?"
    if "livrer" in text or "validation" in text or "récapitulatif" in text:
        return "Quelle preuve me permet de dire que cette étape est terminée ?"
    if "prompt" in text or "méthode" in text:
        return "Est-ce que ma demande dit clairement le contexte, la sortie et les limites ?"
    if "chatgpt" in text or "comparaison" in text:
        return "Ai-je besoin d’une réponse, ou d’une action dans un vrai dossier ?"
    if "dossier" in text or "fichier" in text:
        return "Si je reviens demain, est-ce que je retrouve vite le bon fichier ?"
    if "dépannage" in text or "erreur exacte" in text or "bloque" in text:
        return "Quelle information exacte dois-je garder avant de chercher une solution ?"
    return "Qu’est-ce que je dois comprendre, faire, puis vérifier avant de continuer ?"


def badge(text: str, color: str) -> str:
    colors = {
        "blue": "bg-blue-600 text-white",
        "violet": "bg-violet-600 text-white",
        "cyan": "bg-cyan-200 text-slate-950",
        "orange": "bg-orange-200 text-slate-950",
        "green": "bg-emerald-200 text-slate-950",
    }
    return f'<span class="{colors[color]} border-2 border-slate-950 px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] shadow-[3px_3px_0_#111827]">{e(text)}</span>'


def code_block(lines: list[str]) -> str:
    return (
        '<div class="relative border-2 border-slate-950 bg-slate-950 p-5 text-white shadow-[8px_8px_0_#111827]">'
        '<button type="button" class="copy-btn absolute right-3 top-3 border-2 border-white bg-white px-3 py-1 text-xs font-black text-slate-950 transition hover:-translate-y-0.5">Copier</button>'
        '<pre class="overflow-auto pr-20 text-sm leading-7"><code>'
        + e("\n".join(lines))
        + "</code></pre></div>"
    )


def table(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f'<th class="border-2 border-slate-950 bg-blue-100 px-4 py-3 text-left text-xs uppercase tracking-[.14em]">{e(h)}</th>' for h in headers)
    body = ""
    for row in rows:
        body += "<tr>" + "".join(f'<td class="border-2 border-slate-950 bg-white px-4 py-3 align-top text-sm leading-6 text-slate-700">{cell}</td>' for cell in row) + "</tr>"
    return f'<div class="overflow-auto border-2 border-slate-950 bg-white shadow-[8px_8px_0_#111827]"><table class="w-full min-w-[760px] border-collapse">{head and f"<thead><tr>{head}</tr></thead>"}<tbody>{body}</tbody></table></div>'


def all_sections() -> list[dict[str, str]]:
    result = []
    for chapter, summary, tag, color, items in CHAPTERS:
        for title, story, action, check in items:
            result.append(
                {
                    "chapter": chapter,
                    "summary": summary,
                    "tag": tag,
                    "color": color,
                    "title": title,
                    "story": story,
                    "action": action,
                    "check": check,
                }
            )
    return result


def section_header(item: dict[str, str], n: int) -> str:
    return f"""
      <div class="mb-6 flex flex-wrap items-center gap-3">
        {badge(f"{n:02d}", item["color"])}
        {badge(item["tag"], item["color"])}
        <span class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] text-slate-700 shadow-[3px_3px_0_#111827]">{e(item["chapter"])}</span>
      </div>
    """


def detail_cards(item: dict[str, str]) -> str:
    rows = [
        ("01", "Pourquoi c’est utile", item["story"], "bg-blue-50"),
        ("02", "Ce que tu fais", item["action"], "bg-violet-50"),
        ("03", "Comment tu vérifies", item["check"], "bg-white"),
        ("04", "Question à te poser", question_for(item), "bg-cyan-50"),
    ]
    body = ""
    for number, title, content, tone in rows:
        body += f"""
        <div class="grid gap-0 sm:grid-cols-[150px_1fr]">
          <div class="{tone} border-b-2 border-slate-950 px-5 py-4 sm:border-b-0 sm:border-r-2">
            <p class="font-mono text-[11px] font-black uppercase tracking-[.16em] text-slate-500">{number}</p>
            <p class="mt-2 text-base font-black leading-6 text-slate-950">{e(title)}</p>
          </div>
          <div class="bg-white px-5 py-4">
            <p class="max-w-3xl text-[15px] leading-7 text-slate-700">{e(content)}</p>
          </div>
        </div>
        """
    return f"""
      <div class="mt-7 overflow-hidden border-2 border-slate-950 bg-white shadow-[7px_7px_0_#111827]">
        <div class="border-b-2 border-slate-950 bg-slate-950 px-5 py-3">
          <p class="font-mono text-[11px] font-black uppercase tracking-[.18em] text-white">Lecture guidée</p>
        </div>
        <div class="divide-y-2 divide-slate-950">
          {body}
        </div>
      </div>
    """


def layout_a(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-8 lg:grid-cols-[1.05fr_.95fr] lg:items-start">
        <article class="border-2 border-slate-950 bg-white p-7 shadow-[8px_8px_0_#111827]">
          <h2 class="font-display text-3xl font-black tracking-tight text-slate-950 sm:text-5xl">{e(item["title"])}</h2>
          <p class="mt-5 text-lg leading-8 text-slate-700">{e(item["summary"])}</p>
          {detail_cards(item)}
        </article>
        {visual_for(item, n)}
      </div>
    </section>
    """


def layout_b(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-6 lg:grid-cols-3">
        <div class="border-2 border-slate-950 bg-blue-600 p-7 text-white shadow-[8px_8px_0_#111827] lg:col-span-1">
          <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-blue-100">Message élève</p>
          <h2 class="mt-4 font-display text-3xl font-black">{e(item["title"])}</h2>
          <p class="mt-4 leading-7 text-blue-50">{e(item["story"])}</p>
        </div>
        <div class="border-2 border-slate-950 bg-white p-7 shadow-[8px_8px_0_#111827] lg:col-span-2">
          <div class="grid gap-4 md:grid-cols-2">
            <div class="border-2 border-slate-950 bg-violet-50 p-5"><p class="font-black">Étape</p><p class="mt-2 text-slate-700">{e(item["action"])}</p></div>
            <div class="border-2 border-slate-950 bg-white p-5"><p class="font-black">Résultat attendu</p><p class="mt-2 text-slate-700">{e(item["check"])}</p></div>
          </div>
          <p class="mt-6 text-lg leading-8 text-slate-700">Lis cette section comme une consigne de travail. Tu n’as pas besoin de retenir chaque mot. Tu dois surtout comprendre le geste à faire et le point à vérifier.</p>
          <div class="mt-6 grid gap-6 lg:grid-cols-[.85fr_1.15fr] lg:items-start">
            <div class="border-2 border-slate-950 bg-cyan-50 p-5 shadow-[5px_5px_0_#111827]">
              <p class="font-black text-slate-950">Question à te poser</p>
              <p class="mt-2 leading-7 text-slate-700">{e(question_for(item))}</p>
            </div>
            {visual_for(item, n + 11)}
          </div>
        </div>
      </div>
    </section>
    """


def layout_c(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="border-2 border-slate-950 bg-white shadow-[8px_8px_0_#111827]">
        <div class="border-b-2 border-slate-950 bg-violet-600 px-5 py-3 font-mono text-xs font-black uppercase tracking-[.16em] text-white">Bloc pratique à copier</div>
        <div class="grid gap-0 lg:grid-cols-[.95fr_1.05fr]">
          <div class="p-7">
            <h2 class="font-display text-3xl font-black text-slate-950 sm:text-5xl">{e(item["title"])}</h2>
            <p class="mt-5 text-lg leading-8 text-slate-700">{e(item["story"])}</p>
          </div>
          <div class="border-t-2 border-slate-950 p-7 lg:border-l-2 lg:border-t-0">
            {code_block([item["action"], "", "Vérification :", item["check"]])}
          </div>
        </div>
        <div class="grid gap-6 border-t-2 border-slate-950 p-7 lg:grid-cols-[.8fr_1.2fr] lg:items-start">
          <div class="border-2 border-slate-950 bg-cyan-50 p-5 shadow-[5px_5px_0_#111827]">
            <p class="font-black text-slate-950">Question à te poser</p>
            <p class="mt-2 leading-7 text-slate-700">{e(question_for(item))}</p>
          </div>
          {visual_for(item, n + 17)}
        </div>
      </div>
    </section>
    """


def layout_d(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-8 lg:grid-cols-[.9fr_1.1fr] lg:items-center">
        {visual_for(item, n + 5)}
        <div>
          <h2 class="font-display text-3xl font-black text-slate-950 sm:text-5xl">{e(item["title"])}</h2>
          <p class="mt-5 text-lg leading-8 text-slate-700">{e(item["story"])}</p>
          <div class="mt-6 border-2 border-slate-950 bg-white p-6 shadow-[8px_8px_0_#111827]">
            <p class="font-black text-slate-950">Consigne simple pour toi</p>
            <p class="mt-2 text-slate-700">{e(item["action"])}</p>
            <p class="mt-4 border-l-4 border-blue-600 pl-4 font-semibold text-slate-800">{e(item["check"])}</p>
            <p class="mt-4 border-2 border-slate-950 bg-cyan-50 p-4 font-semibold text-slate-800">{e(question_for(item))}</p>
          </div>
        </div>
      </div>
    </section>
    """


def layout_e(item: dict[str, str], n: int) -> str:
    rows = [
        ["Point à comprendre", e(item["story"])],
        ["Action élève", e(item["action"])],
        ["Validation", e(item["check"])],
        ["Question à te poser", e(question_for(item))],
        ["Erreur à éviter", "Passer à l’étape suivante sans avoir ouvert ou vérifié le résultat."],
    ]
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-8 lg:grid-cols-[.8fr_1.2fr]">
        <div>
          <h2 class="font-display text-3xl font-black text-slate-950 sm:text-5xl">{e(item["title"])}</h2>
          <p class="mt-5 text-lg leading-8 text-slate-700">{e(item["summary"])}</p>
        </div>
        <div class="space-y-6">
          {table(["Élément", "Explication"], rows)}
          {visual_for(item, n + 23)}
        </div>
      </div>
    </section>
    """


def layout_f(item: dict[str, str], n: int) -> str:
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-8 lg:grid-cols-[.95fr_1.05fr] lg:items-start">
        <div class="border-2 border-slate-950 bg-white p-7 shadow-[8px_8px_0_#111827]">
          <h2 class="font-display text-3xl font-black text-slate-950 sm:text-5xl">{e(item["title"])}</h2>
          <p class="mt-5 text-lg leading-8 text-slate-700">{e(item["story"])}</p>
          <div class="mt-6 border-l-4 border-blue-600 bg-blue-50 px-5 py-4">
            <p class="font-black text-slate-950">Question à te poser</p>
            <p class="mt-2 leading-7 text-slate-700">{e(question_for(item))}</p>
          </div>
        </div>
        <div class="space-y-6">
          <div class="overflow-hidden border-2 border-slate-950 bg-white shadow-[8px_8px_0_#111827]">
            <div class="grid sm:grid-cols-[150px_1fr]">
              <div class="border-b-2 border-slate-950 bg-blue-50 px-5 py-4 sm:border-b-0 sm:border-r-2">
                <p class="font-mono text-[11px] font-black uppercase tracking-[.16em] text-blue-700">À faire</p>
              </div>
              <p class="px-5 py-4 text-[15px] font-semibold leading-7 text-slate-800">{e(item["action"])}</p>
            </div>
            <div class="grid border-t-2 border-slate-950 sm:grid-cols-[150px_1fr]">
              <div class="border-b-2 border-slate-950 bg-violet-50 px-5 py-4 sm:border-b-0 sm:border-r-2">
                <p class="font-mono text-[11px] font-black uppercase tracking-[.16em] text-violet-700">À vérifier</p>
              </div>
              <p class="px-5 py-4 text-[15px] font-semibold leading-7 text-slate-800">{e(item["check"])}</p>
            </div>
          </div>
          {visual_for(item, n + 29)}
        </div>
      </div>
    </section>
    """


LAYOUTS = [layout_a, layout_b, layout_c, layout_d, layout_e, layout_f]


def render_section(item: dict[str, str], n: int) -> str:
    return LAYOUTS[(n - 1) % len(LAYOUTS)](item, n)


def nav() -> str:
    links = [
        ("Départ", "#section-01"),
        ("Installer", "#section-19"),
        ("Exercice", "#section-33"),
        ("Prompts", "#section-39"),
        ("Sécurité", "#section-45"),
        ("Récap", "#section-81"),
    ]
    return "".join(
        f'<a class="border-2 border-slate-950 bg-white px-3 py-2 text-xs font-black uppercase tracking-[.12em] text-slate-950 no-underline shadow-[3px_3px_0_#111827] transition hover:-translate-y-0.5 hover:bg-blue-600 hover:text-white" href="{href}">{label}</a>'
        for label, href in links
    )


def source_table() -> str:
    rows = [
        ["Vue d’ensemble Claude Code", f'<a href="{DOCS["overview"]}" target="_blank" rel="noopener">Documentation officielle</a>'],
        ["Installation", f'<a href="{DOCS["setup"]}" target="_blank" rel="noopener">Advanced setup Claude Code</a>'],
        ["CLI", f'<a href="{DOCS["cli"]}" target="_blank" rel="noopener">CLI reference</a>'],
        ["Application Desktop", f'<a href="https://code.claude.com/docs/en/desktop" target="_blank" rel="noopener">Claude Code on Desktop</a>'],
        ["Mémoire CLAUDE.md", f'<a href="{DOCS["memory"]}" target="_blank" rel="noopener">How Claude remembers your project</a>'],
        ["Sécurité", f'<a href="{DOCS["security"]}" target="_blank" rel="noopener">Security</a>'],
        ["Prix Claude", f'<a href="{DOCS["plans"]}" target="_blank" rel="noopener">Choisir un plan Claude</a>'],
        ["Claude Code avec Pro/Max", f'<a href="{DOCS["pro_max"]}" target="_blank" rel="noopener">Limites et crédits</a>'],
        ["Premier jour avec Claude Code", f'<a href="{DOCS["first_day"]}" target="_blank" rel="noopener">Guide Help Center</a>'],
        ["Node.js", f'<a href="{DOCS["node"]}" target="_blank" rel="noopener">Téléchargement officiel Node.js</a>'],
    ]
    return table(["Ressource", "Lien"], rows)


def render() -> str:
    sections = all_sections()
    html_sections = "\n".join(render_section(item, i) for i, item in enumerate(sections, 1))
    return f"""<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Support technique - Séance 01 - Claude Code | DENEM Academy</title>
  <link rel="icon" href="logo-denem.jpeg">
  <link href="assets/tailwind-s1.css" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; }}
    body {{ margin:0; background:#fff; color:#0f172a; font-family:Inter,system-ui,sans-serif; overflow-x:hidden; }}
    .section-block {{ scroll-margin-top:110px; }}
    .reveal {{ opacity:0; transform:translateY(16px); transition:opacity .5s ease, transform .5s ease; }}
    .reveal.visible {{ opacity:1; transform:translateY(0); }}
    .progress-line {{ transform-origin:left; transform:scaleX(0); }}
    .copy-btn.copied {{ background:#bbf7d0; }}
    a {{ color:#1d4ed8; text-decoration:underline; text-decoration-thickness:2px; text-underline-offset:3px; }}
    @media (prefers-reduced-motion: reduce) {{ .reveal {{ transition:none; }} }}
  </style>
</head>
<body class="bg-white">
  <div class="fixed left-0 top-0 z-[90] h-1 w-full bg-slate-200"><div id="progress" class="progress-line h-full bg-gradient-to-r from-blue-600 via-violet-600 to-cyan-400"></div></div>

  <nav class="z-50 border-b-2 border-slate-950 bg-white lg:sticky lg:top-0">
    <div class="mx-auto flex max-w-7xl flex-col gap-4 px-4 py-4 sm:px-6 lg:flex-row lg:items-center lg:justify-between lg:px-8">
      <a href="#top" class="flex items-center gap-3 text-slate-950 no-underline">
        <img src="logo-denem.jpeg" alt="Logo DENEM" class="h-11 w-11 border-2 border-slate-950 object-cover shadow-[4px_4px_0_#111827]">
        <span><b class="block font-display text-lg leading-none">DENEM Academy</b><small class="font-mono text-xs uppercase tracking-[.14em] text-slate-500">Support élèves - Séance 01</small></span>
      </a>
      <div class="flex flex-wrap gap-2">{nav()}</div>
    </div>
  </nav>

  <header id="top" class="mx-auto max-w-7xl bg-white px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
    <div class="grid gap-8 lg:grid-cols-[1.04fr_.96fr] lg:items-center">
      <div>
        <div class="mb-5 inline-flex border-2 border-slate-950 bg-blue-600 px-4 py-2 font-mono text-xs font-black uppercase tracking-[.18em] text-white shadow-[5px_5px_0_#111827]">Support technique pour les élèves</div>
        <h1 class="font-display text-5xl font-black leading-[.92] tracking-tight text-slate-950 sm:text-7xl lg:text-8xl">Claude Code.<br><span class="text-blue-600">Tu installes.</span><br><span class="text-violet-600">Tu pratiques.</span></h1>
        <p class="mt-7 max-w-3xl text-xl leading-9 text-slate-700">Ce support est fait pour toi. Il ne répète pas la vidéo mot pour mot. Il transforme la séance en méthode claire : quoi faire, pourquoi le faire, quoi vérifier, et comment éviter les erreurs.</p>
        <div class="mt-8 flex flex-wrap gap-3">
          <a href="#section-01" class="border-2 border-slate-950 bg-slate-950 px-5 py-3 font-black text-white no-underline shadow-[5px_5px_0_#111827] transition hover:-translate-y-1">Commencer</a>
          <a href="transcription/seance-01-transcription.md" class="border-2 border-slate-950 bg-white px-5 py-3 font-black text-slate-950 no-underline shadow-[5px_5px_0_#111827] transition hover:-translate-y-1">Transcription</a>
          <a href="{DOCS["setup"]}" target="_blank" rel="noopener" class="border-2 border-slate-950 bg-blue-100 px-5 py-3 font-black text-slate-950 no-underline shadow-[5px_5px_0_#111827] transition hover:-translate-y-1">Doc Claude Code</a>
        </div>
      </div>
      <div class="border-2 border-slate-950 bg-white p-4 shadow-[8px_8px_0_#111827]">
        <figure class="group overflow-hidden border-2 border-slate-950 bg-white shadow-[8px_8px_0_#111827]">
          <img class="aspect-[16/10] w-full bg-white object-contain transition duration-300 group-hover:scale-[1.015]" src="assets/claude-code-interface/terminal-start.png" alt="Interface terminal Claude Code" loading="lazy">
          <figcaption class="border-t-2 border-slate-950 bg-white px-4 py-3 text-sm font-semibold text-slate-700">Interface terminal Claude Code, sans donnée sensible.</figcaption>
        </figure>
        <div class="mt-4 grid grid-cols-3 gap-3">
          <div class="border-2 border-slate-950 bg-blue-50 p-3 text-center"><b class="block text-3xl font-black">{len(sections)}</b><span class="text-xs font-bold uppercase">sections</span></div>
          <div class="border-2 border-slate-950 bg-violet-50 p-3 text-center"><b class="block text-3xl font-black">{len(INTERFACE_SCREENS)}</b><span class="text-xs font-bold uppercase">interfaces</span></div>
          <div class="border-2 border-slate-950 bg-white p-3 text-center"><b class="block text-3xl font-black">6</b><span class="text-xs font-bold uppercase">formats</span></div>
        </div>
      </div>
    </div>
  </header>

  <section class="mx-auto max-w-7xl bg-white px-4 py-8 sm:px-6 lg:px-8">
    <div class="grid gap-4 md:grid-cols-5">
      <div class="border-2 border-slate-950 bg-blue-50 p-5 shadow-[4px_4px_0_#111827]"><b>Théorie</b><p class="mt-2 text-sm text-slate-700">Tu comprends avant de cliquer.</p></div>
      <div class="border-2 border-slate-950 bg-cyan-50 p-5 shadow-[4px_4px_0_#111827]"><b>Pratique</b><p class="mt-2 text-sm text-slate-700">Tu fais une action simple.</p></div>
      <div class="border-2 border-slate-950 bg-violet-50 p-5 shadow-[4px_4px_0_#111827]"><b>Méthode</b><p class="mt-2 text-sm text-slate-700">Tu gardes un réflexe.</p></div>
      <div class="border-2 border-slate-950 bg-orange-50 p-5 shadow-[4px_4px_0_#111827]"><b>Vigilance</b><p class="mt-2 text-sm text-slate-700">Tu évites une erreur.</p></div>
      <div class="border-2 border-slate-950 bg-emerald-50 p-5 shadow-[4px_4px_0_#111827]"><b>Validation</b><p class="mt-2 text-sm text-slate-700">Tu sais si c’est bon.</p></div>
    </div>
  </section>

  {html_sections}

  <section class="mx-auto max-w-7xl bg-white px-4 py-16 sm:px-6 lg:px-8">
    <div class="border-2 border-slate-950 bg-white p-7 shadow-[8px_8px_0_#111827]">
      <div class="mb-5 inline-flex border-2 border-slate-950 bg-violet-600 px-4 py-2 font-mono text-xs font-black uppercase tracking-[.18em] text-white">Sources</div>
      <h2 class="font-display text-4xl font-black text-slate-950 sm:text-6xl">Les liens à garder.</h2>
      <p class="mt-5 max-w-3xl text-lg leading-8 text-slate-700">Ces liens servent aux élèves qui veulent vérifier une commande ou reprendre l’installation depuis une source officielle.</p>
      <p class="mt-3 max-w-3xl border-l-4 border-blue-600 pl-4 text-sm font-semibold leading-6 text-slate-700">Prix vérifiés le 3 juin 2026 sur le Help Center Claude : Pro 20 $/mois US, Max 5x 100 $/mois, Max 20x 200 $/mois. Les prix peuvent changer selon la région, les taxes et les décisions d’Anthropic.</p>
      <div class="mt-8">{source_table()}</div>
    </div>
  </section>

  <div id="egg" class="pointer-events-none fixed bottom-5 left-1/2 z-[80] hidden -translate-x-1/2 border-2 border-slate-950 bg-white px-5 py-3 font-mono text-sm font-black shadow-[6px_6px_0_#111827]">Tu avances bien : petite étape, vraie vérification.</div>

  <script>
    const progress = document.getElementById('progress');
    const reveals = document.querySelectorAll('.reveal');
    const io = new IntersectionObserver((entries) => {{
      entries.forEach((entry) => {{ if (entry.isIntersecting) entry.target.classList.add('visible'); }});
    }}, {{ threshold: 0.12 }});
    reveals.forEach((el) => io.observe(el));
    function updateProgress() {{
      const h = document.documentElement;
      progress.style.transform = `scaleX(${{h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight)}})`;
    }}
    document.addEventListener('scroll', updateProgress, {{ passive: true }});
    updateProgress();
    document.querySelectorAll('.copy-btn').forEach((btn) => {{
      btn.addEventListener('click', async () => {{
        const code = btn.parentElement.querySelector('code').innerText;
        await navigator.clipboard.writeText(code);
        btn.classList.add('copied');
        const old = btn.innerText;
        btn.innerText = 'Copié';
        setTimeout(() => {{ btn.innerText = old; btn.classList.remove('copied'); }}, 1100);
      }});
    }});
    let logoClicks = 0;
    document.querySelector('nav img').addEventListener('click', () => {{
      logoClicks += 1;
      if (logoClicks >= 5) {{
        const egg = document.getElementById('egg');
        egg.classList.remove('hidden');
        setTimeout(() => egg.classList.add('hidden'), 2400);
        logoClicks = 0;
      }}
    }});
  </script>
</body>
</html>"""


if __name__ == "__main__":
    html = render()
    OUT.write_text(html, encoding="utf-8")
    INDEX_OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.name} and {INDEX_OUT.name}: {html.count('<section')} sections, {html.count('<img ')} images")
