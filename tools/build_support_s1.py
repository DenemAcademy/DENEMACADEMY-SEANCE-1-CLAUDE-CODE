from __future__ import annotations

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "support-technique-seance-01.html"
INDEX_OUT = ROOT / "index.html"

DOCS = {
    "overview": "https://code.claude.com/docs/en/overview",
    "setup": "https://code.claude.com/docs/en/quickstart",
    "cli": "https://code.claude.com/docs/en/cli-usage",
    "memory": "https://code.claude.com/docs/en/memory",
    "settings": "https://code.claude.com/docs/en/settings",
    "security": "https://code.claude.com/docs/en/security",
    "workflows": "https://code.claude.com/docs/en/common-workflows",
    "troubleshooting": "https://code.claude.com/docs/en/troubleshooting",
    "desktop": "https://code.claude.com/docs/en/desktop-quickstart",
    "ide": "https://code.claude.com/docs/en/ide-integrations",
    "mcp": "https://code.claude.com/docs/en/mcp",
    "github": "https://code.claude.com/docs/en/github-actions",
    "sdk": "https://code.claude.com/docs/en/agent-sdk/overview",
    "hooks": "https://code.claude.com/docs/en/hooks",
    "node": "https://nodejs.org/en/download",
    "npm": "https://docs.npmjs.com/",
    "plans": "https://support.claude.com/en/articles/11049762-choosing-a-claude-ai-plan",
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
    "install-claude-command.png": ("Commande d’installation", "Installation officielle de Claude Code."),
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

# Final narrative used by the renderer. It follows one beginner-friendly business example from start to finish.
CHAPTERS = [
    (
        "Acte 1 - Avant même d’installer",
        "Le point de départ est simple : comprendre ce que Claude Code va faire dans un vrai dossier.",
        "Découverte",
        "blue",
        [
            ("Le moment où tout est encore flou", "Au début, Claude Code peut sembler abstrait. L’idée à retenir est simple : vous allez parler à Claude dans un dossier précis de votre ordinateur. Le fil rouge sera une page vitrine pour un restaurant fictif, Le Comptoir Bleu, parce que tout le monde comprend ce qu’un restaurant doit montrer : nom, horaires, menu, adresse, bouton de réservation.", "Gardez cette phrase comme point de départ : `Je vais créer une page simple pour Le Comptoir Bleu, étape par étape.` Ne cherchez pas encore à faire beau. Cherchez seulement à comprendre le chemin.", "Vous savez quel projet vous allez suivre pendant toute la séance."),
            ("Le rôle réel de Claude Code", "Claude Code n’est pas seulement une fenêtre où l’on pose des questions. Il peut lire le dossier, créer des fichiers, modifier une page, expliquer une erreur et vous dire ce qui a changé. Sur le terrain, c’est utile quand vous devez avancer vite sur une page, un script ou une correction sans tout copier-coller à la main.", "Expliquez l’outil avec vos mots : `Claude Code travaille dans mon dossier et m’aide à produire un résultat que je peux ouvrir.` Cette phrase suffit pour démarrer.", "Vous ne confondez pas une réponse dans un chat avec une action dans un dossier."),
            ("La différence avec ChatGPT", "ChatGPT aide surtout à réfléchir, expliquer, reformuler ou préparer un plan. Claude Code sert quand il faut toucher de vrais fichiers. Pour Le Comptoir Bleu, ChatGPT pourrait proposer le texte du restaurant, mais Claude Code peut créer `index.html`, modifier le bouton, ajouter une section horaires et vous dire quels fichiers ont bougé.", "Retenez une règle terrain : réflexion seule = chat classique ; fichier à créer ou corriger = Claude Code. Ce réflexe évite de perdre du temps.", "Vous savez pourquoi Claude Code devient utile dès qu’un fichier doit exister."),
            ("Le résultat final de la séance", "À la fin, vous ne devez pas seulement avoir lu des explications. Vous devez savoir installer Claude Code, ouvrir un dossier propre, demander une première page, vérifier le rendu, corriger une erreur simple et préparer un lien partageable. L’exemple du restaurant sert de support, mais la méthode pourra servir tous les jours.", "Notez le résultat final attendu : `une page simple pour Le Comptoir Bleu, consultable dans un navigateur, avec un résumé clair des fichiers créés`.", "Vous savez où la séance veut vous emmener."),
            ("Le dossier devient votre zone de travail", "Claude Code travaille là où vous le lancez. C’est un détail très important. Si vous le lancez dans le mauvais dossier, il peut regarder les mauvais fichiers, créer une page au mauvais endroit ou modifier quelque chose qui ne concerne pas la séance.", "Avant chaque session, prenez l’habitude de regarder le nom du dossier affiché dans le terminal. Sur le terrain, ce petit contrôle évite beaucoup de problèmes.", "Vous comprenez pourquoi le dossier actif passe avant le prompt."),
            ("Le contrôle reste dans vos mains", "Claude Code peut aller vite, mais il ne doit pas décider seul. Vous gardez trois responsabilités : expliquer ce que vous voulez, lire ce qu’il propose, puis ouvrir le résultat. Même si la réponse paraît propre, il faut vérifier la page comme une vraie personne qui visite le site du restaurant.", "Répétez la boucle : `je demande, Claude propose, je vérifie, puis je corrige.` Elle servira dans presque toutes les sections.", "Vous ne cliquez pas sur accepter sans comprendre le geste."),
            ("Le vocabulaire minimal", "Il y a quelques mots à connaître. Le terminal sert à taper des commandes. Le dossier contient le projet. Un fichier est une pièce du projet, par exemple `index.html`. Une commande lance une action, par exemple `claude`. Un diff montre les lignes modifiées.", "Gardez ces mots dans une note. Si un mot vous bloque, ne sautez pas l’étape : demandez à Claude Code de l’expliquer avec une phrase simple.", "Vous avez les mots de base pour suivre sans vous perdre."),
            ("Le piège du copier-coller", "Quand on débute, on copie souvent du code depuis un chat, puis on colle dans un fichier. Ça peut marcher, mais c’est lent et fragile. Claude Code réduit ce travail parce qu’il peut créer le fichier directement dans le dossier, puis vous expliquer ce qu’il a fait.", "Quand vous voyez un bloc de code long, posez-vous la question : `est-ce que je dois vraiment copier cela à la main, ou est-ce que Claude Code peut créer le fichier ?`", "Vous voyez le gain concret de l’outil."),
            ("Le rythme de travail à garder", "La bonne vitesse n’est pas de tout demander en une fois. La bonne vitesse, c’est une petite demande, un résultat visible, puis une correction. Pour Le Comptoir Bleu, on va d’abord créer une page très simple, puis seulement ensuite améliorer les textes, le bouton, les horaires et la version mobile.", "Découpez toujours : une action, une vérification. Si vous mélangez dix demandes, vous ne saurez plus laquelle a créé le problème.", "Vous savez avancer sans transformer la séance en brouillard."),
            ("La première feuille de route", "La suite est volontairement progressive : installer, créer le dossier, lancer Claude Code, produire la page, améliorer la page, contrôler, puis livrer. Chaque étape s’appuie sur la précédente. Si une étape n’est pas claire, il vaut mieux s’arrêter deux minutes que continuer avec une base fragile.", "Gardez le plan ouvert. Votre objectif n’est pas de tout mémoriser, mais de savoir quoi faire ensuite.", "Vous êtes prêt à passer à l’installation sans brûler les étapes."),
        ],
    ),
    (
        "Acte 2 - Installer sans se perdre",
        "La machine doit être prête avant de créer la page du restaurant.",
        "Installation",
        "cyan",
        [
            ("Le compte Claude à prévoir", "Claude Code utilise votre accès Claude. Selon le compte, le plan et l’organisation, les limites peuvent changer. Pour une première séance, l’important est de savoir avec quel compte vous allez vous connecter et de ne pas mélanger compte personnel, compte client et clé API.", "Ouvrez Claude dans le navigateur et vérifiez que vous pouvez vous connecter. Gardez la même adresse email pour la suite.", "Vous savez quel compte servira à lancer Claude Code."),
            ("Le budget expliqué simplement", "Les plans peuvent changer avec le temps, donc il faut toujours vérifier la page officielle. Au 3 juin 2026, le Help Center liste Pro à 20 $/mois aux États-Unis, Max 5x à 100 $/mois et Max 20x à 200 $/mois. Pro peut suffire pour apprendre ; Max devient utile si vous travaillez souvent et que les limites vous coupent en pleine session.", "Avant de payer plus, observez votre usage réel. Tip terrain : on ne choisit pas un plan parce qu’il a l’air plus sérieux, on le choisit parce qu’il fait gagner du temps tous les jours.", "Vous savez relier le prix à un besoin réel."),
            ("L’abonnement n’est pas l’API", "C’est une confusion fréquente. L’abonnement sert à utiliser Claude et Claude Code avec votre compte. L’API sert quand une application appelle Claude automatiquement. Pour créer la page du Comptoir Bleu dans votre terminal, vous n’avez pas besoin de publier une clé API.", "Retenez cette phrase : `abonnement = je travaille avec Claude ; API = un logiciel appelle Claude.` Ne mettez jamais une clé API dans une page, une capture ou un dépôt public.", "Vous ne confondez pas usage direct et usage automatisé."),
            ("Le terminal, sans panique", "Le terminal est juste une zone où vous tapez des commandes. Il peut impressionner au début, mais dans cette séance on utilise très peu de commandes. Vous allez surtout taper `claude`, vérifier un chemin et lire quelques messages.", "Ouvrez le terminal de votre système. Sur Mac, ce sera souvent Terminal. Sur Windows, ce sera PowerShell, CMD, Git Bash ou WSL selon votre installation.", "Vous avez un terminal ouvert et vous savez lequel vous utilisez."),
            ("La commande officielle d’installation", "La documentation Claude Code recommande l’installation native. Sur macOS, Linux ou WSL, la commande officielle est `curl -fsSL https://claude.ai/install.sh | bash`. Sur Windows PowerShell, la commande est `irm https://claude.ai/install.ps1 | iex`. Sur Windows CMD, la route est différente, donc il faut bien regarder le terminal utilisé.", "Copiez la commande depuis la documentation officielle au moment de l’installation. Tip terrain : ne copiez pas une commande trouvée dans un ancien message si la page officielle dit autre chose.", "Vous installez Claude Code avec une source récente."),
            ("Windows demande plus d’attention", "Sur Windows, beaucoup d’erreurs viennent du mauvais terminal. Si vous êtes dans PowerShell, certaines commandes CMD ne passent pas. Si vous êtes dans CMD, certaines commandes PowerShell ne passent pas. La doc donne les symptômes pour reconnaître l’erreur.", "Regardez le début de la ligne : `PS C:\\` indique PowerShell. Une ligne sans `PS` indique plutôt CMD. Si vous utilisez WSL, gardez WSL pour toute la séance.", "Vous ne mélangez pas les routes Windows."),
            ("La version qui rassure", "Après l’installation, il faut une preuve simple. La preuve n’est pas `je pense que c’est installé`. La preuve, c’est une commande qui répond. Si `claude --version` affiche une version, Claude Code est bien trouvé par votre terminal.", "Tapez `claude --version`. Si la commande ne répond pas, ne continuez pas la création de page. Corrigez d’abord l’installation.", "La commande Claude Code répond dans le terminal."),
            ("La première connexion", "Au premier lancement, Claude Code peut ouvrir une connexion ou vous donner un lien. C’est normal. L’objectif est de relier le terminal au bon compte Claude pour que l’outil puisse travailler dans votre session.", "Tapez `claude`. Suivez les instructions de connexion. Une fois connecté, revenez au terminal et attendez que la session démarre.", "Claude Code démarre avec le bon compte."),
            ("Le diagnostic avant de paniquer", "Si quelque chose bloque, il ne faut pas lancer dix commandes au hasard. Claude Code propose `claude doctor` pour diagnostiquer l’installation. Si Claude Code démarre déjà, la commande `/doctor` dans la session peut aussi aider.", "En cas de problème, copiez le message exact, puis lancez `claude doctor` si possible. Tip terrain : une erreur exacte vaut mieux qu’une explication approximative.", "Vous avez une méthode simple pour diagnostiquer."),
            ("Node et npm comme repères", "La route officielle actuelle n’oblige pas forcément à installer via npm, mais Node et npm restent utiles dans beaucoup de projets web. Vous les verrez souvent pour lancer un build, installer une dépendance ou comprendre une ancienne installation.", "Tapez `node -v` puis `npm -v` si vous travaillez sur un projet web. Si une commande ne répond pas, notez-le, mais ne mélangez pas ce diagnostic avec l’installation native de Claude Code.", "Vous savez à quoi servent Node et npm sans les confondre avec Claude Code."),
        ],
    ),
    (
        "Acte 3 - Le dossier du Comptoir Bleu",
        "Le projet commence vraiment quand le dossier est clair.",
        "Dossier",
        "cyan",
        [
            ("Le dossier où tout commence", "On crée maintenant l’espace de travail du restaurant. Ce dossier doit contenir seulement ce qui concerne Le Comptoir Bleu. Pas d’anciens tests, pas de captures privées, pas de fichiers clients.", "Créez un dossier nommé `restaurant-comptoir-bleu`. Mettez-le à un endroit simple, par exemple le bureau ou un dossier formation.", "Le dossier existe et son nom est facile à reconnaître."),
            ("Le chemin à vérifier", "Le chemin indique où se trouve le terminal. Si le terminal n’est pas dans `restaurant-comptoir-bleu`, Claude Code ne travaillera pas au bon endroit. C’est une des erreurs les plus courantes au début.", "Entrez dans le dossier avec `cd`, puis vérifiez avec `pwd` sur Mac/Linux/WSL. Sur Windows, vous pouvez aussi regarder le chemin affiché par le terminal.", "Le terminal pointe vers le dossier du restaurant."),
            ("La session Claude Code au bon endroit", "Une fois dans le bon dossier, la commande `claude` lance la session. À partir de ce moment, les demandes doivent rester liées au restaurant. On ne parle pas encore de publication ou de design avancé.", "Tapez `claude` depuis le dossier `restaurant-comptoir-bleu`.", "La session démarre dans le bon dossier."),
            ("La première demande sans modifier", "Avant de créer quoi que ce soit, demandez à Claude Code de regarder le contexte. Cette étape rassure : vous vérifiez qu’il ne part pas dans un autre dossier et qu’il comprend que le projet est vide ou presque.", "Demandez : `Dis-moi dans quel dossier tu travailles et ce que tu vois. Ne modifie aucun fichier.`", "Claude répond sans créer de fichier."),
            ("La note de projet", "Même un petit projet gagne à avoir une note. Elle peut expliquer l’objectif : créer une page simple pour un restaurant fictif. Cette note aide à reprendre plus tard et donne un contexte clair à Claude Code.", "Demandez : `Crée un README.md très simple qui explique le projet Le Comptoir Bleu et comment ouvrir la page quand elle existera.`", "Un fichier `README.md` apparaît avec une explication courte."),
            ("Le fichier de règles simples", "Pour une première séance, un fichier `CLAUDE.md` peut donner les règles du projet. Pas besoin de faire compliqué. Il peut dire : français simple, page HTML, fond blanc, bleu/violet, vérifier mobile, ne pas ajouter de dépendances sans demander.", "Demandez : `Crée un CLAUDE.md avec les règles simples du projet. Garde des phrases courtes.`", "Claude Code a un cadre clair pour la suite."),
            ("La liste des fichiers attendus", "Avant de construire, il faut savoir ce qu’on veut. Pour commencer, un seul fichier `index.html` suffit. Plus tard, on pourra séparer CSS et JS, mais ce n’est pas nécessaire au premier contact.", "Demandez à Claude Code de proposer une structure minimale de fichiers pour la première version, sans créer encore la page.", "Vous savez quels fichiers seront créés."),
            ("Le moment de dire non", "Si Claude Code propose trop de fichiers, une architecture compliquée ou un framework, dites non pour cette séance. Le but n’est pas de faire un site complexe. Le but est de comprendre le flux complet.", "Répondez : `Pour cette première version, reste sur un index.html simple. Pas de framework.`", "La base reste adaptée à un début."),
            ("Le premier état du dossier", "Avant de créer la page, le dossier doit être lisible. Vous devez voir le README, le CLAUDE.md et rien de confus. Ce contrôle prépare la suite.", "Demandez : `Liste les fichiers présents et explique leur rôle en une phrase chacun.`", "Vous comprenez chaque fichier du dossier."),
            ("La sécurité du projet", "Même dans un exercice simple, prenez de bonnes habitudes. Ne mettez pas de mot de passe, de clé API ou de vraie donnée client dans le dossier. Le restaurant est fictif, donc tout peut rester public.", "Ajoutez dans CLAUDE.md : `Ne jamais ajouter de secret, clé API, token ou donnée privée.`", "Le projet peut être partagé sans risque évident."),
        ],
    ),
    (
        "Acte 4 - La première page apparaît",
        "La page du restaurant naît dans le dossier, puis se vérifie dans le navigateur.",
        "Création",
        "violet",
        [
            ("La demande la plus simple", "On ne demande pas encore un site parfait. On demande une page visible. Le restaurant doit avoir un nom, une phrase d’accueil, quelques plats, des horaires et un bouton de réservation. C’est assez pour apprendre.", "Demandez : `Crée index.html pour Le Comptoir Bleu. Fais une page simple avec nom, accroche, menu court, horaires, adresse fictive et bouton Réserver.`", "Le fichier `index.html` est créé."),
            ("La liste des changements", "Après création, ne vous contentez pas d’un message positif. Vous devez savoir quels fichiers ont été créés ou modifiés. C’est une habitude de travail essentielle.", "Demandez : `Liste les fichiers créés ou modifiés et résume ce que tu as mis dedans.`", "Vous savez exactement ce qui a changé."),
            ("La page ouverte dans le navigateur", "Un fichier HTML doit être ouvert. Le terminal ne suffit pas. Une page peut être techniquement créée, mais illisible, mal cadrée ou vide.", "Ouvrez `index.html` dans votre navigateur. Si vous utilisez Claude Desktop, ouvrez l’aperçu si disponible.", "Vous voyez la première page du Comptoir Bleu."),
            ("Le premier regard utilisateur", "Regardez la page comme une personne qui cherche un restaurant. Est-ce que le nom est clair ? Est-ce qu’on comprend ce qu’on peut faire ? Est-ce que le bouton se voit ? Ce regard vaut plus qu’un long discours technique.", "Notez trois choses : ce qui est clair, ce qui manque, ce qui gêne.", "Vous avez une première liste de correction."),
            ("Le prompt de correction courte", "La première correction doit être précise. Ne dites pas seulement `améliore la page`. Dites ce qui doit changer : titre plus clair, bouton plus visible, menu plus lisible.", "Demandez : `Améliore seulement le haut de page : titre plus clair, phrase courte, bouton Réserver plus visible. Ne touche pas au reste.`", "Une zone précise a été améliorée."),
            ("Le bouton Réserver", "Dans une page business, le bouton principal doit être visible rapidement. Ici, il ne réserve pas vraiment, mais il montre l’action attendue. C’est un réflexe terrain : une page doit guider vers une action.", "Demandez : `Rends le bouton Réserver visible au premier écran et ajoute un lien vers la section contact.`", "Le bouton mène à une zone utile de la page."),
            ("Le menu court", "Un menu trop long fatigue. Pour une première page, trois plats suffisent. L’objectif est de comprendre la structure, pas de faire une vraie carte complète.", "Demandez : `Garde seulement trois plats dans le menu, avec une phrase simple et un prix fictif.`", "Le menu devient lisible en quelques secondes."),
            ("Les horaires faciles à trouver", "Un visiteur cherche vite les horaires. Si l’information est cachée, la page perd son utilité. Claude Code peut réorganiser la page pour rendre cette information plus visible.", "Demandez : `Ajoute une section Horaires claire avec semaine, samedi et dimanche. Utilise des horaires fictifs.`", "Les horaires se trouvent sans chercher."),
            ("La section contact", "Une page de restaurant doit donner une adresse, un téléphone fictif et un moyen de réserver. On ne cherche pas la perfection, on cherche une page complète.", "Demandez : `Ajoute une section Contact avec adresse fictive, téléphone fictif et rappel du bouton Réserver.`", "La page répond aux besoins de base."),
            ("La première sauvegarde mentale", "À ce stade, vous avez déjà fait le cycle complet : demander, créer, ouvrir, corriger. C’est le cœur de Claude Code. Le reste de la séance va rendre ce cycle plus propre et plus fiable.", "Demandez un résumé : `Explique en 5 lignes ce qui existe maintenant et ce qui reste à améliorer.`", "Vous pouvez expliquer le chemin parcouru."),
        ],
    ),
    (
        "Acte 5 - Le contenu devient utile",
        "La page commence à parler comme une vraie page de commerce local.",
        "Contenu",
        "green",
        [
            ("Le nom qui reste en tête", "Le nom Le Comptoir Bleu doit être visible et répété aux bons endroits. Un visiteur doit savoir immédiatement où il est. Ce n’est pas un détail de design, c’est une base de compréhension.", "Demandez : `Vérifie que le nom Le Comptoir Bleu est clair dans le titre, le haut de page et le footer.`", "Le nom du restaurant est visible sans effort."),
            ("L’accroche sans phrase creuse", "Une accroche doit dire quelque chose de concret. `Bienvenue sur notre site` n’aide pas beaucoup. Une meilleure phrase peut dire : cuisine maison, quartier calme, déjeuner rapide, réservation simple.", "Demandez : `Remplace l’accroche par une phrase simple qui donne envie de venir déjeuner, sans mots exagérés.`", "L’accroche donne une raison de rester."),
            ("Le client comprend l’offre", "La page doit répondre à trois questions : qu’est-ce que c’est, où est-ce, comment réserver. Si ces trois réponses sont visibles, la page devient utile même avec un design simple.", "Demandez : `Réorganise les premières sections pour répondre vite à : quoi, où, comment réserver.`", "La page devient plus logique."),
            ("Les plats qui racontent le lieu", "Les plats ne sont pas là pour remplir. Ils donnent une ambiance. Trois plats bien nommés peuvent suffire à installer l’univers du restaurant.", "Demandez : `Renomme les trois plats avec des noms simples et cohérents avec un bistrot moderne.`", "Le menu paraît plus crédible."),
            ("Les prix fictifs propres", "Un prix fictif doit rester réaliste. Des prix incohérents donnent une impression de faux site. Même dans un exercice, le détail compte.", "Demandez : `Ajoute des prix fictifs réalistes et indique qu’il s’agit d’un exemple de page.`", "Les prix ne cassent pas la crédibilité."),
            ("La confiance en quelques lignes", "Une page business a souvent besoin d’un petit bloc rassurant : cuisine maison, produits de saison, réservation rapide, accueil midi et soir. Ce bloc aide sans faire trop commercial.", "Demandez : `Ajoute un bloc Pourquoi venir ? avec trois raisons courtes et concrètes.`", "La page explique pourquoi choisir ce restaurant."),
            ("Les informations pratiques", "Les visiteurs cherchent souvent l’adresse, les horaires et le téléphone. Ces informations doivent être regroupées. Plus c’est simple, plus la page est utile.", "Demandez : `Regroupe horaires, adresse et téléphone dans une section Informations pratiques.`", "Les informations importantes sont ensemble."),
            ("Le style juste", "Le texte doit rester simple. Trop de mots marketing font perdre confiance. Dans cette séance, on préfère des phrases courtes, naturelles, faciles à comprendre.", "Demandez : `Relis tous les textes et retire les phrases trop vagues ou trop commerciales.`", "Le texte paraît plus humain."),
            ("Le footer qui finit proprement", "Le footer n’est pas la partie la plus visible, mais il termine la page. Il peut rappeler le nom, l’adresse fictive et un lien vers le haut ou la réservation.", "Demandez : `Ajoute un footer simple avec le nom du restaurant, l’adresse fictive et un lien Réserver.`", "La page a une vraie fin."),
            ("La page relue comme un client", "Maintenant, relisez sans penser au code. Imaginez que vous cherchez un restaurant pour ce soir. Si vous trouvez vite les informations, la page fait son travail.", "Demandez à Claude Code : `Donne une checklist de lecture côté visiteur, pas côté développeur.`", "Vous vérifiez l’utilité réelle de la page."),
        ],
    ),
    (
        "Acte 6 - Le rendu devient propre",
        "La page doit rester simple, mais elle doit être lisible et sérieuse.",
        "Design",
        "violet",
        [
            ("Le fond blanc qui calme la page", "Un fond blanc aide à lire. Le bleu et le violet servent de repères, pas de décoration partout. Pour une première séance, le design doit rester propre et sérieux.", "Demandez : `Garde le fond blanc. Utilise bleu et violet seulement pour les boutons, badges ou petits accents.`", "La page respire mieux."),
            ("Les espaces qui changent tout", "Un site paraît vite amateur si tout est collé. Les marges, les espacements et les tailles de texte font une grande différence, même sans design compliqué.", "Demandez : `Améliore les espacements entre les sections et rends les titres plus lisibles.`", "La page devient plus agréable à parcourir."),
            ("Le bouton qui se voit vraiment", "Le bouton Réserver est l’action principale. Il doit ressortir, mais sans devenir agressif. Un bouton visible, bien placé, aide le visiteur à comprendre quoi faire.", "Demandez : `Rends le bouton Réserver plus visible avec un style bleu, mais garde un rendu professionnel.`", "L’action principale se repère vite."),
            ("La version mobile révèle les problèmes", "Beaucoup de personnes verront une page de restaurant sur téléphone. Si le menu déborde ou si le bouton est trop petit, la page perd son intérêt.", "Réduisez la fenêtre du navigateur ou utilisez l’aperçu mobile. Demandez : `Corrige les problèmes visibles sur mobile.`", "La page reste lisible sur téléphone."),
            ("Les images sans se tromper", "Une image peut aider, mais une mauvaise image peut rendre la page confuse. Pour cette séance, mieux vaut une image simple ou un bloc visuel propre plutôt qu’une photo prise au hasard.", "Demandez : `Si tu ajoutes une image, utilise une image propre et cohérente avec un restaurant, sinon garde un bloc visuel simple.`", "L’image n’écrase pas le contenu."),
            ("Les couleurs cohérentes", "Une page avec trop de couleurs paraît désordonnée. Pour Le Comptoir Bleu, une palette simple suffit : blanc, texte sombre, bleu, violet léger, gris clair.", "Demandez : `Uniformise les couleurs et évite d’ajouter de nouvelles teintes inutiles.`", "La page paraît plus stable."),
            ("Les textes qui ne débordent pas", "Un titre long ou un prix mal placé peut casser la mise en page. Claude Code doit vérifier que les blocs restent propres sur plusieurs largeurs.", "Demandez : `Vérifie que les titres, boutons et cartes ne débordent pas sur mobile.`", "Aucun élément important ne sort de son cadre."),
            ("Les liens qui se comprennent", "Un lien doit dire où il mène. `Cliquez ici` est moins clair que `Voir les horaires` ou `Réserver une table`. Ce détail aide beaucoup en usage réel.", "Demandez : `Renomme les liens pour qu’ils expliquent clairement l’action.`", "Chaque lien annonce son rôle."),
            ("Le contraste avant le style", "Un joli bouton qui se lit mal est un mauvais bouton. Le contraste entre texte et fond doit rester fort, surtout pour les éléments d’action.", "Demandez : `Vérifie le contraste des boutons et des textes importants.`", "Les éléments importants restent lisibles."),
            ("La page sans surdesign", "Au début, il est tentant de demander beaucoup d’effets. Mais une page business simple doit d’abord être claire. Les animations peuvent venir après, seulement si elles n’empêchent pas la lecture.", "Demandez : `Garde seulement des micro-interactions légères : hover sur les boutons, apparition douce, rien de distrayant.`", "La page reste sérieuse et fluide."),
        ],
    ),
    (
        "Acte 7 - Le contrôle de Claude Code",
        "Vous apprenez à vérifier l’outil au lieu de lui faire confiance trop vite.",
        "Contrôle",
        "orange",
        [
            ("Le plan avant la grosse correction", "Quand une demande devient large, il faut demander un plan. Sinon, Claude Code peut modifier trop de choses à la fois. Le plan vous permet de dire oui ou non avant que les fichiers changent.", "Demandez : `Avant de modifier, propose un plan en 5 étapes pour améliorer la page.`", "Vous validez la direction avant l’action."),
            ("Les permissions qui protègent", "Claude Code peut demander l’autorisation pour certaines actions. Ce n’est pas une gêne, c’est une protection. Au début, gardez un mode où vous voyez les modifications importantes.", "Si Claude Code demande une permission, lisez le fichier ou la commande concernée avant d’accepter.", "Vous savez pourquoi l’outil vous demande confirmation."),
            ("Le diff à lire calmement", "Le diff montre les lignes ajoutées et supprimées. Même si vous ne comprenez pas tout le code, vous pouvez regarder les titres, les textes, les sections et les fichiers concernés.", "Demandez : `Montre-moi un résumé des changements fichier par fichier.`", "Vous savez ce qui a été modifié."),
            ("Le danger des commandes rapides", "Une commande peut installer, supprimer, renommer ou publier. Il faut savoir ce qu’elle fait. Ne lancez pas une commande juste parce qu’elle ressemble à une solution.", "Demandez : `Explique cette commande en français simple avant de la lancer.`", "Vous ne lancez pas une action opaque."),
            ("L’erreur copiée exactement", "Quand une erreur apparaît, ne la reformulez pas trop vite. Copiez le message exact. Claude Code peut mieux aider avec le vrai texte de l’erreur qu’avec une description floue.", "Copiez l’erreur complète et demandez : `Explique ce message et propose une seule correction prudente.`", "La correction part d’une information fiable."),
            ("Le moment de réduire la demande", "Si Claude Code part dans tous les sens, ce n’est pas forcément grave. Il faut simplement réduire la tâche. Une demande plus petite est souvent plus efficace.", "Écrivez : `Stop. On corrige seulement le bouton Réserver. Ne touche pas aux autres sections.`", "La session revient sur une action contrôlable."),
            ("Le dossier vérifié avec Git", "Git permet de voir les fichiers modifiés. Même au niveau débutant, `git status` donne une information précieuse : quels fichiers ont changé et quels fichiers ne sont pas encore suivis.", "Tapez `git status` si le projet est dans Git, ou demandez à Claude Code de vous expliquer comment l’utiliser.", "Vous connaissez l’état des fichiers."),
            ("La session qui devient trop longue", "Une conversation peut devenir lourde ou confuse. Claude Code propose des commandes comme `/clear` ou `/compact`. Elles aident à repartir proprement ou à garder seulement l’essentiel.", "Si la session devient confuse, demandez d’abord un résumé, puis utilisez `/compact` ou `/clear` selon le besoin.", "Vous ne laissez pas le contexte devenir un problème."),
            ("Le fichier CLAUDE.md qui aide", "Le fichier CLAUDE.md garde les règles du projet. Pour Le Comptoir Bleu, il peut rappeler : page simple, restaurant fictif, pas de données privées, fond blanc, bleu/violet, vérifier mobile.", "Demandez : `Mets à jour CLAUDE.md avec les règles finales du projet.`", "Les prochaines demandes restent mieux cadrées."),
            ("La vérification qui ne se délègue pas", "Claude Code peut aider à vérifier, mais il ne remplace pas votre regard. Vous devez ouvrir la page, cliquer les liens, lire les textes et regarder le mobile. C’est le vrai contrôle.", "Demandez une checklist, puis faites-la vraiment point par point.", "Vous validez avec vos yeux, pas seulement avec la réponse de l’outil."),
        ],
    ),
    (
        "Acte 8 - Le lien final et la méthode du quotidien",
        "Le projet se termine avec une page vérifiée et une méthode réutilisable.",
        "Livraison",
        "green",
        [
            ("La dernière lecture complète", "Avant de publier, relisez la page du haut vers le bas. Le but n’est pas de tout changer. Le but est de repérer les fautes visibles, les informations manquantes et les sections qui se répètent.", "Demandez : `Relis la page comme un visiteur et liste les 5 corrections les plus utiles.`", "Vous avez une dernière liste courte."),
            ("La checklist de livraison", "Une checklist évite de publier trop tôt. Pour Le Comptoir Bleu, elle peut vérifier : nom visible, bouton réservation, menu, horaires, contact, mobile, liens, pas de secret.", "Demandez à Claude Code de créer une checklist finale dans `README.md`.", "La livraison se contrôle point par point."),
            ("Le test local", "La page doit s’ouvrir sur votre machine avant de partir en ligne. Si elle ne marche pas localement, la publication ne réglera pas le problème.", "Ouvrez `index.html` dans le navigateur, puis testez aussi en réduisant la fenêtre.", "La page fonctionne en local."),
            ("Le commit qui raconte le travail", "Un commit sert à garder une trace. Le message doit être court et clair. Pas besoin de raconter toute la séance, seulement le changement principal.", "Si Git est prêt, faites un commit du type : `Créer page restaurant Comptoir Bleu`.", "L’historique explique ce qui a été fait."),
            ("La publication GitHub Pages", "GitHub Pages permet d’obtenir un lien consultable. C’est utile pour partager une page simple sans installer de serveur. Il faut seulement pousser les bons fichiers dans le bon dépôt.", "Demandez à Claude Code de vous expliquer les étapes GitHub Pages avant de les faire.", "Vous savez comment le lien public sera créé."),
            ("Le lien qui se vérifie vraiment", "Après publication, ouvrez le lien final dans un navigateur. Ne supposez pas que tout marche parce que le push a réussi. GitHub Pages peut mettre quelques secondes ou minutes à publier.", "Ouvrez l’URL publique et vérifiez le haut de page, le menu, le bouton et la section contact.", "La page publiée correspond à la page locale."),
            ("Le résumé pour une autre personne", "Quand vous livrez une page, même simple, il faut expliquer ce qui existe. Un résumé clair aide à reprendre ou à montrer le travail.", "Demandez : `Rédige un résumé de livraison en 6 lignes : objectif, fichiers, lien, vérifications, limites, prochaine action.`", "Quelqu’un peut comprendre le projet sans ouvrir toute la session."),
            ("La méthode à refaire demain", "Le vrai apprentissage n’est pas seulement la page du restaurant. C’est la méthode : dossier propre, demande claire, résultat visible, correction courte, vérification, livraison.", "Copiez cette méthode dans vos notes. Elle servira pour une page artisan, une page coach, une page service ou un mini-outil interne.", "Vous pouvez refaire le parcours sur un autre projet."),
            ("Le réflexe business quotidien", "Claude Code devient utile tous les jours quand vous l’utilisez pour de petites tâches concrètes : corriger une page, améliorer un bouton, créer une checklist, résumer des fichiers, préparer une livraison.", "Chaque jour, choisissez une tâche courte et demandez un résultat vérifiable. Tip terrain : une tâche de 15 minutes bien cadrée vaut mieux qu’une demande géante.", "L’outil devient un réflexe de travail, pas un gadget."),
            ("La suite logique", "La première séance se termine ici : vous savez ce qu’est Claude Code, comment l’installer, comment lancer une session, comment créer une page simple et comment vérifier. La suite pourra aller plus loin, mais la base est déjà là.", "Gardez Le Comptoir Bleu comme projet d’entraînement. Vous pourrez l’améliorer plus tard avec images, formulaire, SEO ou déploiement plus propre.", "Vous avez un parcours complet du premier terminal au lien final."),
        ],
    ),
]


def e(text: str) -> str:
    return escape(text, quote=True)


def public_copy(html: str) -> str:
    replacements = [
        ("Support élèves", "Support formation"),
        ("Support technique pour les élèves", "Support technique pour vous"),
        ("Message élève", "Message pour vous"),
        ("Action élève", "Action à faire"),
        ("Ce que tu fais", "Ce que vous faites"),
        ("Comment tu vérifies", "Comment vous vérifiez"),
        ("Question à te poser", "Question à vous poser"),
        ("Consigne simple pour toi", "Consigne simple pour vous"),
        ("Ce support est fait pour toi", "Ce support est fait pour vous"),
        ("pour les élèves", "pour vous"),
        ("aux élèves", "à vous"),
        ("des élèves", "des participants"),
        ("les élèves", "vous"),
        ("un élève", "une personne"),
        ("Un élève", "Une personne"),
        ("l’élève", "vous"),
        ("L’élève", "Vous"),
        ("élèves", "participants"),
        ("élève", "participant"),
        ("Tu installes", "Vous installez"),
        ("tu installes", "vous installez"),
        ("Tu pratiques", "Vous pratiquez"),
        ("tu pratiques", "vous pratiquez"),
        ("Tu prépares", "Vous préparez"),
        ("tu prépares", "vous préparez"),
        ("Tu pars", "Vous partez"),
        ("tu pars", "vous partez"),
        ("Tu comprends", "Vous comprenez"),
        ("tu comprends", "vous comprenez"),
        ("Tu vérifies", "Vous vérifiez"),
        ("tu vérifies", "vous vérifiez"),
        ("Tu gardes", "Vous gardez"),
        ("tu gardes", "vous gardez"),
        ("Tu évites", "Vous évitez"),
        ("tu évites", "vous évitez"),
        ("Tu acceptes", "Vous acceptez"),
        ("tu acceptes", "vous acceptez"),
        ("Tu lis", "Vous lisez"),
        ("tu lis", "vous lisez"),
        ("Tu sais", "Vous savez"),
        ("tu sais", "vous savez"),
        ("Tu ne confonds", "Vous ne confondez"),
        ("tu ne confonds", "vous ne confondez"),
        ("Tu vois", "Vous voyez"),
        ("tu vois", "vous voyez"),
        ("Tu construis", "Vous construisez"),
        ("tu construis", "vous construisez"),
        ("Tu dois", "Vous devez"),
        ("tu dois", "vous devez"),
        ("Tu ne copies", "Vous ne copiez"),
        ("tu ne copies", "vous ne copiez"),
        ("Tu choisis", "Vous choisissez"),
        ("tu choisis", "vous choisissez"),
        ("Tu demandes", "Vous demandez"),
        ("tu demandes", "vous demandez"),
        ("Tu lui demandes", "Vous lui demandez"),
        ("tu lui demandes", "vous lui demandez"),
        ("Tu ouvres", "Vous ouvrez"),
        ("tu ouvres", "vous ouvrez"),
        ("Tu corriges", "Vous corrigez"),
        ("tu corriges", "vous corrigez"),
        ("Tu fais", "Vous faites"),
        ("tu fais", "vous faites"),
        ("Tu donnes", "Vous donnez"),
        ("tu donnes", "vous donnez"),
        ("Tu sépares", "Vous séparez"),
        ("tu sépares", "vous séparez"),
        ("Tu nommes", "Vous nommez"),
        ("tu nommes", "vous nommez"),
        ("Tu ne mets", "Vous ne mettez"),
        ("tu ne mets", "vous ne mettez"),
        ("Tu diagnostiques", "Vous diagnostiquez"),
        ("tu diagnostiques", "vous diagnostiquez"),
        ("Tu mets", "Vous mettez"),
        ("tu mets", "vous mettez"),
        ("Tu utilises", "Vous utilisez"),
        ("tu utilises", "vous utilisez"),
        ("Tu repars", "Vous repartez"),
        ("tu repars", "vous repartez"),
        ("Tu compacts", "Vous compactez"),
        ("tu compacts", "vous compactez"),
        ("Tu crées", "Vous créez"),
        ("tu crées", "vous créez"),
        ("Tu écris", "Vous écrivez"),
        ("tu écris", "vous écrivez"),
        ("Tu relis", "Vous relisez"),
        ("tu relis", "vous relisez"),
        ("Tu relies", "Vous reliez"),
        ("tu relies", "vous reliez"),
        ("Tu copies", "Vous copiez"),
        ("tu copies", "vous copiez"),
        ("Tu regardes", "Vous regardez"),
        ("tu regardes", "vous regardez"),
        ("Tu ne forces", "Vous ne forcez"),
        ("tu ne forces", "vous ne forcez"),
        ("Tu réduis", "Vous réduisez"),
        ("tu réduis", "vous réduisez"),
        ("Tu expliques", "Vous expliquez"),
        ("tu expliques", "vous expliquez"),
        ("Tu listes", "Vous listez"),
        ("tu listes", "vous listez"),
        ("Tu formules", "Vous formulez"),
        ("tu formules", "vous formulez"),
        ("Tu dis", "Vous dites"),
        ("tu dis", "vous dites"),
        ("Tu poses", "Vous posez"),
        ("tu poses", "vous posez"),
        ("Tu réfléchis", "Vous réfléchissez"),
        ("tu réfléchis", "vous réfléchissez"),
        ("Tu récupères", "Vous récupérez"),
        ("tu récupères", "vous récupérez"),
        ("Tu bloques", "Vous bloquez"),
        ("tu bloques", "vous bloquez"),
        ("Tu changes", "Vous changez"),
        ("tu changes", "vous changez"),
        ("Tu penses", "Vous pensez"),
        ("tu penses", "vous pensez"),
        ("Tu termines", "Vous terminez"),
        ("tu termines", "vous terminez"),
        ("Tu avances", "Vous avancez"),
        ("tu avances", "vous avancez"),
        ("Tu testes", "Vous testez"),
        ("tu testes", "vous testez"),
        ("Tu restes", "Vous restez"),
        ("tu restes", "vous restez"),
        ("Tu décides", "Vous décidez"),
        ("tu décides", "vous décidez"),
        ("Tu proposes", "Vous proposez"),
        ("tu proposes", "vous proposez"),
        ("Tu ranges", "Vous rangez"),
        ("tu ranges", "vous rangez"),
        ("Tu es", "Vous êtes"),
        ("tu es", "vous êtes"),
        ("Tu arrives", "Vous arrivez"),
        ("tu arrives", "vous arrivez"),
        ("Tu suis", "Vous suivez"),
        ("tu suis", "vous suivez"),
        ("Tu peux", "Vous pouvez"),
        ("tu peux", "vous pouvez"),
        ("Tu veux", "Vous voulez"),
        ("tu veux", "vous voulez"),
        ("Tu vas", "Vous allez"),
        ("tu vas", "vous allez"),
        ("Tu touches", "Vous touchez"),
        ("tu touches", "vous touchez"),
        ("Tu paies", "Vous payez"),
        ("tu paies", "vous payez"),
        ("Tu travailles", "Vous travaillez"),
        ("tu travailles", "vous travaillez"),
        ("Tu lances", "Vous lancez"),
        ("tu lances", "vous lancez"),
        ("Tu connectes", "Vous connectez"),
        ("tu connectes", "vous connectez"),
        ("Tu notes", "Vous notez"),
        ("tu notes", "vous notez"),
        ("Tu retrouves", "Vous retrouvez"),
        ("tu retrouves", "vous retrouvez"),
        ("Tu valides", "Vous validez"),
        ("tu valides", "vous validez"),
        ("Tu ne valides", "Vous ne validez"),
        ("tu ne valides", "vous ne validez"),
        ("Tu ne changes", "Vous ne changez"),
        ("tu ne changes", "vous ne changez"),
        ("Tu ne travailles", "Vous ne travaillez"),
        ("tu ne travailles", "vous ne travaillez"),
        ("Tu n’as", "Vous n’avez"),
        ("tu n’as", "vous n’avez"),
        ("Tu n’es", "Vous n’êtes"),
        ("tu n’es", "vous n’êtes"),
        ("Demande-toi", "Demandez-vous"),
        ("demande-toi", "demandez-vous"),
        ("Connecte-toi", "Connectez-vous"),
        ("connecte-toi", "connectez-vous"),
        ("toi-même", "vous-même"),
        ("Toi,", "Vous,"),
        ("toi,", "vous,"),
        ("t’aide", "vous aide"),
        ("t’expliquer", "vous expliquer"),
        ("t’authentifier", "vous authentifier"),
        ("à ta place", "à votre place"),
        ("ton ordinateur", "votre ordinateur"),
        ("ton dossier", "votre dossier"),
        ("ton projet", "votre projet"),
        ("ton terminal", "votre terminal"),
        ("ton installation", "votre installation"),
        ("ton compte", "votre compte"),
        ("ton environnement", "votre environnement"),
        ("ton besoin", "votre besoin"),
        ("ton cas", "votre cas"),
        ("ton usage", "votre usage"),
        ("ton abonnement", "votre abonnement"),
        ("ta machine", "votre machine"),
        ("ta demande", "votre demande"),
        ("ta vérification", "votre vérification"),
        ("Tes commandes", "Vos commandes"),
        ("tes commandes", "vos commandes"),
        ("Tes demandes", "Vos demandes"),
        ("tes demandes", "vos demandes"),
        ("Tes accès", "Vos accès"),
        ("tes accès", "vos accès"),
        ("Tes préférences", "Vos préférences"),
        ("tes préférences", "vos préférences"),
    ]
    for old, new in sorted(replacements, key=lambda pair: len(pair[0]), reverse=True):
        html = html.replace(old, new)
    html = html.replace("vous vous décidez", "vous décidez")
    html = html.replace("Vous vous décidez", "Vous décidez")
    html = html.replace("vous qui travailles", "vous qui travaillez")
    html = html.replace("Vous évites", "Vous évitez")
    html = html.replace("vous évites", "vous évitez")
    html = html.replace("ton simple", "style simple")
    html = re.sub(r"\bTu\b", "Vous", html)
    html = re.sub(r"\btu\b", "vous", html)
    html = re.sub(r"\btoi\b", "vous", html)
    html = re.sub(r"\bToi\b", "Vous", html)
    return html


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
    text = f"{item['title']} {item['story']} {item['action']} {item['check']} {item['tag']}".lower()
    if "clé api" in text or "secret" in text:
        name = "api-key-warning.png"
    elif "api" in text:
        name = "api-vs-subscription.png"
    elif "max 20" in text or "max 5" in text or "prix" in text or "payer" in text or "achat" in text:
        name = "pricing-plans.png"
    elif "limite" in text or "quota" in text or "usage" in text or "reset" in text or "crédit" in text:
        name = "usage-limits.png"
    elif "connect" in text or "authent" in text or "compte" in text or "/login" in text:
        name = "auth-login.png"
    elif "node" in text or "npm -v" in text:
        name = "install-node-npm.png"
    elif "install" in text or "installation" in text or "installer" in text or "claude --version" in text:
        name = "install-claude-command.png"
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
    text = f"{item['title']} {item['story']} {item['action']} {item['check']} {item['tag']}".lower()
    if "sécurité" in text or "clé" in text or "secret" in text:
        return "Qu’est-ce que je dois protéger avant de publier ou partager ?"
    if "api" in text or "abonnement" in text:
        return "Est-ce que je parle d’un usage direct, ou d’un système qui appelle Claude automatiquement ?"
    if "prix" in text or "plan" in text or "quota" in text or "limite" in text:
        return "Est-ce que ce plan répond à mon usage réel, ou est-ce que je paie trop tôt ?"
    if "connect" in text or "authent" in text or "compte" in text:
        return "Est-ce que la session utilise le compte Claude prévu ?"
    if "installation" in text or "node" in text or "npm" in text:
        return "Quelle preuve simple me montre que l’installation marche vraiment ?"
    if "desktop" in text or "interface" in text:
        return "Qu’est-ce que cette interface me permet de mieux contrôler ?"
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
        '<div class="code-panel max-w-full overflow-hidden border-2 border-slate-950 bg-slate-950 text-white shadow-[8px_8px_0_#111827]">'
        '<div class="flex justify-end border-b-2 border-white/20 bg-slate-900 px-3 py-2">'
        '<button type="button" class="copy-btn border-2 border-white bg-white px-3 py-1 text-xs font-black text-slate-950 transition hover:-translate-y-0.5">Copier</button>'
        "</div>"
        '<pre class="max-w-full whitespace-pre-wrap break-words p-5 text-sm leading-7"><code>'
        + e("\n".join(lines))
        + "</code></pre></div>"
    )


