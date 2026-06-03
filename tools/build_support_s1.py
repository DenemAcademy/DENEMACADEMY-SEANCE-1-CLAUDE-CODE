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
        "Acte 1 - Comprendre l’outil",
        "Vous posez les bases avant de lancer une commande.",
        "Théorie",
        "blue",
        [
            ("Vous partez du bon problème", "Claude Code sert quand vous voulez avancer dans un vrai dossier. Il ne remplace pas votre jugement. Il donne surtout une manière plus directe de passer d’une idée à un fichier vérifiable.", "Formulez le besoin en une phrase : `Je veux obtenir...` puis ajoutez le fichier attendu.", "Vous savez pourquoi vous ouvrez Claude Code avant de commencer."),
            ("Vous voyez Claude Code comme un assistant de projet", "Claude Code peut lire des fichiers, proposer des modifications, lancer certaines commandes et expliquer le résultat. Cette capacité est utile parce qu’elle rapproche la discussion du travail réel.", "Dites à voix haute la différence entre `répondre` et `agir dans un dossier`.", "Vous ne le traitez pas comme une simple zone de chat."),
            ("Vous gardez la décision finale", "Même si l’outil écrit vite, la validation reste humaine. Vous choisissez l’objectif, vous acceptez ou refusez les actions, puis vous ouvrez le résultat pour le vérifier.", "Avant chaque demande, écrivez : `Je vérifierai le résultat en ouvrant...`.", "Vous savez ce qui doit être contrôlé avant de continuer."),
            ("Vous choisissez un résultat visible", "Un bon début ne cherche pas à tout faire. Il cherche une sortie simple : un fichier, une page, une checklist, un résumé ou une correction claire.", "Choisissez une sortie que vous pouvez ouvrir ou relire en moins de deux minutes.", "La première étape reste courte et concrète."),
            ("Vous retenez la boucle de travail", "La méthode de base est simple : dossier, demande, proposition, vérification, correction. Si une étape manque, la session devient vite confuse.", "Gardez cette phrase près du terminal : `Je demande, Claude propose, je vérifie.`", "Vous pouvez reprendre la séance sans regarder la vidéo en boucle."),
            ("Vous comprenez le dossier actif", "Claude Code travaille depuis le dossier où il est lancé. Si ce dossier est mauvais, le contexte sera mauvais aussi. C’est souvent la première cause d’erreur.", "Créez un dossier `formation-s1-claude-code` et ouvrez le terminal dedans.", "Le chemin du terminal correspond au projet prévu."),
            ("Vous savez ce que Claude peut lire", "Claude Code peut utiliser les fichiers du projet pour comprendre le contexte. Cette lecture aide pour corriger ou améliorer, mais elle demande un dossier propre.", "Placez uniquement les fichiers utiles dans le dossier de travail.", "Aucun fichier personnel ou hors sujet ne se trouve dans le projet."),
            ("Vous savez ce que Claude peut modifier", "L’outil peut créer ou modifier des fichiers quand vous l’autorisez. Ce n’est pas dangereux si vous regardez les changements. Ça devient risqué si vous acceptez sans relire.", "Demandez toujours un résumé des fichiers touchés après une action.", "Vous savez exactement ce qui a changé."),
            ("Vous commencez petit", "Une première session doit prouver que le flux fonctionne. Un petit fichier réussi vaut mieux qu’un grand projet commencé dans le flou.", "Demandez une page HTML simple, puis une seule amélioration.", "Vous voyez une progression réelle sans perdre le fil."),
            ("Vous posez la règle d’or", "La règle d’or de la séance est directe : Claude Code accélère l’exécution, pas la réflexion. Vous devez donc cadrer, vérifier et décider.", "Notez cette règle dans votre fichier de notes.", "Vous savez expliquer l’outil avec des mots simples."),
        ],
    ),
    (
        "Acte 2 - Accès, prix et installation",
        "Vous préparez l’accès Claude Code sans confondre abonnement, API et terminal.",
        "Installation",
        "cyan",
        [
            ("Vous choisissez le bon accès", "Claude Code demande un accès Claude compatible. La documentation indique qu’il peut être utilisé avec Pro, Max, Team, Enterprise ou d’autres accès pris en charge.", "Ouvrez la page officielle avant achat et vérifiez le plan disponible dans votre région.", "Vous ne payez pas avant d’avoir compris votre besoin réel."),
            ("Vous comprenez le plan Pro", "Le Help Center indique Pro à 20 $/mois aux États-Unis. Pro peut suffire pour tester, apprendre et faire des sessions raisonnables.", "Classez votre usage : découverte, formation régulière ou production fréquente.", "Vous savez pourquoi Pro peut être un bon départ."),
            ("Vous comprenez Max 5x", "Le plan Max 5x est listé à 100 $/mois. Il vise les usages plus fréquents et donne plus de capacité par session que Pro.", "Passez à Max seulement si les limites vous interrompent souvent dans un vrai travail.", "Le choix du plan repose sur votre usage, pas sur une peur de manquer."),
            ("Vous comprenez Max 20x", "Le plan Max 20x est listé à 200 $/mois. Il vise les usages intensifs, les longues sessions et les personnes qui travaillent souvent avec Claude.", "Demandez-vous si le prix vous fait gagner du temps mesurable pendant vos projets.", "Vous reliez le budget au temps gagné."),
            ("Vous distinguez abonnement et API", "L’abonnement sert à utiliser Claude et Claude Code avec votre compte. L’API sert à faire appeler Claude par un système automatisé, par exemple une application client.", "Retenez : abonnement = usage direct ; API = usage par un logiciel.", "Vous pouvez expliquer la différence sans jargon."),
            ("Vous protégez les clés API", "Une clé API est privée. Si elle est exposée dans une capture, un dépôt GitHub ou un support, quelqu’un peut l’utiliser et créer des coûts.", "Ne mettez jamais une clé dans une page, un README public ou une image.", "Vos accès restent protégés."),
            ("Vous choisissez la méthode officielle d’installation", "La documentation récente recommande l’installation native de Claude Code. Selon votre machine, la route peut être macOS, Linux, WSL, PowerShell, CMD, Homebrew ou WinGet.", "Copiez la commande depuis la page officielle, pas depuis un ancien message.", "Vous installez avec une source à jour."),
            ("Vous gardez Node et npm comme repères", "Certaines séances ou anciennes installations parlent de npm. C’est utile à connaître, surtout pour comprendre les erreurs ou nettoyer une ancienne installation.", "Vérifiez `node -v` et `npm -v` si votre environnement dépend encore de npm.", "Vous savez si Node et npm répondent correctement."),
            ("Vous lancez l’installation proprement", "L’installation doit se faire dans un terminal clair, sans commande copiée au hasard. Si une erreur de permission apparaît, il faut comprendre avant de forcer.", "Installez Claude Code avec la méthode officielle adaptée à votre système.", "La commande `claude --version` répond."),
            ("Vous connectez votre compte", "Au premier lancement, Claude Code peut demander une connexion au compte Claude. C’est normal : l’outil doit savoir avec quel accès il travaille.", "Lancez `claude`, suivez la connexion, puis revenez au terminal.", "La session démarre avec le bon compte."),
        ],
    ),
    (
        "Acte 3 - Premier dossier, première session",
        "Vous créez votre premier espace de travail et vous faites produire un petit résultat.",
        "Pratique",
        "cyan",
        [
            ("Vous créez un dossier propre", "Le dossier est le décor de votre histoire. S’il est propre, Claude Code comprend mieux. S’il contient dix projets mélangés, il risque de lire trop large.", "Créez `formation-s1-claude-code` sur le bureau ou dans un endroit facile à retrouver.", "Le dossier est visible, vide et nommé clairement."),
            ("Vous ouvrez le terminal au bon endroit", "Le terminal doit pointer vers le dossier de travail. Avant de lancer Claude Code, il faut savoir où vous êtes.", "Utilisez `cd` pour entrer dans le dossier, puis affichez le chemin avec `pwd` ou la commande adaptée à votre système.", "Le chemin affiché contient `formation-s1-claude-code`."),
            ("Vous lancez Claude Code", "La commande `claude` ouvre une session interactive. À partir de là, vos demandes concernent le dossier actif.", "Lancez `claude` depuis le dossier prévu.", "Claude Code démarre sans erreur bloquante."),
            ("Vous vérifiez le contexte de départ", "Avant de demander une création, vérifiez que Claude Code a compris le dossier et l’objectif. Une minute de cadrage évite dix minutes de correction.", "Demandez : `Résume le dossier actif et dis ce que vous voyez, sans modifier de fichier.`", "Vous obtenez une réponse de lecture, pas une modification."),
            ("Vous demandez un premier fichier", "Le premier fichier sert à tester la boucle. Il doit être simple, lisible et facile à ouvrir.", "Demandez : `Crée une page HTML simple qui présente un service de création de site.`", "Un fichier HTML apparaît dans le dossier."),
            ("Vous demandez la liste des fichiers", "Après une création, vous devez savoir où chercher. Claude Code doit vous donner les chemins, pas seulement dire que c’est fini.", "Ajoutez : `À la fin, liste les fichiers créés ou modifiés.`", "Vous retrouvez le bon fichier sans fouiller."),
            ("Vous ouvrez le résultat", "Le résultat doit être vu dans son contexte final. Lire le code ne suffit pas si le livrable est une page.", "Ouvrez le fichier dans le navigateur ou l’aperçu Desktop.", "La page s’affiche et vous pouvez la juger."),
            ("Vous corrigez une seule chose", "Une correction ciblée garde la session propre. Si vous demandez tout à la fois, il devient plus dur de voir ce qui a aidé.", "Demandez une amélioration unique : titre, couleur, section ou phrase.", "La modification est visible et facile à comparer."),
            ("Vous demandez une mini checklist", "Claude Code peut aider à vérifier le résultat, mais la vérification reste à faire par vous. La checklist rend ce contrôle plus simple.", "Demandez : `Donne-moi 8 points à vérifier avant de dire que la page est prête.`", "Vous avez une liste concrète de contrôle."),
            ("Vous terminez la session proprement", "Une session propre finit avec une trace. Vous devez savoir ce qui a été créé, ce qui marche et ce qui reste à faire.", "Demandez un résumé final avec fichiers, commandes et prochaines actions.", "Vous pouvez fermer le terminal sans perdre le fil."),
        ],
    ),
    (
        "Acte 4 - Écrire de bonnes demandes",
        "Vous apprenez à guider Claude Code avec des phrases simples et utiles.",
        "Méthode",
        "violet",
        [
            ("Vous donnez le contexte", "Claude Code écrit mieux quand il sait pour qui il travaille, quel est le niveau attendu et quel est le type de rendu. Le contexte évite les réponses génériques.", "Commencez par : `Je prépare un support de formation simple et clair.`", "La réponse suit mieux votre situation."),
            ("Vous donnez la sortie attendue", "Une demande claire dit ce qui doit exister à la fin. Sans sortie attendue, Claude Code peut choisir un format qui ne vous aide pas.", "Précisez : page HTML, README, tableau, checklist, script ou correction.", "Le résultat devient facile à vérifier."),
            ("Vous donnez les contraintes", "Les contraintes protègent la qualité. Elles peuvent porter sur le style, les couleurs, la longueur, les fichiers à ne pas toucher ou le niveau de détail.", "Ajoutez trois contraintes maximum au début, puis complétez si besoin.", "Claude Code sait où aller et où ne pas aller."),
            ("Vous demandez un plan avant le gros travail", "Pour une longue page ou un projet important, le plan doit venir avant la production. C’est le moment où vous pouvez corriger la direction.", "Demandez : `Propose le plan avant de créer les fichiers.`", "Vous validez l’ordre avant l’écriture."),
            ("Vous découpez la demande", "Une grosse demande devient plus fiable quand elle est découpée. Claude Code peut d’abord structurer, puis écrire, puis vérifier.", "Découpez en trois étapes : structure, contenu, contrôle.", "La session avance sans partir dans tous les sens."),
            ("Vous donnez des exemples", "Un exemple court aide souvent plus qu’un long discours. Il montre le niveau de phrase, la forme et le type de résultat attendu.", "Collez un exemple de section ou de phrase que vous aimez.", "Claude Code imite mieux la forme demandée."),
            ("Vous posez une question rhétorique", "Une question rhétorique guide la réflexion du lecteur. Elle rend le support plus humain sans l’alourdir.", "Ajoutez parfois : `Pourquoi cette étape compte ?` ou `Qu’est-ce qui peut mal se passer ?`", "Le texte explique le sens avant l’action."),
            ("Vous évitez les demandes vagues", "Une phrase comme `améliore le site` ne suffit pas. Elle laisse trop de décisions ouvertes et donne souvent un rendu moyen.", "Remplacez le vague par : `améliore la lisibilité mobile de la section installation`.", "La correction devient mesurable."),
            ("Vous demandez une vérification ciblée", "Claude Code peut relire son travail, mais il faut lui dire quoi regarder. Sinon il peut donner un avis trop général.", "Demandez : `Vérifie les liens, les titres, les accents et le responsive.`", "La vérification couvre les vrais risques."),
            ("Vous gardez une voix naturelle", "Le support doit parler simplement. Il doit accompagner sans donner l’impression d’un manuel froid.", "Demandez des phrases courtes, des mots simples et des transitions claires.", "La lecture reste fluide."),
        ],
    ),
    (
        "Acte 5 - Contrôle, sécurité et permissions",
        "Vous laissez l’outil agir, mais vous gardez la main sur les décisions importantes.",
        "Vigilance",
        "orange",
        [
            ("Vous choisissez un mode de permission", "Les permissions définissent ce que Claude Code peut faire sans vous interrompre. Au début, un mode qui demande confirmation aide à comprendre les actions.", "Commencez avec un mode prudent, puis assouplissez seulement quand le projet est clair.", "Vous voyez les actions avant de les accepter."),
            ("Vous lisez les diffs", "Un diff montre ce qui a été ajouté, supprimé ou modifié. C’est l’un des meilleurs endroits pour reprendre le contrôle.", "Avant d’accepter, regardez les lignes modifiées et le fichier concerné.", "Vous savez ce qui entre dans le projet."),
            ("Vous demandez avant les commandes sensibles", "Une commande peut installer, supprimer, déplacer ou publier. Il faut savoir ce qu’elle fait avant exécution.", "Demandez : `Explique la commande avant de la lancer.`", "Vous ne validez pas une commande opaque."),
            ("Vous refusez les suppressions floues", "Le nettoyage peut être utile, mais une suppression mal comprise peut faire perdre du travail.", "Demandez une liste précise des fichiers à supprimer avant action.", "Aucun fichier important ne disparaît par surprise."),
            ("Vous protégez les secrets", "Les secrets incluent mots de passe, tokens, clés API et fichiers d’environnement. Ils ne doivent jamais se retrouver dans une page publique.", "Avant publication, cherchez `.env`, `api_key`, `token` et `secret`.", "Le projet peut être partagé plus sereinement."),
            ("Vous vérifiez avec Git", "Git montre les fichiers modifiés. Même sans être expert, `git status` donne une vision rapide de ce qui a bougé.", "Lancez `git status` avant de commit ou de pousser.", "Vous connaissez la liste des changements."),
            ("Vous lancez les tests utiles", "Un test n’a pas besoin d’être compliqué. Pour une page, ouvrir le site et vérifier le mobile est déjà un vrai test.", "Demandez à Claude Code les commandes de vérification adaptées au projet.", "Vous validez avec des faits."),
            ("Vous utilisez l’aperçu Desktop", "Dans Claude Code Desktop, l’aperçu permet de voir le rendu sans quitter l’interface. C’est pratique pour contrôler vite une page.", "Ouvrez l’aperçu dès qu’un fichier visuel est généré.", "Vous jugez le résultat comme un utilisateur."),
            ("Vous savez arrêter une mauvaise direction", "Si Claude Code produit quelque chose qui ne respecte pas le plan, il faut le dire tôt. Attendre rend la correction plus coûteuse.", "Écrivez : `Stop. Reviens au plan validé et corrige seulement cette partie.`", "La session revient dans le cadre."),
            ("Vous notez la décision finale", "Après une correction importante, il faut garder une trace du choix. Cela aide à expliquer pourquoi le projet est fait ainsi.", "Ajoutez une note courte dans le résumé de session.", "La décision reste compréhensible plus tard."),
        ],
    ),
    (
        "Acte 6 - Construire un vrai support",
        "Vous passez de l’exercice simple à une page longue, utile et structurée.",
        "Production",
        "green",
        [
            ("Vous validez la structure avant le build", "Un long support doit avoir un plan. Sans plan, les sections se ressemblent et le lecteur ne comprend plus le chemin.", "Demandez d’abord les actes, les objectifs et l’ordre des sections.", "La page raconte une progression claire."),
            ("Vous construisez section par section", "Un support long se travaille comme un parcours. Chaque section doit apporter une étape, pas répéter la précédente.", "Demandez à Claude Code de traiter les sections par blocs de 10.", "Le contenu avance dans le bon ordre."),
            ("Vous variez les formats", "Une page sérieuse peut alterner explication, tableau, checklist, bloc à copier, capture et résumé. La variété aide la lecture.", "Associez un format à chaque type de besoin : théorie, action, vigilance, validation.", "Le lecteur ne voit pas 80 blocs identiques."),
            ("Vous reliez les images au sujet", "Une image doit expliquer la section. Une capture de terminal sert à l’installation, un diff sert à la validation, une checklist sert au test.", "Choisissez l’image selon le thème de la section, pas au hasard.", "L’image renforce le texte."),
            ("Vous écrivez pour l’action", "Un bon support ne se contente pas de raconter. Il donne une action faisable maintenant et un critère de réussite.", "Pour chaque section, gardez `ce que vous faites` et `comment vous vérifiez`.", "La section devient utilisable."),
            ("Vous gardez un fond blanc", "Le fond blanc rend le support plus sérieux et plus lisible. Le bleu et le violet servent à hiérarchiser, pas à couvrir toute la page.", "Gardez les couleurs pour les badges, les bandeaux et les zones importantes.", "Le design reste propre."),
            ("Vous soignez le responsive", "Une page utile doit marcher sur ordinateur et mobile. Les cartes, tableaux et blocs de code ne doivent pas déborder.", "Vérifiez largeur, texte long, bouton copier et images sur plusieurs tailles.", "Le support reste lisible partout."),
            ("Vous ajoutez des micro-interactions utiles", "Les petites interactions doivent aider : progression, copie de bloc, apparition douce, hover léger. Elles ne doivent pas gêner la lecture.", "Gardez les animations courtes et désactivables si la personne réduit les mouvements.", "Le site paraît vivant sans devenir lourd."),
            ("Vous relisez les accents et le vocabulaire", "Une bonne page perd vite en crédibilité si les accents manquent ou si le texte change de voix. Le français doit rester propre.", "Cherchez les mots interdits, les tutoiements et les fautes visibles.", "La voix du support reste cohérente."),
            ("Vous faites un audit final", "Avant de publier, Claude Code peut relire avec une grille précise. Cela évite les oublis de dernière minute.", "Demandez : `Audite structure, responsive, liens, images, voix et sécurité.`", "Vous corrigez avant de livrer."),
        ],
    ),
    (
        "Acte 7 - Mémoire, limites et dépannage",
        "Vous apprenez à garder une session stable et à corriger les blocages fréquents.",
        "Dépannage",
        "orange",
        [
            ("Vous créez CLAUDE.md", "CLAUDE.md donne des règles de projet que Claude Code peut relire. C’est utile quand le travail dure plus d’une session.", "Créez `CLAUDE.md` dans les projets sérieux.", "Claude Code retrouve le cadre du projet."),
            ("Vous écrivez des règles concrètes", "Une règle vague aide peu. Une règle concrète dit quoi faire ou quoi éviter.", "Ajoutez : `Phrases courtes. Fond blanc. Bleu et violet pour les repères. Ne pas modifier les vidéos.`", "Les sorties deviennent plus stables."),
            ("Vous notez les commandes du projet", "Si un projet a des commandes de build, de test ou de publication, Claude Code doit pouvoir les retrouver.", "Ajoutez les commandes utiles dans CLAUDE.md avec une phrase d’explication.", "La prochaine session redémarre plus vite."),
            ("Vous utilisez la mémoire avec prudence", "La mémoire aide, mais une mauvaise consigne peut rester trop longtemps. Il faut relire et nettoyer si le projet change.", "Relisez les règles avant une nouvelle phase.", "Aucune ancienne consigne ne tire le projet dans la mauvaise direction."),
            ("Vous nettoyez une session confuse", "Une session longue peut accumuler trop de contexte. Quand les réponses deviennent moins précises, il faut réduire ou repartir proprement.", "Utilisez `/clear` pour repartir ou `/compact` pour garder l’essentiel.", "La conversation redevient lisible."),
            ("Vous comprenez les limites d’usage", "Les limites ne sont pas toujours un bug. Elles peuvent venir du plan, de l’usage cumulé ou d’une session trop longue.", "Si une limite apparaît, notez le message exact et attendez le reset ou réduisez la demande.", "Vous savez quoi faire au lieu de paniquer."),
            ("Vous corrigez `command not found`", "Si `claude` n’est pas reconnu, le terminal ne trouve pas l’installation. Le problème vient souvent du PATH ou d’une installation incomplète.", "Lancez `claude doctor` si possible, puis consultez la page officielle de dépannage.", "Vous identifiez si le souci vient de l’installation."),
            ("Vous évitez les installations en conflit", "Plusieurs installations de Claude Code peuvent créer des versions mélangées. La documentation explique comment repérer et nettoyer ce cas.", "Cherchez les installations multiples avant de réinstaller au hasard.", "Vous gardez une seule route d’installation."),
            ("Vous adaptez Windows", "Sur Windows, PowerShell, CMD, Git Bash et WSL ne se comportent pas toujours pareil. Une commande copiée pour le mauvais terminal peut échouer.", "Vérifiez le terminal utilisé avant de copier la commande.", "La commande correspond à votre environnement."),
            ("Vous gardez les sources officielles", "Le support aide à apprendre, mais les pages officielles confirment les commandes, les prix, les limites et les changements récents.", "Gardez les liens Claude Code, Help Center et Node.js dans vos favoris.", "Vous pouvez vérifier une information à jour."),
        ],
    ),
    (
        "Acte 8 - Livraison et méthode durable",
        "Vous terminez proprement et vous repartez avec une méthode réutilisable.",
        "Validation",
        "green",
        [
            ("Vous relisez le résultat complet", "Avant de publier, parcourez la page comme une personne qui la découvre. Le but est de repérer les ruptures de logique, les doublons et les passages trop rapides.", "Lisez les titres dans l’ordre sans lire tout le texte.", "L’histoire reste compréhensible du début à la fin."),
            ("Vous testez en local", "Un site doit être ouvert dans un navigateur avant publication. Le rendu réel peut révéler un débordement, une image mal cadrée ou un bouton mal placé.", "Lancez un serveur local et ouvrez la page sur desktop et mobile.", "Le site se consulte sans bug visible."),
            ("Vous vérifiez les mots sensibles", "Certains mots peuvent donner une mauvaise impression ou casser la voix du support. Il faut les chercher explicitement.", "Cherchez les tutoiements, les mots interdits et les phrases qui parlent à la mauvaise personne.", "Le texte parle uniquement en `vous`."),
            ("Vous contrôlez les liens", "Un lien mort casse la confiance. Les liens externes doivent pointer vers des sources utiles et cliquables.", "Cliquez les liens principaux : documentation, installation, prix, dépannage.", "Chaque lien ouvre la bonne ressource."),
            ("Vous regardez `git status`", "Avant de commit, il faut voir les fichiers modifiés et les fichiers à ne pas publier. Un gros fichier vidéo ou un fichier système ne doit pas partir par erreur.", "Lancez `git status` et lisez la liste calmement.", "Vous savez ce qui va être versionné."),
            ("Vous faites un commit lisible", "Un commit doit raconter le changement en une phrase courte. Cela aide à retrouver la version plus tard.", "Commitez avec un message comme `Structure support Claude Code séance 1`.", "L’historique reste propre."),
            ("Vous poussez sur GitHub", "Le push envoie le site vers le dépôt public. C’est l’étape où le travail devient consultable ailleurs que sur votre machine.", "Poussez la branche vers le dépôt GitHub Pages prévu.", "La nouvelle version arrive sur GitHub."),
            ("Vous vérifiez l’URL publique", "Après le push, la page peut mettre un peu de temps à se reconstruire. Il faut ouvrir l’URL finale, pas seulement supposer que tout est bon.", "Ouvrez l’URL publique et vérifiez une section du début, du milieu et de la fin.", "Le site publié correspond au site local."),
            ("Vous gardez une méthode réutilisable", "La méthode de cette séance servira ensuite pour d’autres outils. Le plus important n’est pas une commande isolée, mais la façon de cadrer et vérifier.", "Gardez votre checklist : dossier, demande, action, vérification, livraison.", "Vous pouvez refaire le flux sur un autre projet."),
            ("Vous préparez la suite", "La séance suivante pourra comparer Claude Code avec d’autres agents comme Codex. Vous aurez déjà les bases : installer, lancer, demander, vérifier, livrer.", "Notez ce que vous voulez comparer : vitesse, qualité, contrôle, publication.", "Vous arrivez à la suite avec une vraie grille de lecture."),
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
        ("Départ", "#section-01"),
        ("Installer", "#section-17"),
        ("Exercice", "#section-21"),
        ("Prompts", "#section-31"),
        ("Sécurité", "#section-41"),
        ("Livrer", "#section-71"),
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
            "Vous restez aux commandes",
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
        ["Vous voulez comprendre une idée", "Un chatbot suffit souvent. Vous posez une question, vous lisez la réponse, puis vous réfléchissez."],
        ["Vous voulez créer ou modifier des fichiers", "Claude Code est plus adapté. Il travaille dans votre dossier et peut produire un résultat concret."],
        ["Vous voulez corriger une erreur", "Claude Code peut lire les fichiers, proposer une piste, lancer une commande et expliquer le problème."],
        ["Vous voulez livrer proprement", "Vous lui demandez une checklist, puis vous vérifiez vous-même le rendu, les liens, le mobile et les fichiers modifiés."],
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
        <p class="mt-5 text-lg leading-8 text-slate-700">Imaginez que vous ouvrez un dossier sur votre ordinateur et que vous demandez à un assistant de vous aider dedans. Pas juste de parler du projet. De le lire, de proposer une action, de créer un fichier, de corriger une erreur, puis de vous expliquer ce qui a changé.</p>
        <p class="mt-4 text-lg leading-8 text-slate-700">Claude Code sert à ça. C’est un agent de code. Il peut travailler dans le terminal ou dans l’interface Desktop. Il est pratique pour apprendre, créer un site, corriger un script, organiser un projet ou comprendre une erreur. Mais il faut garder une règle simple : vous demandez, il propose, vous vérifiez.</p>
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
      <h2 class="font-display text-4xl font-black leading-tight text-slate-950 sm:text-6xl">80 sections, une seule histoire.</h2>
      <p class="mt-5 text-lg leading-8 text-slate-700">Le support avance comme une méthode : comprendre, installer, lancer, demander, contrôler, produire, dépanner, livrer. Vous pouvez lire dans l’ordre ou revenir à l’acte qui bloque.</p>
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
        <div class="mb-5 inline-flex border-2 border-slate-950 bg-blue-600 px-4 py-2 font-mono text-xs font-black uppercase tracking-[.18em] text-white shadow-[5px_5px_0_#111827]">Support technique guidé</div>
        <h1 class="font-display text-5xl font-black leading-[.92] tracking-tight text-slate-950 sm:text-7xl lg:text-8xl">Claude Code.<br><span class="text-blue-600">Vous installez.</span><br><span class="text-violet-600">Vous livrez.</span></h1>
        <p class="mt-7 max-w-3xl text-xl leading-9 text-slate-700">Ce support ne répète pas la vidéo mot pour mot. Il transforme la séance en méthode claire : quoi faire, pourquoi le faire, quoi vérifier, et comment éviter les erreurs.</p>
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
