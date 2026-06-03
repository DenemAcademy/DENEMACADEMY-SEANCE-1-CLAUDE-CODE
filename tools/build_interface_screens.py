from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "claude-code-interface"
OUT.mkdir(parents=True, exist_ok=True)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Courier New Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Courier New.ttf",
    ]
    for candidate in candidates:
        p = Path(candidate)
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


F_TITLE = font(46, True)
F_SUB = font(24)
F_BODY = font(25)
F_BODY_BOLD = font(25, True)
F_MONO = font(22)
F_MONO_BOLD = font(22, True)
F_SMALL = font(18)
F_SMALL_BOLD = font(18, True)


INK = "#111827"
BLUE = "#2563eb"
VIOLET = "#7c3aed"
CYAN = "#67e8f9"
GREEN = "#bbf7d0"
ORANGE = "#fed7aa"
BG = "#ffffff"
SOFT = "#f8fafc"


def shadow_box(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: str, outline: str = INK, shadow: int = 10) -> None:
    x1, y1, x2, y2 = xy
    draw.rectangle((x1 + shadow, y1 + shadow, x2 + shadow, y2 + shadow), fill=INK)
    draw.rectangle(xy, fill=fill, outline=outline, width=3)


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, fnt: ImageFont.ImageFont, fill: str = INK) -> None:
    draw.text(xy, value, font=fnt, fill=fill)


def wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, width: int, fnt: ImageFont.ImageFont, fill: str = INK, line_gap: int = 10) -> int:
    x, y = xy
    avg = max(8, int(fnt.size * 0.52))
    chars = max(20, width // avg)
    for line in wrap(value, chars):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def terminal(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, lines: list[tuple[str, str]]) -> None:
    x1, y1, x2, y2 = xy
    shadow_box(draw, xy, "#0b1020")
    draw.rectangle((x1, y1, x2, y1 + 56), fill="#111827", outline=INK, width=0)
    for i, color in enumerate(["#f87171", "#fbbf24", "#34d399"]):
        draw.ellipse((x1 + 24 + i * 28, y1 + 19, x1 + 40 + i * 28, y1 + 35), fill=color)
    text(draw, (x1 + 120, y1 + 17), title, F_SMALL_BOLD, "#e5e7eb")
    y = y1 + 84
    for prefix, content in lines:
        text(draw, (x1 + 28, y), prefix, F_MONO_BOLD, "#67e8f9" if prefix.strip().startswith("$") else "#a78bfa")
        y = wrapped(draw, (x1 + 110, y), content, x2 - x1 - 140, F_MONO, "#f8fafc", 7)
        y += 6


def header(draw: ImageDraw.ImageDraw, title: str, subtitle: str, badge: str) -> None:
    shadow_box(draw, (54, 54, 330, 104), BLUE)
    text(draw, (76, 70), badge.upper(), F_SMALL_BOLD, "#ffffff")
    text(draw, (54, 136), title, F_TITLE, INK)
    wrapped(draw, (58, 196), subtitle, 760, F_SUB, "#475569", 10)


def save(name: str, title: str, subtitle: str, badge: str, draw_fn) -> None:
    img = Image.new("RGB", (1440, 900), BG)
    d = ImageDraw.Draw(img)
    header(d, title, subtitle, badge)
    draw_fn(d)
    img.save(OUT / name, quality=92)


def desktop_shell(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], mode: str) -> None:
    x1, y1, x2, y2 = xy
    shadow_box(draw, xy, "#f8fafc")
    draw.rectangle((x1, y1, x2, y1 + 58), fill="#ffffff", outline=INK, width=3)
    text(draw, (x1 + 24, y1 + 17), "Claude Desktop · Code", F_SMALL_BOLD, INK)
    draw.rectangle((x1 + 20, y1 + 80, x1 + 235, y2 - 20), fill="#eef2ff", outline=INK, width=3)
    text(draw, (x1 + 36, y1 + 102), "Sessions", F_SMALL_BOLD, INK)
    for i, label in enumerate(["S1 - installation", "Site test", "Audit client"]):
        y = y1 + 145 + i * 56
        draw.rectangle((x1 + 36, y, x1 + 218, y + 38), fill="#ffffff" if i else "#dbeafe", outline=INK, width=2)
        text(draw, (x1 + 48, y + 9), label, F_SMALL, INK)
    draw.rectangle((x1 + 255, y1 + 80, x2 - 330, y2 - 20), fill="#ffffff", outline=INK, width=3)
    text(draw, (x1 + 280, y1 + 104), mode, F_BODY_BOLD, INK)
    wrapped(draw, (x1 + 280, y1 + 152), "Tu écris ta demande ici. Claude lit le projet, propose un plan, puis tu valides les étapes importantes.", 580, F_BODY, "#334155", 10)
    draw.rectangle((x2 - 305, y1 + 80, x2 - 20, y2 - 20), fill="#111827", outline=INK, width=3)
    text(draw, (x2 - 282, y1 + 104), "Terminal", F_SMALL_BOLD, "#ffffff")
    for i, line in enumerate(["$ npm -v", "$ claude", "$ git status", "$ npm test"]):
        text(draw, (x2 - 282, y1 + 150 + i * 40), line, F_MONO, "#e5e7eb")


