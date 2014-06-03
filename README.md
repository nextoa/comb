Comb
============

A simply and high-performance framework for create concurrent program



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



## How to use comb

### Create A Slot

A legal slot must be named 'Slot' in your module file and it must be at least contain four method:

- `initialize`
	
	initial resource, e.g: database handle
	 	
- `__enter__ ` 

	get next data to do

- `slot`

	custom-code


- `__exit__`

	when slot finished, call this method
	



you can find the demo at : Install_PATH/comb/demo/*.py

#### [List Data](https://github.com/kbonez/comb/blob/master/comb/demo/list.py)
#### [Mongo MQ](https://github.com/kbonez/comb/blob/master/comb/demo/mongo.py)
#### [Mongo MQ garbage](https://github.com/kbonez/comb/blob/master/comb/demo/garbage.py)



### Run
####  Quick view
	comb   comb.demo.list
####  use `--root` option
	comb --root root-path  slot-package.slot-module

#### with SLOTPATH(Plan)
	export SLOTPATH='USER-PATH' && comb slot-package.slot-module
		 
### How to work
![comb sketch](https://raw.githubusercontent.com/kbonez/comb/master/docs/sketch.png "Sketch")


## TODO
- recode comb support to recognise standard user input

## LICENSE
We use [MIT](http://opensource.org/licenses/MIT) License.

## Developer
[Breeze.Kay](mailto:wangwenpei@kbonez.com)







