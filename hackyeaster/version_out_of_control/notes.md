`for i in {1000..0001};do git checkout "$i".zip;unzip -q "$i".zip;cd "$i";done`

hit a few snags:
folders do not like to be nested that deep.
```
~/wow/1000/0999/0998/0997/0996/0995/0994/0993/0992/0991/0990/0989/0988/0987/0986/0985/0984/0983/0982/0981/0980/0979/0978/0977/0976/0975/0974/0973/0972/0971/0970/0969/0968/0967/0966/0965/0964/0963/0962/0961/0960/0959/0958/0957/0956/0955/0954/0953/0952/0951/0950/0949/0948/0947/0946/0945/0944/0943/0942/0941/0940/0939/0938/0937/0936/0935/0934/0933/0932/0931/0930/0929/0928/0927/0926/0925/0924/0923/0922/0921/0920/0919/0918/0917/0916/0915/0914/0913/0912/0911/0909/0908/0907/0906/0905/0904/0903/0902/0901/0900/0899/0898/0897/0896/0895/0894/0893/0892/0891/0890/0889/0888/0887/0886/0885/0884/0883/0882/0881/0880/0879/0878/0877/0876/0875/0874/0873/0872/0871/0870/0869/0868/0867/0866/0865/0864/0863/0862/0861/0860/0859/0858/0857/0856/0855/0854/0853/0852/0851/0850/0849/0848/0847/0846/0845/0844/0843/0842/0841/0840/0839/0838/0837/0836/0835/0834/0833/0832/0831/0830/0829/0828/0827/0826/0825/0824/0823/0822/0821/0820/0819/0818/0817/0816/0815/0814/0813/0812/0811/0810/0809/0808/0807/0806/0805/0804/0803/0802/0801/0800/0799/0798 alex@debvm 34s
❯ git status
fatal: Could not get current working directory: Numerical result out of range
```

had to batch in few hundreds, moving the innermost zip back to the top

at 0722.zip, it contains a single jpg instead of the next folder.

```
~/wow/0723 master* alex@debvm
❯ git ls
dcf4797 [4 months ago] (HEAD, master) Change committed [Philipp Sieber]
44dc751 [4 months ago] Change committed [Philipp Sieber]
93d6302 [4 months ago] Commit committed [Philipp Sieber]

reverting to the first commit yields the correct zip:

~/wow/0723 master* alex@debvm
❯ git co @~~
HEAD is now at 93d6302... Commit committed

~/wow/0723 93d6302...* alex@debvm
❯ unzip -q 0722.zip

~/wow/0723 93d6302...* alex@debvm
❯ ls
0722  0722.zip  trunk.jpg
```

same again at 0396, but it's on a branch of it's own:

```
~/wow/0397 master* alex@debvm
❯ git ls
a0c4344 [4 months ago] (HEAD, master) Commit committed [Philipp Sieber]
27dbde6 [4 months ago] (blaster) Commit committed [Philipp Sieber]

~/wow/0397 master* alex@debvm
❯ git co @~
HEAD is now at 27dbde6... Commit committed

~/wow/0397 heads/blaster* alex@debvm
❯ git st
?? scooter.jpg

~/wow/0397 heads/blaster* alex@debvm
❯ unzip -q 0396.zip 

~/wow/0397 heads/blaster* alex@debvm
❯ ls
0396  0396.zip  scooter.jpg
```

at 0045, we have a password protected zip:

```
~/wow/0046 master alex@debvm
❯ unzip -q 0045.zip 
[0045.zip] 0045/.git/COMMIT_EDITMSG password: 
```
the password is given in both the containing git directory of the zip, and in the one that partially extracts(?)

```
~/wow/0046/0045 master alex@debvm
❯ git ls
37f69df [4 months ago] (HEAD, master) Commit committed. Pass is fluffy99 [Philipp Sieber]

~/wow/0046/0045 master alex@debvm
❯ cd ..
0045  0045.zip

~/wow/0046 master alex@debvm
❯ git ls
37f69df [4 months ago] (HEAD, master) Commit committed. Pass is fluffy99 [Philipp Sieber]
```

and finally in 0001, we have our qr code image:

```
~/wow/0001 master* alex@debvm
❯ git st
 D egg12.png

~/wow/0001 master* alex@debvm
❯ git co egg12.png
```
