from dotenv import load_dotenv
import os


load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID       = int(os.getenv("GUILD_ID"))
ROLE_ID        = int(os.getenv("ROLE_ID"))
CHANNEL_ID     = int(os.getenv("CHANNEL_ID"))

CHIEF_OF_JUSTICE_ROLE_ID = int(os.getenv("CHIEF_ROLE_ID"))
DEPUTY_CHIEF_OF_JUSTICE_ROLE_ID = int(os.getenv("DEPUTY_CHIEF_ROLE_ID"))
SENIOR_JUDGE_ROLE_ID = int(os.getenv("SENIOR_JUDGE_ROLE_ID"))
SENIOR_ATTORNEY_ROLE_ID = int(os.getenv("SENIOR_ATTORNEY_ROLE_ID"))
PROSECUTOR_ROLE_ID       = int(os.getenv("PROSECUTOR_ROLE_ID"))
JUDGE_ROLE_ID            = int(os.getenv("JUDGE_ROLE_ID"))
ATTORNEY_ROLE_ID         = int(os.getenv("ATTORNEY_ROLE_ID"))

SENIOR_JUDGE_ROLE_ID = int(os.getenv("SENIOR_JUDGE_ROLE_ID"))
ATTORNEY_GENERAL_ROLE_ID = int(os.getenv("ATTORNEY_GENERAL_ROLE_ID"))


# ── Ticket Panel ──────────────────────────────────────────────
# ID der gespeicherten Panel-Nachricht (wird vom Bot gesetzt, nicht manuell)
PANEL_MESSAGE_ID: int | None = None

# ── Ticket Kategorien (Dropdown) ──────────────────────────────
# label      → Text im Dropdown
# emoji      → Emoji vor dem Label
# description→ Kurze Beschreibung unter dem Label
# role_id    → Diese Rolle wird angepingt wenn ein Ticket in dieser Kategorie erstellt wird
TICKET_CATEGORIES = [
    {
        "label":       "Chief of Justice",
        "emoji":       "🛠️",
        "description": "An den Chief of Justice",
        "role_id":     CHIEF_OF_JUSTICE_ROLE_ID,
        "value":       "Zum Chief of Justice",
    },
    {
        "label":       "Deputy Chief of Justice",
        "emoji":       "🛡️",
        "description": "An den Deputy Chief of Justice wenden",
        "role_id":     DEPUTY_CHIEF_OF_JUSTICE_ROLE_ID,
        "value":       "Zum Deputy Chief of Justice",
    },
    {
        "label":       "Senior Judge",
        "emoji":       "⚖️",
        "description": "An den Senior Judge wenden",
        "role_id":     SENIOR_JUDGE_ROLE_ID,
        "value":       "Zum Senior Judge",
    },
    {
        "label":       "Richter",
        "emoji":       "🚨",
        "description": "An die Richter wenden",
        "role_id":     JUDGE_ROLE_ID,
        "value":       "Zum Richter",
    },
    {
        "label":       "Attorney General",
        "emoji":       "💼",
        "description": "An den Attorney General wenden",
        "role_id":     ATTORNEY_GENERAL_ROLE_ID,
        "value":       "Zum Attorney General",
    },
    {
        "label":       "Prosecutor",
        "emoji":       "📋",
        "description": "An die Staatsanwälte wenden",
        "role_id":     PROSECUTOR_ROLE_ID,
        "value":       "Zum Staatsanwalt",
    },
    {
        "label":       "Senior Attorney",
        "emoji":       "📁",
        "description": "An die Senior Attorneys wenden",
        "role_id":     SENIOR_ATTORNEY_ROLE_ID,
        "value":       "Zum Senior Attorney",
    },
    {
        "label":       "Attorney",
        "emoji":       "💼",
        "description": "An die Attorneys wenden",
        "role_id":     ATTORNEY_ROLE_ID,
        "value":       "Zum Attorney",
    }
]

# ── Rules ────────────────────────────────────────────────────
# Channel in dem das Regelwerk-Panel gepostet wird
RULES_CHANNEL_ID = int(os.getenv("RULES_CHANNEL_ID", os.getenv("CHANNEL_ID")))

# Channel in dem die Rollen-Übersicht gepostet wird
ROLES_CHANNEL_ID = int(os.getenv("ROLES_CHANNEL_ID", os.getenv("CHANNEL_ID")))

# Gespeicherte Panel-Nachrichten-IDs (werden vom Bot gesetzt)
RULES_PANEL_MESSAGE_ID: int | None = None
ROLES_PANEL_MESSAGE_ID: int | None = None

# ── Rollen-Übersicht ──────────────────────────────────────────
# Wird im Rollen-Channel als Embed angezeigt
ROLE_DESCRIPTIONS = [
    {
        "role_id":     CHIEF_OF_JUSTICE_ROLE_ID,
        "emoji":       "⚖️",
        "label":       "Chief of Justice",
        "description": "Leitet das gesamte Justizwesen. Höchste Instanz des Servers.",
    },
    {
        "role_id":     DEPUTY_CHIEF_OF_JUSTICE_ROLE_ID,
        "emoji":       "🛡️",
        "label":       "Deputy Chief of Justice",
        "description": "Unterstützt den Chief of Justice und übernimmt Aufgaben in dessen Abwesenheit.",
    },
    {
        "role_id":     PROSECUTOR_ROLE_ID,
        "emoji":       "📋",
        "label":       "Staatsanwalt",
        "description": "Verfolgt Straftaten und erhebt Anklage im Namen des Staates.",
    },
    {
        "role_id":     JUDGE_ROLE_ID,
        "emoji":       "🔨",
        "label":       "Richter",
        "description": "Leitet Gerichtsverfahren und spricht Urteile.",
    },
    {
        "role_id":     ATTORNEY_ROLE_ID,
        "emoji":       "💼",
        "label":       "Rechtsanwalt",
        "description": "Vertritt Mandanten vor Gericht und berät in Rechtsfragen.",
    },
]

# ── Welcome ───────────────────────────────────────────────────
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID", os.getenv("CHANNEL_ID")))

# ── Rollen-Anfrage ────────────────────────────────────────────
# Channel in dem das Rollen-Anfrage Panel gepostet wird
ROLE_REQUEST_CHANNEL_ID       = int(os.getenv("ROLE_REQUEST_CHANNEL_ID", os.getenv("CHANNEL_ID")))
ROLE_REQUEST_PANEL_MESSAGE_ID: int | None = None

# Diese 2 Rollen werden angepingt wenn jemand eine Rolle anfragen will
# Ping-Rolle 1 → z.B. Chief of Justice
# Ping-Rolle 2 → z.B. Staatsanwalt
ROLE_REQUEST_PING_ROLE_1 = int(os.getenv("ROLE_REQUEST_PING_ROLE_1", os.getenv("CHIEF_ROLE_ID")))
ROLE_REQUEST_PING_ROLE_2 = int(os.getenv("ROLE_REQUEST_PING_ROLE_2", os.getenv("PROSECUTOR_ROLE_ID")))