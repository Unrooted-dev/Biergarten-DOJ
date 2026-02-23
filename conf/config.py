from dotenv import load_dotenv
import os


load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID       = int(os.getenv("GUILD_ID"))
ROLE_IDS        = int(os.getenv("ROLE_IDS"))
CHANNEL_ID     = int(os.getenv("CHANNEL_ID"))

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
        "role_id":     int(os.getenv("TICKET_ROLE_GENERAL",  os.getenv("ROLE_ID"))),
        "value":       "general",
    },
    {
        "label":       "Staatsanwaltschaft",
        "emoji":       "📋",
        "description": "An die Staatsanwaltschaft wenden",
        "role_id":     int(os.getenv("TICKET_ROLE_APPLY",    os.getenv("ROLE_ID"))),
        "value":       "apply",
    },
    {
        "label":       "Richter",
        "emoji":       "🚨",
        "description": "An die Richter wenden",
        "role_id":     int(os.getenv("TICKET_ROLE_REPORT",   os.getenv("ROLE_ID"))),
        "value":       "report",
    },
    {
        "label":       "Anwalt",
        "emoji":       "💬",
        "description": "An einen Anwalt wenden",
        "role_id":     int(os.getenv("TICKET_ROLE_OTHER",    os.getenv("ROLE_ID"))),
        "value":       "other",
    },
]

# ── Welcome ───────────────────────────────────────────────────
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID", os.getenv("CHANNEL_ID")))