def cards(draw: ImageDraw.ImageDraw, items: list[tuple[str, str, str]], y: int = 420) -> None:
    x = 54
    for label, title, body in items:
        shadow_box(draw, (x, y, x + 400, y + 230), "#ffffff")
        draw.rectangle((x, y, x + 400, y + 48), fill=label, outline=INK, width=0)
        wrapped(draw, (x + 22, y + 74), title, 350, F_BODY_BOLD, INK, 8)
        wrapped(draw, (x + 22, y + 140), body, 350, F_SMALL, "#475569", 7)
        x += 450


def folder_panel(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, files: list[tuple[str, str]]) -> None:
    x1, y1, x2, y2 = xy
    shadow_box(draw, xy, "#ffffff")
    draw.rectangle((x1, y1, x2, y1 + 58), fill="#dbeafe", outline=INK, width=3)
    text(draw, (x1 + 24, y1 + 17), title, F_SMALL_BOLD, INK)
    y = y1 + 92
    for icon, name in files:
        draw.rectangle((x1 + 30, y - 10, x2 - 30, y + 42), fill="#f8fafc", outline=INK, width=2)
        text(draw, (x1 + 50, y), icon, F_SMALL_BOLD, BLUE if icon == "DIR" else VIOLET)
        text(draw, (x1 + 120, y), name, F_SMALL, INK)
        y += 66


def diff_panel(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, rows: list[tuple[str, str]]) -> None:
    x1, y1, x2, y2 = xy
    shadow_box(draw, xy, "#ffffff")
    draw.rectangle((x1, y1, x2, y1 + 58), fill="#eef2ff", outline=INK, width=3)
    text(draw, (x1 + 24, y1 + 17), title, F_SMALL_BOLD, INK)
    y = y1 + 92
    for marker, line in rows:
        fill = "#dcfce7" if marker == "+" else "#fee2e2" if marker == "-" else "#ffffff"
        draw.rectangle((x1 + 28, y - 8, x2 - 28, y + 38), fill=fill, outline="#cbd5e1", width=1)
        text(draw, (x1 + 48, y), marker, F_MONO_BOLD, "#16a34a" if marker == "+" else "#dc2626" if marker == "-" else "#64748b")
        text(draw, (x1 + 88, y), line, F_MONO, INK)
        y += 52


