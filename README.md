</p>
  <img src="https://media.discordapp.net/attachments/1023648075937497110/1034236447248625755/icon.png" alt="Cemu PB Loader"/>
</p>

# Cemu Private Battle Loader
Allows users playing Splatoon with Cemu to go on maps that aren't meant to be played online in private battles.

- [Cemu Private Battle Loader](#cemu-private-battle-loader)
  - [Downloading](#downloading)
  - [Usage](#usage)
  - [FAQ](#faq)
  - [Bug Reports](#bug-reports)
  - [Known Issues](#known-issues)

# Downloading
Download the executable program *(.exe)* from the release tab and place it in the same folder where *Cemu.exe* is located at.

# Usage
After downloading the program and putting it on the Cemu folder, you can now open the program (Make sure you are already on a Private Battle), if you have messed with addresses in cemu before; select your region on the dropdown (located at the top right of the window) and then press the **"MemorySearcher Backup"** button, you should see a message saying that the backup is successful. Select your map at the dropdown located at the top left of the window (Do not select Plaza or Octo Valley unless you know what you are doing) and if you have not selected your region yet, at the top right of the window there is a dropdown, select the region of your splatoon copy and then press the **"Select Map** button (Make sure you have memory searcher closed before pressing the button), it should say that it was successful, you can now open memory searcher **(Cemu [Top Bar]>Tools>Memory Searcher)** and set the teams to play on the map! (Note that in most of these maps, Team Bravo does not have a spawn! So they will fall to their death the entire match. In the next update there will be an option to set the first 4 players to always be in Team Alpha even if no one is in Team Bravo)

</p>
  <img src="https://media.discordapp.net/attachments/1023648075937497110/1034278775409614899/unknown.png" alt="Cemu PB Loader"/>
</p>

# FAQ

## Can you get banned for this?
It is not possible to be banned for using this program, **make sure you are not using any Static.pack edit/Model edit that modifies one of the maps listed in the program.**

## I clicked the *"Set First 4 Players to Alpha"* checkbox but it isn't working!
Make sure you have clicked the checkbox in either the stage select menu or the team select menu and see if Memory Searcher is open **(Cemu [Top Bar]>Tools>Memory Searcher)**

## I clicked the *"Set First 4 Players to Alpha"* checkbox and all players are set to Alpha but I can't click the set teams button!
Change the teams until you are able to press the button, after that, the first 4 players in the private battle will be on Team Alpha even if you set one of them/some to Team Bravo.

## Everybody crashed once the match started!
Make sure the mode is **Turf war** and that you did not select these stages: **Plaza**, **Octo Valley**.

## This program seems familiar...
There's another program that does this aswell (Private Battle Map Tester) but that program is meant for Wii U, this program is meant for Cemu Emulator instead.

## The program didn't set the maps!
After you press the **"Select Map** button, make sure you have Memory Searcher open: **(Cemu [Top Bar]>Tools>Memory Searcher)**.

## I set another map but it loaded the map I set before!
Once a match starts, make sure to close Memory Searcher, and when that same match ends, use the program and then open Memory Searcher, it should work.

# Bug Reports
If you ever spot a bug, please create a [new issue](https://github.com/token-canary/Cemu_PrivateBattleLoader/issues), also make sure to look at the FAQ!

# Known Issues
In **v2.0.1**, setting a map without the 4 players patch and then setting another map with the 4 players patch will cause the addresses to corrupt, to avoid this issue; **once you want to use the 4 players patch after setting a map without the patch, press the wipe addresses button, and then you can set a map with the patch.**
