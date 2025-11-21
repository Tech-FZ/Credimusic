# Credimusic

Credimusic is a music player written in Python, focusing on making crediting music in livestreams easier.

## IMPORTANT

Due to this codebase relying on the now proprietary PySimpleGUI, it will be discontinued. Community support may continue, but I see myself forced to archive this repo. Sorry for that.

## How to configure

Create `musicdef.json` within the preferences folder. Then there's the following syntax:

`
{
    "music0": [
        "https://insert.url.here/music.mp3",
        "Credit Info\nWith several lines"
    ]
}
`

## Modules

- PySimpleGUI
- pygame