def table(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f'<th class="border-2 border-slate-950 bg-blue-100 px-4 py-3 text-left text-xs uppercase tracking-[.14em]">{e(h)}</th>' for h in headers)
    body = ""
    for row in rows:
        body += "<tr>" + "".join(f'<td class="border-2 border-slate-950 bg-white px-4 py-3 align-top text-sm leading-6 text-slate-700">{cell}</td>' for cell in row) + "</tr>"
    return f'<div class="max-w-full min-w-0 overflow-x-auto border-2 border-slate-950 bg-white shadow-[8px_8px_0_#111827]"><table class="w-full min-w-[760px] border-collapse">{head and f"<thead><tr>{head}</tr></thead>"}<tbody>{body}</tbody></table></div>'


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
        ("02", "Ce que vous faites", item["action"], "bg-violet-50"),
        ("03", "Comment vous vérifiez", item["check"], "bg-white"),
        ("04", "Question à vous poser", question_for(item), "bg-cyan-50"),
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
          <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-blue-100">Message pour vous</p>
          <h2 class="mt-4 font-display text-3xl font-black">{e(item["title"])}</h2>
          <p class="mt-4 leading-7 text-blue-50">{e(item["story"])}</p>
        </div>
        <div class="border-2 border-slate-950 bg-white p-7 shadow-[8px_8px_0_#111827] lg:col-span-2">
          <div class="grid gap-4 md:grid-cols-2">
            <div class="border-2 border-slate-950 bg-violet-50 p-5"><p class="font-black">Étape</p><p class="mt-2 text-slate-700">{e(item["action"])}</p></div>
            <div class="border-2 border-slate-950 bg-white p-5"><p class="font-black">Résultat attendu</p><p class="mt-2 text-slate-700">{e(item["check"])}</p></div>
          </div>
          <p class="mt-6 text-lg leading-8 text-slate-700">Lisez cette section comme une consigne de travail. Vous n’avez pas besoin de retenir chaque mot. Vous devez surtout comprendre le geste à faire et le point à vérifier.</p>
          <div class="mt-6 grid gap-6 lg:grid-cols-[.85fr_1.15fr] lg:items-start">
            <div class="border-2 border-slate-950 bg-cyan-50 p-5 shadow-[5px_5px_0_#111827]">
              <p class="font-black text-slate-950">Question à vous poser</p>
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
        <div class="grid gap-0 lg:grid-cols-[minmax(0,.95fr)_minmax(0,1.05fr)]">
          <div class="min-w-0 p-7">
            <h2 class="font-display text-3xl font-black text-slate-950 sm:text-5xl">{e(item["title"])}</h2>
            <p class="mt-5 text-lg leading-8 text-slate-700">{e(item["story"])}</p>
          </div>
          <div class="min-w-0 border-t-2 border-slate-950 p-7 lg:border-l-2 lg:border-t-0">
            {code_block([item["action"], "", "Vérification :", item["check"]])}
          </div>
        </div>
        <div class="grid gap-6 border-t-2 border-slate-950 p-7 lg:grid-cols-[.8fr_1.2fr] lg:items-start">
          <div class="border-2 border-slate-950 bg-cyan-50 p-5 shadow-[5px_5px_0_#111827]">
            <p class="font-black text-slate-950">Question à vous poser</p>
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
            <p class="font-black text-slate-950">Consigne simple pour vous</p>
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
        ["Action à faire", e(item["action"])],
        ["Validation", e(item["check"])],
        ["Question à vous poser", e(question_for(item))],
        ["Erreur à éviter", "Passer à l’étape suivante sans avoir ouvert ou vérifié le résultat."],
    ]
    return f"""
    <section id="section-{n:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {section_header(item, n)}
      <div class="grid gap-8 lg:grid-cols-[.8fr_1.2fr]">
        <div class="min-w-0">
          <h2 class="font-display text-3xl font-black text-slate-950 sm:text-5xl">{e(item["title"])}</h2>
          <p class="mt-5 text-lg leading-8 text-slate-700">{e(item["summary"])}</p>
        </div>
        <div class="min-w-0 space-y-6">
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
            <p class="font-black text-slate-950">Question à vous poser</p>
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
        ("C’est quoi", "#intro-claude-code"),
        ("Comprendre", "#section-01"),
        ("Installer", "#section-11"),
        ("Dossier", "#section-21"),
        ("Page", "#section-31"),
        ("Contrôle", "#section-61"),
        ("Lien final", "#section-71"),
    ]
    return "".join(
        f'<a class="border-2 border-slate-950 bg-white px-3 py-2 text-xs font-black uppercase tracking-[.12em] text-slate-950 no-underline shadow-[3px_3px_0_#111827] transition hover:-translate-y-0.5 hover:bg-blue-600 hover:text-white" href="{href}">{label}</a>'
        for label, href in links
    )


def intro_block() -> str:
    cards = [
        (
            "01",
            "Un assistant dans votre projet",
            "Claude Code est un outil d’Anthropic qui se lance dans un dossier de travail. Il ne regarde pas seulement une question isolée : il peut comprendre les fichiers autour, proposer une modification et vous aider à avancer sur un vrai projet.",
            "bg-blue-50",
        ),
        (
            "02",
            "Pas seulement un chatbot",
            "Un chatbot répond surtout dans une conversation. Claude Code peut aussi agir : créer un fichier, modifier du code, lancer une commande, expliquer une erreur ou préparer une checklist. C’est utile, mais ça demande plus de contrôle.",
            "bg-violet-50",
        ),
        (
            "03",
            "La décision finale reste humaine",
            "Claude Code propose et exécute, mais vous décidez. Vous lisez ce qu’il veut faire, vous regardez les fichiers modifiés, vous ouvrez le résultat, puis vous acceptez ou vous demandez une correction. L’outil ne valide pas à votre place.",
            "bg-cyan-50",
        ),
        (
            "04",
            "Le dossier compte beaucoup",
            "La règle simple : Claude Code travaille là où vous le lancez. Si vous l’ouvrez dans le bon dossier, il a le bon contexte. Si vous l’ouvrez au mauvais endroit, il peut regarder ou modifier des éléments qui ne concernent pas l’exercice.",
            "bg-white",
        ),
    ]
    card_html = ""
    for number, title, text, tone in cards:
        card_html += f"""
          <article class="border-2 border-slate-950 {tone} p-5 shadow-[6px_6px_0_#111827]">
            <p class="font-mono text-[11px] font-black uppercase tracking-[.16em] text-slate-500">{number}</p>
            <h3 class="mt-3 text-xl font-black leading-7 text-slate-950">{e(title)}</h3>
            <p class="mt-3 text-[15px] leading-7 text-slate-700">{e(text)}</p>
          </article>
        """
    decision_rows = [
        ["Comprendre une idée", "Un chatbot suffit souvent. Vous posez une question, vous lisez la réponse, puis vous réfléchissez."],
        ["Créer un vrai fichier", "Claude Code est plus adapté. Il travaille dans votre dossier et peut produire un résultat concret."],
        ["Corriger une erreur", "Claude Code peut lire les fichiers, proposer une piste, lancer une commande et expliquer le problème."],
        ["Livrer proprement", "Vous lui demandez une checklist, puis vous vérifiez vous-même le rendu, les liens, le mobile et les fichiers modifiés."],
    ]
    decision_html = ""
    for situation, tool in decision_rows:
        decision_html += f"""
          <div class="grid sm:grid-cols-[220px_1fr]">
            <div class="border-b-2 border-slate-950 bg-blue-100 px-5 py-4 sm:border-b-0 sm:border-r-2">
              <p class="font-mono text-[11px] font-black uppercase tracking-[.14em] text-slate-600">Situation</p>
              <p class="mt-2 font-black leading-6 text-slate-950">{e(situation)}</p>
            </div>
            <div class="bg-white px-5 py-4">
              <p class="font-mono text-[11px] font-black uppercase tracking-[.14em] text-slate-500">Outil à privilégier</p>
              <p class="mt-2 text-[15px] leading-7 text-slate-700">{e(tool)}</p>
            </div>
          </div>
        """
    return f"""
  <section id="intro-claude-code" class="mx-auto max-w-7xl bg-white px-4 py-12 sm:px-6 lg:px-8">
    <div class="grid gap-8 lg:grid-cols-[1.05fr_.95fr] lg:items-start">
      <div class="border-2 border-slate-950 bg-white p-7 shadow-[8px_8px_0_#111827]">
        <div class="mb-5 inline-flex border-2 border-slate-950 bg-violet-600 px-4 py-2 font-mono text-xs font-black uppercase tracking-[.18em] text-white shadow-[5px_5px_0_#111827]">Avant la pratique</div>
        <h2 class="font-display text-4xl font-black leading-tight text-slate-950 sm:text-6xl">C’est quoi Claude Code ?</h2>
        <p class="mt-5 text-lg leading-8 text-slate-700">Imaginez que vous ouvrez un dossier vide et que vous construisez, pas à pas, une petite page pour un restaurant fictif : Le Comptoir Bleu. Claude Code va vous aider à créer les fichiers, améliorer la page, vérifier le résultat et préparer une livraison simple.</p>
        <p class="mt-4 text-lg leading-8 text-slate-700">Le but n’est pas de tout comprendre d’un coup. Le but est de suivre une seule histoire : installer l’outil, créer le dossier, lancer Claude Code, demander une page, l’ouvrir, corriger, contrôler, puis obtenir un lien consultable.</p>
        <div class="mt-6 border-l-4 border-blue-600 bg-blue-50 px-5 py-4">
          <p class="font-black text-slate-950">Question simple</p>
          <p class="mt-2 leading-7 text-slate-700">Est-ce que vous voulez seulement une explication, ou est-ce que vous voulez obtenir un vrai fichier dans un vrai dossier ? Cette question aide à savoir quand utiliser Claude Code.</p>
        </div>
      </div>
      <figure class="overflow-hidden border-2 border-slate-950 bg-white shadow-[8px_8px_0_#111827]">
        <img class="aspect-[16/10] w-full bg-white object-contain" src="assets/claude-code-interface/desktop-files-preview.png" alt="Interface Claude Code avec fichiers et aperçu" loading="lazy">
        <figcaption class="border-t-2 border-slate-950 bg-white px-4 py-3 text-sm font-semibold text-slate-700">Claude Code aide à passer d’une demande à des fichiers vérifiables.</figcaption>
      </figure>
    </div>

    <div class="mt-8 grid gap-5 md:grid-cols-2 xl:grid-cols-4">
      {card_html}
    </div>

    <div class="mt-8 grid gap-8 lg:grid-cols-[.95fr_1.05fr] lg:items-start">
      <div class="border-2 border-slate-950 bg-slate-950 p-6 text-white shadow-[8px_8px_0_#111827]">
        <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-cyan-200">La boucle à retenir</p>
        <ol class="mt-5 space-y-4 text-base leading-7">
          <li><b>1. Vous ouvrez le bon dossier.</b><br><span class="text-slate-300">Claude Code doit partir du bon contexte.</span></li>
          <li><b>2. Vous formulez une demande claire.</b><br><span class="text-slate-300">Vous dites le résultat attendu, le public et les contraintes.</span></li>
          <li><b>3. Claude propose ou modifie.</b><br><span class="text-slate-300">Il peut écrire, corriger, lancer une commande ou expliquer.</span></li>
          <li><b>4. Vous vérifiez.</b><br><span class="text-slate-300">Vous ouvrez le fichier, vous lisez le diff, vous testez le rendu.</span></li>
        </ol>
      </div>
      <div>
        <div class="overflow-hidden border-2 border-slate-950 bg-white shadow-[8px_8px_0_#111827]">
          <div class="border-b-2 border-slate-950 bg-blue-600 px-5 py-3">
            <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-white">Quand utiliser quoi ?</p>
          </div>
          <div class="divide-y-2 divide-slate-950">
            {decision_html}
          </div>
        </div>
      </div>
    </div>
  </section>
    """


def journey_map() -> str:
    cards = ""
    start = 1
    for index, (chapter, summary, tag, color, items) in enumerate(CHAPTERS, 1):
        end = start + len(items) - 1
        color_class = {
            "blue": "bg-blue-50",
            "violet": "bg-violet-50",
            "cyan": "bg-cyan-50",
            "orange": "bg-orange-50",
            "green": "bg-emerald-50",
        }[color]
        cards += f"""
          <a href="#section-{start:02d}" class="group block border-2 border-slate-950 {color_class} p-5 text-slate-950 no-underline shadow-[6px_6px_0_#111827] transition hover:-translate-y-1 hover:shadow-[9px_9px_0_#111827]">
            <div class="flex items-center justify-between gap-3">
              <span class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-[11px] font-black uppercase tracking-[.14em] shadow-[3px_3px_0_#111827]">Sections {start:02d}-{end:02d}</span>
              <span class="font-mono text-[11px] font-black uppercase tracking-[.14em] text-slate-500">{e(tag)}</span>
            </div>
            <h3 class="mt-5 text-2xl font-black leading-7 text-slate-950">{e(chapter)}</h3>
            <p class="mt-3 text-[15px] leading-7 text-slate-700">{e(summary)}</p>
            <p class="mt-5 font-mono text-xs font-black uppercase tracking-[.16em] text-blue-700">Ouvrir l’acte {index:02d}</p>
          </a>
        """
        start = end + 1
    return f"""
  <section id="plan-parcours" class="mx-auto max-w-7xl bg-white px-4 py-12 sm:px-6 lg:px-8">
    <div class="mb-8 max-w-4xl">
      <div class="mb-5 inline-flex border-2 border-slate-950 bg-slate-950 px-4 py-2 font-mono text-xs font-black uppercase tracking-[.18em] text-white shadow-[5px_5px_0_#111827]">Plan du support</div>
      <h2 class="font-display text-4xl font-black leading-tight text-slate-950 sm:text-6xl">80 sections, un projet qui avance.</h2>
      <p class="mt-5 text-lg leading-8 text-slate-700">Tout suit le même exemple : Le Comptoir Bleu. Vous partez sans installation, puis vous arrivez à une page de restaurant simple, vérifiée et prête à être partagée.</p>
    </div>
    <div class="grid gap-5 md:grid-cols-2 xl:grid-cols-4">
      {cards}
    </div>
  </section>
    """


def source_table() -> str:
    rows = [
        ["Vue d’ensemble Claude Code", f'<a href="{DOCS["overview"]}" target="_blank" rel="noopener">Documentation officielle</a>'],
        ["Installation", f'<a href="{DOCS["setup"]}" target="_blank" rel="noopener">Quickstart Claude Code</a>'],
        ["CLI", f'<a href="{DOCS["cli"]}" target="_blank" rel="noopener">CLI reference</a>'],
        ["Application Desktop", f'<a href="{DOCS["desktop"]}" target="_blank" rel="noopener">Claude Code Desktop</a>'],
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

  <nav class="z-50 border-b-2 border-slate-950 bg-white">
    <div class="mx-auto flex max-w-7xl flex-col gap-4 px-4 py-4 sm:px-6 lg:flex-row lg:items-center lg:justify-between lg:px-8">
      <a href="#top" class="flex items-center gap-3 text-slate-950 no-underline">
        <img src="logo-denem.jpeg" alt="Logo DENEM" class="h-11 w-11 border-2 border-slate-950 object-cover shadow-[4px_4px_0_#111827]">
        <span><b class="block font-display text-lg leading-none">DENEM Academy</b><small class="font-mono text-xs uppercase tracking-[.14em] text-slate-500">Support formation - Séance 01</small></span>
      </a>
      <div class="flex flex-wrap gap-2">{nav()}</div>
    </div>
  </nav>

  <header id="top" class="mx-auto max-w-7xl bg-white px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
    <div class="grid gap-8 lg:grid-cols-[1.04fr_.96fr] lg:items-center">
      <div>
        <div class="mb-5 inline-flex border-2 border-slate-950 bg-blue-600 px-4 py-2 font-mono text-xs font-black uppercase tracking-[.18em] text-white shadow-[5px_5px_0_#111827]">Séance 01 · Claude Code</div>
        <h1 class="font-display text-5xl font-black leading-[.92] tracking-tight text-slate-950 sm:text-7xl lg:text-8xl">Le Comptoir Bleu.<br><span class="text-blue-600">Un dossier.</span><br><span class="text-violet-600">Une page.</span></h1>
        <p class="mt-7 max-w-3xl text-xl leading-9 text-slate-700">Vous partez de zéro. Vous installez Claude Code, vous créez le dossier du restaurant, vous générez une première page, vous l’améliorez, puis vous vérifiez le résultat comme dans un vrai travail quotidien.</p>
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

  {intro_block()}

  {journey_map()}

  <section class="mx-auto max-w-7xl bg-white px-4 py-8 sm:px-6 lg:px-8">
    <div class="grid gap-4 md:grid-cols-5">
      <div class="border-2 border-slate-950 bg-blue-50 p-5 shadow-[4px_4px_0_#111827]"><b>Théorie</b><p class="mt-2 text-sm text-slate-700">Vous comprenez avant de cliquer.</p></div>
      <div class="border-2 border-slate-950 bg-cyan-50 p-5 shadow-[4px_4px_0_#111827]"><b>Pratique</b><p class="mt-2 text-sm text-slate-700">Vous faites une action simple.</p></div>
      <div class="border-2 border-slate-950 bg-violet-50 p-5 shadow-[4px_4px_0_#111827]"><b>Méthode</b><p class="mt-2 text-sm text-slate-700">Vous gardez un réflexe.</p></div>
      <div class="border-2 border-slate-950 bg-orange-50 p-5 shadow-[4px_4px_0_#111827]"><b>Vigilance</b><p class="mt-2 text-sm text-slate-700">Vous évitez une erreur.</p></div>
      <div class="border-2 border-slate-950 bg-emerald-50 p-5 shadow-[4px_4px_0_#111827]"><b>Validation</b><p class="mt-2 text-sm text-slate-700">Vous savez si c’est bon.</p></div>
    </div>
  </section>

  {html_sections}

  <section class="mx-auto max-w-7xl bg-white px-4 py-16 sm:px-6 lg:px-8">
    <div class="border-2 border-slate-950 bg-white p-7 shadow-[8px_8px_0_#111827]">
      <div class="mb-5 inline-flex border-2 border-slate-950 bg-violet-600 px-4 py-2 font-mono text-xs font-black uppercase tracking-[.18em] text-white">Sources</div>
      <h2 class="font-display text-4xl font-black text-slate-950 sm:text-6xl">Les liens à garder.</h2>
      <p class="mt-5 max-w-3xl text-lg leading-8 text-slate-700">Ces liens servent à vérifier une commande, reprendre l’installation ou confirmer une information depuis une source officielle.</p>
      <p class="mt-3 max-w-3xl border-l-4 border-blue-600 pl-4 text-sm font-semibold leading-6 text-slate-700">Prix vérifiés le 3 juin 2026 sur le Help Center Claude : Pro 20 $/mois US, Max 5x 100 $/mois, Max 20x 200 $/mois. Les prix peuvent changer selon la région, les taxes et les décisions d’Anthropic.</p>
      <div class="mt-8">{source_table()}</div>
    </div>
  </section>

  <div id="egg" class="pointer-events-none fixed bottom-5 left-1/2 z-[80] hidden -translate-x-1/2 border-2 border-slate-950 bg-white px-5 py-3 font-mono text-sm font-black shadow-[6px_6px_0_#111827]">Vous avancez bien : petite étape, vraie vérification.</div>

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
        const code = btn.closest('.code-panel').querySelector('code').innerText;
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
    html = public_copy(render())
    OUT.write_text(html, encoding="utf-8")
    INDEX_OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.name} and {INDEX_OUT.name}: {html.count('<section')} sections, {html.count('<img ')} images")
