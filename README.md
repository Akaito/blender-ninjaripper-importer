blender-ninjaripper-importer
============================

Import ninja ripper's (sometimes "dx ripper") v1.1 output into Blender.


### How to Use (Once Installed)

1. Get a plaintext "RIPDUMP 1.1" from Ninja Ripper (newer versions are currently not supported).
2. Go to File -> Import -> Ninja/DX Ripdump.
3. Find Ninja Ripper's outputs.  Usually in a directory like "<game-dir>/_Ripper/frames/frame00/".
4. Pick as many mesh0000.rip.txt files as you like.  Select all of them to make things easier.


### How to Install as a Blender Addon

1. In Blender, go to File -> User Preferences.
2. Go to the Addons tab.
3. Use "Install from File...", and pick io_import_ripdump.py
4. Go to the "User" category of the Addons tab to easily find your new addon.
5. Click the checkbox next to "Import-Export: Import Ninja Ripper/Dx Ripper RIPDUMP" to enable the addon.
6. Click "Save User Settings", if you don't want to have to do that again.
	Close the preferences window.