SCENES = [
    (
        "terminal-start.png",
        "Le terminal Claude Code",
        "Voici l’idée à montrer aux élèves : Claude Code démarre dans un dossier précis. Le chemin du dossier compte autant que le prompt.",
        "interface",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Claude Code v2.1.112",
            [
                ("$", "cd ~/Desktop/formation-s1-claude-code"),
                ("$", "claude"),
                ("›", "Bienvenue dans Claude Code. Dossier actif : formation-s1-claude-code"),
                ("›", "Astuce : commence petit. Demande un fichier simple, puis vérifie."),
            ],
        ),
    ),
    (
        "install-node-npm.png",
        "Pourquoi Node.js ?",
        "Node.js installe npm. npm installe Claude Code. Si npm ne répond pas, tu ne peux pas continuer proprement.",
        "installation",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Pré-requis",
            [
                ("$", "node -v"),
                ("→", "v20.x ou plus récent"),
                ("$", "npm -v"),
                ("→", "npm répond. Tu peux installer Claude Code."),
            ],
        ),
    ),
    (
        "install-claude-command.png",
        "Installer Claude Code",
        "La commande npm reste une route simple. La documentation officielle rappelle aussi de ne pas utiliser sudo avec npm.",
        "installation",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Installation npm",
            [
                ("$", "npm install -g @anthropic-ai/claude-code"),
                ("→", "Claude Code est installé comme commande globale."),
                ("$", "claude --version"),
                ("→", "2.1.112 (Claude Code)"),
            ],
        ),
    ),
    (
        "first-prompt.png",
        "Premier prompt propre",
        "Un bon premier prompt ne demande pas tout. Il demande une petite sortie vérifiable.",
        "prompt",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Exercice élève",
            [
                ("$", "claude"),
                ("›", "Crée une page HTML simple pour un freelance IA."),
                ("›", "À la fin, liste les fichiers créés et explique comment ouvrir la page."),
                ("→", "Tu obtiens un fichier, une consigne d’ouverture et une base à corriger."),
            ],
        ),
    ),
    (
        "cli-help.png",
        "Aide CLI",
        "La commande d’aide montre que Claude Code peut être lancé en mode interactif, en mode print, avec des permissions et des options.",
        "cli",
        lambda d: terminal(
            d,
            (54, 330, 1380, 820),
            "claude --help",
            [
                ("$", "claude --help"),
                ("→", "Usage: claude [options] [command] [prompt]"),
                ("→", "-p, --print : réponse non interactive"),
                ("→", "--permission-mode : default, plan, acceptEdits, auto"),
                ("→", "doctor : vérifie la santé de l’installation"),
            ],
        ),
    ),
    (
        "permissions-modes.png",
        "Modes de permission",
        "La question à poser aux élèves : est-ce que je veux qu’il demande avant d’agir, ou est-ce que je lui fais déjà confiance ?",
        "sécurité",
        lambda d: cards(
            d,
            [
                (BLUE, "Ask permissions", "Mode conseillé au début. Claude demande avant les actions importantes."),
                (VIOLET, "Plan mode", "Utile pour réfléchir avant de modifier le projet."),
                (ORANGE, "Bypass", "À éviter hors environnement isolé. Trop de liberté pour un débutant."),
            ],
            400,
        ),
    ),
    (
        "pricing-plans.png",
        "Prix et plans Claude",
        "Les prix changent selon la région et les taxes. Le support donne la base officielle à vérifier avant achat.",
        "prix",
        lambda d: cards(
            d,
            [
                (BLUE, "Pro", "$20/mois aux États-Unis. Usage régulier, mais limites plus vite atteintes."),
                (VIOLET, "Max 5x", "$100/mois. Plus de capacité par session pour les gros travaux."),
                (CYAN, "Max 20x", "$200/mois. Capacité plus large pour usage intensif."),
            ],
            400,
        ),
    ),
    (
        "usage-limits.png",
        "Limites d’usage",
        "Pro et Max partagent les limites entre Claude et Claude Code. Si tu utilises beaucoup les deux, tout compte.",
        "prix",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Quand tu touches la limite",
            [
                ("?", "Pourquoi ça bloque ?"),
                ("→", "Ton activité Claude + Claude Code compte dans la même capacité."),
                ("→", "Options : attendre, ajouter des crédits, passer à Max, ou réduire la demande."),
            ],
        ),
    ),
    (
        "desktop-code-tab.png",
        "Claude Code Desktop",
        "Le Code tab de Claude Desktop donne une interface graphique : sessions, dossier projet, terminal, fichiers et prévisualisation.",
        "desktop",
        lambda d: desktop_shell(d, (54, 330, 1380, 820), "Session : support technique S1"),
    ),
    (
        "desktop-terminal-pane.png",
        "Terminal intégré Desktop",
        "Dans Desktop, le terminal peut être dans la même session. Il voit le même dossier que Claude.",
        "desktop",
        lambda d: desktop_shell(d, (54, 330, 1380, 820), "Terminal intégré : même dossier, même contexte"),
    ),
    (
        "memory-claude-md.png",
        "CLAUDE.md",
        "Le fichier CLAUDE.md donne une mémoire de projet. Pour un support élève, il fixe le ton, les limites et les règles.",
        "mémoire",
        lambda d: terminal(
            d,
            (54, 330, 1380, 820),
            "CLAUDE.md",
            [
                ("#", "Règles du projet"),
                ("-", "Répondre en français simple."),
                ("-", "Toujours expliquer l’action à l’élève."),
                ("-", "Ne jamais modifier les vidéos."),
                ("-", "Vérifier la version mobile avant livraison."),
            ],
        ),
    ),
    (
        "troubleshooting.png",
        "Dépannage simple",
        "Quand ça bloque, ne panique pas. Tu vérifies le chemin, Node, npm, puis l’erreur exacte.",
        "dépannage",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Diagnostic élève",
            [
                ("$", "pwd"),
                ("$", "node -v && npm -v"),
                ("$", "claude --version"),
                ("?", "Copie l’erreur exacte. Ne la reformule pas trop tôt."),
            ],
        ),
    ),
    (
        "project-folder.png",
        "Dossier de projet",
        "Claude Code travaille dans le dossier ouvert. Si le dossier est propre, les actions sont plus faciles à vérifier.",
        "dossier",
        lambda d: folder_panel(
            d,
            (54, 350, 1380, 820),
            "~/Desktop/formation-s1-claude-code",
            [
                ("DIR", "assets/"),
                ("FILE", "support-technique-seance-01.html"),
                ("FILE", "CLAUDE.md"),
                ("FILE", "README.md"),
                ("FILE", "commandes-s1.md"),
            ],
        ),
    ),
    (
        "auth-login.png",
        "Connexion du compte",
        "Au premier lancement, tu te connectes avec le même compte que Claude. C’est ce lien qui donne accès au plan Pro ou Max.",
        "connexion",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Connexion Claude Code",
            [
                ("$", "claude"),
                ("→", "Ouvre le lien de connexion dans le navigateur."),
                ("→", "Connecte-toi avec le compte Claude utilisé pour Pro ou Max."),
                ("✓", "La session terminal est authentifiée."),
            ],
        ),
    ),
    (
        "plan-mode.png",
        "Plan mode",
        "Avant une grosse modification, Plan mode aide à réfléchir. Claude propose une route avant de toucher aux fichiers.",
        "méthode",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Mode plan",
            [
                ("⇧", "Shift + Tab : passer en Plan mode"),
                ("›", "Propose un plan avant de modifier le support."),
                ("→", "Claude explique les étapes et attend ta validation."),
                ("?", "Est-ce que ce plan sert vraiment l’élève ?"),
            ],
        ),
    ),
    (
        "diff-approval.png",
        "Relire un diff",
        "Quand Claude modifie un fichier, tu dois regarder ce qui change. Le diff rend la validation plus concrète.",
        "validation",
        lambda d: diff_panel(
            d,
            (54, 335, 1380, 820),
            "Modification proposée",
            [
                ("-", "Titre générique"),
                ("+", "Installer Claude Code sans se perdre"),
                (" ", "Explication courte pour les élèves"),
                ("+", "Vérification : ouvrir le fichier dans le navigateur"),
                ("?", "Accepter seulement si le résultat est clair"),
            ],
        ),
    ),
    (
        "file-created.png",
        "Fichier créé",
        "Une demande réussie laisse une preuve simple : le fichier existe, son nom est clair, et tu sais l’ouvrir.",
        "résultat",
        lambda d: folder_panel(
            d,
            (54, 350, 1380, 820),
            "Résultat après la demande",
            [
                ("FILE", "index.html"),
                ("FILE", "style.css"),
                ("FILE", "README.md"),
                ("FILE", "checklist-test.md"),
                ("DIR", "assets/"),
            ],
        ),
    ),
    (
        "git-status.png",
        "Vérifier Git",
        "Git status montre les fichiers modifiés. Même débutant, tu dois savoir regarder ce résumé avant de publier.",
        "git",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "git status",
            [
                ("$", "git status --short"),
                ("→", "M support-technique-seance-01.html"),
                ("→", "?? assets/claude-code-interface/"),
                ("?", "Est-ce que je veux vraiment publier ces fichiers ?"),
            ],
        ),
    ),
    (
        "npm-test.png",
        "Tester une commande",
        "Quand un projet contient des tests ou un build, Claude Code peut les lancer. Toi, tu lis le résultat.",
        "test",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Vérification technique",
            [
                ("$", "npm run build"),
                ("→", "Compilation terminée."),
                ("$", "npm test"),
                ("→", "Aucun test bloquant."),
            ],
        ),
    ),
    (
        "update-doctor.png",
        "Doctor et update",
        "Quand l’installation semble étrange, tu diagnostiques avant de changer dix choses à la fois.",
        "diagnostic",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Santé de l’installation",
            [
                ("$", "claude doctor"),
                ("→", "Vérifie la configuration locale."),
                ("$", "claude update"),
                ("→", "Met à jour Claude Code si nécessaire."),
            ],
        ),
    ),
    (
        "desktop-files-preview.png",
        "Fichiers et aperçu",
        "Desktop aide les élèves à visualiser le projet : fichiers à gauche, demande au centre, aperçu ou terminal à droite.",
        "desktop",
        lambda d: desktop_shell(d, (54, 330, 1380, 820), "Aperçu : support-technique-seance-01.html"),
    ),
    (
        "desktop-permissions.png",
        "Permissions Desktop",
        "Un élève doit voir les actions avant de les accepter. Les permissions rendent ce contrôle visible.",
        "desktop",
        lambda d: cards(
            d,
            [
                (BLUE, "Voir l’action", "Claude explique la commande ou le fichier concerné."),
                (VIOLET, "Accepter", "Tu valides si le changement est logique."),
                (ORANGE, "Refuser", "Tu refuses si tu ne comprends pas encore."),
            ],
            400,
        ),
    ),
    (
        "desktop-usage.png",
        "Suivre l’usage",
        "Les limites sont normales. Suivre l’usage évite de croire que l’outil est cassé quand un quota est atteint.",
        "desktop",
        lambda d: cards(
            d,
            [
                (BLUE, "Usage", "Claude et Claude Code partagent la capacité du plan."),
                (VIOLET, "Reset", "Attendre peut suffire si le besoin n’est pas urgent."),
                (CYAN, "Crédits", "Selon le plan, des crédits peuvent aider à continuer."),
            ],
            400,
        ),
    ),
    (
        "windows-terminal.png",
        "Windows et terminal",
        "Sur Windows, garde le même terminal pendant la séance. Changer de terminal peut changer le chemin et les commandes.",
        "windows",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Windows",
            [
                ("PS", "node -v"),
                ("PS", "npm -v"),
                ("PS", "claude"),
                ("?", "Suis-je dans PowerShell, CMD, Git Bash ou WSL ?"),
            ],
        ),
    ),
    (
        "api-vs-subscription.png",
        "Abonnement ou API",
        "Un abonnement sert à travailler dans Claude. L’API sert à un système qui appelle Claude automatiquement.",
        "budget",
        lambda d: cards(
            d,
            [
                (BLUE, "Abonnement", "Toi, tu utilises Claude et Claude Code."),
                (VIOLET, "API", "Une application ou une automatisation appelle Claude."),
                (ORANGE, "À retenir", "L’API se paie séparément de Pro ou Max."),
            ],
            400,
        ),
    ),
    (
        "api-key-warning.png",
        "Clé API privée",
        "Une clé API est un secret. Elle ne doit pas apparaître dans une capture, un support ou un dépôt GitHub.",
        "sécurité",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Secret à protéger",
            [
                ("!", "Ne colle jamais une clé API dans le support."),
                ("!", "Ne publie jamais une clé dans GitHub."),
                ("→", "Si elle a été montrée : révoque-la et recrée-la."),
            ],
        ),
    ),
    (
        "source-docs.png",
        "Sources officielles",
        "Quand tu doutes d’une commande ou d’un prix, tu vérifies la documentation officielle avant de continuer.",
        "source",
        lambda d: cards(
            d,
            [
                (BLUE, "Docs Claude Code", "Installation, CLI, Desktop et workflows."),
                (VIOLET, "Help Center", "Plans, Pro, Max, limites et première journée."),
                (CYAN, "Node.js", "Pré-requis pour npm et installation."),
            ],
            400,
        ),
    ),
    (
        "prompt-constraints.png",
        "Prompt avec contraintes",
        "Un prompt clair donne le contexte, le format attendu et les limites. L’élève garde ainsi le contrôle.",
        "prompt",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Demande structurée",
            [
                ("›", "Je crée un support pour élèves débutants."),
                ("›", "Sortie attendue : une page HTML responsive."),
                ("›", "Contraintes : fond blanc, violet/bleu, phrases simples."),
                ("›", "À la fin, liste les fichiers modifiés."),
            ],
        ),
    ),
    (
        "checklist-test.png",
        "Checklist de test",
        "Une livraison sérieuse se vérifie. La checklist transforme un ressenti en points concrets.",
        "test",
        lambda d: diff_panel(
            d,
            (54, 335, 1380, 820),
            "Checklist élève",
            [
                ("+", "La page s’ouvre sans erreur."),
                ("+", "Les liens externes sont cliquables."),
                ("+", "Le mobile ne déborde pas."),
                ("+", "Les images illustrent la bonne section."),
                ("?", "Qu’est-ce que je dois corriger avant de publier ?"),
            ],
        ),
    ),
    (
        "clear-compact.png",
        "Nettoyer la session",
        "Quand la conversation devient trop longue, tu peux clarifier le contexte au lieu de continuer dans le flou.",
        "session",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Commandes de session",
            [
                ("/", "/clear : repartir avec une session plus propre"),
                ("/", "/compact : garder l’essentiel sur un projet long"),
                ("?", "Est-ce que la session aide encore, ou est-elle devenue confuse ?"),
            ],
        ),
    ),
    (
        "error-copy.png",
        "Copier l’erreur exacte",
        "Une erreur exacte est une donnée de travail. Une erreur reformulée trop vite peut faire perdre du temps.",
        "dépannage",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Erreur à transmettre",
            [
                ("$", "npm install -g @anthropic-ai/claude-code"),
                ("×", "permission denied: /usr/local/lib/node_modules"),
                ("→", "Copie l’erreur complète avant de demander de l’aide."),
            ],
        ),
    ),
    (
        "delivery-summary.png",
        "Résumé de livraison",
        "À la fin, un élève doit pouvoir expliquer ce qui a été produit et comment le vérifier.",
        "livraison",
        lambda d: terminal(
            d,
            (54, 360, 1380, 820),
            "Fin de session",
            [
                ("✓", "Fichiers créés : index.html, README.md"),
                ("✓", "Vérification : page ouverte en navigateur"),
                ("→", "Prochaine action : corriger le texte de la section 2"),
            ],
        ),
    ),
]


if __name__ == "__main__":
    for scene in SCENES:
        save(*scene)
    print(f"Wrote {len(SCENES)} interface screens to {OUT}")
