note to self

I'm currently stuck on preparing thre file for configparser.

the command using sed to remove all trailing backslash works for the most part, it can remove around 95% of the trailing backslashes.

However there are 43 exception.

I've tried to split the file into smaller collections, in hopes that the issue was with the large file and caching, it didn't work.

I've tried several commands such as perl and multiple combinations of sed, didn't work.

Once the master.conf is processed with sed, even with grep -E "[\\]$" I cannot match and trailing backslashes, however it is for sure still in the file.


