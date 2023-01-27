# PlOszukiwacz Cryptolocker

## How to run
1. Clone this repo
```
git clone https://github.com/PlOszukiwaczDEV/Cryptolocker.git
```
2. Cd
```
cd Cryptolocker
```
3. Install requirements
```
pip install -r requirements.txt
```
or
```
pip install cryptography
pip install tkinter
```
4. Run

### Cryptolocker CLI
* Genereate key
```
python cryptolocker_cli.py -g <key-file-name>
```
* Encrypt a file
```
python cryptolocker_cli.py -k <key-file-name> -e <file-to-encrypt>
```
* Decrypt a file
```
python cryptolocker_cli.py -k <key-file-name> -d <file-to-decrypt>
```
* Restore
```
python cryptolocker_cli.py -r '<restore-key>'
```

## Todo
Cryptolocker GUI
Add restore feature

## Author
* PlOszukiaczDEV - All

## License

Distributed under the GNU GENERAL PUBLIC LICENSE v3.0. See `LICENSE` for more information.

