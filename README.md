Comb
============


Comb is a framework use to simply develop threads program.



## INSTALL

### Requirement


- Python2.7(I haven't test on other version.If you success work it on other version,let me know)
- [Optional] 
	- Mongo
	- Redis(Plan)
	- Mysql(Plan)



### Install from pypi

	sudo pip install comb


### Install from source

	git clone git@github.com:kbonez/comb.git
	cd comb && sudo python setup.py install



## Howto use comb

### Create Slot

you can find the demo at : comb/demo/*.py

I will write document as soon as possible.

### Run
#### with SLOTPATH(Plan)

	export SLOTPATH && comb slot-package.slot-module
		 
####  use `--root` option(Plan)
	comb --root root-path  slot-package.slot-module
		 



## Developer
[Breeze.Kay](mailto:wangwenpei@kbonez.com)

## LICENSE
We use [MIT](http://opensource.org/licenses/MIT) License.





