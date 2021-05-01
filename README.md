# make_xyz
Script made to equalize indices of xyz files for NEB calculations, saves the time to create new file by hand.
Will only work for reactions were the total number of atoms doesnt change right now, i.e. rearrangement reactions.
I can try and update the script if someone wants to use it for a different reaction. Let me know.

I do not claim that this is the most efficient or beautifull way of solving this problem, but it worked for me.

If you want to run a NEB calculation using ORCA you'll want both your initial xyz and end xyz to have the same 
index. This script will rearrange your end .xyz to match the index of the start .xzy using an index file provided.

Bear in mind that you'll have to provide your files in XMOL format to do the NEB calculation. If you already use
XMOL files be sure to set the first two lines to themselves to keep the header. In this case you'll have to add
+2 to the indices of your atoms which you've aquired using something like ChemCraft. The xyz files should also 
contain one blank line at the end.
